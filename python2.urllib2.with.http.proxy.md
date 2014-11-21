python HTTP Proxy实现和urllib2的使用
===============================

## HTTP Proxy HTTP代理##
http代理的原理：
客户端用代理的ip和port替换服务器的ip和地址建立socket连接；
将HTTP请求发送至代理。
代理收到http请求，根据http请求的地址与服务器建立连接，
将客户端请求转至服务器，将服务器应答转至客户端，
客户端除了负责用代理的ip和port，代替服务器的ip和port建立socket，
还必须补全Request line（请求行）中的 Path-to-resoure（资源路）为全路径，
根据Request header中的Host字段补全。
删除请求头中的Proxy-Connection字段
代理负责客户端和服务器之间的请求和应答转发。


[HTTP代理客户端python实现](https://raw.githubusercontent.com/codepongo/utocode/master/httpproxy.py/clientofhttpproxy.py)


[HTTP代理服务器python实现](https://raw.githubusercontent.com/codepongo/utocode/master/httpproxy.py/serverofhttpproxy.py)
## urllib2源码 ##
* OpenerDirector 为处理http协议的类，包含三类对象
 + 第一类是负责处理请求数据的对象存储在process_request
 + 第二类是负责处理应答数据的对象储存在process_response
 + 第三类是通讯相关对象类存储在handle_open
               
* build_opener 函数创建OpenerDirector对象并通过add_handler()将筛选的handler加入
对象至OpenDirector
<pre data-language="python">
    default_classes = [ProxyHandler, UnknownHandler, HTTPHandler,
                       HTTPDefaultErrorHandler, HTTPRedirectHandler,
                       FTPHandler, FileHandler, HTTPErrorProcessor] # 所有基础模块
    if hasattr(httplib, 'HTTPS'):
        default_classes.append(HTTPSHandler)
    skip = set()
    for klass in default_classes:
        for check in handlers:
            if isclass(check):
                if issubclass(check, klass):
                    skip.add(klass) #有用户自定义的基础模块的继承类则去除基础模块
            elif isinstance(check, klass):
                skip.add(klass)
    for klass in skip:
        default_classes.remove(klass)

    for klass in default_classes:
        opener.add_handler(klass())

    for h in handlers:
        if isclass(h):
            h = h()
        opener.add_handler(h)
</pre>
OpenerDirector的三类对象通过其函数名区分。
<pre>
protocol_request 如 http_request属于process_request;
protocol_response属于process_response;
protocol_open属于handle_open
</pre>

<pre data-language="python">
def open(self, fullurl, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        # pre-process request
        meth_name = protocol+"_request"
        for processor in self.process_request.get(protocol, []):
            meth = getattr(processor, meth_name)
            req = meth(req)

        response = self._open(req, data)

        # post-process response
        meth_name = protocol+"_response"
        for processor in self.process_response.get(protocol, []):
            meth = getattr(processor, meth_name)
            response = meth(req, response)

        return response
</pre>
<pre data-language="python">
def _open(self, req, data=None):
        protocol = req.get_type()
        result = self._call_chain(self.handle_open, protocol, protocol +
                                  '_open', req)
</pre>
<pre data-language="python">
    def _call_chain(self, chain, kind, meth_name, *args):
        # Handlers raise an exception if no one else should try to handle
        # the request, or return None if they can't but another handler
        # could.  Otherwise, they return the response.
        handlers = chain.get(kind, ())
        for handler in handlers:
            func = getattr(handler, meth_name)

            result = func(*args)
            if result is not None:
                return result
</pre>


## urllib2 代理相关 ##
### Request ###
* self.host为设置为代理地址
* self. __ original 为真正地址

### ProxyHandler ###
初始化时，会增加protocol_open方法，该方法调用proxy_open进行设置代理
<pre data-language="python">
        for type, url in proxies.items():
            setattr(self, '%s_open' % type,
                    lambda r, proxy=url, type=type, meth=self.proxy_open: \
                    meth(r, proxy, type))
</pre>


**注意设置代理时，代理模块会读取系统的代理设置**


<pre data-language="python">
   def proxy_open(self, req, proxy, type):

        if req.host and proxy_bypass(req.host): #注意：proxy_bypass
            return None

</pre>
proxy_bypass 位于urllib模块中,会读取保存在操作系统中的代理设置，windows在注册表
中
<pre data-language="python">
            internetSettings = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                r'Software\Microsoft\Windows\CurrentVersion\Internet Settings')
            proxyEnable = _winreg.QueryValueEx(internetSettings,
                                               'ProxyEnable')[0]
            if proxyEnable:
                # Returned as Unicode but problems if not converted to ASCII
                proxyServer = str(_winreg.QueryValueEx(internetSettings,
                                                       'ProxyServer')[0])
</pre>

