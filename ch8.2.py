def adder(num1, num2):
   try:
      n1 = int(num1) if num1.lstrip('-').isdigit() else float(num1)
      n2 = int(num2) if num2.lstrip('-').isdigit() else float(num2)
      ans = n1 + n2
      return int(ans) if type(ans) == int  else ans
   except :
      print("num1 or num2 is NOT VALID !!!")
      exit()
print(" **** Adder Function ***")
num1, num2 = input('Enter 2 numbers: ').split()
result = adder(num1, num2)
fstring = f"{num1} + {num2} = {result}" 
print(fstring)
print("====== End of program =====")
   