Function Pointers To Malloc And Free
=========================================
Recently, I read the source of sqlite, cJSON and expat.
There is a structure in these source.
It looks like:
<pre>
typdef struct {
	void* (*mallocFn)(size_t s)
void ( * freenFn)(void * p)
} Mem;
</pre>
The structure has two function pointer members.
The one'type is the malloc function.The Other'type is the free function.


In the source, there is a function interface for set the function pointer.


When the program needs alloc and free memory, it calls the functions to be pointed
by the two members of the structure. 


In my opinion, there are three advantages:

* Check memory leak.To implement the malloc and free functions with mark a 
record.When the program is end, check the records to find out memory leak.(I often use it)

* Improve the performance.To implement the memory pool myself.(I never use it)

* Out-Of-Memory testing.(this advantage is found in sqlite document)
