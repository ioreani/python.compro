print("*** Sum odd / Subtract even ***")
num = input("Enter numbers : ").split()
sum = 0
for i in num :
    num = int(i)
    if num%2!=0 :
        sum += num
    else :
        sum -= num
print(f"Sum is {sum}")