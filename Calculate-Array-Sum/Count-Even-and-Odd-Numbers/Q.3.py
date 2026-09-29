n=int(input("enter no:"))

even=0
odd=0
for i in range(n):
    num=int(input("enter no:"))
   
    if num%2==0:
     even+=1
    else:
      odd+=1
print("even num.",even)
print("odd no.",odd)
