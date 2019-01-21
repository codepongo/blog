Debug python Script with pdb
===
## Usage

### Launch

to debug a script, you can run

> python -m `script_to_debug.py` arguments

The program will break in the first line of the script.
pdb will automatically enter post-mortem debug and restart

### Insert Statment to Break the Running Script

> import pdb;pdb.set_trace()

if you want to suspend on exception in pdb, try post_mortem method

> import pdb;pdb.post_mortem()

### Configure

**.pdbrc** locates home folder or current folder  
aliases is in this file

to include py script into my.pdbrc, use execfile() to run a file containing your Python code.

#### .pdbrc

<pre>
<code data-language="python">
#Print a dictionary, sorted. %1 is the dict, %2 is the prefix for the names.
alias p_ for k in sorted(%1.keys()): print "%s%-15s= %-80.80s" % ("%2",k,repr(%1[k]))

#Print the member variables of a thing.
alias pi p_ %1.__dict__ %1.

#Print the member variables of self.
alias ps pi self

#Print the locals.
alias pl p_ locals() local:

#Next and list, and step and list.
alias nl n;;l
alias sl s;;l

execfile(".pdbrc.py")
</code>
</pre>


#### pdbrc.py
in the same directory as the .pdbrc

<pre>
<code data-language="python">
print ".pdbrc.py"
</code>
</pre>

## Command
Arguments to commands must be separated by whitespace  
multiple commands may be entered on a single, sparated by **;;**
### Help
* h(elp) [command]

### Stack Frames
* w(here)
* d(own)
* u(p)

### Breakpoints
* b(reak) [filename:]:lineno | function[, condition]]  
without argument, list all breaks
* tbreak [filename:]:lineno | function[, condition]] 
* cl(ear)  [filename:]:lineno | function[, condition]] 
* disable [bpnumber [bpnumber ...]]
* enable [bpnumber [bpnumber ...]]
* ignore bpnumber [count]
* condition bpnumber [condition]
* commands [bpnumber]
  
### Evaluation
* s(tep)
* n(ext)
* unt(il)
* r(eturn)
* c(ont(inue))
* j(ump) lineno

### View
* l(ist) [first[, last]]
* a(rgs)
* p expression

### Macro
* alias [name [command]]
* unalias name



## PDB Source Code

Three main classes in this module, the pdb uses the modules bdb and cmd.

* cdb.py
* cmd.py
* pdb.py

## Bibliography
<https://nedbatchelder.com/blog/200704/my_pdbrc.html>  
<https://wiki.python.org/moin/PdbRcIdea>  
<https://stackoverflow.com/questions/44155444/how-to-write-a-working-pdbrc-file>  
<https://docs.python.org/2/library/pdb.html>
<https://stackoverflow.com/questions/45446944/suspend-on-exception-in-pdb>

