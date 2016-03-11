Flashes the specified window 
===========================================

## FlashWindow function ##


<pre data-language="C">
BOOL WINAPI FlashWindow(
  _In_ HWND hWnd,
  _In_ BOOL bInvert
);
</pre>


[FlashWindow in MSDN](https://msdn.microsoft.com/en-us/library/windows/desktop/ms679346.aspx)


[demo](https://github.com/codepongo/utocode/blob/master/windows/tFlashWindow.c)


<pre data-language="C">
//cl tFlashWindow.c && tFlashWindow.exe
#include <windows.h>
#pragma comment(lib, "User32.lib")
int main(int argc, char* argv[]) {
	HWND w = GetConsoleWindow();
	while(TRUE) {
		FlashWindow(w, TRUE);
		Sleep(700);
	}
	return 0;
}
</pre>


## FlashWindowEx function ##


<pre data-language="C">
BOOL WINAPI FlashWindowEx(
  _In_ PFLASHWINFO pfwi
);
</pre>


[FlashWindowEx in MSDN](https://msdn.microsoft.com/en-us/library/windows/desktop/ms679347.aspx)


[FLASHWINFO structure](https://msdn.microsoft.com/en-us/library/windows/desktop/ms679348.aspx)
