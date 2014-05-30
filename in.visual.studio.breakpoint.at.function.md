In Visual Studio Breakpointing At Function
==========================================
menu: Debug - New Breakpoint(ctrl+B) vs菜单：调试 - 新断点（ctrl+B）
<pre>
Function:{,,dynamic.dll}_functionW@size
e.g.
{,,kernel32.dll}_CreateProcessW@40
</pre>
* dynamic is the DLL name dynamic为DLL名称
* **NOTICE** there is a underline at the front of 'function' 注意函数名前有下划线
* function is the function name function为函数名
* W/A is ascii or unicode function W/A为区别windows API的ascii和unicode版
* size is the size of all arguments of the function, [more(chinese)](http://blog.csdn.net/lcy9819/article/details/6542277) 
size为函数所有参数的字节数，[详细](http://blog.csdn.net/lcy9819/article/details/6542277)

for example 例如:


<pre data-language="c">
int
WINAPI
MessageBoxW(
    __in_opt HWND hWnd,
    __in_opt LPCWSTR lpText,
    __in_opt LPCWSTR lpCaption,
    __in UINT uType);
size = sizeof(HWND) + sizeof(LPCWSTR) + sizeof(LPCWSTR) + sizeof(UINT)
</pre>
so, the breakpoint at the 'messagebox' function is 
所以，messagebox函数的断点function应添为
<pre>
{,, User32.dll}_MessageBoxW@16
</pre>

## reference 参考##
[break point on create process](http://stackoverflow.com/questions/1130906/can-i-add-breakpoint-on-createprocess-in-vs)


[rule for function name](http://blog.csdn.net/lcy9819/article/details/6542277)
