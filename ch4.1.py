print(" *** Sum of common divisors ***")
n1,n2 = input("Enter n1 n2 : ").split()
n1 = int(n1)
n2 = int(n2)
sum = 0
i = 1
while i<=n1:
    if n1%i==0 and n2%i==0:
        print(f"{i}", end=" ")
        sum += i
    i += 1
print(f" ==> {sum}")
