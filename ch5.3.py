print(" *** Pyramid-II ***")
x = input("Enter height : ")
x = int(x)
sentent = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = 0
for row in range(x) :
    line = ' '*(x-row-1)
    for ch in range(2*row+1):
     line += sentent[n%26]
     n += 1
    print(line)
print("===== End of program =====")