print("*** Shopping List 2 ***")
inp = input("Enter some pairs of (operation, item): ").split(',')
shopping_dict = {
    "egg" : 1,
    "ham" : 1,
    "water" : 1,
    "soda" : 1
}
for cmd in inp :
    cmd = cmd.strip()
    if not cmd:
       continue
    parts = cmd.split()
    op = parts[0]
    if op =='a':
        item = parts[1].lower()
        if item in shopping_dict:
            shopping_dict[item] +=1
        else :
            shopping_dict[item] =1
    elif op == 'r':
        item = parts[1].lower()
        if item in shopping_dict:
            shopping_dict[item] -=1
            if shopping_dict[item] == 0:
                del shopping_dict[item]
    else :
        print("Operation not supported!")
        exit()
print("Final shopping dict is",shopping_dict )