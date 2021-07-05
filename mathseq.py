'''
Mathseq is a basic library prototype that helps you make infinite sequence and see the mystery 
behind it in different ways

'''

__all__=["Sequences","types","listProp"]

class Sequences:
	''' A class of 10 sequences that infinitely generate sequences ..'''
	def __init__(self,limit):
		self.limit = limit

	def composite_generator(self,end):
		''' -It generates composite numbers which are just opposite of prime numbers,, it means real numbers that
			-aren't a prime number is a composite number
			
			-The way of Generate composite numbers is looping through desired range and check the number
			-is either devidable by something not 1 or the number itself or not,if it is then the number is composite. '''
		n = 2
		while n > 0:
			for x in range(2, n):
				if n % x == 0:
					yield n
					break
				else:
					pass
			n+=1

	def prime_generator(self,end):
		''' -Prime numbers are considered as the most exciting numbers among the math lovers..

			-A Prime number can only devided by the number itself and 1 .

			- The largest known prime number (as of December 2020) is 282,589,933 − 1 And It basically started from 2.
			'''
	    for n in range(2,end):
	        for x in range(2, n):
	            if n % x == 0:
	                break
	            else:
	            	yield n

	
	def vaneck(self):
		''' Vaneck's sequence generates numbers in a unique way .. it checks  '''

		stored = [0]
		while True:
			sublist = stored[:-1][::-1]
			if stored[-1] not in sublist:
				stored.append(0)
			else:
				indexed = sublist.index(stored[-1])
				print
				stored.append(indexed+1)
			yield stored[-1]
		

	def odd_seq(self,inverse=False):
		''' This is a simple function that generates odd sequence of either positive in infinite or negative '''
		if inverse == False:
				n = 1
				while True:
					yield n
					n+=2
		elif inverse == True:
			n = -1
			while True:
				yield n
				n-=2
		else:
			raise ValueError(f"odd_seq Sequence Doesn't Contain value \"{inverse}\"")

	def even_seq(self,inverse=False):
		''' -even_seq generates infinite sequence of even number by following simple formula of "n+2" '''
		n = 0
		if inverse == False:
				while True:
					yield n
					n+=2
		elif inverse == True:
			while True:
				yield n
				n-=2
		else:
			raise ValueError(f"even_seq Sequence Doesn't Contain value \"{inverse}\"")


	def fibonacci(self):
		''' - Fibonacci is really a mysterious sequence !

			- Following this simple logic of "fn = fn-1 + fn-2 " fibonacci is generated.
				
				x y r
				-----
				0 1 1
				1 1 2
				2 1 3
				3 2 5
				5 3 2

			This is just a simple visualization of fibonacci number

		'''

		x , y  = 0 ,1
		while True:
			x = y
			y = x+y
			yield x

	def xibonacci(self,x,inverse=False):
		''' X-ibonacci has no existance in real life. this is a basic function that generates different sequence
			That follows the simple law of f = f(n.-n) 
			It generates :
				- fibonacci
				- tribonacci
				- tetrabonacci
				- hexabonacci

		 '''
		inp = int(x)
		emp = []
		for i in range(inp-1):
			emp.append(0)
		if inverse == False:
			emp.append(1)
		else:
			emp.append(-1)
		while True:
			x = emp[-inp:]
			emp = emp[-inp:]
			y = sum(emp)
			yield emp[-1]
			emp.append(y)
	

class types:
	def __init__(self):
		pass

	def is_odd(self,chac):
		self.chac = chac
		if chac % 2 != 0:
			return True
		else:
			return False

	def is_even(self,chac):
		self.chac = chac
		if chac % 2 != 0:
			return False
		else:
			return True

	def is_prime(self,chac):
		self.chac = chac
		is_prime = False
		if self.chac > 1:
			for i in range(2,self.chac):
				if (self.chac % i) == 0:
					is_prime = True
					break
		if is_prime:
			return False
		else:
			return True


class listProp(types):
	def __init__(self,lists):
		self.lists = lists
		if type(lists) == list:
			print("bal")
		else:
			raise TypeError("Only List Objects Are Iterable")


	def sub_list(self,n):
		l = self.lists
		x = [l[i:i + n] for i in range(0, len(l), n)] 
		return x

	def summaker(self,devide=None,prime_state=None,even_state=None,odd_state=None):
		if devide is not None:
			lists = self.sub_list(devide)
			emp = []
			for l in lists:
				emp.append(sum(l))
			return emp
		else:
			lists = self.lists
			return sum(self.lists)

