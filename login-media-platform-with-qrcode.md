扫描二维码登录微信公众平台
==============================
[read the python source code directly](https://raw.githubusercontent.com/codepongo/weixin/master/push/push.py)


* 登录，发送POST至https://mp.weixin.qq.com/cgi-bin/login （与原有流程一致）
* 申请ticket 发送POST至https://mp.weixin.qq.com/misc/safeassistant，请求数据为action=get_ticket&auth=ticket获取ticket
* 链接qrserver 发送POST至https://mp.weixin.qq.com/safe/safeqrconnect 获取uuid
* 获取二维码 发送GET至https://mp.weixin.qq.com/safe/safeqrcode获取二维码图片
* 循环发送GET至https://mp.weixin.qq.com/safe/safeuuid轮询获取当前登录状态（二维码是否被扫描）
* 二维码被正确扫描后，发送POST至https://mp.weixin.qq.com/cgi-bin/securewxverify获取token
