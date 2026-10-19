print(" *** Max Min ***")
numbers = input("Enter numbers : ").split()
list_num = []
for i in numbers :
    num = int(i)
    list_num.append(num)
print(f"list = {list_num}")

max_val = list_num[0]
min_val = list_num[0]
for num in list_num :
    if num  > max_val:
        max_val = num 
    elif num < min_val:
        min_val = num
print(f"Max = {max_val}")
print(f"Min = {min_val}")