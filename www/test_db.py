
from models import User, Blog, Comment
from transwrap import db

db.create_engine(user='*',password='*',database='awesome',host='192.168.166.30',port=3359)
u = User(name='Test',email='a@exapmle.com',password='111111',image='blank')
u.insert()

print 'new user id:',u.id

u1 = User.find_first('where email=?','a@exapmle.com')
print u1