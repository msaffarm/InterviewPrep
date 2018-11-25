from collections import Counter



def main():
	a = Counter({'a':2,'b':3,'d':8})
	b = Counter(a=4,b=6,c=9)
	print(a)
	# print(list(a.elements()))
	print(b)
	# only positive count elements
	print("a-b= " + str(a-b))
	print("b-a= " + str(b-a))
	print("a+b= " + str(a+b))
	print("a & b (and)min = " + str(a&b))
	print("a | b (or)max= " + str(a|b))
	b.subtract(a)
	print(b)


if __name__ == '__main__':
	main()