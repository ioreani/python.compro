print(" *** Find startswith lines ***")
try:
   file_name, prefix = input("Enter file name : ").split()
   f = open(file_name)
   lines = f.readlines()
   f.close()
   count = 0
   for line in lines:
       if line.startswith(prefix):
            count+=1
   print(f"Total lines : {len(lines)}")
   print(f'The number of lines staring with "{prefix}" is {count}')
except:
   pass