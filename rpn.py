#!/usr/bin/env python3

import operator
import math

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'.': operator.floordiv,
	'&': operator.and_,
	'|': operator.or_,
	'~': operator.not_,
	'!': math.factorial,
}

def calculate(arg):
	stack = list()
	numargs = 0
	for token in arg.split():
		try:
			value = int(token)
			numargs = numargs + 1
			stack.append(value)
		except ValueError:
			if numargs == 1:
				arg = stack.pop()
				if token == '%':
					result = arg / 100.
				else:
					function = operators[token]
					result = function(arg)
			else:
				function = operators[token]
				arg2 = stack.pop()
				arg1 = stack.pop()
				result = function(arg1, arg2)
			stack.append(result)
		#print(stack)
	if len(stack) != 1:
		raise TypeError

	return stack.pop()

def main():
	while True:
		print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
	main()

