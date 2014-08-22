chromium进程通信-笔记
==============================
[原文inter process communication](http://dev.chromium.org/developers/design-documents/inter-process-communication)
## 实现 ##
* windows采用命名管道
* linux/x os 采用socketpair()
* browser process中 I/O thread处理消息避免UI thread阻塞；view通过ChannelProxy进行消息的收发，ChannelProxy::MessageFilter
插入RenderProcessHost用于过滤资源请求类消息在I/O thread中处理
* render process中 main render thread用于处理browser和webkit的通信，并提供同步通信机制
## 消息类型 ##
* control message - 直接由View/ViewHost处理
* routed message - 由View派发给注册routed的对象处理
* View message - 发送给RenderView的消息
* ViewHost message - 发送给RenderViewHost的消息
* PluginProcess - message browser process发送给plugin process的消息
* PluginProcessHost - plugin process发送给browser process的消息
### 消息声明 ###
* 文件 render_messages_internal.h
<pre data-language="csharp">
IPC_MESSAGE_ROUTED2(ViewHostMsg_MyMessage, GURL, int)
IPC_MESSAGE_CONTROL0(ViewMsg_MyMessage)
</pre>
* 参数太多则可以使用结构体包装
### 发送消息 ###
<pre data-language="csharp">
Send(new ViewMsg_StopFinding(routing-id));
</pre>
### 处理消息 ###
<pre data-language="csharp">
MyClass::OnMessageReceived(const IPC::Message& message) {
  IPC_BEGIN_MESSAGE_MAP(MyClass, message)
    // Will call OnMyMessage with the message. The parameters of the message will be unpacked for you.
    IPC_MESSAGE_HANDLER(ViewHostMsg_MyMessage, OnMyMessage)  
    ...
    IPC_MESSAGE_UNHANDLED_ERROR()  // This will throw an exception for unhandled messages.
  IPC_END_MESSAGE_MAP()
}

// This function will be called with the parameters extracted from the ViewHostMsg_MyMessage message.
MyClass::OnMyMessage(const GURL& url, int something) {
  ...
}
</pre>
## 同步消息 ##
IPC::SyncMessage 阻塞进程直到返回
<pre data-language="csharp">
/* 声明 */
IPC_SYNC_MESSAGE_CONTROL2_1(SomeMessage,  // Message name
                            GURL, //input_param1
                            int, //input_param2
                            std::string); //result
/* 处理 */
IPC_MESSAGE_HANDLER(MyMessage, OnMyMessage)
to the OnMessageReceived function, and write:
void RenderProcessHost::OnMyMessage(GURL input_param, std::string* result) {
  *result = input_param.spec() + " is not available";
}
</pre>
