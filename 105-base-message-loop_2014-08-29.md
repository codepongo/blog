chromium 消息循环
===========================

## message loop ##
* 线程的事件处理循环
* 每个thread至少有一个message loop
* message loop主要处理task，依靠不同类型的message pump也可以处理其他任务，如 UI消息等
* message loop 继承MessagePump::Delegate 实现委托接口
* message loop 有可重入保护，一个任务未执行完，其他任务不可以开始
* 只有当创建嵌入message pump时，才可发生可重入，如创建模态对话框，OLE函数（拖拽），打印等。
* destruction_observers message loop 销毁时，通知此列表的对象。list结构，观察者模式
* PostTask() 多线程调用，使task在messageloop所属线程的run()中被处理
* DeleteSoon() ReleaseSoon() 保持变量，使之一直在消息循环中有效
* 运行相关函数被重新封装至RunLoop类中
* task_observers_ task被处理之前和之后通知 观察者模式
* type_ 类型 与 message pump相关
* nestable_tasks_allowed_ 可重入标识
* 两个队列 work_queue（需要被处理的task的队列）, delayed_work_queue_（按时间排序）,
* IncomingTaskQueue智能指针 IncomingTaskQueue批量复制到work_queue或delayed_work_queue中起到减少锁等待的作用
* MessageLoopForUI/MessageLoopForIO 提供为pump加入（删除）观察者的接口
* lazy_tls_ptr 静态对象保持message loop指针


## message loop proxy ##
* 多线程访问message loop对象，使用proxy管理message loop生命周期
* 返回带引用计数的message loop的智能指针
* 相关文件 message_loop_proxy.cc(h) message_loop_impl.cc(h)


## message pump ##
* 消息泵，派发task，处理非task任务
* mesage loop的pump_指向message pump
* loop按类型包含一个同类型的pump
* 用来负责处理task以外的消息，决定task处理的时机，委托给loop处理task 委托模式
* pump 的 run loop过程
 + DoInernalWork() 处理非task任务，如UI消息,完成端口消息
 + WaitForWork() 阻塞等待任务
 + 循环调用DoInternalWork(), DoWork(), DoDelayedWork()保证所有队列任务都可被执行
 + 每次循环检查退出标志
<pre data-language="csharp">
for (;;) {
	bool did_work = DoInternalWork();
	if (should_quit_)
		break;
	did_work |= delegate_->DoWork();
	if (should_quit_)
		break;

	TimeTicks next_time;
	did_work |= delegate_->DoDelayedWork(&next_time);
	if (should_quit_)
		break;
  
	if (did_work)
		continue;

	did_work = delegate_->DoIdleWork();
	if (should_quit_)
		break;
  
	if (did_work)
		continue;
  
	WaitForWork();
}
</pre>
* message loop default
 + evnet_唤醒loop
 + delayed_work_time_ 定时处理delayed work
* message pump ozone:This class implements a message-pump for processing events from input devices Refer to MessagePump for further documentation.
* message pump dispatcher:嵌套message loop 的消息派发相关
* message_pump_observer.h x11相关


## windows 下 message pump的实现 ##
<pre>
            MessagePumpWin
                 |
              interit
                 |
         +---------------+
         |               |
MessagePumpForUI MessagePumpForUI
</pre>
* MessagePumpWin
 + 观察者列表 在处理消息的前后分别通知观察者，观察者模式
 + 延时任务运行时间
 + RunState 消息运行，包括消息重入的处理
* MessagePumpForUI
 + 实现为一个传统的本地windows message pump
 + kMsgHaveWork是一个特殊消息作为一个event去唤醒sub pump处理task
   - 避免kMsgHaveWork被重复放入消息队列  检查have_work_变量保证
   - sub pump无task时自动挂起，有task时被自动唤醒
   - WM_PAINT和WM_TIMER优先级总是高于其他投递的消息（如，kMsgHaveWork）
 + DoRunLoop() 消息泵，相当于
<pre data-language="csharp">
while(GetMessage(&Msg,NULL, 0, 0) > 0) 
{
    TranslateMessage(&Msg);
    DispatchMessage(&Msg); 
}
</pre>
 + WndProcThunk() 消息处理函数
* MessagePumpForIO
 + 完成端口
 + 观察者列表 在处理消息的前后分别通知观察者。观察者模式


## run loop ##


* 消息循环
* 从message loop剥离，在栈上分配对象，速度更快；降低message loop的复杂度
* _loop为message loop对象的指针
* previous_run_loop_ 上一个run loop的指针
 + BeforeRun()中push Runloop stack
 + AfterRun()中pop Runloop stack
* 每次run前都发一个quit task目的是如果之前有message loop则退出。


## 线程内消息 ##
线程内部是如何进行的。但你需要进行费时的操作时候，可以派发一个事件和回调函数给
自身线程的MessageLoop，然后MessageLoop会调度该回调函数以执行其操作。问题是这有必要
吗？直接调用不就可以吗？答案是不可以，或者说是最好不要这么做，其原因在于，如果当前的
MessageLoop里面有优先级更高的事件和任务需要处理时，你这样做会阻碍它们的执行。


## 参考 ##
[理解WebKit和Chromium: 消息循环(Message Loop)](http://blog.csdn.net/milado_nju/article/details/8539795)
[Chrome学习笔记（一）：线程模型，消息循环](http://bigasp.com/archives/478)
[理解WebKit和Chromium_ Chromium的多线程机制](http://blog.csdn.net/milado_nju/article/details/8027625)
