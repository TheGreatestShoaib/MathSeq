"""
this is the doc string of this model
i'll just write it someday just yeah thats all
"""

import time
import random


def composite_numbers():
	'''
	-It generates composite numbers which are just opposite of prime numbers,,
	it means real numbers that
	aren't a prime number is a composite number

	'''
	n = 2
	while n > 0:
		for x in range(2, n):
			if n % x == 0:
				yield n
				break
		n+=1


def prime_numbers(end):
	'''
	- A number that is divisible only by itself and 1  (e.g. 2, 3, 5, 7, 11).


	- Prime numbers are very useful in cryptography
	Prime numbers are considered as the most exciting numbers among the math lovers..

	'''

	for n in range(2,end):
		for x in range(2, n):
			if n % x == 0:
				pass
			else:
				yield n





def odd_seq(inverse=False):
	'''

	This function generates odd sequence
	An odd number is a number which is not divisible by 2.

	'''
	if inverse is False:
			n = 1
			while True:
				yield n
				n+=2
	else:
		n = -1
		while True:
			yield n
			n-=2


def even_seq(inverse=False):
	'''

	- even_seq generates infinite sequence of even numbers
	-A number which is divisible by 2 and generates a remainder of 0 is called an even number.

	'''
	n = 0
	if inverse is False:
			while True:
				yield n
				n+=2
	else:
		while True:
			yield n
			n-=2


def fibonacci():
	'''

	- In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence,
		called the Fibonacci sequence, such that each number is the sum of the two preceding ones,
		starting from 0 and 1.

	- The Following Formula is "fn = fn-1 + fn-2 ".

	- Fibonacci is really a mysterious sequence !
	'''

	x , y  = 0 ,1
	while True:
		r = x + y
		x = y
		y = r
		yield x


def xibonacci(x,inverse=False):
	'''
	- xibonacci isn't a real sequence rather it's just a method that generates
	a sequence of number such that each term from the "x"
	onward is the sum of previous "x" terms.

	similar as fibonacci that sums previous "x" terms.

	-xibonacci usually requires one positional arguments that is the value of "x".

	- possible sequences that could be generated through this method:

			- fibonacci
			- tribonacci
			- tetrabonacci
			- hexabonacci

			And so on ... to the infinity !

	'''
	inp = int(x)
	empty_list = []
	for _ in range(inp-1):
		empty_list.append(0)
	if inverse is False:
		empty_list.append(1)
	else:
		empty_list.append(-1)
	while True:
		x = empty_list[-inp:]
		empty_list = empty_list[-inp:]
		y = sum(empty_list)
		yield empty_list[-1]
		empty_list.append(y)



def lucas_number(inverse=False):
	'''
	- The Lucas sequence has the same recursive relationship as the "Fibonacci" sequence,
	where each term is the sum of the two previous terms, but with different starting values

	- This produces a sequence where the ratios of successive terms approach the golden ratio,
	and in fact the terms themselves are roundings("round()") of integer powers of the golden ratio.


	- `x` and `y` are the constant starting_point for `Lucas Sequence`.

	'''
	if not inverse:
		x,y,r = 2,1,0
	else:
		x ,y,r = -2,-1,0
	while True:
		yield x
		r = x+y
		x = y
		y = r


def catalan_numbers():
	"""
	- In combinatorial mathematics,the Catalan numbers form a sequence of natural numbers
	that occur in various counting problems,often involving recursively defined objects.

	- Follows "n = 1/(n+1)(2n*n)"

	"""
	res = 0
	catalan_list = [1,1]
	i = 0
	while True:
		yield catalan_list[i]
		res = 0
		for x in range(len(catalan_list)):
			res += catalan_list[x] * catalan_list [-(x+1)]
		catalan_list.append(res)
		i+=1




def vaneck_seq(inverse=False):
	'''
	-This Algorithm was taked from OEIS and the author is Ehsan Kia..

	'''

	try:
		list_vanseq = [0]
		last_pos = {}
		i = 0
		while True:
			new_value = i - last_pos.get(list_vanseq[i], i)
			list_vanseq.append(new_value)
			last_pos[list_vanseq[i]] = i
			yield new_value
			i += 1
	except KeyError:
		pass

def pronic_numbers():
	'''
	- A pronic number is a number which is the product of two consecutive integers,
	that is, a number of the form n(n + 1).
	
	- Details:
				* https://en.wikipedia.org/wiki/Pronic_number
				* https://oeis.org/A002378

	'''

	increase , digit = 0 , 0
	while True:
		digit += increase
		yield digit
		increase+=2

def random_numbers(number_type="regular",limits=1000,seed=None):
	'''
	- Random Numbers Are Just Random Numbers As It Looks By Its Name,

	- Use Seed For Controlling their Randomness,

	- `Limits` Defines The Range.

	'''
	while True:

		if seed is not None:
			random.seed(seed)

		breh  = random.randint(0,10**4)
		yield breh


def looknsay(starting_point="1",inverse=None):
	'''
	- To generate a member of the sequence from the previous member, read off the digits of the previous member,
	counting the number of digits in groups of the same digit. For example:

			- 1 is read off as "one 1" or 11.
			- 11 is read off as "two 1s" or 21.
			- 21 is read off as "one 2, then one 1" or 1211.
			- 1211 is read off as "one 1, one 2, then two 1s" or 1112

	
	- The sequence grows indefinitely. In fact, any variant defined by
	starting with a different integer seed number will (eventually) also grow indefinitely,

	'''
	starting_point = str(starting_point)

	def count_next(word):
		prev= word[0]
		count= 1
		say =  ''
		for curr in word[1:]:
			if curr == prev:
				count += 1
				continue
			say += str(count) + prev
			prev = curr
			count = 1

		breh = say + str(count) + prev
		return breh
	
	recursed_val = count_next(starting_point)

	if recursed_val == "11":
		yield "1"

	yield recursed_val
	yield from looknsay(recursed_val)
