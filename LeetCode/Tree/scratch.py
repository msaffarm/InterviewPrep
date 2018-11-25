def foo(*args,**kwargs):
	for x in args:
		print(x)
	for k,v in kwargs.items():
		print(k)


l = [1,2,3]
g = [4,5,6]
c = dict(zip(l,g))
a,b = zip(*c)
print(a)
d = dict(a=2,b=3,d=4)

# foo(*l,**d)
