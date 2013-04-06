Github Useful Help github帮助
=========================

* [Register 注册](https://github.com/users)

* [Create repository 创建库](https://help.github.com/articles/creating-a-new-repository)	
*新建库*
可以在任何有权限的账户上创建库，无论是个人或组织帐号
	1. 在任意页面的右上角的用户条，点击“Create a New Repo"按钮
	2. 选择创建库的帐号
	3. 输入库名字，选择库类型public公有或private私有；然后点击“Create repository”

* [Delete repository 删除库](https://help.github.com/articles/deleting-a-repository)
*删除库*
	1. 切换至要删除的库
	2. 选择库操作条上的“Settings”
	3. 点击“Delete this repository”在Danger Zone 区域
	4. 阅读警告，输入库名
	5. 点击“I understand the consequences, delete this repository”

* Establish a secure connectio
	[SSH Keys](https://help.github.com/articles/generating-ssh-keys)
	如果决定不使用推荐的HTTPS方法,也能用SSH keys去建立一个安全的终端到github的链接,
	下面的步骤将引导你产生一个SSH key然后加入公钥到github帐号
	1. 检查SSH keys
	首先，我们需要检查一个存在的ssh keys在你的计算机。
	cd ~/.ssh
	如果没有文件或路路，那么进行第二步，否则密钥对已存在那么跳到第三步。
	2. 产生新的SSH key
	产生新的SSH key
	ssh-keygen -t rsa -C "your_email@example.com"
	3. 加入SSH key到GitHub
	拷贝公钥到剪切版 ~/.ssh/id_rsa.pub
		1. 进入账户设置“Account Settings”
		2. 点击侧栏的“SSH Keys”
		3. 点击“Add SSH key”
		4. 黏贴公钥到“Key”区域
		5. 点击“Add key”
		6. 确认密码后，添加成功
	4. 测试
	ssh -T git@github.com
