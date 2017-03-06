""" Function to generate prime numbers between 0 and n ie nos greater than 1 but only divisible by themselves"""

def prime_generator_fn(n):
	"""All positive integers less than n"""
	for num in range(n):
		"""Condition 1 for prime: Must be greater than 1"""
		if num > 1:
			"""Condition 2 for prime: remainder if divided by any other number other than itself and 1"""	
			for i in range(2,num):
				if (num % i==0):
					break
		        else:
		        	prime_num = num
			    	print(prime_num)
	

prime_generator_fn(16)