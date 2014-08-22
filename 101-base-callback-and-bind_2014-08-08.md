callback and bind
======================

## 文档 ##
base/callback.h中注释
## 作用 ##
参数传递与函数调用分离，可异步调用
task包装callback通过message传递给另一线程执行
## 功能 ##
callback本质上是对函数指针的封装，bind是把成员函数，函数等转化成callback对象。
## 关键对象 ##
BindState<>由bind创建，callback保持。
## 产生 ##
bind系列和callback系列都是由pump.py通过xxx.x.pump生成的。
## 限制 ##
bind最多支持7个参数的函数转换。
类成员函数指针
<pre data-language="csharp">
#include <stdio.h>
class C;
class C {
public:
	void print(int x) {
		printf("%d\n", x);
	};
	int add(int x, int y) {
		return (x + y);
	};
};
int
main(int argc, char* argv[])
{
	C c;
	C* pc = new C();
	int (C::*add)(int,int);
	typedef void (C::*PF)(int);
	PF print = &C::print;
	add = 0;
	add = &C::add;
	int i = (c.*add)(5,6);
	(pc->*print)(i);
	return 0;
}

</pre>
