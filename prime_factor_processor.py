"""
author - kash sabba
reads a number from command line, checks for an integer input
writes back a list of prime factors for the input number

within the virtual environment, navigate to where the code is saved and run
python prime_factorization.py 1000
"""

import sys
import os
import glob
import logging

# get logger
logger = logging.getLogger()

# check to see if output directory already exists
directory_check = os.path.isdir(os.path.join(os.getcwd() + '\\saved_output'))

# create the output directory if doesn't exist
if not(directory_check):
	os.mkdir(os.getcwd() + '\\saved_output')

# global path variable
saved_path = os.path.join(os.getcwd() + '\\saved_output\\')

def compute_prime_factors(input_value):
	"""
	function reads an integer input value
	calculates the prime factors, returns the list of prime factors
	prints the list of prime factors in console
	"""

	logger.info(msg="computed prime factors for -- {}".format(input_value))

	# empty list for collection in the loop below and an initial number divisor
	prime_factor_list = []
	divisor = 2

	# loop terminates when input value is equal to 1
	while input_value > 1:

		# check if input value divided by divisor has a remainder of zero
		# if remainder is zero, collect the divisor in the list
		# update the input value and reset the divisor/skip the rest of loop
		if ((input_value % divisor) == 0):
			prime_factor_list.append(divisor)
			input_value = input_value / divisor
			divisor = 2
			continue

		# increment the divisor by 1 if doesn't satisfy the if condition
		divisor = divisor + 1

	# we expect the list to have at least one value
	# we expect the input value to be 1 after loop ends
	assert (len(prime_factor_list) > 0)
	assert (input_value == 1)

	# print in console and return
	print(prime_factor_list)
	return prime_factor_list

def write_prime_factors_to_file(input_value, output_path):
	"""
	function reads input_value and output path to write list of prime factors
	"""
	
	prime_factor_output = open(output_path + '{0}.txt'.format(str(input_value)), "w")
	prime_factor_list = compute_prime_factors(input_value)
	prime_factor_output.write(str(prime_factor_list))
	prime_factor_output.close()

def create_list_of_values_computed(output_path):
	"""
	function reads through all input_value text files if produced and collects all input_value file names into a list
	"""

	# initiate a list to collect
	list_input_values_computed = []

	for file in glob.glob(os.path.join(output_path, "*.txt")):
		list_input_values_computed.append(file.split("\\")[-1].split(".")[0])

	return list_input_values_computed

def check_if_input_value_computed(input_value):
	"""
	function checks if prime factors are computed for a given input value
	if computed, it retrieves the list from the saved text file
	if not computed, it calls write_prime_factors_to_file function which calls compute_prime_factors function
	"""

	# collects the list of input_value file names already produced 
	input_values_computed = create_list_of_values_computed(saved_path)

	if str(input_value) not in input_values_computed:
		print("new computation")
		write_prime_factors_to_file(input_value, saved_path)
	else:
		print("already computed value - retrieving from saved output")
		logger.info(msg="retrieving from saved output, prime factors for -- {}".format(input_value))
		saved_file_prime_computed = open(saved_path + '{0}.txt'.format(str(input_value)), "r")
		print(saved_file_prime_computed.read())

def run():
	"""
	check for correct input number type
	call the function check_if_input_value_computed
	"""
	logging.basicConfig(filename='log_prime_factors.log', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

	try:
		input_int_number = int(sys.argv[1])
		if input_int_number > 1:
			check_if_input_value_computed(input_int_number)
		else:
			print("please input an integer value greater than 1")
	except:
		print("please input an integer value greater than 1")

if __name__ == '__main__':
	run()
