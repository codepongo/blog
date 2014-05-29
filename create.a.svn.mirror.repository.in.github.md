Create a Subversion Mirror Repository In Github
=========================================
在Github上建立一个SVN的镜像库
-----------------------------------------
1.[Create repository 创建库](http://codepongo.com/blog/4WiIFW)


2.clone the git repository 克隆代码至本地
<pre data-language="shell">
$git clone git@github.com:user-name/repository-name
</pre>


3.set svn as a remote repository 把svn仓库添加为远程仓库
<pre data-language="shell">
$git svn init -T http://url/svn/trunk/
</pre>


4.fetch 获取svn仓库的代码
<pre data-language="shell">
$git svn fetch
</pre>


5.show all branch 显示所有分支
<pre data-language="shell">
$git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
  remotes/origin/trunk
</pre>
remotes/trunk is the svn branch 其中，remotes/trunk为svn分支


6.merge 合并svn分支
<pre data-language="shell">
$git merge trunk
</pre>


7.push 推送至github
<pre data-language="shell">
$git push
</pre>

## refference ##
[在GitHub上建立一个SVN仓库的镜像](http://blog.yesmeck.com/archives/create-svn-mirror-on-github/)
