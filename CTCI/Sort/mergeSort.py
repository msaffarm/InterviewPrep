def merge(a,b):

	c = []
	while a and b:
		if a[0] > b[0]:
			c.append(a[0])
			a.pop(0)
		else:
			c.append(b[0])
			b.pop(0)
	if not a:
		c += b
	elif not b:
		c += a
	return c


def merge_sort(l):
	if len(l)==1:
		return l

	middle = len(l)//2
	a = merge_sort(l[:middle])
	b = merge_sort(l[middle:])

	return merge(a,b)


def main():
	l = list(range(1000))
	# print(l[:1])
	# return 
	print(merge_sort(l))


if __name__ == '__main__':
	main()