import heapq



def main():
	l = [5,3,1,388,19,4]
	heapq.heapify(l)
	print(heapq.heappop(l))


if __name__ == '__main__':
	main()