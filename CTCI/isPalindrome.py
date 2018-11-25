
def is_palindrome(s,start,end):
	if end-start==1 or end-start==2:
		return s[start]==s[end]

	return s[start]==s[end] and is_palindrome(s,start+1,end-1)


def main():
	s = "addl7ldda"
	print(is_palindrome(s,0,len(s)-1))


if __name__ == '__main__':
	main()