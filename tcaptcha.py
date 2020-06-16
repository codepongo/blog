import anydbm
import os
import time
indexdir = 'temp'
print os.path.join(indexdir, 'captch.db')
captchadb = anydbm.open(os.path.join(indexdir,'captcha.db'), 'c')
print dir(captchadb)
for k in captchadb.keys():
    if k == '':
        print captchadb[k]
        del captchadb[k]
        break
    if time.time() - float(3600) > float(k):
        print k, captchadb[k]
print '======'
for k in captchadb.keys():
    print k, captchadb[k]
captchadb.close()

