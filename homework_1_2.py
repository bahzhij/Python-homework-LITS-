str = '((((((((((((((2, 3)))))))))))))'
result_open = str.count('(')
result_closed = str.count(')')
if result_open == result_closed:
	print('Parentheses are balanced')
elif result_open < result_closed:
	print('Missing opening parenthesis')
else:
	print('Missing closing parenthesis')
