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
import unittest

def compute_prime_factors(input_value):
	"""
	function reads an integer input value
	calculates the prime factors, writes the list of prime factors to a text file and prints in console
	"""

	# setting up text file to write using input value as the file name
	prime_factor_output = open('{0}.txt'.format(str(input_value)), "w")

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

		# increment the divisor by 1
		divisor = divisor + 1

	# we expect the list to have at least one value
	assert (len(prime_factor_list) > 0)

	# writing the list of factors and closing the file
	prime_factor_output.write(str(prime_factor_list))
	prime_factor_output.close()

	# printing in console
	return print(prime_factor_list)

def check_input_value_computed(input_value):
	"""
	function checks if prime factors are computed for a given input value
	if computed, it retrieves the list from the saved text file
	if not computed, it calls compute prime factors function above
	"""

	# initiate an empty list to collect file name values
	list_input_values_computed = []

	# loop through files if any and collect into the empty list created above
	for file in glob.glob("*.txt"):
		list_input_values_computed.append(file.split(".")[0])

	# check if a file exists with input value
	# if not, launch compute prime factor function
	if str(input_value) not in list_input_values_computed:
		print("new computation")
		compute_prime_factors(input_value)
	else:
		print("already computed value - retrieving from saved space")
		prime_factor_computed = open('{0}.txt'.format(str(input_value)), "r")
		print(prime_factor_computed.read())

def run():
	"""
	error handler to check for correct input number type
	call the function to check the input value already computed
	run compute function or retrieve from saved space
	"""
	try:
		input_int_number = int(sys.argv[1])
		if input_int_number > 1:
			check_input_value_computed(input_int_number)
		else:
			print("please input a valid integer value")
	except:
		print("please input a valid integer value")

if __name__ == '__main__':
	run()
