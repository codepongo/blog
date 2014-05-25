#!/bin/sh
#html
if [ ! -d "$1" ];then
	mkdir $1
fi
cp *.jpg $1
cp *.png $1
cp *.css $1
cp *.ico $1
cp -r rainbow $1
#cgi-bin
if [ ! -d "$2" ];then
	mkdir $2
fi
cp *.py $2
cp -r pyftpdlib $2
#data 
if [ ! -d "$3" ]; then
	mkdir $3
fi
cp *.md $3
cp *.txt $3
