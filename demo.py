from mathseqs import Sequences , Listprop
import mathseqs
import sys
import math

#PHI = abs(( math.sqrt(5)+1)/2)

#phi = PHI


luca = Sequences.lucas_number()

lucas = []
even_list = []

for _ in range(0,100):
	lucas.append(next(luca))

print(lucas)

for l in lucas:
	print(l)
	print("prime : ",mathseqs.is_prime(l))
	print("perfect :",mathseqs.is_perfect(l))
	print("odd : ",mathseqs.is_odd(l))