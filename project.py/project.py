# take user input 
# ask which operator they want to use : +
# how many numbers to operate : 2 , [2,3]
# then show the result with operator sign : 2 + 3 = 5

                          # Day-05 Learning 📅
                          # Starting Time: 1:00 am 🕐
                          # Ending Time: 2:45 am 🕐
                          
print("HI")
operator=input("which operator do you wanna use,like +,-,*....") #we can take input by input() function.+
y=int(input("How many numbers to operate"))   # we can chose which type of input i want to take like int,float etc by int(),flost() build in function.
list=[]
for x in range(y):
    value=input(f"type the value:")
    list.append(value)
print(f"these numbers you have taken{list}")
if operator == '+':
    result=0
    for x in list:
        result+=int(x)
elif operator == '-':
    for x in list:
        rasult
elif operator == '*':
    result=1
    for x in list:
        result*=int(x) 
elif operator == '/':
    result=float(0)
    
print(f"final result={result}")