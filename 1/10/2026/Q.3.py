num =int(input("Enter a number:"))
even=0
odd=0   
while num>0:
    if num%2==0:
        even=even+1
    else:
        odd=odd+1
    num=num//10
    
    
print("Even digits:", even)
print("Odd digits:", odd)