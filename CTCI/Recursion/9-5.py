
def find_perms(s,perms):
	
	if len(s)==1:
		perms.append(s)
		return

	c = s[0]
	find_perms(s[1:],perms)
	added_perms = []
	for perm in perms:
		for i in range(len(perm)+1):
			added_perms.append(perm[:i] + c + perm[i:])
	perms.clear()
	perms += added_perms



def main():
	s="mansour"
	perms=[]
	find_perms(s,perms)
	print(perms)

if __name__ == '__main__':
	main()