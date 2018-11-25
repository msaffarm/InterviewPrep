# Form a cycle with a permutation of the first  positive integers.
# The cycle is called Prime Cycle if all neighboring pairs sum up to be a prime.
# The two distinct prime cycles for n=6 are:
#  1 4 3 2 5 6
#  1 6 5 2 3 4
# The permutation 3 2 5 6 1 4 is considered the same as the first sequence.
# How many distinct prime cycles are there for n=16?
from math import sqrt

def is_prime(a):
	if a==1:
		return False
	for i in range(2,int(sqrt(a))+1):
		if a%i==0:
			return False
	return True


def is_rotated(str1,str2):
	if str1 in str2+str2:
		return True
	return False


def is_in_set(valids,s):
	if any(is_rotated(x,s) for x in valids):
		return True
	return False


def check_valid(s,i):
	if len(s)==0:
		return True
	if str(i) in s:
		return False
	if is_prime(int(s[-1])+i):
		return True
	return False


def backtrack(n,start,end,valids,s=None):

	if not s:
		s = []
	if start==end+1:
		tmp = "".join(s)
		if not is_in_set(valids,tmp):
			# print("tmp={}".format(tmp))	
			valids.add(tmp)
		return

	for i in range(1,n+1):
		if not check_valid(s,i):
			continue
		t = list(s)
		t.append(str(i))
		backtrack(n,start+1,end,valids,t)


def main():
	n = 
	valids = set()
	backtrack(n,1,n,valids)
	# print(valids)
	print(len(valids))

if __name__ == '__main__':
	main()