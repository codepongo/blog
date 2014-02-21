The Cahche module in Planet
====================================
##modules ##

<pre data-language="C">
+--------------+       +-----+
|planet.Channel|-+-is--|cache|
+----------+---+  \    +-----+
            \      \         +------+
             \      +-have-+-|dbhash|
              \           /  +------+
                +--------+
</pre>
### dbhash ###



Planet(http://www.planetplanet.org/) uses the hashdb module to cache the feeded
data.


The **dbhash** module provides a function to open databases using the BSD db library. 
This module mirrors the interface of the other Python database modules that 
provide access to DBM-style databases. The bsddb module is required to use dbhash.

<pre data-language="python">
"""output the hashdb"""
import sys
import dbhash
db = dbhash.open(sys.argv[1], 'r')
print db.first()
for i in xrange(1, len(db)):
    print db.next()
db.close()
</pre>

The **dbm** library was a simple database engine, originally written by Ken Thompson 
and released by AT&T in 1979. The name is a three letter acronym for database 
manager, and can also refer to the family of database engines with APIs and 
features derived from the original dbm.

## planet.Channel and cache modules ##


the module description is very clear and easy to know, so you can use 
[help()](http://www.python.org/doc//current/library/functions.html#help) to
show the module description and read it.


## database file ##
the database is key/value database
* " keys" is the key of the root item. 

* the root item's value is the keys of the channel properties that is splited 
by blank space. 

* the key in that there is not blank space is the key of the news item. 

* the news item's value is the keys of the news properties that is splited 
by blank space.

* the news property's key is the unit of the news item's key and the part of the
news item's value.

* the channel property item and the news property item the key of that includes
the string " type" is provided the type of the news property's value.

For example:
the RSS:
<pre data-language="xml">
<?xml version="1.0" encoding="utf-8"?>
<rss>
<channel>
<title>CodePongo: json</title>
<lastBuildDate>Thu, 22 Aug 2013 18:16:02 +0200</lastBuildDate>
<item>
<title><h1>cJSON source analysis</h1> </title>
</item>
</channel>
</rss>
</pre>


the database:


<pre data-language="C">
(' keys', 'lastbuilddate title')
('lastbuilddate type', 'string')
('lastbuilddate', 'Thu, 22 Aug 2013 18:16:02 +0200')
('title type', 'string')
('title', 'CodePongo: json')
('http://codepongo.com/blog/3uhyc1/ title type', 'string')
('http://codepongo.com/blog/3uhyc1/ title', '<h1>cJSON source analysis</h1>')
('http://codepongo.com/blog/3uhyc1/', 'title')
</pre>

## reference ##


[planet home page](http://www.planetplanet.org/)


[planet introduction](http://simple-is-better.com/project/planet)


[dbhash module](http://www.python.org/doc//current/library/dbhash.html)
[database](http://en.wikipedia.org/wiki/Trivial_Database)
