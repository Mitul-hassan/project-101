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
    
print(calcNum)