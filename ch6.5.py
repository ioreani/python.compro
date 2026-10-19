print(" *** Odd/Even at Left/Right ***")
numbers = input("Enter numbers : ").split()
odd = []
even = []
for i in numbers :
    num = int(i)    
    if num%2!=0 :
        odd.append(num)
    else :
        even.append(num)
print(f"odd = {odd}")
print(f"even = {even}")
print(f"odd+even = {(even)+ (odd)}")
odd.reverse()
new = odd  + even
print(f"new = {new}")