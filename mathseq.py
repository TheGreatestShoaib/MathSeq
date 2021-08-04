'''

Mathseq is a basic library prototype that helps you make infinite sequence and see the mystery 
behind it in different ways '''

import math

used_math = math.sqrt(16)
PHI = abs(( math.sqrt(5)+1)/2)


__all__=["Sequences","Listprop","is_prime","is_odd","is_even","PHI"]
DEFINE = ''' Hello '''



def is_odd(chac):
	''' hello '''
	is_odd = True

	if chac % 2 == 0:
		is_even = False

	return is_odd

class Sequences:
	''' A class of famous sequences that infinitely generate sequences ..'''
	def __init__(self,inverse_val=False):
		self.inverse = inverse_val


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


	def prime_generator(self,end):

		''' -Prime numbers are considered as the most exciting numbers among the math lovers..

			-A Prime number can only devided by the number itself and 1 .

			
			
		'''

		for n in range(2,end):
			for x in range(2, n):
				if n % x == 0:
					pass
				else:
					yield n





	def odd_seq(self,inverse=None):
		''' 
		This function generates odd sequence
		An odd number is a number which is not divisible by 2.
		'''
		if inverse is None : inverse = self.inverse
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


	def even_seq(self,inverse=None):
		''' 
		- even_seq generates infinite sequence of even numbers 
		-A number which is divisible by 2 and generates a remainder of 0 is called an even number.
		 '''
		if inverse is None : inverse = self.inverse
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



	def xibonacci(self,x,inverse=None):
		''' 
			sequence That follows the simple law of f = f(n.-n) 
			It generates :
				- fibonacci
				- tribonacci
				- tetrabonacci
				- hexabonacci

		 '''
		if inverse is None : inverse = self.inverse
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



	def lucas_number(self,inverse=None):
		''' Lucas Number

		'''
		if inverse is None : inverse = self.inverse
		if not inverse:
			x,y,r = 2,1,0
		else:
			x ,y,r = -2,-1,0
		while True:
			yield x
			r = x+y
			x = y
			y = r




	def vaneck_seq(self,inverse=None):
		''' 
		-This Algorithm was taked from OEIS and the author is Ehsan Kia.. 

		 '''
		if inverse is None : inverse = self.inverse
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

	def pronic_number(self,inverse=None):
		''' Pronic Number Doc  '''
		if inverse is None : inverse = self.inverse
		increase , digit = 0 , 0
		while True:
			digit += increase
			yield digit
			increase+=2

	def random_numbers(self,type="regular"):
		''' this is just a prototype'''

		pass


	def look_and_say(self):
		''' '''

		pass



class Listprop:
	r'''
	-Listprop Maintains A Balance Between Lists. It Manipulates Them .
	-It has Basic Properties of Doing Sum , Shaping a List and etc

	'''
	SORT_ALGOS = ["unique_sort","merge_sort","default"]
	SEARCH_ALGOS = ["linear_search","binary_search"]


	def __init__(self,lists):
		self.lists = lists
		if isinstance(self.lists, list):
			pass
		else:
			raise TypeError("Only List Objects Are Iterable")


	def sub_list(self,shape):
		''' This is doc '''
		
		self.lists = self.lists
		shappedlist = [self.lists[i:i + shape ] for i in range(0, len(self.lists),shape )] 
		return shappedlist


	def midpend(self,indexkey,*argv):
		''' it will insert "value" after every "indexkey" into list '''
		lead = len(self.lists)
		i = indexkey
		v = 0
		maximum = len(self.lists)+(len(self.lists)//indexkey*len(argv))-len(argv)
		print(maximum)
		while i < len(self.lists):
			if len(self.lists) > maximum:
				break
			for arg in argv:
				self.lists.insert(i+v,arg)
				#print(arg)
				v += 1
			i+=indexkey
			
	def loopend():
		''' will add values by looping around '''
		pass



	def adimension(self,d):
		''' it converts a list into any dimesion you want '''
		for i in range(d):
			pass

	def searchlists(self,*argv,algo="linear"):
		''' it searches a list in various algo'''
		matchs = {}
		for index,value in enumerate(self.lists):
			for arg in argv:
				if value == arg:
					print(f"matched {value} in index number {index}")



	def sortlist(self,algo="insertion"):
		''' sorts a list '''

		pass

	def sumlist(self,devkey,op):
		''' '''
		




		pass

	def infocheck(self,func):
		''' it returns information about a certain list '''
		def inner(fun):
			pass
			return fun(2) 
		return inner(func)
		



#infocheck(is_even=True,is_prime=False)



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

