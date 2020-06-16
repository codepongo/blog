codepongo's blog
====

<http://codepongo.com/blog>
## Update
2020/06/16 blog can use the [webpy](https://webpy.org) as the web framework.

## Modules
* blog.py - Light weight blog system  
Base on [Kukkaisvoima](http://23.fi/kukkaisvoima) version 15b3TA.
[kukkaissvoima in github](https://github.com/Petteri/kukkaisvoima)
* cgiserver.py - a python http cgi server
  + pyftp.py - a ftp server  
  Base on [pyftpdlib](http://code.google.com/p/pyftpdlib/)
## Issues


## Test

### Comment
`blog/{entry}?postcomment` creates the comment
`blog/{entry}?admin` gos to the admin page
`blog/{entry}/?delcomment={comment_id}` gets the page to delete 
`blog/{entry}?deletecomment` posts the request to delete the comment.
`blog/{entry}/?unsubscrib={subscribe_id} cancels the subscribtion.

### RSS
`blog/feed` subscribes the blog
`blog/{category}/feed' subscribes the category

### Archive
`blog/archive` presents the whole entries.

### Category
`blog/categories` presents the whole tags
`blog/categories/{category}` presents the whole tags

### Search
`blog/search` searchs the keyword in both the entries and the comments.


### Blog

`blog/{categrory}?page=0`  and `blog/{categrory}` present the entries in the categroy

`blog/{entry} shows the entry.

### Captcha
`blog/captcha?{float} displays a captcha image.
`captcha.py` can check wether the captcha works or not.
`blog/captcha?{float}` can clear the cache.

## TODO
* code highlight: try 'pyments'


