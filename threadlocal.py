import threading

local_school = threading.local()

def process_student():
    print 'hello %s in (%s)' % (local_school.student, threading.currentThread().name)

def process_thread(name):
    local_school.student=name
    process_student()

t1 = threading.Thread(target=process_thread,args=('a',), name='thraed-a')
t2 = threading.Thread(target=process_thread,args=('b',),name='thread-b')
t1.start()
t2.start()
t1.join()
t2.join()