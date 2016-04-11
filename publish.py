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
    if len(sys.argv) == 4:
        img_path = mkdir(sys.argv[3])
    else:
        img_path = ''
    for f in os.listdir(source):
        name,ext = os.path.splitext(f)
        if ext in ['.md']:
            des = os.path.join(data_path, f)
            if not os.path.isfile(des):
                shutil.copy(os.path.join(source, f), des)
        if ext in ['.txt']:
            if sys.platform == 'linux2':
                new_name = f.replace('_', ':')
            else:
                new_name = f
            des = os.path.join(data_path, new_name)
            if not os.path.isfile(des):
                shutil.copy(os.path.join(source, f), des)
        if img_path != '':
            if ext in ['.png']:
                des = os.path.join(img_path, f)
                if not os.path.isfile(des):
                    shutil.copy(os.path.join(source, f), des)

if "__main__" == __name__:
    main()
