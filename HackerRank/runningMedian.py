import heapq


class RunningMedian(object):

	def __init__(self):
		self.lower = []
		self.higher = []
		heapq.heapify(self.lower)
		heapq.heapify(self.higher)


	def _add_element(self,n):
		if not self.lower and not self.lower:
			heapq.heappush(self.lower,n)




	def computer_median(self,n):
		self._add_element(n)
		if len(self.lower)==len(self.higher):
			return (self.get_min(self.higher) + self.get_max(self.lower))/2
		elif len(self.lower) > len(self.higher):
			return self.get_max(self.lower)
		else:
			return self.get_min(self.higher)


	def get_min(self,l):
		return heapq.heappop(l)


	def get_max(self,l):
		return heapq.nlargest(1,l)


def main():
	# z = [1,5,3]
	# heapq.heapify(z)
	# print(heapq.nlargest(1,z))
	# return

	RM = RunningMedian()
	l = [4,6,1,12,2]
	for i in range(len(l)):
		RM.computer_median(l[i])


if __name__ == '__main__':
	main()