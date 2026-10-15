def bubbleSort(numList):
    global swapCount
    n = len(numList)
    for i in range(n) :
        for j in range(0,n - i -1) :
            if numList[j] > numList[j+1] :
                numList[j], numList[j+1] = numList[j+1], numList[j]
                swapCount +=1
                print(f"{swapCount} => {numList}")
    return swapCount
print(" *** Bubble sort ***")
swapCount = 0
numinput = input("Enter numbers : ").split()
numList = [int(x) for x in numinput]
print(numList)
bubbleSort(numList)
print("Sorted =>", numList)
print(f"swap count = {swapCount}")
print("===== End of program =====")