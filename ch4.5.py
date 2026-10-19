print(" *** Fibonacci sequence ***")
a = input("Enter a0 a1 n : ")
a = a.split()
a0 = int(a[0])
a1 = int(a[1])
n = int(a[2])
count = 2
print(f"{a0}, {a1}" ,end="")
while count < n :
    a2 = a0 + a1
    if count <= n :
        print(f", {a2}", end ="")
    else :
        print(a2, end=" ")
    a0 = a1
    a1 = a2
    count = count + 1
print("\n===== End of program =====")    