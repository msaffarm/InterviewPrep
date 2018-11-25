
def create_subsets(s,subsets):

	if len(s)==0:
		return

	x = s.pop()
	create_subsets(s,subsets)
	added_items = []
	added_items.append([x])
	for sub in subsets:
		t = list(sub)
		t.append(x)
		added_items.append(t)
	subsets += added_items


def main():
	s = [1,2,3]
	subsets = []
	create_subsets(s,subsets)
	print(subsets)


if __name__ == '__main__':
	main()

