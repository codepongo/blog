Chrome扩展学习笔记
====================================


[Chrome扩展及应用开发](http://www.ituring.com.cn/minibook/950)


## include_globs/exclude_globs ##
* 可选的
* 由于matches是必须选的，所以只能用来限制matches匹配的页面
* 通配符?匹配任意单个字符，比matches语法灵活


[参考](http://open.chrome.360.cn/extension_dev/content_scripts.html#include-exclude-globs)

## JavaScript getAttribute() 和 setAttribute()

<pre data-language="javascript">
object.getAttribute("attribute")
object.setAttribute("attribute","value");
</pre>

[参考](http://www.cnblogs.com/sunky/articles/2322734.html)


## event_page.js ##

[参考](http://hyjk2000.github.io/2013/06/18/use-event-pages-in-chrome-extension/)


## unlimitedStorage ##

提供一个用于存储HTML5的客户端的数据，如数据库和本地存储的文件，不设限额。如果没有这个权限，扩展限制为5MB本地存储空间。
<pre data-language="javascript">
{
	"manifest_version":2,
	"name":"crx",
	"description:"chrome extension",
	"version":"0.0.0",
	"permissions":["unlimitedStorage"]
}
</pre>

**关闭网页后，chrome.storage.StorageArea.get存储的数据不被清除。**

## desktop notify demo ##
popup和background都没有webkitNotifications。

[chrome offical notification example](http://src.chromium.org/chrome/trunk/src/chrome/common/extensions/docs/examples/)

## chrome.tabs.sendMessage 不指定tabId ##


**有多个extension使用了chrome_url_overrides 最后安装的extension起作用**


## chrome app启动 ##
* chrome.exe  --profile-directory=Default --app-id=
* chrome://apps/


## filesystem ##
* chooseEntry
* Entry
* FileEntry
* DirectoryEntry
* FileWriter 
* FileReader
* DirectoryReader
<pre>
   chooseEntry
        |
      create
        |
        V
      Entry
        | 
       derive
        /\
       /  +---------------------+
      /                         |
 FileEntry                 DirectoryEntry
    |                           |  
    +                           |
   /  \                  +------+-------+--------------+ 
create contain-file-+    |      |       |              |
  |                 |   create getFile getDirectory  removeRecursively
FileWriter   FileReader  |
                  DirectoryReader
</pre>


## JavaScript apply() ##
Function.apply(obj,args)方法能接收两个参数
    obj：这个对象将代替Function类里this对象
    args：这个是数组，它将作为参数传给Function（args-->arguments）


[参考](http://www.cnblogs.com/delin/archive/2010/06/17/1759695.html)


## 文字转语音 ##
[loudspeaker](https://github.com/codepongo/loudspeaker)


## 参考资料 ##
[360 chrome extension development documents](http://open.chrome.360.cn/extension_dev/overview.html)
[crxdoczh镜像](https://lmk123.duapp.com/extensions/index)
[crx samples](http://src.chromium.org/chrome/trunk/src/chrome/common/extensions/docs/examples/)

