"""
here i'll put module docstring

"""

#__all__ = ["is_odd","is_prime","is_even","is_perfect"]

def is_odd(chac):
	''' hello '''

	if chac % 2 == 0:
		return False

	return True


def is_even(chac):
	''' haha '''
	if chac % 2 != 0:
		return False

	return True


def is_prime(chac):
	''' will add later '''
	if chac > 1:
		for i in range(2,chac):
			if (chac % i) == 0:
				return True

	return False


def is_perfect(n):
	''' breh do i just have to '''
	factors = []
	for i in range(1,n):
		if (n % i) == 0:
			factors.append(i)
	if sum(factors) == n:
		return True

	return False
