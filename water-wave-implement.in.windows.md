windows下实现水波纹效果
=========================================
## 使用余（正）弦函数公式 ##
<pre>
y = a * cos(x * b)
</pre>
其中，a决定幅度，b决定周期。

## 关键流程 ##
根据余弦公式绘制曲线，形成闭合路径，再填充颜色，做遮罩成去掉无用部分


## 源代码 ##
* 源码地址:[waterwave.cpp](https://raw.githubusercontent.com/codepongo/utocode/master/windows/watewave.cpp)
* 编译
<pre>
Setting environment for using Microsoft Visual Studio 2008 x86 tools.
>cl waterwave.cpp /Zi /link user32.lib gdi32.lib
</pre>


## 参考 ##

[异形窗口](http://blog.csdn.net/MoreWindows)  
[水波纹效果-iOS实现](https://github.com/LiweiDong/WaterWave)










