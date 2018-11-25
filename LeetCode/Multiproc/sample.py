# import multiprocessing as mp
from multiprocessing import Pool
import time
from math import sqrt


def is_prime(x):
	if x==1:
		return True
	for i in range(2,int(sqrt(x))+1):
		if x%i==0:
			return False
	return True


def fn(a):
	return sum(x for x in range(1,a) if is_prime(x))


def main():
	start = time.time()
	num_of_procs = 8
	l = [1000000,2000000,3000000,4000000,5000000,6000000]
	with Pool(processes=num_of_procs) as p:
		res = p.map(fn,l)
	end = time.time()
	print("Elapsed time is= {0:.5f}".format(end-start))
	print(res)


if __name__ == '__main__':
	main()