chromium 线程封装
===========================
## 实现 implementation ##
* PlatformThread - 平台级线程函数的封装
A namespace for low-level thread functions.
<pre data-language="charp">
PlatformThread::Create(PlatformThread::Delegate delegate) {
	CreateThreadInternal(delegate);
}

PlatformThread::CreateThreadInternal() {
	params->delegate = delegate_;
	CreateThread(
			NULL, statck_size, ThreadFunc,params, flags, NULL);
}

DWORD ThreadFunc(param) {
	delegate->ThreadMain();
}

</pre>

PlatformThread::Creat调用CreateThread,ThreadFunc为thread过程函数，
delegate作为参数的一部分传入。


ThreadFunc中调用ThreadMain()。


in PlatformThread::Create the CreateThread is called, 
ThreadFunc is the thread process function.
delegate is a part of the ThreadFunc parameter.
in ThreadFunc, ThreadMain function is called


* Thread - 线程抽象
A simple thread abstraction that establishes a MessageLoop on a new thread.
<pre data-language="charp">
Thread : PlatformThread::Delegate {
	// PlatformThread::Delegate methods:
	virtual void ThreadMain() OVERRIDE;
}

void Thread::ThreadMain() {
	// Let the thread do extra initialization.
	// Let's do this before signaling we are started.
	Init();
	Run();
	// Let the thread do extra cleanup.
	CleanUp();
}
</pre>
Thread继承PlatformThreadDelegate实现纯虚函数ThreadMain()，
ThreadMain默认构建MessageLoop，
也可以不构建MessageLoop,message-pump-factory.is_null()，
MessageLoop构建成功后通过PostTask ThreadQuitHelper退出线程


Thread class inherits the PlatformThreadDelegate.
the virtual ThreadMain function is implemented.
in ThreadMain function, MessageLoop is usually constructed and run.
But if the message pump's factory is null, the MessageLoop will not be constructed.
if MessageLoop is constructed, the thread exit by post ThreadQuitHelper task 


<pre data-language="charp">
message_loop_->PostTask(FROM_HERE, base::Bind(&ThreadQuitHelper));
</pre>
