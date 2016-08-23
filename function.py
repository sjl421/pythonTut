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

