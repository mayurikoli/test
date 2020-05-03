list=[]
temp=[]
no=int(input("Enter limit:"))
for x in range(no):
	num=(int(input("Enter Number :")))
	list.append(num)
for x in list:
	if x not in temp:
		temp.append(x)
print(temp)
	
