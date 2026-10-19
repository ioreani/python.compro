print(" *** Integer type and odd even ***")
number = input("Enter any number : ")
number = int(number)
if number < 0 :
    print(f"{number} is negative.")
elif number == 0:
    print(f"{number} is zero.")
else :
    print(f"{number} is positive.")

if number%2==0:
    print(f"{number} is even.")
else  :
     print(f"{number} is odd.")
