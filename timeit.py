import time
def calculate_time(any_function):
	def wrapper_function(*args, **kwargs):
		a=time.time()
		output=any_function(*args, **kwargs)
		b=time.time()
		c=b-a
		print(f"Total time {c}")
		return output
	return wrapper_function
