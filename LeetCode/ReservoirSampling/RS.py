from random import randint

def sample_k_items(l,k):
	selected = []
	for i,x in enumerate(l):
		if i < k:
			selected.append(x)
		else:
			s = randint(0,i)
			if s < k:
				selected[randint(0,k-1)] = x
	return selected


def main():
	l = list(range(1000))
	k = 1
	print(sample_k_items(l,k))


if __name__ == '__main__':
	main()