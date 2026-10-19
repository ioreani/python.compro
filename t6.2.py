print(" *** Sequence Verification ***")
num = input("Enter Input : ").split()
num_list = []
for i in num :
    num = int(i)
    num_list.append(num)

is_ascending = True
is_descending = True

for i in range(len(num_list)-1):
    if num_list[i]>num_list[i+1]:
        is_ascending = False
    elif  num_list[i]<num_list[i+1]:
        is_descending = False

if is_ascending:
    print("Ascending sequence !!!")
elif is_descending:
    print("Descending sequence !!!")
else :
    print("Neither ascending or descending sequence !!!")