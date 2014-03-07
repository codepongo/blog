Combine some commits of GIT in one Git合并多条提交记录
=================================
## show commit count 显示提交记录数 ##
<pre data-language="Shell">
git rev-list HEAD --count
</pre>
## combine commit or modify commit message 合并或修改记录 ##
* command 命令
<pre data-language="Shell">
git rebase -i HEAD~$x
</pre>
其中$x代表你期望操作的记录数，小于提交记录数
$x is the count of commit that you want to combine or change,
$x is less than commit count


如 e.g.
> 你想操作最后十条，则$x为10 
if you want to change the last ten commits, the value of $x is 10.
<pre data-language="Shell">
pick 123456 init
pick 7890ab add text
pick cdef12 modify text
pick 345678 modify text

# Rebase abcdef..345678 onto abcdef
#
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out
</pre>


* edit 编辑


change the "pick" that is in front of the commit line to "s",
the commit will combine to previous commit.
在你期望合并的commit将前面的pick更改成s就行，
此条commit将于上一条commit合并


change the "pick to "r", the commit message will be modify.
pick改成r表示修改当前提交信息


e.g.例如：
> "pick 345678 modify text" --> "s 345678 modify text"


* change commit message after saving 保存后，重新编写提交信息
<pre>
 # This is a combination of 2 commits.
 # The first commit's message is:

 modify text

 # This is the 2nd commit message:

 modify text

 # Please enter the commit message for your changes. Lines starting
 # with '#' will be ignored, and an empty message aborts the commit.
 # HEAD detached at 8658d47
 # You are currently editing a commit while rebasing branch 'master' on 'ddcff57'.
 #
 # Changes to be committed:
 #   (use "git reset HEAD^1 <file>..." to unstage)
 #
 #	new file:   ignorelist
 #	modified:   README.md
 #
 # Untracked files:
 #   (use "git add <file>..." to include in what will be committed)
 #
</pre>
<pre>
 change text

 # Please enter the commit message for your changes. Lines starting
 # with '#' will be ignored, and an empty message aborts the commit.
 # HEAD detached from 18e598b
 # You are currently editing a commit while rebasing branch 'master' on 'ddcff57'.
 #
 # Changes to be committed:
 #   (use "git reset HEAD^1 <file>..." to unstage)
 #
 #	new file:   README.md
 #
 # Untracked files:
 #   (use "git add <file>..." to include in what will be committed)
 #
</pre>
* push 推送至远程
<pre>
git push -f
</pre>

