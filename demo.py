from mathseq import Sequences
import mathseq
import sys
import math

#PHI = abs(( math.sqrt(5)+1)/2)

#phi = PHI


luca = Sequences.lucas_number()

lucas = []
even_list = []

for _ in range(0,100):
	lucas.append(next(luca))



fact = mathseq.get_factorials(6)


print(fact)
