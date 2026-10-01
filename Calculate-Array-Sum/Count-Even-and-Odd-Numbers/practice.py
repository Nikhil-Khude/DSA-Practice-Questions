num=int(input("enter no:"))
even=0
odd=0
for i in range(num):
    if num%2==0:
        even+=1
    if num%2!=0:
        odd+=1
print("even",even)
print("odd",odd)