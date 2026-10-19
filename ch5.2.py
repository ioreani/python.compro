print(" *** Word Triangle ***")
x = input("Enter Word: ")
row = 0
for row in range(len(x)) :
    line = x[0:row+1]
    print(line)
    row += 1