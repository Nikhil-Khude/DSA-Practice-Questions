arry =list(map(int,input("enter no:").split()))
min=arry[0]
max=arry[0]
for i in arry:
    if i<min:
        min=i
    if i>max:
        max=i
print("min:",min)
print("max:",max)