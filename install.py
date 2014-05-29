import sys
import os
import shutil

def mkdir(path):
    try:
        os.makedirs(path)
    except:
        pass
    return path

def main():
    source = mkdir(sys.argv[1])
    html_path = mkdir(sys.argv[2])
    cgi_path = mkdir(sys.argv[3])
    data_path = mkdir(sys.argv[4])
    for f in os.listdir(source):
        name,ext = os.path.splitext(f)
        if ext in ['.jpg', '.png', '.css', '.ico']:
            shutil.copy(os.path.join(source, f), os.path.join(html_path, f))
        elif f == 'rainbow':
            shutil.copytree(os.path.join(source, f), os.path.join(html_path, f))
        elif ext == '.py':
            if f in ['cgiserver.py', 'blog_setting.py']:
                continue
            shutil.copy(os.path.join(source, f), os.path.join(cgi_path, f))
        elif f == 'letters.bmp':
            shutil.copy(os.path.join(source, f), os.path.join(cgi_path, f))
        elif ext in ['.md']:
            shutil.copy(os.path.join(source, f), os.path.join(data_path, f))
        elif ext in ['.txt']:
            if sys.platform == 'linux':
                new_name = f.replace('_', ':')
            else:
                new_name = f
            shutil.copy(os.path.join(source, f), os.path.join(html_path, new_name))
        else:
            print os.path.join(source, f)

if "__main__" == __name__:
    main()
