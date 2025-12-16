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
    elif operatorSign[i] == '>>':
        calcNum=int(calcNum)
        calcNum >>= numList[i + 1]
    elif operatorSign[i] == '<<':
        calcNum=int(calcNum)
        calcNum <<= numList[i + 1]
    elif operatorSign[i] == "&":
        calcNum=int(calcNum)
        calcNum &= numList[i + 1]
    elif operatorSign[i] == '^':
        calcNum=int(calcNum)
        calcNum ^= numList[i + 1]
        
print(calcNum)



# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR


# Example to run : 10 >> 2 * 11 << 3 / 10 & 2 ^ 6