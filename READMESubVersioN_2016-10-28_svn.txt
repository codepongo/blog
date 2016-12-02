<h1> SVN tutorial</h1>

2008-12-15 发布


一、创建库
zuohaitao@jack:~$ svnadmin create ~/svndb_t
二、修改库配置
zuohaitao@jack:~$ gvim ~/svndb_t/conf/passwd
[user]section下增加
zuohaitao = zuohaitaossecret
zuohaitao@jack:~$ gvim ~/svndb_t/conf/svnserve.conf
[general]下行去掉注释
password-db = passwd
三、启动svnserve(使用svn协议)
zuohaitao@jack:~$ svnserve -d -r ~/svndb_t
四 、导入一个项目
推荐版本布局
/trunk
/branches
/tags
zuohaitao@jack:~$ svn import ~/svnpoject_t svn://localhost/svnproject_t
其中 ~/svnpoject_t是一个目录 svn://localhost/svnproject_t是服务器保存路径
五、检出项目
svn checkout svn://localhost/svndb_t/svnproject_t ~/sandbox_t
六、日常操作
＊更新
 svn update
zuohaitao@jack:~/sandbox_t$ svn update -r N
其中N为版本号
＊修改
 svn add
 svn delete
 svn copy
 svn move
＊校验修改
 svn status
 svn status -v
 svn diff
＊取消修改
 svn revert
＊冲突
 svn update
 svn resolved
＊提交
 svn commit
七、删除库
rm -rf ~/svndb_t
八、停止svnserve
ps -ef
kill PID
其中PID为svnserve的进程ID

