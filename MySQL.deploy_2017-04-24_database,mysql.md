部署mysql
=====================================


## 版本 ##


<pre>
>bin\mysqld.exe --version
bin\mysqld.exe  Ver 5.7.18 for Win32 on AMD64 (MySQL Community Server (GPL))
</pre>


## 配置 ##


<pre>
[mysqld]
basedir = "d:\\mysql"
datadir = "d:\\mysql\\data"
</pre>


## 初始化 ##


<pre>
>bin\mysqld.exe --console --initialize-insecure
</pre>


## 启动 ##


<pre>
>bin\mysqld.exe --console
</pre>


## 登录 ##


<pre>
>bin\mysql -u root --skip-password
</pre>


## 修改root密码 ##


<pre>
>alter user 'root'@'localhost' identified by 'password';
</pre>


## 建立用户 ##


<pre>
>bin\mysql -u root -p
>create user 'username'@'%' indentified by 'password'
</pre>


## 创建数据库 ##


<pre>
create database db;
</pre>


## 提权 ##


<pre>
grant all privileges on db.* to username;
flush privileges;
</pre>


## 允许root远程 ##


<pre>
grant all privileges on *.* to 'root'@'%' identified by 'password';
</pre>
