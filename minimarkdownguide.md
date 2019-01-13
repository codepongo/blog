Markdown Syntax Guide
======================

# Headers
## Setext

    This is an Main Title
    =====================
    This is an Sub Title
    ----------------------

## Atx-style headers

* This is an H1
* This is an H2
* This is an H3
* This is an H3
* This is an H4
* This is an H5
* This is an H6

# Lists

    * 壹
      + 壹 - 壹
        - 壹 - 壹 - 壹
        - 壹 - 壹 - 貳
      + 壹 - 貳
    * 貳
    * 叁
      1. 叁 - 壹
      2. 叁 - 貳
as:  

* 壹
    + 壹 - 壹
        - 壹 - 壹 - 壹
        - 壹 - 壹 - 貳
    + 壹 - 貳
* 貳
* 叁
    1. 叁 - 壹
    2. 叁 - 貳


# Emphasis
* _\_em\__
* **\*\*strong\*\***

# link
## automatic link

    <http://codepongo.com>
as:  
<http://codepongo.com>

## inline link

    [This](http://codepongo.com) is a link.
as:  
 [This](http://www.baidu.com) is a link.

## reference link
    [This][1] is a reference-style link.
    [1]: http://codepongo.com/ "codepongo"
as:  
[This][1] is a reference-style link.  
[1]: http://codepongo.com/ "codepongo"


# image

\!\[alt=markdown.jpg\](markdown.jpg)
as:   
 ![alt=markdown.jpg](markdown.jpg)

# paragraph

    $(linesep)
    this is in the first paragraph.
    $(linesep)
    this is in the second paragraph.$(blank)$(blank)
    this is in the third paragraph.
    this is in the third paragraph also.
    $(linesep)
    $(linesep)
    ...
as:  
this is in the first paragraph.

this is in the second paragraph.  
this is in the third paragraph.
this is in the third paragraph also.


...

# sample

------------------------------------------------------------------------------

Title
===========================

Sub Title
-------------------------------------------

# Section One

This is a Section Contents.
The second sentence is in the first paragraph.

The third line is in the second paragraph of the section one.  
I use the line break in the fourth sentence.


# Section Two

There is two lists in this section.

The below is unordered list:  

* 1
  + 1-1
    - 1-1-1
    - 1-1-2
  + 1-2
* 2
* 3
  + 3-1
 + 3-2

The ordered list is below:  

1. First
   1. First-One
   2. First-Two
2. Second
   1. Second-One
   2. Second-Two
more detail about Second-Two
there are some pagraph in Second-Two  
this is the second sentence, but there is only one pagraph in it.
3. Third


# Section Three

there is a long long long long long long long long long long long long  
long long sentence in this section.

there is a line break before the last two long

# Section Four

* [This][1] is a reference-style link.
* [This](http://codepongo.com) is a link.
* <http://codepongo.com>


# Section Five

there are two pargraphs in this section.  
this is one pargraph

this is the other pargraph


# Section Six
An image is in this section.  
![alt=markdown.jpg](markdown.jpg)


# Bibliography
<http://markdown.tw>  
<https://github.com/trentm/python-markdown2>  
<http://daringfireball.net/projects/markdown/syntax>  
<https://github.github.com/gfm/>
<https://spec.commonmark.org/>
