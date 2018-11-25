from math import ceil


def countPS(x,n,start):
	if x < 0:
		return 0
	if x==0:
		return 1
	s = 0
	for i in range(ceil(x**(1.0/n))):
		s += countPS(x-(i+start)**n,n,i+start+1)
	return s


def main():
	x = int(input())
	n = int(input())
	# x = 100
	# n = 2
	print(countPS(x,n,1))

if __name__ == '__main__':
	main()
