print(" *** Data type integer float string ***")
x = input("Enter a word : ")
try :
    if '.' in x:
        x = float(x)
        print(f"{x:.5f} / 3 = {(x/3):.5f}")
    else :
        x = int(x)
        print(f"{x} // 7 = {(x//7)}")

except :
    print(f"{x} {x} {x} {x}")