def doubler(a_function):
	def wrapper_function(*args, **kwargs):
		a_function(*args, **kwargs)
		a_function(*args, **kwargs)
	return wrapper_function
