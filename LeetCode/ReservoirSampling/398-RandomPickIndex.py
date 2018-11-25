from random import randint

class Solution(object):

	def __init__(self,nums):
		self.nums = nums


	def pick(self,target):
		selected = []
		k = 1
		counter = 0
		for i,x in enumerate(self.nums):
			if x!=target:
				continue
			if counter < k:
				selected.append(i)
			else:
				s = randint(0,counter)
				if s < k:
					selected[randint(0,k-1)] = i
			counter += 1
		return selected[0]


def main():
	l = [3, 5, 1, 8, 6, 0, 7, 2, 7, 8]
	s=Solution(l)
	print(s.pick(3))


if __name__ == '__main__':
	main()


