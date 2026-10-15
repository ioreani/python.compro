print(" *** Find number of lines for specific word ***")
try :
    file_name, word = input("Enter file name and word : ").split()
    f = open(file_name)
    lines = f.readlines()
    f.close()
    count = 0
    for line in lines:
      if word in line :
        count+=1
    print(f'Number of lines having "{word}" => {count}')
    print(f"Total lines => {len(lines)}")

except:
   pass