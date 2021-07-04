


#  1 11 21 1211 111221 

f = 1
s = 11
final = 0

curr = 0

for i in str(s):
	if str(f) == i:
		curr+=1
final = str(curr)+str(f)

print(final)
