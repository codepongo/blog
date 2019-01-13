#encoding:utf8
import markdown2
import sys
import os
def convert(markdown, html):
    print markdown, '->', html
    with open(markdown, 'rb') as r:
        md = r.read()
    with open(html, 'wb') as f:
        html = markdown2.gfmarkdown(md)
        html = html.replace('<img src="', '<img src="/')

        html = html.replace('\n</code></pre>', '</code></pre>')
        f.write(html.encode('utf-8'))
        f.write('\n#html')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage:python md2html.py source.md target.txt'
        sys.exit(-1)
    convert(sys.argv[1], sys.argv[2])
