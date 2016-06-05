import random
import time

def timerfunc(func):
	"""
	A timer decorator
	"""
	def function_timer(*args, **kwargs):
		"""
		A nested function for timing other functions
		"""
		start = time.time()
		value = func(*args, **kwargs)
