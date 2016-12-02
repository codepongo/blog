最简单的ASP模型——ASP新闻发布系统
======================================


整理自百度空间，2006-08-07，发布。



## 一、文件结构 ##
<pre>
news-+admin-+add.asp 后台显示页面
     |      |
     |      +cklogin.asp 后台管理验证页面
     |      |
     |      +conn.asp 数据库连接
     |      |
     |      +del.asp 删除
     |      |
     |      +edit.asp 编辑
     |      |
     |      +login.asp 后台管理登录
     |      |
     |      +logout.asp 后台退出
     |      |
     |      +save.asp 保存
     |      |
     |      +write.html 写入界面
     |      
     +date--+news.mdb 数据库文件
     |     
     |
     +images+page.gif 图片
     |      
     +conn.asp 数据库连接
     |
     +index.asp 首页
     |
     +look.asp 显示页
     |
     +foot.asp include尾部文件
</pre>


## 二、文件内容 ##

### △news.mdb数据库文件 ###


```
news:表
id  自动
name  文本   发表新闻人的姓名
content  备注*   发表新闻的内容
count  数字   新闻被浏览的次数
time  日期/时间 新闻发表的时间
title  文本  新闻标题
```


### △conn.asp ###


```
<%
set db=server.createobject("adodb.connection")
db.open "DBQ="&server.mappath("date/news.mdb")&";driver={microsoft access driver (*.mdb)}"
%>
```


### △cklogin.asp ###
```
<%
name = trim(request.from("username"))
pwd = trim(request.from("password"))

if name = "" or pwd = "" then
  response.write"<script language = javascript>alter('输入完整信息 请返回');history.back(-1)</script>"
end if

if name = "admin" and pwd = "admin" then
  session("manager") = "yes" '设置服务器session
  response.redirect "add.asp"
else
  response.write "<script language = javascript>alter('密码输入错误');history.back(-1)</script>
end if
%>
```


### △logout.asp ###

```
<%
session("manager") = ""
response.redirect "../index.asp"
%>
```
</pre>

### △write.html ###
<pre>
 ---------------------------------
| 录入时间 __________（使用now录入）|
| 新闻标题 __________ 为TITLE      |
| 新闻内容 ---------- 为content    |
| 录入者   __________ 为name       |
|                                  |
|                                  |
|   确定         重写              |
-----------------------------------
</pre>


<pre>
<form name = "write" method = "post" action="save.asp">
<input name = "content" id = "content">
<textarea name = "name" type = "text" id = "name">
<input type = "submit" name = "submit" value="确定">
<input type = "submit" name = "submit2" value = "重置"><!-- ???这好象有问题 -->
</form>
</pre>

### △save.asp ###

```
<!-- #include file = "conn.asp" -->
<%
dim flag
flag = session("manager")
if flag = "" then
  response.redirect "login.asp"
end if

set rs = server.createobject("adodb.recordset")
sql = "select * from news"
rs.open sql,db,1,3
rs.addnew
rs("title") = trim(request.form("title"))
rs("name") = trim(request.form("name"))
rs("content") = server.htmlencode(request.form("content")) '字符串转化成html代码
rs("count") = 0
rs("time") = now()
rs.update
rs.close
set rs = nothing
response.redirect "add.asp"
%>

△add.asp
<!-- #include file = "conn.asp" -->
<%
dim flag
flag = session("manager")
if flag = "" then
response.redirect "login.asp"
end if

sql = "select * from news order by id desc" 'id降序排列
set rs = db.execute(sql)
%>
<table>
<%do while not rs.eof%>
 <tr>
  <td align = "center"><%=rs("id")%></td>
  <td><a href=../look.asp?id=<%rs("id")%> target = "_blank"><%=rs("title")%></a></td>
  <td><%=rs("time")%></td>
  <td align = "center"><a href=edit.asp?id=<%=rs("id")%>>编辑</a></td>
  <td align = "center"><a href=del.asp?id=<%=rs("id")%>>删除</a></td>
 </tr>
<%
rs.movenext
loop
%>
</table>
```

### △del.asp ###


```
<!-- #include file = "conn.asp" -->
<%
id = request.querystring("id")
delsql = "delete * from news where id="&id
db.execut(delsql)
response.redirect "add.asp"
%>
```


### △edit.asp ###
```
<!-- #include file = "conn.asp" -->
<%id = request.querystring("id")
set rs = server.createobject("adodb.recordset")
editsql = "select * from news where id = "&id
rs.open editsql,db,1,3

rs("title") = trim(request.form("title"))
rs("content") = server.htmlencode(request.form("content"))
rs("name") = trim(request.form("name"))
rs.update
response.redirect "add.asp"
end if
%>
```

### △index.asp ###
```
<!-- #include file = "conn.asp" -->
<%
sql = "select * from news order by id desc"
set rs = db.execute(sql)
%>
.
.
.
<% do while not rs.eof%>
<a href = look.asp?id=<%=rs("id")%> target = "_blank">
<%=rs("title") %>
</a>
(<%=rs("name")%>发表)浏览过<%=rs("count")%>次
<%
rs.movenext
loop
%>
```


### △look.asp ###



```
<!-- #include file = "conn.asp" -->
<%
'判断传递参数
if not isempty(request.querystring("id")) then
  id = request.querystring("id")
else
 id = 1
end if

function htmltotext(content) 'html转化为字符串
  htmlnr = content
  if content <> "" then
    htmlnr = replace(htmlnr,chr(13),"<br>")
    htmlnr = replace(htmlnr,chr(34),"&quot;")
    htmlnr = replace(htmlnr,chr(32),"&nbsp;")
  end if
end function

set rs = server.createobject("adodb.recordset")
sql = "select * from news where id = "&id
rs.open sql,db,1,3
rs("count") = rs("count") + 1
rs.update
%>
标题:<%=rs("title")%>
<%=rs("time")%>
该新闻已被浏览过<%=rs("count")%>次
作者:<%rs=("name")%>
<%=htmltotext(rs("content"))%> '???好象有问题吧...
<input type="button" name="submit" value="关闭窗口" onclick="javascript:window.close()">
```

