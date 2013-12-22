Project-Generator
========================
## introduction ##

[https://github.com/Piot/Project-Generator](https://github.com/Piot/Project-Generator)

Project-Generator makes the native IDE project files.



it supports Visual Studio(windows), Xcode(mac os x), makefile(linux) and so on.


it likes the [GYP](https://code.google.com/p/gyp/).
but, it is smaller, simpler and easier to understand than GYP.
its config option in a XML file is more readable than GYP input format file.

## process in generate.py##
* parses arguments
* project module creates target project
* project parser module initials target project with xml node
* generator module write to the project files with project write module
## project ##
### project.py ###
* class SourceFileNode - all source files
* class Dependecy - dependent projects
* class Define - macros
* class Settings - project settings likes include paths, defines, dependecies, libraries,framewoorks and so on
* class configuration - inherit from Settings, it is a build Settings with a name such as "debug", "relase" and so on.
* class Project - the project object
* relationship
<pre data-language="C">
Project+- depandencies
       +- configurations
       +- settings-+-paths
                   +-defines
                   +-denpendecies
                   +-libraries
                   +-frameworks
</pre>
### project\_object.py ###
### project\_parser.py ###
initial project object with xml node
### project\_path.py ##
operation about paths
### project\_write.py ###
* class ProjectFileCreator:a Factory in where ProjectFileOutput is made.
* class ProjectOutput:a controller of project file's indent 
* class ProjectFileOutput:inherit from **ProjectOutput** wrapper of file operation

## generator ##
* codeblocks.py
* codelite.py
* makefile.py makefile in Linux platform
* visualc.py Visual Studio in Windows platform
* xcode.py Xcode in Mac OS X platform


