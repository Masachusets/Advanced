import datetime
from functools import wraps


def logger(log_path='log.log'):
	def logger_simple(foo):
		@wraps(foo)
		def new_foo(*args, **kwargs):
			log_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			result = foo(*args, **kwargs)
			with open(log_path, 'a') as log:
				log.write(f'{log_time}. {foo.__name__}{*args, *kwargs.items()}. Result: {result}\n')
			return result
		return new_foo
	return logger_simple

