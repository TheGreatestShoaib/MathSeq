


def dec_search(listed):
	if listed is not None:
		return listed



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

	def linear_search(self,*argv):
		''' it searches a list in various algo'''
		matches = {}
		for index,value in enumerate(self.lists):
			for arg in argv:
				if value == arg:
					matches[index] = value

		return map(dec_search,matches)


	def binary_search(self):
		pass



	def merge_sort(self):
		''' sorts a list '''

		pass

	def selection_sort(self):

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
		
