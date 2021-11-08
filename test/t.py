from mathseq import seq

breh = seq.random_numbers()


say = [next(breh) for _ in range(10)]

print(say)

# for i in range(10):
# 	print(next(breh))



	# else:
	# 	list_vanseq = [0]
	# 	last_pos = {}
	# 	i = 0
	# 	while True:
	# 		new_value = -abs(i - last_pos.get(list_vanseq[i], i))
	# 		list_vanseq.append(new_value)
	# 		last_pos[list_vanseq[i]] = i
	# 		yield list_vanseq[-1]
	# 		i += 1