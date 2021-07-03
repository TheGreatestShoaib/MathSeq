from mathseq import Sequences , list_prop ,types
import sys


type = types()


fib = Sequences(10)
g = fib.prime_generator(100)   # give firt 1000 prime number
odd_list = []

for _ in range(10):
	odd_list.append(next(g))



print(odd_list)

#hello = list_prop("odd_list")















#seq.clear()
"""
print(" prime :",t.is_prime(int(sys.argv[1])))
print(" ODD  :",t.is_odd(int(sys.argv[1])))
print(" Even :",t.is_even(int(sys.argv[1])))
"""

