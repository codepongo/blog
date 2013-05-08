# -*- coding:utf-8 -*-

# Config variables
# Url of the blog (without trailing /)
baseurl = 'http://127.0.0.1:8000/blog'
# Use absolute url for this, like http://yourdomain/blog/kukka.css
stylesheet = '/concise.css'
# Use absolute url for this, like http://yourdomain/blog/feed-icon-14x14.png
feedicon = '/feed-icon-14x14.png'
blogname = 'CodePongo'
slogan = ''
description = ""
encoding = 'utf-8'
defaultauthor = 'zuohaitao'
favicon = 'http://127.0.0.1:8000/favicon.ico'
doctype = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'
# Email to send comments to
blogemail = ''
# Language for the feed
language = 'zh_cn'
# Number of entries per page
numberofentriesperpage = 5
# Directory which contains the blog entries
datadir = '.'
# Directory which contains the index and comments. Must be script
# writable directory
indexdir = 'temp'
# Maximum comments per entry. Use -1 for no comments and 0 for no
# restriction
maxcomments = 30
# answer to spamquestion (question variable is l_nospam_question)
nospamanswer = '5'
# This is admin password to manage comments. password should be
# something other than 'password'
passwd = 'p'
# New in version 10
sidebarcomments = True
# Gravatar support (picture in comments according to email), see
# http://gravatar.com for more information
gravatarsupport = False
# Entry and comment Date format
dateformat = "%Y-%m-%d %H:%M:%S"
# Show only first paragraph when showing many entries
entrysummary = False
# New in version 15
shorturl = True
#data file name delimiter
delimiter = '_'
#google analytics
google_analytics_script = """\
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-39694782-1', 'codepongo.com');
  ga('send', 'pageview');
</script>"""

#google adsense
google_adsense_script = """"""
# Number of visible categories in sidebar
numberofvisiblecategories = 50

