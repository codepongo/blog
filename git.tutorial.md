GIT Tutorial GIT指南
=====================

* Repository Configure 库配置

	+ git init --bare _name_.git
		initial an empty git repository 初始化一个空git库

* Local Setting 本地配置

	+ git config user.name _name_
		设置用户名 set user name 

	+ git config user.email _email_
		设置email地址 set user email 

* Status 状态查询
	
	+ git log --oneline --graph
		显示日志
		show log

	+ git status -s
		显示工作区状态
		show work box status 


* Box - Stage 工作区和暂存区

	+ git add -A
		加入所有修改至缓存区
		add file new file, removing file and motified content to stage 

	+ git add -u
		加入修改内容至缓存区
		update motified content to stage 
	

	+ git rm _file_
		移除文件
		remove file from work box and stage 

	 + git diff
		比较工作区和暂存区
		compare stage with HEAD(local Repository) 

	+ git checkout -- _file_
		从缓存区恢复至工作区
		restore file in work box from stage 


* Stage - Repository 暂存区和库

	+ git reset, git reset HEAD, git reset -- _file_
		用库重置暂存区
		restore stage from repository 
	
	+ git diff --cached
		比较暂存区和库
		compare stage with HEAD(local Repository) 

	+ git commit -m '_message_'
		提交缓存区至库
		commit stage to repository 

* Box - Repository 工作区和库

	+ git diff HEAD
		比较工作区和库
		compare work box with HEAD(local Repository) 

* Repository - Stage - Box

	+ git reset --hard HEAD
		用库恢复工作区和暂存区
		restore work box and stage from repository 

	+ git checkout [_commit_] -- _file_
		检出至工作区和暂存区
		checkout  to work box and stage 

* Repository 
	
	+ git reset --soft HEAD^
		还原至上一版本
		revert to last version(HEAD^) 

	+ git commit --amend -m 'new comment'
		modify log 修改版本日志

	
* Local Repository - Remote Repository 本地库和远程库

	+ git clone file://_path.name.git_
		克隆git库
		clone git repository

	+ git push
		更新远程库
		update remote repository 

	+ git pull
		获取远程库，合并到本地
		fetch and merge remote to local 


* With __S__ub__V__ersio__N__

<pre>	
svnadmin create		git init --bare
svn checkout		git clone
svn update			git pull
svn revert			git reset git checkout --
					git [commit] checkout --
svn add				git add
svn rm				git rm
svn mv				git mv
svn diff			git diff 
						git diff --cached
					git diff HEAD
svn status			git status -s
svn commit -m ''	git commit -m '';git push
svn log				git log	
</pre>

* 保存当前工作进度

	+ git stash
		save work box to the stash
		保存进度

	+ git stash list
		显示进度列表
		list stash

	+ git stash apply
		恢复进度
		apply a single stashed state on the top of work box
	
	+ git stash pop
		从进度列表移动某个缓存覆盖工作区
		remove a single stashed state and apply it on the top of work box

	+ git stash clear
		删除所有存储的进度
		clean the stash
		
