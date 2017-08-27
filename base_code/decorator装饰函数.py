import functools
'''
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
  

def log(text):
      def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                   print('begin call')
                   re=func(*args,**kw)
                   print('end call')
                   return re
            return wrapper
      return decorator(func=text) if callable(text) else decorator
@log
def f():
       print('@log')
@log('execute')
def f1():
       print('@log("execute")')
f()
f1()

'''
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s'%func.__name__)
		return func(*args,**kw)
	return wrapper

@log
def f():
	print('pass')

f()