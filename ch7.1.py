print(" *** Adding number ***")
word = input("Enter your words : ").split()
ans = []
count = 0
for i in word :
    count+=1
    new = i + str(count)
    ans.append(new)
print(ans)
print(*ans)