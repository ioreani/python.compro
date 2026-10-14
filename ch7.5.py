print(" *** Find divisible number *** ")
x = input("Enter sNum divisor : ")
sNum, divisor =x.split()
divisor = int(divisor)
ans = []
for x in range(10) :
    for y in range(10) :
        num_str = sNum.replace('x',str(x)).replace('y',str(y))
        num = int(num_str)
        if num % divisor ==0:
            ans.append(num)
print(ans)
print("===== End of program =====")