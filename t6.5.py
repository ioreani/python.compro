print(" *** Odd/Even at Left/Right ***")
num = input("Enter numbers : ").split()
odd = []
even = []
for i in num :
    num = int(i)
    if num%2==0:
        even.append(num)
    else :
        odd.append(num)
print(f"odd = {odd}")
print(f"even = {even}")
print(f"odd+even = {odd+even}")
odd.reverse()
new = odd+even
print(f"new = {new}")