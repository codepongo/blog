终止用户会话 Terminate User Session
====================================
1. return user's terminal name


> tty 


2. display who is logged in and what they are doing


> w 


3. send a signal or report process status


> skill -KILL -v pts/\* 


4. signal processes based on name and other attributes


> pkill -9 -t pts/\*


