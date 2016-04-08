reverse static library in windows
=============================================
逆向windows静态库
---------------------------------------------
### list all objs in static library 列出静态库中所有obj###

lib staticlibrary.lib /List

### export obj from static library 导出指定的obj###

lib staticlibrary /EXTRACT:membername

### disassemble obj file 反汇编obj###

objdump -S membername.obj > membername.asm

