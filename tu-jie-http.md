《图解HTTP》笔记
==========================

## HTTP相关协议 ##
* TCP/IP协议簇


<pre>
+-----------+
|应用层     |HTTP数据
+-----------+
|传输层     |IP数据报（TCP首部+HTTP数据）
+-----------+
|网络层     |IP首部+TCP首部+HTTP数据
+-----------+
|数据链路层 |以太网首部+IP首部+TCP首部+HTTP数据
+-----------+
</pre>


* TCP 分割，打上标记序号和端口号


* IP 增加MAC地址（因为ARP协议，在TCP/IP协议簇中是在IP层实现的,所以增加网络地址是在IP层）


* ARP协议 根据通信方的IP地址就可以反查出对应的MAC地址。


* 三次握手保证数据送达目标（SYNsynchronize-SYN和ACK-ACK acknowledgement）


* NIC Networking Interface Card


* DNS 域名查IP和IP反查域名

## URL/URI ##


协议方案名://登录信息（认证）@服务器地址:端口号/带层次的文件路径?查询字符串#片段标识符


<pre>
http://user:pass@www.example.com:80/dir/index.html?uid=1#ch1
</pre>

## Session/Cookie ##


HTTP/1.1 是无状态协议，为了实现保持状态功能，引入了cookie技术。


服务器应答报文首部Set-Cookie 
请求报文首部包含Cookie
### GET 请求 ###
<pre>
GET /index.html HTTP/1.1
Host:www.example.com
</pre>

### POST 请求 ###
<pre>
POST /form/entry HTTP/1.1
Host: www.example.com
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 16

name=ueno&age=37
</pre>

### 应答 ###
<pre>
HTTP/1.1 200 OK
Date: Wed, 17 Feb 2016 17:22:00 GMT
Content-Length: 362
Content-Type: text/html

...
</pre>


## 请求方法 method ##
* GET:获取资源
* POST 传输实体主体
* PUT 传输文件
* HEAD 获得报文首部
* DELETE 删除文件
* OPTIONS 询问支持的方法
* TRACE 追踪路径
* CONNECT 要求用隧道协议链接代理


## 请求格式 ##

请求行   Method URI HTTP/version(CRLF)
消息报头 head(CRLF)
(CRLF)
请求正文 body

## HTTP 1.1 完善 ##
* 持久性链接 Connection:Keep-Alive 
* 管线化（不用等待相应亦可直接发送下一个请求）
* session  保存状态


## HTTP 报文 格式 ##
* 分隔符CR(Carriage Return)[0x0D]LF(Line Feed)[0x0A]
* 请求报文=报文首部（请求行+请求首部字段+通用首部字段+实体首部字段+其他[RFC里未定义的首部])+报文主体
* 响应报文=报文首部（状态行+响应首部字段+通用首部字段+实体首部字段+其他[RFC里未定义的首部])+报文主体

## 编码和压缩 ##
* 压缩格式：gzip(GNU zip), compress deflate(zlib), identity
* 分块传输：Transfer-Encoding:chunked。每一块都会用16进制来标记块的大小，最后一块使用"0(CRLF)"标记
<pre>
...
Transfer-Encoding:chunked


cf0

...0xcf0(3312)字节分块数据...


392

...0x392(914)字节分块数据...


0
</pre>

## 复合数据 ##
MIME(Multipurpose Internet Mail Extensions)


### multipart/form-data ###
<pre>
Content-Type:multipart/form-data;boundary=AaB03x

--AaB03x
Content-Disposition:form-data;name="field1"

Joe Blow
--AaB03x
Content-Disposition:form-data;name="pics";filename="file1.txt"
Content-Type:text/plain

...(file1.txt的数据)...
--AaB03x--
</pre>


### multipart/byteranges ###
<pre>
HTTP/1.1 206 Partial Content
Date:Fri, 13 Jul 2012 02:45:26 GMT
Last-Modified:Fri, 31 Aug 2007 02:02:20 GMT
Content-Type:multipart/byteranges; boundary=THIS_STRING_SEPARATES

--THIS_STRING_SEPARATES
Content-Type:application/pdf
Content-Range:bytes 500-999/8000

...(范围指定的数据)...
--THIS_STRING_SEPARATES
Content-Type:application/pdf
Content-Range:bytes 7000-7999/8000

...(范围指定的数据)...
--THIS_STRING_SEPARATES--
</pre>
### 范围请求 ###
<pre>
GET /tip.jpg HTTP/1.1
Host:www.abc.com
Range:bytes=5001-10000
</pre>
<pre>
HTTP/1.1 206 Partial Content
Date:Fri, 13 Jul 2012 04:39:17 GMT
Content-Range: bytes 5001-10000/10000
Content-Length:5000
Content-Type:image/jpeg

...(tip.jpg内容)...
</pre>

## 服务器协商 ##
相关首部字段
* Accept 
* Accept-Charset
* Accept-Encoding
* Accept-Language
* Content-Language


## HTTP状态码 ##
* 1XX Informational(信息性状态码) 接收的请求正在处理
* 2XX Success(成功状态码) 请求正常处理完毕
 + 200 ok
 + 204 no content
 + 206 partial content
* 3XX Redirection(重定向状态码) 需要进行附加操作以完成请求
 + 301 moved permanently 永久重定向
 + 302 found 临时重定向
 + 303 see other 临时重定向并用GET方法获取
 + 304 not modified 允许请求但未满足条件
 + 307 temporary redirect 临时重定向禁止POST变换成GET
* 4XX Client Error(客户端错误状态码) 服务器无法处理请求
 + 400 bad request
 + 401 unauthorized 第一次需要认证，第二次是认证失败
 + 403 forbidden 禁止访问
 + 404 not found

* 5XX Server Error(服务器错误状态码) 服务器处理请求错误
 + 500 internal server error 服务器出错
 + 503 service unavailable 服务器维护


_浏览器实际实现中301、302、303，307都会将POST方法变成GET方法_


## 区别单台虚拟主机实现多个域名，通过Host首部加以区分 ##

## 通用数据转发程序 ##

* 代理:转发功能的程序，一般代理都是指客户端部分的转发程序。
* 反向代理：服务端前置的代理叫反向代理。
* 网关：转发其他服务器通信数据的服务器，与反向代理的区别是，网关还有协议转换的作用。即能使通信线路上的服务器提供非HTTP协议服务，而反向代理只提供HTTP服务的转发
* 隧道：客户端与服务器之间的中转，并保持双方通信连接的程序。 


## HTTP首部字段结构 ##
由字段名和字段值构成，中间用冒号分隔。字段值可以由多个指令参数组成，多个指令之间由逗号分隔，指令可以有指令值（指令值为可选项，可有可无），指令和指令值用等号分隔。
<pre>
Cache-Control:private, max-age=0, no-cache
</pre>

## HTTP首部字段分类 ##
### 通用首部 General Header Fields ###
   + Cache-Control 控制缓存
   + Connection 逐跳首部，连接管理
     - Connection:Upgrade 发送至下个服务器时，不转发Upgrade首部
     - Connection:Close 关闭连接
   + Date 创建报文的日期时间 GMT时间 GMT=UTC 与北京时间差8个小时
   + Pragma 报文指令
   + Trailer 报文末端的首部一览，报文主体后，记录了哪些首部字段多用于分块传输
   + Transfer-Encoding 指定报文主体的传输编码方式
   + Upgrade 升级为其他协议
   + Via 代理服务器相关信息
   + Warning 错误通知


### 请求首部 Request Header Fields ###
 + Accept 用户代理可处理的媒体类型
 + Accept-Charset 优先的字符集
 + Accept-Encoding 优先的内容编码
 + Accept-Language 优先的语言（自然语言）
 + Authorization Web认证信息
 + Expect 期待服务器的特定性温
 + From 用户的电子邮箱地址
 + Host 请求资源所在服务器
 + If-Match 比较实体标记（ETag）
 + If-Modified-Since 比较资源的更新时间
 + If-None-Match 比较实体标记（与If-Match相反）
 + If-Range 资源未更新时发送实体Byte的范围请求
 + If-Unmodified-Since 比较资源的更新时间（与If-Modified-Since相反）
 + Max-Forwards 最大传输逐跳数
 + Proxy-Authorization 代理服务器要求客户端的认证信息
 + Range 实体的字节范围请求
 + Referer 对请求中URI的原始获取方 [referer拼写错误，应为referrer]
 + TE 传输编码的优先级
 + User-Agent HTTP客户端程序的信息


### 响应首部 Response Header Fields ###
 + Accept-Ranges 是否接受字节范围请求
 + Age 推算资源创建经过时间
 + ETag 资源的匹配信息
 + Location 令客户端重定向至指定URI
 + Proxy-Authenticate 代理服务器对客户端的认证信息
 + Retry-After 对再次发起请求的时机要求
 + Server HTTP服务器的安装信息
 + Vary 代理服务器缓存的管理信息
 + WWW-Authenticate 服务器对客户端的认证信息





### 实体首部 Entity Header Fields ###
 + Allow 资源可支持的HTTP方法
 + Content-Encoding 实体主体适用的编码方式
 + Content-Language 实体主体的自然语言
 + Content-Length 实体主体的大小（单位：字节）
 + Content-Location 替代对应资源的URL
 + Content-MD5 实体主体的报文摘要
 + Content-Range 实体主体的位置范围
 + Content-Type 实体主体的媒体类型
 + Expires 实体主体过期的日期时间
 + Last-Modified 资源的最后修改日期时间

### 其他首部（非HTTP/1.1 首部字段）###
 + 为cookie服务的首部
  - Cookie
  - Set-Cookie
 
 + 其他首部
  - Content-Disposition
  - X-Frame-Options
  - X-XSS-Protection
  - P3P

## 逐跳首部和端到端首部 ##
* 端到端首部（End-to-end Header）: 必须转发至终端
* 逐跳首部（Hop-by-hop Header）：仅对单次转发有效
 + Connection
 + Keep-Alive
 + Proxy-Authenticate 
 + Proxy-Authentication 
 + Trailer
 + TE
 + Transfer-Encoding

## HTTPS ##
* SSL(Secure Socket Layer)
* TLS(Transport Layer Security) SSL3.1
* HTTPS(HTTP Secure)(HTTP over SSL) = HTTP + SSL
* CA颁发的证书用来证明通信所用公钥的真实性和作为通信一方的服务器（也可认证客户端）是否规范。
* EV SSL(Extended Vailidation SSL Certificate)和自签名证书

### HTTPS 通信机制 ###
<pre>
Client                           Server          
  |                                |
  +---Handshake:ClientHello------->|
  |<--Handshake:ServerHello--------+
  |<--Handshake:Certificate--------+
  |<--Handshake:ServerHelloDone----+
  |                                |
  +---Handshake:ClientKeyExchange->|
  +---ChangeCipherSpec------------>|
  +---HandShake:Finished---------->|
  |                                |
  |<--ChangeCipherSpec-------------+
  |<--HandShake:Finished-----------+
  |                                |
  |---Application Data(HTTP)------>|
  |<--Application Data(HTTP)-------+
  |                                |
  |                                |
  |-=Alert:warning,close notify--->|

</pre>
 + ClientHello: SSL版本，加密组件（Cipher Suite）列表（所使用的加密算法及密钥长度等）
 + ServerHello: SSL版本，加密组件（Cipher Suite）列表（从客户端列表中筛选出来）
 + Certificate: 包含公开密钥
 + ServerHelloDone: 握手结束
 + ClientKeyExchange:随机密码串(Pre-master secret)用公钥加密
 + ChangeCipherSpec:提示服务器，之后通信采用通过Pre-master secret产生的密钥加密
 + Finished:连接至今全部报文的整体校验值，握手成功与否由服务器是否能正确解密该报文作为判定标准
 + 服务器发送ClientKeyExchange提示客户端
 + 发送Finished报文，校验并判定握手是否成功


SSL的慢的原因包括两方面：由于数据变大导致传输数据变多，导致通信慢和加解密的计算计算需要耗时，导致客户端和服务器的处理速度慢。


## HTTP 认证机制 ##

### BASIC ###
* WWW-Authenticate:Basic realm="pompt"
* Authorization:Basic user:password Base64 encode

### DIGEST ###
* WWW-Authenticate:Digest realm="DIGEST", nonce="random string"
* Authorization:Digest username="user", realm="DIGEST", nonce="random string", uri="/digest/", response="password md5 hash"
* Authentication-Info:


### 基于表单认证 ###
* 表单认证流程
  1. POST username password
  2. Set-Cookie包含sessionid
  3. 其他通信带有Cookie


密码安全保存：先利用给密码加盐的方式增加额外信息，再使用散列函数计算出散列值后保存。
加盐Salt就是由服务器随机生成一个字符串，但要保证长度足够长，并且是真正随机生成的。然后把它和密码字符串相连起来（前后都可以）生成散列值。减少密码特征，无法利用密码特征库进行破解。


## HTTP 追加协议 ##
* Ajax:局部更新
* Comet:持续连接便于推送
* SPDY:在应用层与传输层之间加入新的会话层，使用SSL，通过单一TCP连接处理多个HTTP请求实现多路复用，提高效率
* WebSocket:HTTP的Upgrade: websocket字段握手并切换协议
* WebDAV:对web服务器上的文件直接操作，分布式文件系统。HTTP/1.1 追加方法 HTTP协议主体为XML格式
 + PROPFIND: 获取属性
 + PROPPATCH: 修改属性
 + MKCOL: 创建集合
 + COPY: 复制资源及属性
 + MOVE: 移动资源
 + LOCK: 资源枷锁
 + UNLOCK: 资源解锁
 + 102 Processing 正常处理请求，但目前是处理中状态
 + 207 Multi-Status 存在多种状态
 + 422 Unprocessible Entity 格式正确，内容有误
 + 423 Locked 资源已被加锁
 + 424 Failed Dependency 处理与某请求关联的请求失败，因此不再维持依赖关系
 + 507 Insufficient Storage 保存空间不足


## Web 安全 ##
* 输入输出值转义不完全引发的安全漏洞
 + 跨站脚本攻击
 + sql注入攻击
 + shell命令注入攻击
 + http首部注入攻击
 + 邮件首部注入攻击
 + 目录遍历攻击
 + 远程文件包含漏洞

* 设置和设计缺陷引发的安全漏洞
 + 强制浏览
 + 不正确的错误消息处理
 + 开放重定向
* 会话引发的安全漏洞
 + 会话劫持
 + 会话固定攻击
 + 跨站点请求伪造
* 密码破解
* 点击劫持
* dos攻击
* 后门程序
