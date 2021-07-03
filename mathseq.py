
class Sequences:
	def __init__(self,limit):
		self.limit = limit


		# Prime number generator
	def composite_generator(self,end):
	    for n in range(2,end):     
	        for x in range(2, n):
	            if n % x == 0:
	                yield n
	                break
	        else:
	            pass

	def prime_generator(self,end):
	    for n in range(2,end):     
	        for x in range(2, n):
	            if n % x == 0:
	                break
	        else:
	            yield n

	def odd_seq(self,inverse=False):
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
		x , y , r  = 0 ,1 ,0
		while True:
			x = y
			y = x+y
			yield x

	def xibonacci(self,x,inverse=False):
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





class types():
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


class list_prop(types):
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



