from mathseq import *
import sys





fib = Sequences(inverse_val=True)
g = fib.even_seq(inverse=False)
k = fib.lucas_number(inverse=False)
odd_list = []
even_list = []

for _ in range(100):
	#odd_list.append(next(g))
	#dd_list.append(next(g))
	even_list.append(next(k))



#print(odd_list,even_list)


print(even_list)


#hello = list_prop("odd_list")
'''

for i in odd_list:
	print(type.is_odd(i))
	print(type.is_prime(i))
	print(type.is_even(i))
	print()

'''













#seq.clear()
"""
print(" prime :",t.is_prime(int(sys.argv[1])))
print(" ODD  :",t.is_odd(int(sys.argv[1])))
print(" Even :",t.is_even(int(sys.argv[1])))
"""

