print(" *** Min Max Avg ***")
a,b,c = input("Enter 3 numbers : ").split()
a = int(a)
b = int(b)
c = int(c)
if a<= b and a<=c :
    min = a
    if b<= c:
        mid = b
        max = c
    else :
        mid = c
        max = b
elif b<=a and b<=c:
    min = b
    if a<= c :
        mid = a
        max = c
    else:
        mid = c
        max = a
else :
    min = c
    if a<= b :
        mid = a
        max = b
    else :
        mid = b
        max = a
print(f"min, mid, max ==> {min:.2f},{mid:.2f},{max:.2f}")
print(f"Average ==> {(min+mid+max)/3:.3f}")