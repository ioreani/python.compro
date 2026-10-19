print(" *** File Error Handling ***")
file_name, word = input("Enter file name and word : ").split()
try:
    f = open(file_name)
    lines = f.readlines()
    f.close()

    count = 0
    sum_line_num = 0
    for idx, line in enumerate(lines, start=1):
        if word in line :
            count +=1
            sum_line_num += idx
    print(f'Number of lines having "{word}" => {count}')
    print(f"Sum of line number => {sum_line_num}")
    print(f"Total lines => {len(lines)}")
except:
    print(f"Error can not open file => {file_name}")