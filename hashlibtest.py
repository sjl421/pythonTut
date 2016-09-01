import hashlib

md5 = hashlib.md5()
md5.update('how to user md5 in python?')
print md5.hexdigest()