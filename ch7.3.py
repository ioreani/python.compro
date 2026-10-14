print(" *** Toggle first vowel ***")
x = input("Enter words : ")
x = x.split()
for i in range(len(x)):
    for c in x[i] :
        if c in "aeiouAEIOU" :
            new_c = c.upper() if c in "aeiou" else c.lower()
            x[i] = x[i].replace(c,new_c,1)
            break
print(" ".join(x))
print("===== End of program =====")