def find_subsets(s,target):

	if target==0:
		return True

	elif target < 0:
		return False

	if len(s)==1:
		return s[0]==target

	t = list(s)
	x = t.pop(0)
	return find_subsets(t,target) or find_subsets(t,target-x)


def main():
	s = list(range(10))
	target = 3
	print(find_subsets(s,target))
	

if __name__ == '__main__':
	main()