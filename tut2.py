age=20
if age >= 6:
	print 'teenager'
elif age >=18:
    print 'adult'
else:
    print 'kid'    

names=['a','b','c']
for name in names:
    print name

sum=0
for x in range(101):
    sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

def my_abs(x):
	if not isinstance(x,(int)):
		raise TypeError('bad')
	if x>=0:
		return x
	else:
		return -x

print my_abs(-6)  
#my_abs('abc')        
import math
def move(x,y,step,angle=0):
	nx= x + step*math.cos(angle)
	ny= y - step*math.sin(angle)
	return nx,ny
x,y=move(100,100,60,math.pi/6)	
print x,y


def enroll(name,gendar,age=6,city="beijign"):
	print 'name:',name
	print 'gendar:',gendar
	print 'age:',age
	print 'city:',city
enroll('kk','M')
enroll('mm','f',7)
enroll('ppp','M',city='tinajin')

#可变参数
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print calc(1,2)
print calc(1,2,3)
nums=[1,2,3,4]
print calc(*nums)

#关键字参数
def person(name,age,**kw):
    print 'name:',name,'age:',age,'other:',kw
person('aaa',20)

#递归
def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)
print fact(5)		
print fact(100)
