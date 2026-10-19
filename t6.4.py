print(" *** Max Min ***")
num = input("Enter numbers : ").split()
num_list = []
for i in num :
    num = int(i)
    num_list.append(num)
print(f"list = {num_list}")

max_val = num_list[0]
min_val = num_list[0]
for num in num_list:
    if num > max_val:
        max_val = num
    elif num < min_val :
        min_val = num
print(f"Max = {max_val}")
print(f"Min = {min_val}")