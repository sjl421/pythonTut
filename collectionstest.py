#namedtuple
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print p.x
print p.y

q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print q

dd = defaultdict(lambda : 'N/A')
dd['k1'] = 'abc'
print dd['k1']
print dd['k2']

d = dict([('a',1),('b',2),('c',3)])
print d
od = OrderedDict([('a',1),('b',2),('c',3)])
print od

c = Counter()
for ch in 'Programming':
    c[ch] = c[ch] + 1

print c