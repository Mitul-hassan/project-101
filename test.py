          #First Day of Learning

'''
1. Comment (Single/Multi) ✅
2. Variable 
3. Print
'''
#1.learning comment single and multiple.

#single comment
print("we can comment a single line with the sign of #")
#for example-
#print("hello world")

'''
learning multiple comment
'''
#python does not really have any synthex for multiple comment.But one thing we can do that we can add # infront of every line for commrnting or
# we can take a big string wihin """ """ this sign cause python does not take any string uless we add any varriale with it.

# 2. learning  variables.
'''
variables are container for storing data value.python has no command for diclering the varriable.a variable is created when we first assain a value.

'''
x=11
y="MItul"
print(y,x)

#variable does not need to decler any particular type even we can change the type as our needing.
z=11
z='Mitul'
print(z)

#by casting we can specify the data type
a=str(3) #here a is a string '3'
a=int(3) #here integrer 3.
a=float(3) #here float 3.0.

#with the help of 'type()' function we can get the data type of a variable.
print(type(x))
print(type(y))

#variable names are case sentative
a=11
A='mitul' #A will not over write a.

'''
 A varible name can contain only alpha numeric character and underscore(A-z,0-9,_).
 and can't start with number must start with latter or underscore.can't be any python key-woard.
'''
myvar='mitul'
my_var='mitul'
#my-var='mitul'     -illegal variable name
#my var='mitul'     -illegal variable name
my_variable_name='mitul'
MyVariableName='mitul'

#python allows to assign value to multiple variable in one line.
b,c,d='mahmudul','hassan','mitul'
print(b)
print(c)
print(d)

#like B,C,D='banana' it does not allow

#If we have a collection of values in a list, tuple etc. Python allows us to extract the values into variables. This is called unpacking.
fruits=['apple','banana','cherry']
e,f,g=fruits
print(e,f,g)

#output variable
#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
h,i,j='python','is','awesome'
print(h,i,j)

#global variable
#global vriable can be used by every one, both inside and outside of function
m='awawsome'
def myfunc():
    print("puthon is",m)
    myfunc()
#create a variavle inside a function with the name as the global vraiable.
m='awawsome'
def myfunc():
    m='fantastic'
    print('python is',m)
myfunc()
print('python is',m)
#To create a global variable inside a function, we can use the global keyword.
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

#3.learning output
#By default, the print() function ends with a new line.
#If we want to print multiple words on the same line, we can use the end parameter:
print('hello world',end=" ")
print('i will print on the same line')
#note:we add a space after end=" " for better readability.