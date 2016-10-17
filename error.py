import logging

try:
	print 'try...'
	r=10/0
	print 'result:',r
except ZeroDivisionError, e:
	logging.exception(e)	 
finally:
	print 'finally...'
print 'end'	