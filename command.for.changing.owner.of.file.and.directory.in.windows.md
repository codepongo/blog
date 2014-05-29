windows下批量修改文件（或文件夹）权限或所有者
===================================================


[原文](http://www.toxingwang.com/windows-server/winserver/355.html)


* 强制将当前目录下的所有文件及文件夹、子文件夹下的所有者更改为管理员组(administrators)命令：
<pre data-language="Shell">
takeown /f * /a /r /d y
</pre>

* 将所有当前目录下的文件、子文件夹的NTFS权限修改为仅管理员组(administrators)完全控制(删除原有所有NTFS权限设置)：

<pre data-language="Shell">
cacls * /T /G administrators:F
</pre>

* 在原有当前目录下的文件、子文件夹的NTFS权限上添加管理员组(administrators)完全控制权限(并不删除原有所有NTFS权限设置)：
<pre data-language="Shell">
cacls * /T /E /G administrators:F
</pre>

* 取消管理员组(administrators)完全控制权限(并不删除原有所有NTFS权限设置)：
<pre data-language="Shell">
cacls \\Server\path /t /e /r "mddq\domain admins"
cacls \\Server\path /t /e /r "mddq\domain admins"
</pre>
