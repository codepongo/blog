cJSON source analysis
=============================
## Introduction ##


cJSON paser with a single file of C, and a single header file.like description 
of README, the library can take away as much legwork and is the dumbest possible
parser.


homepage:[http://sourceforge.net/projects/cjson/?source=directory](http://sourceforge.net/projects/cjson/?source=directory)


mirror:[https://github.com/openxc/cJSON](https://github.com/openxc/cJSON)


license:**MIT**


the function of the cJSON library is that the string formatted json(JSON data) and 
the json structure(cJSON object) convert to each other.


## Notice ##

* **no** safe with multi-threads
* when cJSON\_Parse() and cJSON\_CreateXXX() functions are finished, call cJSON\_Delete to free.
* when cJSON\_PrintXXX() functions are finished, call Hooks::free\_fn to free.
* strdup() needs free.

## Structure ##
In README, the author introducts two way to use the libaray.one is AUTO mode and
the other is MANUAL mode.
There is a structure introduction in the manual mode part.
<blockquote>
Here's the structure:
typedef struct cJSON {
	struct cJSON *next,*prev;
	struct cJSON *child;

	int type;

	char *valuestring;
	int valueint;
	double valuedouble;

	char *string;
} cJSON;

By default all values are 0 unless set by virtue of being meaningful.

next/prev is a doubly linked list of siblings. next takes you to your sibling,
prev takes you back from your sibling to you.
Only objects and arrays have a "child", and it's the head of the doubly linked list.
A "child" entry will have prev==0, but next potentially points on. The last sibling has next=0.
The type expresses Null/True/False/Number/String/Array/Object, all of which are #defined in
cJSON.h

A Number has valueint and valuedouble. If you're expecting an int, read valueint, if not read
valuedouble.

Any entry which is in the linked list which is the child of an object will have a "string"
which is the "name" of the entry. When I said "name" in the above example, that's "string".
"string" is the JSON name for the 'variable name' if you will.

Now you can trivially walk the lists, recursively, and parse as you please.
You can invoke cJSON\_Parse to get cJSON to parse for you, and then you can take
the root object, and traverse the structure (which is, formally, an N-tree),
and tokenise as you please. 
</blockquote>


In fact, json structure is a tree, so cJSON struct is like the node of tree that
has child node pointer and sibling pointers
there are three type structure in json. those are object, number and string.
the type member is as the type in json. the type member'value are False, True, 
NULL, Number, String, Array and Object.
the value is stored in the one of valuestring, valueint and valuedouble by the type.

<pre>
 +------+          +-----+           +-----+
 |cJSON |---prev---|cJSON| ---next---|cJSON|
 +------+          +-----+           +-----+
                      |
                    child      
                      |        +-----+          +-----+          +-----+
                      +--------|cJSON|---prev---|cJSON|---next---|cJSON|
                               +-----+          +-----+          +-----+
</pre>


## Functions ##

print\_xxxx functions are convert json to string
parse\_xxxx functions are convert string to json

### convert functions ###
* cJSON\_strcasecmp() - strcmpcase()
* cJSON\_strdup() - strdup()
* parse\_number() - atoi() and atof() 
* print\_number() - itoa() and fto2()
* parse\_string() - to a unescape string
* print\_string() - to a unescape string
* print\_string\_ptr() - to a escape string

### parse functions ###
* skip() - trim invisible char such as whitespace cr lf
* parse\_value() - parse json token
* print\_value() - json to string
* parse\_array() - parse json array token
* print\_array() - json array to string
* parse\_object() 

### all function ###
* cJSON\_strcasecmp() - strcmpcase()
* cJSON\_strdup() - strdup()
* cJSON\_InitHooks() - set malloc and free
* cJSON\_New\_Item() - structure
* cJSON\_Delete()
* parse\_number() - atoi() and atof() 
* print\_number() - itoa() and fto2()
* parse\_string() - to a unescape string
* print\_string() - to a unescape string
* print\_string\_ptr() - to a escape string
* skip() - trim invisible char such as whitespace cr lf
* cJSON\_ParseWithOpts - return\_parse\_end:the point to the remain string require\_null\_terminated:there is no remain string or return error
* cJSON\_Parse() - string to json the same as cJSON\_ParseWithOpts(value, 0, 0)
* cJSON\_Print() - json to string
* cJSON\_PrintUnformatted() - json to unformatted string
* parse\_value() - parse json token
* print\_value() - json to string
* parse\_array() - parse json array token to string
* print\_array() - json array to string
* parse\_object() - string to json object
* print\_object() - json object
* cJSON\_GetArraySize() - json array size
* cJSON\_AddItemToArray() - add json to json array
* cJSON\_AddItemToObject() - add json to json object
* cJSON\_AddItemReferenceToArray() - add json to json array without clone
* cJSON\_AddItemReferenceToObject() - add json to json object without clone
* cJSON\_DetachItemFormObject
* parse\_object() 


## Process ##

parse\_value() - parse the type of json or call parse\_array() or parse\_object()
parse\_array() - in loop, parse call parse\_value() for every object in array.
parse\_object() - call parse self and loop to parse its childern by parse\_string


