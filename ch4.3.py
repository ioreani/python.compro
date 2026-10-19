print(" *** Arithmetic Sequence ***")
x1 = input("Enter an integer(n) : ")
x1 = int(x1)
i = 2
x2 = 0
while i <= x1 :
    x2 = x2+i
    if i+2 <= x1 :
        print(i, end="+")
    else :
        print(f"{i}" , end=" ")
    i += 2
print("=", x2)