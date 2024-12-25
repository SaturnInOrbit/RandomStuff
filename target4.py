tria = eval(input("Enter amount of triangles: "))
for x in range(1,8):
	for y in range(1,tria+1):
		print(x * "* ",end="\t")
	print()