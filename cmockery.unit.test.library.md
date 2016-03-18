C语言 单元测试框架 —— Cmockery
================================


[Cmockery](https://github.com/google/cmockery)是google开源的一套C语言单元测试框架。


## 选择原因 ##
正如编写这个框架的动机，选择这个测试框架的原因在于
__兼容性好__ 、**耦合度低** 、**不依赖外部库** 。总得来说，就是简单！


## 功能 ##
按照功能，可分为四个模块


### test execution 测试运行模块 ###


测试单元用例是以函数形式给出
<pre data-language="c">
void test_function(void** state) {
}
</pre>


然后，将其添加到一个测试单元组当中，测试单元组为一个数组
<pre data-language="c">
const UnitTest tests = {
	unit_test(test_function),
};
</pre>


运行测试
<pre data-language="c">
run_tests()
</pre>


如果出现异常，则程序会中断测试。如果发生错误，输出相关信息后继续执行下一条单元测试用例。


### assertion 断言 ###

<pre>
expect_assert_failure():类似于C语言中的assert

assert_{type}_equal(), assert_{type}_equal:用于检查运行结果。

expect_{type}()，用于函数输入参数和测试用例的检查
</pre>


### Dynamic Memory Allocation 内存泄漏检查 ###


用于宏定义的方式重新定义C运行库的内存管理函数，通过在申请内存时，加入信息头记录在链表当中的方式检测内存泄漏。


### Mock 模拟测试 ###

1. 重写待测试中需要进行模拟测试的函数
2. 在重写模拟测试函数中调用mock()
3. 调用函数前，先用will_return()指定，返回值
<pre data-language="C">
//1
int* need_to_mock() {
	//2
	return (int*)mock();
}
int* want_to_test_func() {
	return need_to_mock();
void test_function(void** state) {
	//3
	will_return(want_to_test_func, 0x2046);
	assert_true(want_to_test_func() == 1);
}
int main(int, char**) {
	const UnitTest u[] = {
		unit_test(test_function),
	}
	return run_tests(u);
}
</pre>


### State 环境状态 ###

通过unit\_test\_setup\_teardonw可以在单元测试运行之前改变（预装载）和恢复环境状态（测试后卸载）。


## Problem 存在的问题 ##


* 在内存检测部分，没有对realloc函数进行处理，导致在有realloc调用的时候程序崩溃
此问题在[cmocka](https://cmocka.org)已被解决。
* free(0),释放一个空指针程序将崩溃，在test_free中加入判空操作。

[this is my fork that fixes those problems above](https://github.com/codepongo/cmockery)

## reference ##

[什么是mock测试](http://stackoverflow.com/questions/2665812/what-is-mocking)
[用cmockery做mocking测试](http://tonybai.com/2009/08/22/introduce-cmockery-for-c-unit-test/)
