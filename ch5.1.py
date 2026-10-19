print(" *** Alphabet classification ***")
x = input("Input Sentence to count : ")
vowel = 'aeiou'
consonant = 'bcdfghjklmnpqrstvwxyz'
count_vowel = 0
count_consonant = 0
for i in x.lower() :
    if i in vowel :
        count_vowel += 1
    elif i in consonant :
        count_consonant += 1
print(f"\nVowel in this sentence is {count_vowel}")
print(f"Consonant in this sentence is {count_consonant}")
print("===== End of program =====")