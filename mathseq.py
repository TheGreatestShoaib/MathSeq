


def fibonacci(limits):
	x , y , r , i = 0 ,1 ,0 ,1
	emp = [0]
	while i < limits:
		r = x+y
		x = y
		y = r
		emp.append(r)
		i += 1
	return emp


def odd_seq(self,limits):
	self.limits = limits
	emp = []
	i = 1
	while i <= self.limits:
		emp.append(i)
		i += 2
	return 
	
def even_seq(self,limits):
	self.limits = limits
	emp = []
	i = 0
	while i <= self.limits:
		emp.append(i)
		i += 2
	return 
	


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



