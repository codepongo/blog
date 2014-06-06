Launch To Desktop In Windows7 win7创建显示桌面快捷方式
================================
* create a file and name it "desktop.scf" 新建名为“desktop.scf“的文件


* copy bellow content in it 复制下面内容到文件中
<pre>
[Shell]
Command=2
IconFile=%SystemRoot%system32SHELL32.dll,34
[Taskbar]
Command=ToggleDesktop
</pre>


* create a shortcut and move it into the "~\favorites\links" 
创建一个快捷方式并拷贝到用户目录下的favorites\links下
~ belongs to your home directory 

