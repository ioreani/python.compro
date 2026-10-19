print(" *** Transform second ***")
x = input("Enter seconds : ")

if '.' in x or (not x.replace("_","").replace("-","").isdigit()):
        print(f"! ! ! please enter a whole number ==> {x}")
        print(" --- program end ---")
else :
        x = int(x)
        original = x
        if x < 0:
                print("This number ({x}) is not VALID !!!")
        else :
                weeks = x//(7*24*60*60)
                x = x%(7*24*60*60)

                days = x//(24*60*60)
                x = x%(24*60*60)

                hours = x//(60*60)
                x= x%(60*60)

                minutes = x//60
                seconds = x%60

                result = ""

                if weeks > 0:
                        result = result + f"{weeks} weeks"
                if days > 0:
                        result = result + f"{days} days"
                if hours > 0:
                        result = result + f"{hours} hours"
                if minutes >0:
                        result = result + f"{minutes} minutes"
                if seconds >0 :
                        result = result + f"{seconds} seconds"

                result = result.strip()
                print(f"{original:,} seconds ==> {result} minutes")
                print(" --- program end --- ")