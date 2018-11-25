import string
LOWERCASE = string.ascii_lowercase


def recursive_print(s,idx):
	if idx==len(s):
		return
	recursive_print(s,idx+1)
	print(s[idx],end="")
	

def reverse_with_pointers(str):
	l,r = 0, len(str)-1
	list_str = list(str)
	while l < r:
		tmp = list_str[l]
		list_str[l] = list_str[r]
		list_str[r] = tmp
		l+=1
		r-=1
	return "".join(list_str)


def reverse_with_special_chars(str):
	l,r = 0, len(str)-1
	list_str = list(str)
	while l < r:
		while not list_str[l].isalpha():
			l+=1
		while not list_str[r].isalpha():
			r-=1
		tmp = list_str[l]
		list_str[l] = list_str[r]
		list_str[r] = tmp
		l+=1
		r-=1

	return "".join(list_str)


def remove_duplicates(str):
	char_set = set()
	removed = []
	for char in str:
		if char not in char_set:
			char_set.add(char)
			removed.append(char)
	return "".join(removed)


def main():
	a = "this is a string"
	# print(a.find("is"))
	b = a.upper()
	# print(b.isupper())
	# print(a.title())
	# recursive_print("mansour",0)
	print(reverse_with_pointers("abcdef"))
	print(reverse_with_special_chars("Ab,c,de!$"))
	print(remove_duplicates("geeksforgeek"))
	print(LOWERCASE)


if __name__ == '__main__':
	main()