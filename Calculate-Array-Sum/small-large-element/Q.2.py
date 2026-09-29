arr =list(map(int,input("enter numbers:").split()))
min=arr[0]
max=arr[0]

for num in arr:
    if num<min:
        min=num
    if num>max:
        max=num
print("minimum",min)
print("maximum",max)