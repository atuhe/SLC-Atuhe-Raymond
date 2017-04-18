import unittest
import prime_Number as prime


class PrimeTest_case(unittest.TestCase):
	def setUp(self):
		self.result = prime.generate_prime_numbers()
	
	def testing_lists_return_type(self):
		self.assertIsInstance(self.result, list)
	
	def testing_typeInteger(self):
		for x in self.result:
			self.assertIsInstance(x, int)
		
	


if __name__ == '__main__':
	unittest.main()

