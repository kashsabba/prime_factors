import unittest
import os
from prime_factor_processor import compute_prime_factors
from prime_factor_processor import create_list_of_values_computed

class TestPrimeFactors(unittest.TestCase):
	"""
	standard test class
	"""

	def test_compute_prime_factors(self):
		"""
		test to check the list from compute_prime_factors function
		"""

		result_list = compute_prime_factors(100)
		expected_list = [2, 2, 5, 5]
		self.assertListEqual(result_list, expected_list)

	def test_create_list_of_values_computed(self):
		"""
		test to check the file names from output is consistent with written input_values
		"""

		test_path = os.path.join(os.getcwd() + '\\test_output\\')
		result_file_names = create_list_of_values_computed(test_path)
		expected_file_names = ['100', '1025', '2560']
		self.assertListEqual(result_file_names, expected_file_names)

		
if __name__ == '__main__':
	unittest.main()

