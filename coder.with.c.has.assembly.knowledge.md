C程序员的基础汇编知识
============================
## 堆和栈的布局 ##
<pre data-language="C">
+--------------------+ <----高地址
|       ...          |        
+--------------------+ <----栈起始地址
|   栈向低地址增长   |        
|         V          |        
|      自由空间      |        
|         ^          |        
|   堆向高地址增长   |        
+--------------------+ <----堆起始地址
|全局变量            |
|.data已初始化       |
|.bss未初始化        |        
+--------------------+        
|      ...           |        
+--------------------+ <-----低地址
</pre>
## 80X86 32位CPU寄存器 ##
* 数据寄存器:EAX EBX ECX EDX
* 变址寄存器:ESI EDI
* 指针寄存器:ESP EBP
* 段寄存器:ES CS SS DS FS GS
* 指令急诊寄存器:EIP
* 标志寄存器:EFlags

## 函数调用的出入栈保护 ##


堆栈平衡:函数调用前后ESP值是一样的,本质上是保证EIP的一致


<pre data-language="C">
call address
address:
 push ebp;esp向下偏移4字节;将ebp的值拷贝至新esp位置
 mov ebp, esp;
 ...
 pop ebp
 ret
</pre>
* call address - 函数调用后esp位置存的是eip地址
* 进入函数后保存ebp值至栈
* 使ebp为esp此后可随意改变esp和便于使用ebp进行栈内寻址


## 条件跳转 ##


ZF(zero flag)= EFlags第六位
CF(carry flag)=EFlags第零位


* jmp jump
* je,jz jump if (equal) zero 等于则跳转 ZF=1
* jne,jnz jump if not (equal) zero 不等于则跳转 ZF=0
* jb jump if below 小于则跳转CF=1
* jnb jump if not below 不小于则跳转 CF=0
* ja jump if above 大于则跳转 CF=0且ZF=0
* jna jump if not above 不大于则跳转 CF=1或ZF=1

## 函数调用/返回##
* call address相当于push eip和jump address
* ret 相当于pop eip
* push xxx 相当于sub esp,4和mov esp,xxx
* pop xxx 相当于mov [esp], xxx和add esp,4

## 栈上变量 ##
<pre data-language="C">
push ebp
mov ebp,esp
sub esp,048;栈上开辟空间存局部变量和寄存器值
push ebx
push esi
push edi
lea edi,[ebp-0C0h];起始
mov ecx,30h;被重复执行次数
mov eax,0CCCCCCCCh
rep stos dword ptr es:[edi] ;rep指令的目的是重复其上面的指令STOS指令的目的是将eax中的值拷贝到ES:EDI指向的地址.
</pre>


初始化堆栈和分配局部变量,向分配好的局部变量空间放入int3中断,防止栈上内容被意外执行。


## 参考 ##
[http://stackoverflow.com/questions/4024492/can-anyone-help-me-interpret-this-simple-disassembly-from-windbg](http://stackoverflow.com/questions/4024492/can-anyone-help-me-interpret-this-simple-disassembly-from-windbg)
