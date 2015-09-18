fix highlighted markdown files in Vim
=============================================
* syntax files loading procedurce
 + 1 $VIM/vimfiles/syntax/type.vim (~/.vim/syntax/type.vim)
 + 2 $VIMRUNTIME/syntax/type.vim
 + 3 $VIM/vimfiles/after/syntax/type.vim (~/.vim/after/syntax/type.vim)


**create markdown.vim in after/syntax**


* priority
When several syntax items may match, these rules are used:
 + 1 When multiple Match or Region items start in the same position, the item defined last has priority.
 + 2 A Keyword has priority over Match and Region items.
 + 3 An item that starts in an earlier position has priority over items that start in later positions.
<pre data-language="python">
syn region markdownItalic start="\S\@<=\*\|\*\S\@=" end="" keepend contains=markdownLineStart
syn region markdownItalic start="\S\@<=_\|_\S\@=" end="" keepend contains=markdownLineStart

</pre>


**in markdown.vim, add two lines above.**
