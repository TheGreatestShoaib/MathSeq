from mathseq import Sequences , list_prop ,types
import sys


type = types()


fib = Sequences(10)
fib2 = fib.fibonacci()
even = fib.even_seq()
odd = fib.odd_seq()

odd_list = []

for _ in range(10):
	odd_list.append(next(odd))

print(odd_list)

for i in odd_list:
	if type.is_prime(i):
		print(i)
















#seq.clear()
"""
print(" prime :",t.is_prime(int(sys.argv[1])))
print(" ODD  :",t.is_odd(int(sys.argv[1])))
print(" Even :",t.is_even(int(sys.argv[1])))
"""

