s=int(input("enter size of array:"))
n=int(input("enter no of elements:"))


print(f"/n squares of {n} numbers starting from {s}:")
for i in range(s, s + n):
    print(i**2)
print("sum of square of first",i,"numbers is",sum)