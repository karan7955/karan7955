height = int(input("enter your hight: "))
extra = 0
spaces = height - 1
for i in range(1,height+1):
	print(" "*spaces,"*"*i,"*"*extra)
	spaces -= 1
print((height-1)*" ","||")
