Roll Back with GIT GIT回滚
==============
* force reset to the version of the last two 
 取消当前版本之前的两次提交
<pre>
git reset --hard HEAD~2 
</pre>
* force push to the remote re
 强制提交到远程版本库，从而删除之前的两次提交数据
<pre>
git push origin HEAD --force
</pre>
