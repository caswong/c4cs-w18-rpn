import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_adds(self):
		result = rpn.calculate('1 1 + 2 +')
		self.assertEqual(4, result)
	def test_subtract(self):
		result = rpn.calculate('5 2 -')
		self.assertEqual(3, result)
	def test_toomany(self):
		with self.assertRaises(TypeError):
			result = rpn.calculate('1 2 3 +')
	def test_mult(self):
		result = rpn.calculate('2 3 *')
		self.assertEqual(6, result)
	def test_divide(self):
		result = rpn.calculate('9 3 /')
		self.assertEqual(3, result)
	def test_exp(self):
		result = rpn.calculate('5 2 ^')
		self.assertEqual(25, result)
	def test_intdiv(self):
		result = rpn.calculate('10 3 .')
		self.assertEqual(3, result)
	def test_percent(self):
		result = rpn.calculate('75 %')
		self.assertEqual(0.75, result)
	def test_and(self):
		result = rpn.calculate('1 0 &')
		self.assertEqual(0, result)
	def test_or(self):
		result = rpn.calculate('1 0 |')
		self.assertEqual(1, result)
	def test_not(self):
		result = rpn.calculate('0 ~')
		self.assertEqual(1, result)
	def test_factorial(self):
		result = rpn.calculate('4 !')
		self.assertEqual(24, result)
