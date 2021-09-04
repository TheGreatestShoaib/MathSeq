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


find = Listprop(lucas)
found = find.linear_search(2,5,7,9,4,6,7,8,3,3,3,3,3,3,2,2,12,3,4)


fact = mathseqs.get_factorials(6)


print(fact)