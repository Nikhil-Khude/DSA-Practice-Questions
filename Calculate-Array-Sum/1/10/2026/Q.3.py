num=int(input("enter a no.:"))
orgignal=num
reversed=0
while(num>0):
    reminder=num%10
    reversed=reversed*10+reminder
    num=num//10
print("original no:",orgignal)
print("revresed no:",reversed)