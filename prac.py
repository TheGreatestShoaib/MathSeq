
bruh = [x for x in range(100)][::4]

x = 2
y = 1
r = 0

i = 0
while i < 10:
	r = x+y
	yield x
	x = y
	y = r
	i+=1

















"""
class Hello:

	def __init__(self,listed,value=True):
		self.listed = listed
		self.value = value

	def fock(self):
		for content in self.listed:
			print(content)



	def main(self,text=self.value):
		#if text is None : text = self.value
		
		return text
"""
