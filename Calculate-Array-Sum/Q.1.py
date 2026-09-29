num=int(input("enter no :"))
sum =0
while num>0:
    sum+= num%10
    num = num//10
print("sum",sum)
