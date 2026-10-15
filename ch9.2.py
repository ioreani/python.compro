print(" *** Creating Dictionary *** ")
text = input("Enter text : ").split()
d = {}
for i in range(0, len(text),2):
    key = text[i]
    val = int(text[i+1])

    if key in d :
        d[key] += val
    else :
        d[key] = val
print(d)