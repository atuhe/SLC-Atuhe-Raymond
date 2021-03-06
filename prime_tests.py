import unittest
import prime_Number as prime_function


class PrimeTest_case(unittest.TestCase):
	def setUp(self):
		self.value = prime_function.prime_number_generator(10)

	def testing_lists_return_type(self):
		self.assertIsInstance(self.value, list)

	def testing_typeInteger(self):
		for x in self.value:
			self.assertIsInstance(x, int)

	def test_negation(self):
		for x in self.value:
			self.assertGreater(x, 0)

	def testing_single_entry(self):
		for x in self.value:
			self.assertFalse(x == 1)

	def test_prime_even_number(self):
		for x in self.value:
			self.assertFalse(x > 2 and x % 2 == 0)

	def test_divisible_by_three_number(self):
		for x in self.value:
			self.assertFalse(x > 3 and x % 3 == 0)




if __name__ == '__main__':
	unittest.main()

