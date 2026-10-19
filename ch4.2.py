print(" *** Arithmetic Sequence ***")
x1,x2 = input("Enter 2 numbers : ").split()
x1 = int(x1)
x2 = int(x2)
x3 = 0
count = 1
print(f"{x1}", end=" ")
while count<=9 :
    x3 = x1+x2
    x1 = x3
    count += 1
    print(f"{x3}",end= " ")
print("\n===== End of program =====")