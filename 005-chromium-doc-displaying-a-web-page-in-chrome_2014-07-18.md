chromium显示网页-笔记
========================
[原文display a web page in chrome](http://dev.chromium.org/developers/design-documents/displaying-a-web-page-in-chrome)
## 层 ##
* Browser
 + 代码位置：src/chrome/browser
* Tab contents
 + 代码位置：src/chrome/browser/tab_content
* Render host
 + 代码位置：src/chrome/browser/renderer_host
* Render
 + src/chrome/rendererer
 + RenderView
  - 代码位置：/content/render/render_view_impl.cc
  - 继承于RenderWidget，RenderWidget负责input处理和绘制
* Webkit glue(WebView, WebWidget, WebFrame, etc)
 + 代码位置：src/webkit/glue
 + 封装webkit接口
 + 转化webkit内建类型为chromium类型，如，std::string 代替 WebCore::String；GURL代替KURL。
 + 简化webkit对象命名，如：WebCore::Frame 变成 WebFrame
 + test shell基于glue的测试程序
* Webkit/Webkit Port
 + 代码位置：third_party/Webkit
 + webkit开源代码，Port是webcore平台相关接口的实现
## 时序 ##
1. browser process的UI thread创建RenderProcessHost
2. RenderProcessHost创建render process并在browser process的I/O thread中创建ChannelProxy
3. ChannelProxy监听命名管道，将消息转发给RenderProcessHost
4. ChannelProxy中包含ResourceMessageFilter过滤某些消息（如网络通信）直接交给I/O thread 处理
 - ResourceMessageFilter::OnMessageReceived()
5. RenderProcessHost将view相关消息派发给RenderViewHost处理，本身处理view无关消息
 - RenderProcessHost::OnMessageReceived()
6. view相关消息在RenderViewHost和RenderWidgetHostView基类中处理
7. RenderView(Widget)Host都有与之对应的RenderView(Widget)位于render process，
8. 每个平台都有一个 (RenderWidgetHostView[Aura|Gtk|Mac|Win])用于集成至平台。
<pre data-language="csharp">
  render process                               browser process
       |                                            |
    +--+--------------+                +---------------------+
    |                  \              /                       \
render thread        main thread    I/O(IPC) thread     Main browser(UI) thread
    |                    |            |                         |
 webkit                  |            |                         |
    |                    |            |                         |
renderWidget::SetCursor  |            |                         |
    |                    |            |                         |
renderView::Send()       |            |                         |
    |                    |            |                         |
RenderThead::Send()      |            |                         |
    |            IPC::SyncChannel     |                         |
    |                    |-----IPC----|                         |
    |                    |      IPC::ChannelProxy               |
    |                    |            |                         |
    |                    | ResourceMessageFilter                |
    |                    |            |                         |
    |                    |            |   RenderProcessHost::OnMessageReceived
    |                    |            |                         |
    |                    |            |    RenderViewHost::OnMessageReceived
    |                    |            |                         |
    |                    |            |     RenderViewHost::OnMessageReceived
    |                    |            |                         |
    |                    |            |     RenderWidgetHost::OnMsgSetCursor 
    |                    |            |                         |
</pre>
<pre data-language="csharp">
  render process                               browser process
       |                                            |
    +--+------------------------+                +---------------------+
    |                            \              /                       \
render thread                 main thread    I/O(IPC) thread     Main browser(UI) thread
    |                             |            |                         |
    |                             |            | RenderWidgetHost:ForwardMouseEventToRenderer
    |                             |            |                         |
    |                             |            |                   WebMouseEvent 
    |                             |            |                         |
    |                             |            | RenderWidgetHost::ForwardInputEvent
    |                             |            |                         |
    |                             |            |          RenderWidgetHost::Send
    |                             |      IPC::ChannelProxy               |
    |                             |----IPC-----|                         |
    |                         IPC::Channel     |                         |
RenderView::OnMessageReceived     |            |                         |
    |                             |            |                         |
RenderViewHost::OnMessageReceived |            |                         |
    |                             |            |                         |
RenderWidgetHost::OnMsgSetCursor  |            |                         |
    |                             |            |                         |
</pre>
