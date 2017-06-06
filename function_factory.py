def own_print(first):
	def add_arguments(second):
		return first + " it's " + second
	return add_arguments

func = own_print('foo')
print(func('bar'))