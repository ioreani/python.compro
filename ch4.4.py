print(" *** Power of n ***")
n = input("Enter n num : ")
n = n.split()
n1 = int(n[0])
n2 = int(n[1])
i = n1
count = 1 
while  i < n2 :
    i = i*n1
    count = count + 1
if i == n2 :
       print(f"{n2} is the power of {n1}.")
       print(f"{n2} =" , end=" ")
       j = 1
       while j <= count :
          if j == count :
             print(n1)
          else :
             print(n1, end="*")
          j = j + 1
else :
       print(f"{n2} is NOT the power of {n1}.")
print("===== End of program =====")