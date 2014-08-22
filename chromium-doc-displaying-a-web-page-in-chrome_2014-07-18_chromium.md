<h1>chromium显示网页-笔记</h1>

<p><a href="http://dev.chromium.org/developers/design-documents/displaying-a-web-page-in-chrome">原文display a web page in chrome</a></p>

<h2>层</h2>

<ul>
<li>Browser
<ul>
<li>代码位置：src/chrome/browser</li>
</ul></li>
<li>Tab contents
<ul>
<li>代码位置：src/chrome/browser/tab_content</li>
</ul></li>
<li>Render host
<ul>
<li>代码位置：src/chrome/browser/renderer_host</li>
</ul></li>
<li>Render
<ul>
<li>src/chrome/rendererer</li>
<li>RenderView</li>
<li>代码位置：/content/render/render<em>view</em>impl.cc</li>
<li>继承于RenderWidget，RenderWidget负责input处理和绘制</li>
</ul></li>
<li>Webkit glue(WebView, WebWidget, WebFrame, etc)
<ul>
<li>代码位置：src/webkit/glue</li>
<li>封装webkit接口</li>
<li>转化webkit内建类型为chromium类型，如，std::string 代替 WebCore::String；GURL代替KURL。</li>
<li>简化webkit对象命名，如：WebCore::Frame 变成 WebFrame</li>
<li>test shell基于glue的测试程序</li>
</ul></li>
<li>Webkit/Webkit Port
<ul>
<li>代码位置：third_party/Webkit</li>
<li>webkit开源代码，Port是webcore平台相关接口的实现
<h2&gt;时序</h2&gt;</li>
</ul></li>
</ul>

<ol>
<li>browser process的UI thread创建RenderProcessHost</li>
<li>RenderProcessHost创建render process并在browser process的I/O thread中创建ChannelProxy</li>
<li>ChannelProxy监听命名管道，将消息转发给RenderProcessHost</li>
<li>ChannelProxy中包含ResourceMessageFilter过滤某些消息（如网络通信）直接交给I/O thread 处理
<ul>
<li>ResourceMessageFilter::OnMessageReceived()</li>
</ul></li>
<li>RenderProcessHost将view相关消息派发给RenderViewHost处理，本身处理view无关消息
<ul>
<li>RenderProcessHost::OnMessageReceived()</li>
</ul></li>
<li>view相关消息在RenderViewHost和RenderWidgetHostView基类中处理</li>
<li>RenderView(Widget)Host都有与之对应的RenderView(Widget)位于render process，</li>
<li>每个平台都有一个 (RenderWidgetHostView[Aura|Gtk|Mac|Win])用于集成至平台。</li>
</ol>

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

#html