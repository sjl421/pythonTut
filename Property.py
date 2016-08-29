class Stu(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 and 100')
        self._score = value

    def __str__(self):
        return 'student object name :%s' % self.score


s=Stu()
s.score=11
print s.score
print s

#iter
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return  self

    def next(self):
        self.a,self.b=self.b,self.a + self.b
        if self.a > 1000:
            raise StopIteration();
        return self.a

for n in Fib():
    print n

