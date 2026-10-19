x = input("Enter a word and a number: ")
word, key = x.split()
key = int(key)
if key < 1 or key > 26 :
    print("Number must be between 1-26")
else :
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    word = word.upper()
    result = ""
    for i in word :
        position = abc.find(i)
        new_position = (position-key)%26
        result += abc[new_position]
print(result)