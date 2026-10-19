print(" *** Histogram ***")
file = input("Enter file name and word : ")

try:
    fname, targetword = file.split()
    fhand = open(fname)
    
    countline = 0
    counts = 0 
    linesum = 0
    char_freq = {}
    
    for line in fhand:
        countline += 1
        
        # เช็คว่ามีคำนี้ปรากฏในบรรทัดหรือไม่
        if targetword in line:
            # นับจำนวนครั้งที่คำนี้ปรากฏในบรรทัด
            counts += line.count(targetword)
            linesum += countline
            
            # เก็บความถี่ตัวอักษรเฉพาะในบรรทัดที่มีคำนี้อยู่
            for char in line:
                if char.isalpha():
                    char_freq[char] = char_freq.get(char, 0) + 1
                    
    fhand.close()
    
    print(f'Number of "{targetword}" => {counts}')
    print(f"Sum of line number => {linesum:,}")
    print(f"Total lines => {countline:,}")
    
    # แสดง 3 อันดับแรก
    for _ in range(3):
        if not char_freq:
            break
        
        best_char = None
        max_count = -1

        for char, count in char_freq.items():
            if count > max_count:
                max_count = count
                best_char = char
            elif count == max_count:
                if best_char is None or char > best_char:
                    best_char = char

        stars = "*" * max_count
        print(f" {best_char}  => {stars} {max_count}")
        
        del char_freq[best_char]

except:
    print(f"Error can not open file => {fname}")

print("===== End of program =====")