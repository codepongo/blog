High DPI 相关的Windows桌面应用程序开发技术
====
High DPI Desktop Application Development on Windows

UWP程序可以被系统自动适配，其他技术实现的程序（raw Win32 programming，Windows 
Form，WPF等）不能自动适配，默认情况下会自动被系统做位图拉伸适配导致显示模糊。


High DPI技术，主要是解决由于显示器分辨率越来越高，如果使用固定DPI（如windows操作系统为96）而导致传统UI上的元素（字体，图形等）显示越来越小，肉眼辨识越来越费力的问题。
在高分辨率下，对元素进行拉伸（放大）处理（即定义一个伸缩率，伸缩率乘以标准DPI则为实际采用的DPI值），如设置更大的字号，加载更大规格的图像资源等。


High DPI技术主要有三类应用场景：

* 多显示器
* 远程桌面
* 实时缩放，即程序运行时，进行显示拉伸改变后，程序可实时自适应。

## DPI 感知模式
* `DPI_AWARENESS_CONTEXT_UNAWARE` 应用程序不关心DPI改变，系统始终采用 96DPI 根据比率自动进行像素级适配, 其结果是UI显示很模糊。
* `DPI_AWARENESS_CONTEXT_SYSTEM_AWARE` 应用程序对启动时所在的显示器做适配，不需要系统进行自动适配，这样就保证了，在此模式下，应用程序在其初始化所处的显示器清晰显示，不模糊。但当显示器DPI实时改变或切换显示器显示时，系统会自动进行像素级适配，进而导致渲染效果的模糊。
* `DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE` 在DPI发生变化时，系统只做通知，不自动适配，由应用程序自己进行适配（缩放和布局）。
* `DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2` PerMonitor 升级版，增强对DPI变化的处理能力。
  + 顶层窗口的子窗体也会收到 DPI 改变的通知
  + 自动处理非客户端区域的DPI适配
  + 自动适配Win32菜单
  + 对话框大小自动适配DPI改变
  + 改善控件对DPI改变的适配
  + 改善对 UxTheme（Visual styles）的支持


不同系统所支持的DPI感知模式是不一样的; 不同UI框架技术，在不同版本系统上的表现也是不一样的。

## 升级已存在的程序
大部分程序是 DPI awareness 模式。

### 升级至 PerMonitor 模式的步骤
1. mainfest 中设置DPI感知模式
2. 重构布局逻辑，使之可以在代码相应DPI发生改变时可重用。
3. DPI敏感数据（DPI/字体/尺寸/等）应进行换算后更新。
4. DPI改变发生，位图资源需要重新载入。
5. 替换API为相应的DPI敏感版本
6. 多显示器，多DPI设置场景测试应用
7. 对于无法适配的窗体，可采用混合模式使他们通过位图级别的拉伸进行适配

### 混合模式 Mixed-Mode DPI Scaling

在时间不够或使用了没有源码的第三方UI库等无法做DPI适配的情况下，可采混合DPI感知
模式的方案，调用 `SetThreadDpiAwarenessContext` 去改变和恢复DPI感知模式。

* 线程可以任何时候更改自己的DPI感知模式
* DPI感知模式发生变化后，任何API将以与其DPI感知模式相符的情况运行
* 窗体的DPI感知模式，在其创建时被定义，其窗体过程中将使用保持这个感知模式。

### 测试

* DPI不同的多显示器来回切换应用程序
* 使用不同DPI值，启动程序
* 当程序运行时，改变缩放因子，测试程序是否实时适配
* 切换主显示，测试应用；这个测试对于发现硬编码的坐标和尺寸及其有帮助

## 注意事项
* DPI改变后，确认鼠标始终处于窗体相对位置
* 避免DPI改变递归循环
* 通过 `WM_GETDPISCALEDSIZE` 消息预设大小
* 一些DPI敏感的API的返回值将根据DPI感知模式被虚拟化。但微软没有提供文档对这些API进行有效的说明。
* 对没有DPI感知的API，需做一些额外处理。
* 进程的DPI感知模式，一旦初始化是不能被改变的。 但由于窗体树上的父子窗体必须保持一致的DPI感知模式。所以，进程的DPI感知模式会由窗体父子关系的改变(CreateWindow和SetParent)可能触发而强制重置。 


## WPF应用支援High DPI模式
详见: [WPF应用支持High DPI](https://docs.microsoft.com/en-us/windows/desktop/hidpi/declaring-managed-apps-dpi-aware)


## 参考
* [High DPI Desktop Application Development on Windows](https://docs.microsoft.com/en-us/windows/desktop/hidpi/high-dpi-desktop-application-development-on-windows)
* [关于Windows高DPI的一些简单总结](http://www.cppblog.com/weiym/archive/2014/03/03/205841.html)
* [Visual Styles](https://docs.microsoft.com/en-us/windows/desktop/controls/themes-overview)
* [High DPI Scaling Improvements for Desktop Applications and “Mixed Mode” DPI Scaling in the Windows 10 Anniversary Update (1607)](https://blogs.windows.com/buildingapps/2016/10/24/high-dpi-scaling-improvements-for-desktop-applications-and-mixed-mode-dpi-scaling-in-the-windows-10-anniversary-update/#aC5WgsIYVpkkSxIg.97)
* [High-DPI Scaling Improvements for Desktop Applications in the Windows 10 Creators Update (1703)](https://blogs.windows.com/buildingapps/2017/04/04/high-dpi-scaling-improvements-desktop-applications-windows-10-creators-update/#fiAHTSz06PD8ul7S.97) [【译】Windows 10 创作者更新中用于桌面应用的高 DPI 缩放改进](https://zhuanlan.zhihu.com/p/26214150)
* [High DPI](https://docs.microsoft.com/en-us/windows/desktop/api/_hidpi/)
* [Windows DPI Awareness](https://zhuanlan.zhihu.com/p/31268783)
