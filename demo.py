from mathseq import seq
import mathseq
import sys
import math

#PHI = abs(( math.sqrt(5)+1)/2)

#phi = PHI


luca = seq.lucas_number()
fibonacci = seq.fibonacci()
prime = seq.prime_numbers(100)
comp = seq.composite_numbers()
odd =seq.odd_seq()
even = seq.even_seq()
odd_inv =seq.odd_seq(inverse=True)
even_inv = seq.even_seq(inverse=True)
cat = seq.catalan_numbers()
van = seq.vaneck_seq()
pronic = seq.pronic_numbers()
xbo_six = seq.xibonacci(3)





print("This is odds seq : ",end="")
for _ in range(0,10):
	print(next(odd),end=",")
print("\n")


print("This is even seq : ",end="")
for _ in range(0,10):
	print(next(even),end=",")
print("\n")



print("This is inversen_odd : ",end="")
for _ in range(0,10):
	print(next(odd_inv),end=",")
print("\n")



print("This is inversed even : ",end="")
for _ in range(0,10):
	print(next(even_inv),end=",")	
print("\n")



print("This is fibonacci : ",end="")
for _ in range(0,10):
	print(next(fibonacci),end=",")
print("\n")


print("This is vaneck : ",end="")
for _ in range(0,10):
	print(next(van),end=",")
print("\n")

print("This is catalan_numbers : ",end="")
for _ in range(0,10):
	print(next(cat),end=",")
print("\n")


print("This is pronic: ",end="")
for _ in range(0,10):
	print(next(pronic),end=",")
print("\n")


print("This is xibonaaci with 6 : ",end="")
for _ in range(0,10):
	print(next(xbo_six),end=",")
print("\n")






# fact = mathseq.get_factorials(6)


# print(fact)
