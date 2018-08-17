import sys
import os
import markdown2

def convert(f):
    name, suffix = os.path.splitext(f)
    with open(f, 'rb') as r:
        md = r.read()
        r.close()
    with open(name + '.txt', 'wb') as f:
        html = markdown2.markdown(md)
        html = html.replace('<img src="', '<img src="/')
        f.write(html.encode('utf-8'))
        f.write('\n#html')
        f.close()

if '__main__' == __name__:
    convert(sys.argv[1])
