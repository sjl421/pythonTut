import functools

#变量可以指向函数
f = abs
print f(-10)

#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
#高阶函数
def add(x,y,f):
	return f(x) + f(y)

print add(-5,-8,abs)

#map/reduce
def f(x):
	return x * x

print map(f,[1,2,3,4,5,6])

print map(str,[1,2,3,4,5,6])

#reduce
def add(x,y):
	return x + y

print reduce(add,[1,3,5,7,9])

def str2int(s):
	def fn(x,y):
		return x*10 + y
	def char2num(s):
		return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
	return reduce(fn,map(char2num,s))
print str2int('12333')

def char2num1(s):
	return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
def str2int1(s):
    return reduce(lambda x,y:x*10+y,map(char2num1,s))	
print str2int1('122222')

#filter
def is_odd(n):
	return n % 2 == 1
print filter(is_odd,[1,2,3,4,5,6,7,8])

def not_empty(s):
	return s and s.strip()

print filter(not_empty,['A',' ','bv',None,'  '])

#sorted
print sorted([33,5,7,8,22])

def reverse_cmp(x,y):
	if x > y:
		return -1
	if x < y:
		return 1
	return 0	
print sorted([33,5,7,8,22],reverse_cmp)

#函数作为返回值 闭包（Closure）
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax = ax + n
		return ax
	return sum		
f=lazy_sum(1,3,4,6,7)
print f
print f()

#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1,f2,f3=count()
print f1()
print f2()
print f3()

#匿名函数
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。		
print map(lambda x:x*x,[1,3,5,7,9])

#装饰器
def log(func):
	def wrapper(*args,**kw):
		print 'call %s():' % func.__name__
		return func(*args,**kw)
	return wrapper


def log1(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call %s():' % func.__name__
		return func(*args,**kw)
	return wrapper	

def log2(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
		    print 'call %s %s():' % (text,func.__name__)
		    return func(*args,**kw)
		return wrapper
	return decorator	


@log2('execute')
def now():
	print '2016-08-24'
now()

#偏函数
#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

int2=functools.partial(int,base=2)
print int2('100000')
