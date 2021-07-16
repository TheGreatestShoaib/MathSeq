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