sscanf uses the brackets to format string 
===========================================
sscanf 函数使用中括号格式化字符串
-------------------------------------------
在[]之中的字符串集合可以更好的格式化字符串
a set of characters in brackets ([ ]) can be substituted for the s (string) type character. The set of characters in brackets is referred to as a control string.


* [^characters]
匹配直到所有非此集合中的字符，直到此集合的字符出现为止。If the first character in the set is a caret (^), the effect is reversed: The input field is read up to the first character that does appear in the rest of the character set.


* [characters]
匹配直到出现未在此集合中出现的字符input field is read up to the first character that does not appear in the control string

<pre data-language="C">
#include <stdio.h>
int
main(int argc, char * * a rgv)
{
	char* s = "key= value ";
	char key[1024] = {0};
	char value[1024] = {0};
	char* digits = "pi3.1415926";
	sscanf(s, "%[^=]=%[^\0]", key, value);
	printf("%s\n%s\n", key, value);
	sscanf(digits, "%[abcdefghijklmnopqrstuvwxyz]%[1234567890.]", key, value);
	printf("%s\n%s\n", key, value);
	return 0;
}
</pre>

