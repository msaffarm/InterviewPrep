import string 
LOWERCASE = string.ascii_lowercase
from collections import Counter,defaultdict


# Find the smallest window in a string containing all characters of another string
def find_smallest_window(str,pattern):
	pass


# get all substrs of str
def get_substrs(str):
	l = []
	for step in range(len(str)):
		for i in range(len(str)):
			if i+step < len(str):
				l.append(str[i:i+step+1])
	return l


# Count number of substrings with exactly k distinct characters
def find_substr_size_k(str):
	pass


# check if two strings are anagram of each other
def is_anagram(str1,str2):
	return Counter(str1)==Counter(str2)


# Maximum consecutive repeating character in string
def find_max_repeating_char(str):
	pass


# check if string is palindrome
def is_palindrome(str):
	return str==str[::-1]
	# return str==''.join(reversed(str))


def main():
	s = "abc"
	d = defaultdict(list)
	d["mansour"] += ["hellp"]
	print(d)
	print(s[::-1])


if __name__ == '__main__':
	main()