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
    data_path = mkdir(sys.argv[2])
    for f in os.listdir(source):
        name,ext = os.path.splitext(f)
        if ext in ['.md']:
            shutil.copy(os.path.join(source, f), os.path.join(data_path, f))
        if ext in ['.txt']:
            if sys.platform == 'linux2':
                new_name = f.replace('_', ':')
            else:
                new_name = f
            shutil.copy(os.path.join(source, f), os.path.join(data_path, new_name))

if "__main__" == __name__:
    main()
