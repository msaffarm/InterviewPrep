
# def cal_hist(w):
# 	x = [0]*26
# 	for c in w:
# 		x[ord(c)-ord('a')] += 1
# 	return tuple(x)


# def find_anagrams(w,s):
	
# 	whash = hash(cal_hist(w))
# 	i = 0
# 	while i <= len(s)-len(w):
# 		word = s[i:i+len(w)]
# 		if hash(cal_hist(word))==whash:
# 			print(word)
# 		i += 1


# def main():
# 	w = "man"
# 	s = "mansournammna"
# 	l = find_anagrams(w,s)

# if __name__ == '__main__':
# 	main()

from collections import deque



def main():
	s = deque()
	s.append(1)
	s.append(2)
	s.pop()
	print(s)


if __name__ == '__main__':
	main()