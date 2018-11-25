# Tutorial based on Pycon 2017 videon on decorators:
# https://www.youtube.com/watch?v=UBSyD1RkOX0
# a better one:https://www.codementor.io/sheena/introduction-to-decorators-du107vo5c

# general outline of a decorator function
# def my_decorator(my_func):

# 	def new_function(*args,**kwargs):
# 		# some body of code will be done here
# 		# Probably with a call to my_func
# 		# Probably returning the value of my_func
# 	return new_function


# write a simple timer decorator
import time
from functools import wraps

def timer(func):
	@wraps(func) # name,docstring,etc copying!
	def new_timer_wrapper(*args,**kwargs):
		start = time.time()
		return_val = func(*args,**kwargs)
		end = time.time()
		print("Elapsed time is {:0.5f}".format(end-start))
		return return_val
	return new_timer_wrapper

@timer
def sample_function(**kwargs):
	return {v:k for k,v in kwargs.items()}


####################################################################

# def outer_decorator(*outer_args,**outer_kwargs):                            
#     def decorator(fn):                                            
#         def decorated(*args,**kwargs):                            
#             do_something(*outer_args,**outer_kwargs)                      
#             return fn(*args,**kwargs)                         
#         return decorated                                          
#     return decorator


# decorators with arguments
def check_user(user_type):
	def timer(func):
		@wraps(func) # name,docstring,etc copying!
		def new_timer_wrapper(*args,**kwargs):
			if user_type!="admin":
				raise "Access Denied"
			start = time.time()
			return_val = func(*args,**kwargs)
			end = time.time()
			print("Elapsed time is {:0.5f}".format(end-start))
			return return_val
		return new_timer_wrapper
	return timer

@check_user("admin")
def another_function(x,y):
	print(x**y)

@check_user("mansour")
def second_function(x,y):
	print(x**y + y**x)
   


# property decorator 
class A():
	def __init__(self,x):
		self._x = x

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self,new_x):
		self._x = new_x


def main():
	# x = another_function
	# print(x.__name__)
	# another_function(200,43)
	# print(sample_function(a=1,b=2,c=3))
	# second_function(100,300) raise an error
	print("hello","mansour","mehrjadi",sep="\t")



if __name__ == '__main__':
	main()