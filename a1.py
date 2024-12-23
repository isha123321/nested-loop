num=int(input("enter a number:"))
flag=True
for i in range(2,num,1):
    if num % i== 0:
      flag=False
    break
if (flag==True):
   print("its a prime number")
else :
   print("its a composite number")
