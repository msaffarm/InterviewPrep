

def cal_ways(x,y):

	if x==0 and y==0:
		return 1
	if x<0 or y<0:
		return 0

	return cal_ways(x-1,y) + cal_ways(x,y-1)



def main():
	x,y = 2,2
	print(cal_ways(x,y))


if __name__ == '__main__':
	main()