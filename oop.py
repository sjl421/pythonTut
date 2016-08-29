class Student(object):
	"""docstring for Student"""
	def __init__(self, name,score):
		super(Student, self).__init__()
		self.__name = name
		self.__score = score

	def print_score(self):
	    print '%s : %s' % (self.__name,self.__score)	

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score



#访问限制
#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问		


#继承和多态
#在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
class Animal(object):
	def run(self):
		print "Animal is running ..."

class Dog(Animal):
	def run(self):
		print "Dog is running ..."
class Cat(Animal):
	def run(self):
		print "Cat is running ..."

dog=Dog()
cat=Cat()
dog.run()
cat.run()		


#获取对象信息
print type(123)
print type('int')
print type(None)
print type(abs)

		
print len('abc')
print 'abc'.__len__()

#使用@property
class Stu(object):

    @property
    def score(self):
        return self._score

	@score.setter	
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 and 100')
		self._score=value
			


