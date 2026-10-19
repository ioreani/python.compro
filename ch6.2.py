print(" *** Sequence Verification ***")
num = input("Enter Input : ").split()
numbers = []
for i in num:
    numbers.append(int(i))
    is_ascending = True
    is_descending = True
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            is_ascending = False
        elif numbers[i] < numbers[i+1]:
            is_descending = False
if is_ascending :
    print("Ascending sequence !!!")
elif is_descending :
    print("Descending sequence !!!")
else :
    print("Neither ascending or descending sequence !!!")