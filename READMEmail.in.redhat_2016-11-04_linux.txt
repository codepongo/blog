<h1>RHEL中mail的使用</h1>

2009-03-21 publish in 百度空间

1、SendMail
	$>mail -s "title" usrname
	text
	.<退出编译>
	Cc:

	$>mail -s "title" usrname < text.mail


2、RecvMail

	$>mail
	"/var/spool/mail/root": 1 message 1 unread
	>N 1 xxxxxxxx@localho ......
	&1
	q "quit and move to ~/mbox"
	x "quit"

参考：
[1]http://www.mqney.com/archives/001859.html
[2]《rh033－unit5》:http://v.youku.com/v_playlist/f1528851o1p5.html
