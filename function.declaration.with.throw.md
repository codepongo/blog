C++函数声明中带用throw关键字
===================================
function declaration with throw
-------------------------------

* void f() throw() // **no** exceptions allowed 不允许抛出任何异常
* void f() throw(...) // **all** exceptions allowed 允许抛出任何异常

* void f() throw(type) // **only** the exception of type *type* allowed 只允许抛出type类型的异常

