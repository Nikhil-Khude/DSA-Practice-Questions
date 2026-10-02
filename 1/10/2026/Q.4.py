arr = list(map(int, input("Enter numbers: ").split()))

search = int(input("Enter number to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == search:
        print("Number is present at position:", i + 1)
        found = True

if not found:
    print("Number is not present in the array")