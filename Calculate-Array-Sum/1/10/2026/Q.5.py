#remove duplicate from list
list = [1, 2, 3, 2, 4, 1, 5]
unique_list = []
for item in list:
    if item not in unique_list:
        unique_list.append(item)
print("List after removing duplicates:", unique_list)