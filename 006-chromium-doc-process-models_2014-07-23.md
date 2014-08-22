chromium进程模型-笔记
===================================
[原文process models](http://dev.chromium.org/developers/design-documents/process-models)
网站更像一个应用而不是文档，所以浏览器要向操作系统一样有更高的安全性和鲁棒性。
## 进程模型 ##
* 每个网站的一个实例对应一个进程 默认
* 每个网站对应一个进程  --process-per-site
* 每个tab页对应一个进程 --process-per-tab
* 单进程模型 --single-process
* 渲染进程运行在沙箱内
* 每个插件单独一个进程
* 网页跳转不能切换进程（将来会改进）
* 网页的frame在同一进程中（将来会改进）
* 进程数有限制

