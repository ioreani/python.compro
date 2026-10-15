inp = input("Enter : ").split()
dict_old = {'Volkswagan': 1, 'Toyota': 2, 'Tesla': 2}
print(f"dict_old = {dict_old}")
dict_new = dict_old.copy()

for i in range(0,len(inp),2):
    brand = inp[i]
    count = int(inp[i+1])
    if brand in dict_new :
        print(f"{brand} exists in dicts")
        dict_new[brand] += count
    else :
        print(f"{brand} does not exist")
        dict_new[brand] = count
print(f"dict_new = {dict_new}")