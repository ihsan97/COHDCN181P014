a=0

sum=0
while True:
	a=raw_input("Enter Value: ")
    
	if a=='':
		break
    
	elif a.isdigit()==True:
 	 c=int(a)
       
	 sum=sum+c
print(sum)
