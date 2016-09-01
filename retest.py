import re

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

if re.match(r'^\d{3}\-\d{3,8}$', '010-12345') :
    print 'ok'
else:
    print 'failed'

print re.split(r'\s+', 'a b   c')

print re.split(r'[\s\,]+', 'a,b, c  d')

print re.split(r'[\s\,\;]+','a,b;c d')

#Group regex
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m.group(0)
print m.group(1)
print m.group(2)

print re.match(r'^(\d+)(0*)$','102300').groups()
print re.match(r'^(\d+?)(0*)$','102300').groups()

print re_telephone.match('010-12345').groups()
print re_telephone.match('012-1234567').groups()