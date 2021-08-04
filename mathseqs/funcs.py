
__all__ = ["is_odd","is_prime","is_even","is_perfect","get_factorials"]

def is_odd(chac):
	''' hello '''
	is_odd = True

	if chac % 2 == 0:
		is_even = False

	return is_odd


def is_even(chac):
	''' haha '''
	is_even = True

	if chac % 2 != 0:
		is_even = False

	return is_even
		

def is_prime(chac):
	''' will add later '''
	is_prime = False
	if chac > 1:
		for i in range(2,chac):
			if (chac % i) == 0:
				is_prime = True
				break
	
	if is_prime:
		is_prime = False

	return is_prime

def is_perfect(n):
	''' '''
	factors = []
	for i in range(1,n):
		if (n % i) == 0:
			factors.append(i)
	if sum(factors) == n:
		return True
	else:
		return False

def get_factorials(number):
	get_factorials.factorials = []
	for factorial in range(1,number):
		val = 1
		val = factorial * val
		get_factorials.factorials.append(factorial)
		print(val)
	pass

