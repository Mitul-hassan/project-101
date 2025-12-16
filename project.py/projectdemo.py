countNum = int(input("How many numbers you want to operate with :"))
numList = []
operatorSign = []

for i in range(countNum - 1):
    operatorSign.append(input(f"Give the operator signs {i}: "))
    
for i in range(countNum):
    numList.append(int(input(f"Enter the number of {i} index: ")))
    
calcNum = numList[0]

for i in range(countNum - 1):
    if operatorSign[i] == "+":
        calcNum += numList[i + 1]
    elif operatorSign[i] == "-":
        calcNum -= numList[i + 1]
    elif operatorSign[i] == "*":
        calcNum *= numList[i + 1]
    elif operatorSign[i] == "/":
        calcNum /= numList[i + 1]
    elif operatorSign[i] == '>>':        #calcNum becomes a float (due to /).Then bitwise operators will fail ❌.
        calcNum=int(calcNum)              #Example: calcNum = 5
        calcNum >>= numList[i + 1]          #       calcNum /= 2    now 2.5 (float)
    elif operatorSign[i] == '<<':           #       calcNum &= 3      # ❌ TypeError
        calcNum=int(calcNum)                #       Same for:>>, <<, ^
        calcNum <<= numList[i + 1]
    elif operatorSign[i] == "&":
        calcNum=int(calcNum)
        calcNum &= numList[i + 1]
    elif operatorSign[i] == '^':
        calcNum=int(calcNum)
        calcNum ^= numList[i + 1]
        
print(calcNum)





# Example to run : 10 >> 2 * 11 << 3 / 10 & 2 ^ 6