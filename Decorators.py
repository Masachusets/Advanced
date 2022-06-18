import datetime
from functools import wraps
import pprint

# def decor(foo):
# 	def new_foo(*args, **kwars):
# 		print('Код до вызова функции')
# 		result = foo(*args, **kwars)
# 		print('Код после вызова функции')
# 		return result
#
# 	return new_foo


# def logger(log_path='log.log'):
def logger_simple(foo, log_path='log.log'):
	@wraps
	def new_foo(*args, **kwars):
		log_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		result = foo(*args, **kwars)
		with open(log_path, 'w') as log:
			log.write(f'{log_time}. {foo.__name__}{args, kwars}. Result: {result}')
		return result
	return new_foo

	# return logger_simple


@logger_simple
def some_fun(a, b):
	return a + b


print(some_fun(3, 4))
