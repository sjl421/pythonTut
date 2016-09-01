import codecs
import json
try:
    import cPickle as pickle
except ImportError:
    import  pickle

d = dict(name='bobo', age=11, score=100)
print pickle.dumps(d)
f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()
ff = open('dump.txt','rb')
dd = pickle.load(ff)
ff.close()
print dd

print json.dumps(d)
print json.loads(json.dumps(d))


# with open('D:\coding\pythonTut\oop.py', 'r') as f:
#     print f.read(6)
# with open('D:\\test.jpg', 'rb') as ff:
#     print ff.read(256)
#
# with codecs.open('D:\\coding\pythonTut\gbk.txt', 'r', 'gbk') as fff:
#     print fff.read()
#
# with codecs.open('D:\\coding\pythonTut\utf8.txt', 'w', 'utf-8') as ffff:
#     ffff.write('hello world')