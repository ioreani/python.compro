print(" *** Grade Classification ***")
score = input("Enter your score : ")
x = int(score)
if x < 0 or x >100 :
    print(f"{x:.2f} is invalid ! ! !")
elif x >= 80 :
    print(f"Grade A")
elif x >= 75 :
    print(f"Grade B+")
elif x >= 70 :
    print(f"Grade B")
elif x >= 65 :
    print(f"Grade C+")
elif x >= 60 :
    print(f"Grade C")
elif x >= 55 :
    print(f"Grade D+")
elif x >= 50 :
    print(f"Grade D")
elif 1< x<50:
    print("Grade F")