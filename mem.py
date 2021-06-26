import tracemalloc


def my_complex_analysis_method():
	dif = [x for x in range(1000)]
	#print(dif)


tracemalloc.start()
my_complex_analysis_method()
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()