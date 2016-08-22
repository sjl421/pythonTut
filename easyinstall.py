import os
file_name = 'ez_setup.py'
from urllib import urlopen
data = urlopen('http://peak.telecommunity.com/dist/ez_setup.py')
with open(file_name, 'wb') as f:
    f.write(data.read())
os.system('python %s' % (os.path.join(os.getcwd(),file_name)))