在windows7 x64下 Visual Studio 2013 编译Chromium
=============================
## 1.下载depot_tools ##
## 2. 更新depot_tools ##
<pre data-language="shell">
gclient
</pre>
## 3. 获取代码，托GFW的鸿福，时间要很久。科学上网，是不错的选择##
<pre data-language="shell">
gclient config http://src.chromium.org/svn/trunk/src
gclient sync --force
</pre>
* http://src.chromium.org/svn/trunk/src 为trunk下代码，有可能编译不过，即使编译成功
此版本的浏览器很可能有许多问题，建议使用release下的版本代码。
如： http://src.chromium.org/svn/releases/35.0.1916.153/
* 目录路径不能包含'@'字符，svn update时，会出... a peg version ...的错误
## 4. 生成工程文件 ##
<pre data-language="shell">
set GYP_MSVS_VERSION＝2013
set GYP_GENERATORS=msvs-ninja,ninja
gclient runhooks --force
</pre>
## 5. 编译 ##
debug版,不设置GYP_DEFINES link时会出错
<pre data-language="shell">
set GYP_DEFINES=component=shared_library
ninja -C out\Debug chrome
</pre>
release版
<pre data-language="shell">
ninja -C out\Release chrome.exe
</pre>

## 参考 ##
[Chromium building with nanja or najia+vs2013](http://blog.csdn.net/talking12391239/article/details/21444591)
