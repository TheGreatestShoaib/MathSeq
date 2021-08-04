
class Sequences:
	def composite_generator(self):
		'''
		-It generates composite numbers which are just opposite of prime numbers,,
		it means real numbers that
		aren't a prime number is a composite number
			
		
		-The way of Generate composite numbers is looping through desired range
		And check the number is either devidable by something not 1 
		or the number itself or not,if it is then the number is composite. 

		'''
		n = 2
		while n > 0:
			for x in range(2, n):
				if n % x == 0:
					yield n
					break
			n+=1


	def prime_generator(end):

		''' -Prime numbers are considered as the most exciting numbers among the math lovers..

			-A Prime number can only devided by the number itself and 1 .

			
			
		'''

		for n in range(2,end):
			for x in range(2, n):
				if n % x == 0:
					pass
				else:
					yield n





	def odd_seq(inverse=None):
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


	def even_seq(inverse=None):
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
		- Fibonacci is really a mysterious sequence !

		- Following this simple logic of "fn = fn-1 + fn-2 " fibonacci has generated.

		'''

		x , y  = 0 ,1
		while True:
			r = x + y
			x = y
			y = r
			yield x



	def xibonacci(x,inverse=None):
		''' 
			sequence That follows the simple law of f = f(n.-n) 
			It generates :
				- fibonacci
				- tribonacci
				- tetrabonacci
				- hexabonacci

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



	def lucas_number(inverse=None):
		''' Lucas Number

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




	def vaneck_seq(inverse=None):
		''' 
		-This Algorithm was taked from OEIS and the author is Ehsan Kia.. 

		 '''
		if inverse is False:
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
			except:
				print("hel")
		else:
			list_vanseq = [0]
			last_pos = {}
			i = 0
			while True:
				new_value = -abs(i - last_pos.get(list_vanseq[i], i))
				list_vanseq.append(new_value)
				last_pos[list_vanseq[i]] = i
				yield list_vanseq[-1]
				i += 1

	def pronic_number(inverse=None):
		''' Pronic Number Doc  '''
		increase , digit = 0 , 0
		while True:
			digit += increase
			yield digit
			increase+=2

	def random_numbers(type="regular"):
		''' this is just a prototype'''

		pass


	def look_and_say(self):
		''' '''

		pass