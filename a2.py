startvalue=int(input("enter a value:"))
endvalue=int(input("enter a value:"))
for num in range(startvalue , endvalue):
    flag=True
    for i in range(2,num,1):
      if num % i== 0:
        flag=False
        break
    if (flag==True):
       print(num,end=" , ")