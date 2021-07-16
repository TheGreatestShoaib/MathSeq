

class Hello:

	def __init__(self,value=True):
		self.value = value

	def fock(self):
		print("odd")

	def main(self,text=None):
		if text is None : text = self.value
		
		return text


hello = Hello(value=False)
print(hello.main())

