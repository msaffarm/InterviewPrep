def find_traverse_ways(n,steps_dict):
	if n==0:
		return 1
	if n < 0:
		return 0

	if n in steps_dict:
		return steps_dict[n]
	else:
		steps_dict[n] = find_traverse_ways(n-1,steps_dict) +\
		 find_traverse_ways(n-2,steps_dict) + find_traverse_ways(n-3,steps_dict)

	return steps_dict[n]



def main():
	# s = int(input().strip())
	# for a0 in range(s):
	# 	n = int(input().strip())
	steps_dict = {}
	print(find_traverse_ways(800,steps_dict))




if __name__ == '__main__':
	main()