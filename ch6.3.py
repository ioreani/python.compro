print(" *** Maximum occurence ***")
num = input("Enter numbers : ").split()
num_list = []
for i in num :
    num = int(i)
    num_list.append(num)
print(num_list)

data = []
for num in num_list :
    if num == -1 :
        break
    data.append(num)

max_count = 0
for num in data :
    count = data.count(num)
    if count  > max_count :
        max_count = count 
print(f"Max count = {max_count}")

ans = []
for num in data :
    if data.count(num) == max_count and num not in ans :
        ans.append(num)
print(f"Max occurence = {ans}")