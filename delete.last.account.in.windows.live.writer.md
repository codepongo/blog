Delete the last account of windows write live 2011
===================================================

删除Windows write live 2011上最后一个帐号
------------------------------------------


There is a terrible user experience in Windows Live Writer 2011.
Windows Live Writer 2011有个坑爹的设计，


You can not delete the last blog account, because of the delete button is disabled.
你不能通过界面删除最后一个博客帐号。


But, you can edit regedit to delete the last account
可以通过编辑注册表去删除帐号


Find "HKEY\_CURRENT\_USER\Software\Microsoft\Windows Live\Writer\WebLogs" the random GUID that denotes your account.
找到"HKEY\_CURRENT\_USER\Software\Microsoft\Windows Live\Writer\WebLogs"删除名为随机的GUID的子键


[Deleting Your Last And Only Blog From Windows Live Writer](http://www.thousandtyone.com/codepersona/DeletingYourLastAndOnlyBlogFromWindowsLiveWriter.aspx)
