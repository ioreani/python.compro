def draw_square(n,t) :
    if t == 1:
        for i in range(n) :
            for j in range(n):
               if i ==0 or i==n-1 or j==0 or j==n-1:
                print("*",end="")
               else :
                print(" ",end="")
            print()
    elif t == 2:
        for i in range(n) : 
                for j in range(n):   
                    if i ==0 or i==n-1 or j==0 or j==n-1:
                        if i == 0:
                            ch = (n-j)%10
                        elif i == n-1:
                            ch = (j+1)%10
                        elif j==0 :
                            ch =(n-i)%10
                        else :
                            ch = (i +1)%10
                        print(ch, end="")
                    else :
                        print(" ", end="")
                print()
    elif t == 3:
            for i in range(n) : 
                    for j in range(n): 
                        if j <= i:
                            ch = (j+1)%10
                        else:
                            ch = (i+1)%10
                        print(ch, end="")
                    print()
print(" *** Display square ***")
inp = (input("Enter height type : ")).split()
n = int(inp[0])
t = int(inp[1])
draw_square(n,t)
print("===== End of program =====")