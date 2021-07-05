A181391 = [0]

last_pos = {}

for i in range(10):
	print("i",i)

    new_value = i - last_pos.get(A181391[i], i)
    #print(last_pos.get(A181391[i] ,"I value :"+str(new_value,i)))
    #print("i",i)

    A181391.append(-abs(new_value))

    last_pos[A181391[i]] = i
    print(-abs(new_value))
    # print(last_pos)

# Ehsan Kia, Jun 12 2019

#print(A181391)

print(A181391)