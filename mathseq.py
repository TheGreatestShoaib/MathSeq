import math


#Sequence Class : 

# even sequence
# odd sequence
# composite sequence
# prime sequence
# VanEck sequence
# Look and say sequence   --Have to DO
# fibonacci sequence
# xibonacci sequence generator
# Random Sequence  		--Have to DO
#
#

#Pattern Class: --Have to DO

# Generate Continious Pattern 
# Recognize Patterns

#list_prop

# Devide list into sublist
# sum lists
# manipulate lists 		--Have to DO
#
#


#type class:

#get types either prime or nor , odd or even etc
#
#


'''
Mathseq is a basic library prototype that helps you make infinite sequence and see the mystery 
behind it in different ways

'''

__all__=["Sequences","Types","listProp"]

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

			-The largest known prime number (as of December 2020) is 282,589,933 − 1 And It basically started from 2.
			
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


	def even_seq(self,inverse=False):
		''' -even_seq generates infinite sequence of even number by following simple formula of "n+2" '''
		n = 0
		if inverse is False:
				while True:
					yield n
					n+=2
		else:
			while True:
				yield n
				n-=2



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
		if inverse is False:
			emp.append(1)
		else:
			emp.append(-1)
		while True:
			x = emp[-inp:]
			emp = emp[-inp:]
			y = sum(emp)
			yield emp[-1]
			emp.append(y)
	
	def VanEck_seq(self,inverse=False):
		''' -This Algorithm was taked from OEIS and the author is Ehsan Kia.. 

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
					#print(last_pos[list_vanseq])
					yield new_value
					i += 1
			except Exception as error:
				print(error)
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

		return "hello"


class Types:
	''' types return either True or False based on its functionality '''
	def __init__(self):
		pass

	def is_odd(self,chac):
		''' hello '''
		if chac % 2 != 0:
			return True
		else: #pylint: disable=no-else-return
			return False

	def is_even(self,chac):
		''' haha '''
		if chac % 2 != 0:
			return False
		else:	#pylint: disable=no-else-return
			return True

	def is_prime(self,chac):
		''' will add later '''
		is_prime = False
		if chac > 1:
			for i in range(2,chac):
				if (chac % i) == 0:
					is_prime = True
					break
		if is_prime:
			return False
		else:	#pylint: disable=no-else-return
			return True


class listProp(Types):
	''' -listProp Maintain A Balance Between Lists. It Manipulates Them .
		- It has Basic Properties of Doing Sum , Shaping a List 

	'''
	def __init__(self,lists):
		self.lists = lists
		if type(lists) == list:
			print("bal")
		else:
			raise TypeError("Only List Objects Are Iterable")


	def Sublist(self,shape):
		''' This is doc '''
		
		mainlist = self.lists
		shappedlist = [mainlist[i:i + shape ] for i in range(0, len(mainlist),shape )] 
		return shappedlist

	def summaker(self,devide=None,prime_state=None,even_state=None,odd_state=None): #pylint : disable=unused-argument
		
		''' Man this is Annoying '''

		if devide is not None:
			lists = self.Sublist(devide)
			emp = []
			for lst in lists:
				emp.append(sum(lst))
			return emp
		else:
			lists = self.lists
			return sum(self.lists)

