print(" *** Creating Dictionary ***")
text = input("Enter text : ").split()
d = {}
for i in range(0,len(text),2):
    d[text[i]] = text[i+1]
print(d)