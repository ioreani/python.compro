print(" *** Transform to seconds ***")
h,m,s = input("Enter h m s : ").split()
h = int(h)
m = int(m)
s = int(s)
total = h*3600 + m*60 + s
print(f"{h} hours {m} minutes {s} seconds = {total:,d} seconds")