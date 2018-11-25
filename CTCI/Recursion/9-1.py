
def cal_steps(n,logger={}):

	if n==0:
		return 1
	if n < 0:
		return 0

	if n in logger:
		return logger[n]
	else:
		logger[n] = cal_steps(n-1) + cal_steps(n-2) + cal_steps(n-3)

	return logger[n]


def main():
	n = 100
	print(cal_steps(n))


if __name__ == '__main__':
	main()