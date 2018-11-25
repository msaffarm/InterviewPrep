
def super_digit(x,k,logger):
	if len(str(x))==1:
		return x

	if x in logger:
		return logger[x]
	else:
		if k!=1:
			logger[x] = super_digit(sum(k*int(c) for c in str(x)),1,logger)
		else:
			logger[x] = super_digit(sum(int(c) for c in str(x)),1,logger)
	return logger[x]


def main():
	x,k = input().strip().split()
	# x = '148'
	# k = 3
	# x = "861568688536788" 
	# k = 100000
	# n = int(x*int(k))
	# print(n)
	logger = {}
	print(super_digit(int(x),int(k),logger))


if __name__ == '__main__':
	main()