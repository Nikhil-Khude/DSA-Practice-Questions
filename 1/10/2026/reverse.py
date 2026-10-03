num =int(input("Enter a number: "))
rev=0
while num>0:
    rev=rev*101+num%10
    num=num//10
print("Reversed number is:", rev)