            # Day-01 Learning 📅
            # Starting Time: 11:35 am 🕐
             # Ending Time: 2:30 am 🕐

'''
1. Comment (Single/Multi) ✅
2. Variable✅
3. Print✅
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

            # Day-02 Learning 📅
            # Starting Time: 11:05 am 🕐
            # Ending Time: 2:00 am 🕐
            
                   
'''
operators✅
'''
                   
#operators:used to perform operation on variables and values.
# + operator usally use to add of two valued as well as can be use to add a variable and vlue or add two variables.
print(5+10)
sum1= 100+50
sum2=sum1+250
sum3=sum1+sum2
print(sum1,sum2,sum3)

#arithmetic opwerators
x=15
y=4
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y) # **=power
print(x//y) # //=floor division(rounds down to the nearest integer)

#assignment operator
x+=2 #x=x+2
x**=3
x&=3 #binary 'and' operation bit wise(suppose x=2=0010
                         #   3=0011 so the and of 0010
                        #                        0011
                        #                       =0010=2)
x|=3 #binary bit wise 'or' operation.
x^=3 # bit wise 'x-or' operation.
x>>=3 #right shift of 3 bits.
x<<=2 #left shift of 2 bits.
print(x:=3) # x=3 print(x).known as walrus operator.                     
x=5
y=3
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print(1<x<10)
print(1<x and x<10)
print(1<x or x<10)
print(not(x>3 and x<10))  # reverse the result with not.
x=[1,2,3]
y=[1,2,3]
print(x is y)     #'is''is not' checks both variables point to the same object in memory.
print(x is not y)
print(x==y)       # '==' check if the values of both variables are equal.            
fruits=["apple","banana","chery"]
print("pineapple" in fruits)     # 'in'returns true if a sequence with specified value is present in the object.               
print("pineapple" not in fruits) #'not in' returns true if a sequence with specified value is not present in the object. 
text='hello world'
print('hi' in text)
print ("hello" in text)
print('z' not in text)
'''
which operator will work first,second,third......
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction
'''
             # Day-03 Learning 📅
             # Starting Time: 1:05 am 🕐
             # Ending Time: 2:30 am 🕐
                
'''
Lists(access list,change list,add list,remove list)✅
'''

'''list are used to store multiple items in a single variable.Lists are created using square brackets.
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If we add new items to a list, the new items will be placed at the end of the list.list item can be of any data type.
'''
thislist=["apple","banana","cherry"]
print(thislist)
list1=[1,2,3,4,5]
list2=[True,False,False]
list3=['abc',34,True,'male']
print(list3)
print(type(list1))
#list() comstructor:we can create new list using this.
list4=list(('mahmudul','hassan','mitul','fahim','ashik','ananta'))
print(list4)

#ACCESS ITEMS
#access them by referring to the index number
print(list4[1])
#Negative indexing means start from the end.-1 refers to the last item, -2 refers to the second last item etc.
print(list4[-1])
#we can specify a range of indexes by specifying where to start and where to end the range.When specifying a range, the return value will be a new list with the specified items.
print(list4[2:5]) #that means from 2 index to befor 5.5 is not included and index start from 0.
print(list4[2:])  #this will return from 2 to end.
print(list4[-4:-1])
#To determine if a specified item is present in a list use the in keyword
if "mahmudul" in list4:
    print("yes,hete acche")

#Change Item Value
#To change the value of a specific item, refer to the index number
#suppose to change the second item.
list4[1]='shakil'
print(list4)
# to change 1 to excluding 3
list4[1:3]=['billah','masum'] 
print(list4)
#If we insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
list4[1:2]=['alif','fardin']
print(list4) #The length of the list will change when the number of items inserted does not match the number of items replaced.
#if we insert less items than we replace, the new items will be inserted where we specified, and the remaining items will move accordingly.
list4[1:3]=['abul']
print(list4)

#Add List Items
#Insert Item
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.this method inserts an item at the specific index.
thislist=['apple','banana','chery']
thislist.insert(2,'watermelon')
print(thislist) #watermelon will inserted in idex 2 and before index value will take place after watermelon and other values one by one.
# As a result of the example above, the list will now contain 4 items

#Append Items:To add an item to the end of the list, use the append() method.
thislist=['apple','banana','cherry']
thislist.append('orange')
print(thislist)
#Extend List:To append elements from another list to the current list, use the extend() method.
thislist=['apple','banana','chery']
tropical=['mango','pineapple','papaya']
thislist.extend(tropical)
print(thislist) #The elements will be added to the end of the list.
#Add Any Iterable:The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove List Items
#Remove Specified Item:The remove() method removes the specified item.
thislist=['apple','banana','cherry']
thislist.remove('banana')
print(thislist)
#If there are more than one item with the specified value, the remove() method removes the first occurrence
#Remove the first occurrence of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#The pop() method removes the specified index.If we do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#The del keyword also removes the specified index.
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
del thislist  #The del keyword can also delete the list completely if we donot mention the index.
#The clear() method empties the list.The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

              # Day-04 Learning 📅
              # Starting Time: 10:30 am 🕐
              # Ending Time: 12:30 am 🕐
'''
1.loop list✅
2.comprehension list✅
'''
#LOOP LIST
#print all item in the list one by one by using for loop.
thislist=['apple','banana','cherry']
for x in thislist:
    print(x) 
    
#using index number:
thislist=['apple','banana','cherry']
for i in range (len(thislist)):
    print(thislist[i])  #Using the range() and len() functions to create a suitable iterable.

#using while loop:
thislist=['apple','banana','cherry']
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1

#LOPING USING LIST COMPREHENSION:
#short hand 'for' loop.
thislist=['alu','kadu','jingha']
[print(x) for x in thislist]

#using 'for' loop without list comprehension 
fruits=['apple1','banana1','cherry1','kiwi1','mango1']
newlist=[]

for fruit in fruits:
    if "apple1" in fruit:
        newlist.append(fruit) 
    elif "banana1" in fruit:
        newlist.append("hunky punky")    
    # break
print(newlist)

#with list comrehension
fruits=['alu','kadu','jhinga','morich']
print(len(fruits))
newlist=[x for x in fruits if "a" in x]
print(newlist)

#synthex=[(return ki korbo)(lopp & condition) ]
newlist=[x for x in fruits if x!='alu']
print(newlist)
newlist=[x for x in range(10)] #use of range() function.
print(newlist)
newlist=[x for x in range(8) if x<5]
print(newlist)
#Set the values in the new list to upper case:
newlist=[x.upper() for x in fruits]
print(newlist)
#Set all values in the new list to 'hello'
newlist=['hello' for x in fruits]
print(newlist)
#Return "orange" instead of "morich"
newlist=[x if x!='morich' else 'orange' for x in fruits]
print(newlist)

                  # Day-06 Learning 📅
                  # Starting Time: 1:15 am 🕐
                  # Ending Time: 2:52 am 🕐
'''
1.sort list✅
2.copy list✅
3.join list✅
4.list method✅
'''
#sort list:'sort()' method that will sort the list alphanumerically,assending by default.
thislist=['orrange', 'mango','kiwi','pineapple','banana']
thislist.sort()
print(thislist)

thislist=[100,50,65,82,23]
thislist.sort()
print(thislist)

#to sort descending, use the keyword argument "reverse=True".
thislist=['ornage','mango','kiwi','pineapple','banana']
thislist.sort(reverse=True)
print(thislist)

#customizing a function using the key word argument "key=function".The function will return a number that will be used to sort the list .
#sort the list bassed on how close the number is to 50:
def myfunc(n):
    return abs(n-50)

thislist=[100,50,65,82,23]
thislist.sort(key=myfunc)    #this will minus 50 from the element and sort in ascending order then it will return as the main elemnt. 
print(thislist)  #like first, minus reslt in ascending order =[0,15,27,32,50] if we convert it to main element=[50,65,23,32,100].

#by default the 'sort()' mthod is case sensative.
thislist=['banana','Oraange','Kiwi','cherry']
thislist.sort()
print(thislist)

#if we want case-insensative sort function we have to use 'str.lower' as a key function.
thislist.sort(key=str.lower) #str.lower converts each word to lowercase only for comparison, not permanently.
print(thislist)

#The 'reverse()' method reverses the current sorting order of the elements.
thislist=['banan','Orange','Kiwi','cherry'] #current sorting order.
thislist.reverse() #this will just revese the lis.
print(thislist) 

#Copy list:You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#using the 'copy()' method,list() method,:(slice) operator.
thislist=['apple','banana','chery']
mylist=['hassan','mitul']
mylist=thislist.copy()
mylist=list(thislist)
mylist=thislist[:]
print(mylist) #after coping from thislist all element of mylist will be replaced by thislist element.there will no elment of mylist.

#Join list
#using '+' operator
list1=['a','b','c']
list2=[1,2,3]
list3=list1+list2
print(list3)
#by appending all the items from list2 into list1.
list1=['a','b','c']
list2=[1,2,3]
for x in list2:
    list1.append(x)
print(list1)
#using 'extend()' method
list1.extend(list2)
print(list1)


                # Day-07 Learning 📅
                # Starting Time: 1:15 am 🕐
                # Ending Time: 2:52 am 🕐
'''
Python Tuples
1.Access Tuples✅
2.Update Tuples✅

'''
#Tuples are use to store multiple items in a single variable.
#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.
thistuple= ('apple','banana','cherry')
print(thistuple)

#To determine how many items a tuple has, use the len() function:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ('apple',)
print(thistuple)
thistuple = ('apple') #not a tuple

#Tuple items can be of any data type.String, int and boolean data types.
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

#It is also possible to use the tuple() constructor to make a tuple.
thistuple =tuple(('apple','banan','cherry'))
print(thistuple)

#Access tuple items
#access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative indexing means start from the end.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#can specify a range of indexes by specifying where to start and where to end the range.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#To determine if a specified item is present in a tuple use the in keyword:
thistuple = ('apple','banana','cherry')
if 'apple' in thistuple:
    print('yes,apple has')
    
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

#change tuple values:
x=('apple','banana','cherry')
y=list(x)
y[1]='kiwi'
x=tuple(y)
print(x)

#add items:
thistuple = ('apple','banana','chery')
y = list(thistuple)
y.append('orange')
thistuple = tuple(y)
print(thistuple)

#add tuple to tuple:
thistuple = ('apple', 'banan', 'orange')
y = ('green', 'yellow', 'orange')
thistuple += y
print(thistuple)

#remove tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

                # Day-08 Learning 📅
                # Starting Time: 1:15 am 🕐
                # Ending Time: 2:52 am 🕐
'''
1.Unpack Tuple.✅
2.Loop Tuple.✅
'''
#1.unpack tuple:When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"

fruits =('apple','banana','cherry')

(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)
#The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

#using Asterisk(*):Assign the rest of the values as a list called "red".
fruits=('apple','banana','cherry','strwberr','raspberry')
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits=('alu','begun','naspoti','dundul','bedena')
green,*tropic,red=fruits
print(green)
print(tropic)
print(red)

#2.Loop tuples:
#we can loop through the tuple items by using a for loop.
thistuple=('mahmus','hassan,','mitul')
for x in thistuple:
    print(x)

#eferring to their index number.Using the range() and len() functions to create a suitable iterable.
for i in range(len(thistuple)):
    print(thistuple[i])

#using whole loop:
thistuple=('apple','banana','naspoti')
i=0
while i < len(thistuple) :
    print(thistuple[i])
    i+=1
    
                # Day-09 Learning 📅
                # Starting Time: 12:30 am 🕐
                # Ending Time: 1:00 am 🕐
'''
1.Join tuples✅
2.Tuple methods✅
'''                
#1.join tuples
#Join two tuples:to join two or more tuples we can use the '+' operator.

tuple1=('a','b','c')
tuple2=(1,2,3)
tuple3=tuple1+tuple2
print(tuple3)

#multiply tuples:if we want to multiply the content of a tuple a given numbers of times, we can use the '*' sign.
fruits=('apple','banana','cherry')
mytuple=fruits*2
print(mytuple)

#Tuples methods
#'count()' return the number of times a specified value occur in a tuple.
thistuple=(1,2,3,4,5,3,4,5,6,6,7)
x=thistuple.count(3)
print(x)

#'index()' searches the tuple for a specific value and return the posituon of where it is found.
nametuple=('mahmudul','hassan','mitul')
print(nametuple.index('mitul')) 

                    # Day-10 Learning 📅
                    # Starting Time: 11:30 am 🕐
                    # Ending Time: 12:30 am 🕐
'''
1.Python set✅
2.Access set✅
3.Add set✅
'''

#1.Python set:

#Sets are used to store multiple items in a single variable.A set is a collection which is unordered, unchangeable*, and unindexed.
#Unordered:Set items are unchangeable, but you can remove items and add new items.Sets are unordered, so you cannot be sure in which order the items will appear.
#Unchangeable:Once a set is created, you cannot change its items, but you can remove items and add new items.
myset={'apple','banana','cherry'}
print(myset)

#Duplicates Not Allowed:Sets cannot have two items with the same value.One item of same value will shown.
thisset= {'apple','banana','cherry','apple'}
print(thisset)

#The values True and 1 and The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset= {'apple','banana','cherry',True,1,2}
print(thisset)
thisset={'apple','banana','cherry',False,True,0}
print(thisset)

#get the length of the set by len() function.
thisset={'apple','banana','cherry'}
print(len(thisset))

#Data type:set item can be of any data type:
set1={'apple','banana','chery'}
set2={1, 5, 7, 9, 3}
set3={True, False, False}
setmix={'abc', 34, True, 40, 'male'}

#data type of a set:
myset={'apple','banan','cherry'}
print(type(myset))

#using the set() constructor to make a set:
thisset= set(('apple','banana','cherry')) ## note the double round-brackets
print(thisset)

#2.Access set item:You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the 'in' keyword.
thisset={'apple','banana','cherry'}
for x in thisset:
    print(x)

#check if 'banana' is present in the set:
thisset={'apple','banana','cherry'}
print('banana' in thisset)

#check if 'banana' is NOT present in the set:
thisset={'apple','banana','cherry'}
print('banana' not in thisset)

#3.Add set item:Once a set is created, you cannot change its items, but you can add new items.
#to add one set item to a set use the 'add()' method.
thisset={'apple','banana','cherry'}
thisset.add('orange')
print(thisset)

#Add Sets:To add items from another set into the current set, use the update() method.
thisset={'apple','banana','cherry'}
tropical={'pineapple','mango','papaya'}

thisset.update(tropical)
print(thisset)

#Add Any Iterable:The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset={'apple','banana','cherry'}
mylist=['kiwi','orange']
thisset.update(mylist)
print(thisset)

                    # Day-11 Learning 📅
                    # Starting Time: 12:05 am 🕐
                    # Ending Time: 12:30 am 🕐
'''
1.Remove set item✅
2.loop in set✅
'''
#1.Remove set item:To remove an item in a set, use the remove(), or the discard() method.
thisset={'apple','banana','cherry'}
thisset.remove('banana')
print(thisset)
#if the remove item does not exit in the set, remove() method will give an error.

#using discard() method:If the item to remove does not exist, discard() will NOT raise an erro.so this is safer than remove() method.
thisset={'apple','banana','cherry'}
thisset.discard('banana')
print(thisset)

#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.
thisset={'apple','banana','cherry'}
x=thisset.pop()
print(x)
print(thisset)

#The clear() method empties the set:
thisset={'apple','banana','cherry'}
thisset.clear()
print(thisset)

#The del keyword will delete the set completely:
thisset={'apple','banana','cherry'}
del thisset
#print(thisset)=there is no thisset so this will give error.

#2.loop through the set:we can loop through the set items by using a for loop:
myset={'apple','banana','cherrry'}
for x in myset:
    print(x)

                     # Day-12 Learning 📅
                    # Starting Time: 12:30 am 🕐
                    # Ending Time: 1:30 am 🕐
'''
1.Join set✅
2.Frozen set✅
3.set methods✅
'''
#1.Join set:There are several ways to join two or more sets in Python.The union() and update() methods joins all items from both sets.
#The Union() method returns a new set with all items from both sets.The union() method allows you to join a set with other data types, like lists or tuples.

set1={'a','b','c'}
set2={1,2,3}
set3=set1.union(set2)
print(set3)

#You can use the | operator instead of the union() method, and you will get the same result.The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
set1={'a','b','c'}
set2={1,2,3}
set3=set1|set2
print(set3)

#All the joining methods and operators can be used to join multiple sets.When using a method, just add more sets in the parentheses, separated by commas.
set1={'a','b','c'}
set2={1,2,3}
set3={'John','elena'}
set4={'apple','banana','cherry'}
myset=set1.union(set2,set3,set4)
print(myset)
  
#When using the | operator, separate the sets with more | operators:
set1={'a','b','c'}
set2={1,2,3}
set3={'john','alena'}
set4={'apple','banana','cherry'}
myset=set1|set2|set3|set4
print(myset)     

#The union() method allows you to join a set with other data types, like lists or tuples.
x={'a','b','c'}
y=(1,2,3)
z=x.union(y)
print(z)
 
# The update() method inserts all items from one set into another.The update() changes the original set, and does not return a new set.
#The update() method inserts the items in set2 into set1:
set1={'a','b','c'}
set2={1,2,3}
set1.update(set2)
print(set1)

# Both union() and update() will exclude any duplicate items.

#Intersection:Keep ONLY the duplicates.The intersection() method will return a new set, that only contains the items that are present in both sets.
set1={'apple','banana','cherry'}
set2={'google','microsoft','apple'}
set3=set1.intersection(set2)
print(set3)

#we can use the & operator instead of the intersection() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

#Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1={'appple','banana','cherry'}
set2={'google','microsoft','apple'}
set1.intersection_update(set2)
print(set1)

#The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

#Difference:The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1={'apple','banana','cherry'}
set2={'google','microsoft','apple'}
set3=set1.difference(set2)
print(set3)

#we can use the - operator instead of the difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

# The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

#The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

#Symmetric Differences:The symmetric_difference() method will keep only the elements that are NOT present in both sets.
#Keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
#we can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)
# The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

#2.Python frozenset:frozenset is an immutable version of a set.
'''Like sets, it contains unique, unordered, unchangeable elements.
Unlike sets, elements cannot be added or removed from a frozenset.'''
#Creating a frozenset:Use the frozenset() constructor to create a frozenset from any iterable.
x=frozenset({'apple','banana','cherry'})
print(x)
print(type(x))
'''
Frozenset Methods:
Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.'''
#copy() :Returns a shallow copy
fs=frozenset({1,2,3})
cp=fs.copy()
print(fs)
print(cp)

#difference():	'-'	Returns a new frozenset with the difference
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.difference(b))
print(a - b)

#ntersection():	'&'	Returns a new frozenset with the intersection
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b))
print(a & b)

#isdisjoint():Returns whether two frozensets have an intersection
a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))

#issubset():'<=' / '<'	Returns True if this frozenset is a (proper) subset of another
a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)

#ssuperset():'>=' / '>'	Returns True if this frozenset is a (proper) superset of another
a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))
print(a >= b)
print(a > b)

#symmetric_difference():'^'	Returns a new frozenset with the symmetric differences	
a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.symmetric_difference(b))
print(a ^ b)

#union():'|'	Returns a new frozenset containing the union	
a = frozenset({1, 2})
b = frozenset({2, 3})
print(a.union(b))
print(a | b)

                    # Day-13 Learning 📅
                    # Starting Time: 1:20 am 🕐
                    # Ending Time: : am 🕐
'''
1.Puthon Dictionaries✅
2.Access in dictionarie✅
'''    
#Dictionaries are used to store data values in key:value pairs.A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict={
    "brand": "ford",
    "model":"mustang",
    'year' :1964
}  
print(thisdict)

#Dictionary items are ordered, changeable, and do not allow duplicates.Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
thisdict={
    'brand':'ford',
    'model':'mustag',
    'year': 1964
}
print(thisdict['brand'])    

#When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
#Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

#Changeable:Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#Duplicates Not Allowed:Dictionaries cannot have two items with the same key.
#Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Dictionary Length:To determine how many items a dictionary has, use the len() function:
#Print the number of items in the dictionary:
print(len(thisdict))

#Dictionary Items - Data Types.The values in dictionary items can be of any data type:
#String, int, boolean, and list data types:
thisdict={
    'brand':'ford',
    'electric':False,
    'year': 1964,
    'colors':['red','wehite','blue']
}
#From Python's perspective, dictionaries are defined as objects with the data type 'dict':
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#The dict() Constructor:It is also possible to use the dict() constructor to make a dictionary.
thisdict=dict(name='john',age=36,country='norway')
print(thisdict)

                    # Day-14 Learning 📅
                    # Starting Time: 1:20 am 🕐
                    # Ending Time: : am 🕐
#Access Dictionary✅
#Accessing items:we can access the items of a dictionary by referring to its key name, inside square brackets
thisdict={
    'brand':'Foard',
    'model':'Mustang',
    'year': 1964
}
x=thisdict['model']
print(x)
#There is also a method called get() that will give the same result:
x=thisdict.get('year')
print(x)

#Get keys:The keys() method will return a list of all the keys in the dictionary.
x=thisdict.keys()
print(x)
#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#Get Values:The values() method will return a list of all the values in the dictionary.
x=car.values()
print(x)
#Make a change in the original dictionary, and see that the values list gets updated as well:
car={
    'brand':'foard',
    'model':'mustang',
    'year':'1964'
}
x=car.values()
print(x) #before the change
car['year']=2010
print(x) #after the change
#Add a new item to the original dictionary, and see that the values list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

#Get Items:The items() method will return each item in a dictionary, as tuples in a list.
x=car.items()
print(x)
#The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
#Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

#Check if Key Exists:o determine if a specified key is present in a dictionary use the in keyword:
thisdict={
    'brand':'Foard',
    'model':'Mustang',
    'year':1964
}
if 'model' in thisdict:
    print('yes')


                    # Day-15 Learning 📅
                    # Starting Time: 1:20 am 🕐
                    # Ending Time: : am 🕐
'''
1.Change Dictionary Items.✅
2.Add Dictionary Items✅
'''
#1.Change Values:we can change the value of a specific item by referring to its key name:
thisdict={
    'brand':'Foard',
    'model':'Mustang',
    'year':1964
}
thisdict['year']=2018

#Update Dictionary:The update() method will update the dictionary with the items from the given argument.The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict={
    'brand':'Foard',
    'model':'Mustang',
    'year':1964
}
thisdict.update({'brand':'Ferari',
               'model':'F40'  })
print(thisdict)

#2.Add Dictionary Items.
#Adding Items:Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict={
    'brand':'Foard',
    'model':'Mustang',
    'year':1964
}
thisdict['color']='red'
print(thisdict)

#Update Dictionary:The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
#The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict={
    'brand':'Foard',
    'model':'Mustang',
    'year':1964
}
thisdict.update({'color':'read'})

                    # Day-16 Learning 📅
                    # Starting Time: 1:20 am 🕐
                    # Ending Time: : am 🕐
'''
1.Removing Items
2.Loop Through a Dictionary
'''
#Removing Items
#The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
thisdict={
    'brand': 'Ford',
    'model':'Mustang',
    'year':1964
}
del thisdict['model']
print(thisdict) #this will casuse an error because 'thisdict' no longer exists.

#The clear() method empties the dictionary:
thisdict={
    'brand':'Ford',
    'model':'Mustang',
    'year':1964
}
thisdict.clear()
print(thisdict)

#2.Loop Through a Dictionary:You can loop through a dictionary by using a for loop.When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
#Print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)

#Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])
    
#we can also use the values() method to return values of a dictionary:
for x in thisdict.values():
    print(x)

#we can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
    print(x)

#Loop through both keys and values, by using the items() method:
for x,y in thisdict.items():
    print(x,y)
              
              
                    # Day-17 Learning 📅
                    # Starting Time:5:30 pm 🕐
                    # Ending Time: : m 🕐
'''
1.Copy Dictionaries.
2.Nested Dictionaries.
3.Dictionary Methods.
'''
#1.Copy Dictionaries:
#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

#There are ways to make a copy, one way is to use the built-in Dictionary method copy().
thisdict={
    'brand':'Ford',
    'model':'Mudtang',
    'year':1964
}
mydict=thisdict.copy()
print(mydict)

#Another way to make a copy is to use the built-in function dict().
thisdict={
    'brand':'Fosrd',
    'model':'Mustang',
    'year':1964
}
mydict=dict(thisdict)
print(mydict)

#2.Nested Dictionaries:A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily={
    'child1':{
        'name':'emil',
        'year':2004
    },
    'child2':{
        'name':'Tobias',
        'year':2007
    },
    'child3':{
        'name':'Linud',
        'year':2011
    }
}
print(myfamily)

#Or, if we want to add three dictionaries into a new dictionary:
child1={
    'name':'Emil',
    'year':2004
}
child2={
    'name':'Tobaias',
    'year':2007
}
child3={
    'name':'Linus',
    'year':2011
}

myfamily={
    'child1':child1,
    'child2':child2,
    'child3':child3
}

#Access Items in Nested Dictionaries:To access items from a nested dictionary, we use the name of the dictionaries, starting with the outer dictionary.
print(myfamily['child2']['name'])

#Loop Through Nested Dictionaries:we can loop through a dictionary by using the items() method like this:
#Loop through the keys and values of all nested dictionaries:
for x,obj in myfamily.items():
    print(x)
    for y in obj:
        print(y+':',obj[y])

#fromkeys() Method:The fromkeys() method returns a dictionary with the specified keys and the specified value.
#Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#setdefault() method:The setdefault() method returns the value of the item with the specified key.If the key does not exist, insert the key, with the specified value, see example below
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "white")
print(x)

                    # Day-18 Learning 📅
                    # Starting Time: 12:30 pm 🕐
                    # Ending Time: : m 🕐

#Python Match(Switch):The match statement is used to perform different actions based on different conditions.Instead of writing many if..else statements, you can use the match statement.
#The 'match' statement selects one of many code blocks to be executed.
'''
Syntax:

match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block

'''
day=4
match day:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Satturday')
    case 7:
        print('Sunday')

usergrade='B-'
match usergrade:
    case 'A':
        print('Excellent')
    case 'A-':
        print('Great')
    case 'B':
        print('Good')
    case 'B-':
        print('Not bad')
    case 'D':
        print('Bad')
    
#Default Value:Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
#The value _ will always match, so it is important to place it as the last case to make it behave as a default case.
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

#Combine Values:Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
day=4
match day:
    case 1|2|3|4|5:
        print('Today is a weekday')
    case 6|7:
        print('I love weekends')

#If Statements as Guards:You can add if statements in the case evaluation as an extra condition-check.
month=5
day=3
match day:
    case 1|2|3|4|5 if month==4:
        print('A weekday in April')
    case 1|2|3|4|5 if month==5:
        print('A weekday in May')
    case _:
        print('No match')
    
                    # Day-19 Learning 📅
                    # Starting Time: 2:00 pm 🕐
                    # Ending Time: : m 🕐
'''
Python Functions:A function is a block of code which only runs when it is called.A function can return data as a result.A function helps avoiding code repetition.
'''
#Creating a Function:In Python, a function is defined using the def keyword, followed by a function name and parentheses:
def my_function():
    print('Hello from a function')
#This creates a function named my_function that prints "Hello from a function" when called.The code inside the function must be indented. Python uses indentation to define code blocks.

#Calling a Function:To call a function, write its name followed by parentheses:
def my_function():
    print('Hello from a function')

my_function()
'''
Function Names
Function names follow the same rules as variable names in Python:
A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)

Valid function names:
calculate_sum()
_private_function()
myFunction2()
'''
def farenheit_to_celsius(farenheit):
    return (farenheit - 32)* 5/9

print(farenheit_to_celsius(77))
print(farenheit_to_celsius(95))

#Return Values:Functions can send data back to the code that called them using the return statement.When a function reaches a return statement, it stops executing and sends the result back:
def get_greeting():
    return "hello from a function"

message=get_greeting()
print(message)
#If a function doesn't have a return statement, it returns None by default.

#The pass Statement:Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
def my_function():
    pass
#The pass statement is often used when developing, allowing you to define the structure first and implement details later.

                    # Day-20 Learning 📅
                    # Starting Time: 10:30 pm 🕐
                    # Ending Time: : m 🕐
#Function Arguments:Information can be passed into functions as arguments.Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
             #The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

def my_function(fname):
    print(fname + 'Refsenes')

my_function('Email')
my_function('Tobais')
my_function('Linus')

#Parameters vs Arguments:From a function's perspective -A parameter is the variable listed inside the parentheses in the function definition.An argument is the actual value that is sent to the function when it is called.
def my_function(name): # name id the parameter
    print('Hello', name)

my_function('Email') #'Email' is an argument

#Number of Arguments:By default, a function must be called with the correct number of arguments.If your function expects 2 arguments, you must call it with exactly 2 arguments.
def my_function(fname,lname):
    print(fname+'',lname)

my_function('Email','Refsnes')

#Default Parameter Values:You can assign default values to parameters. If the function is called without an argument, it uses the default value:
def my_function(name='friend'):
    print('Hello',name)
my_function('email')
my_function('tobais')
my_function()
my_function('linus')

#Keyword Arguments:we can send arguments with the key = value syntax.This way, with keyword arguments, the order of the arguments does not matter.
def my_function(animal,name):
    print('I have a',animal)
    print('My',animal+"'s name is", name)
my_function(animal='dog',name='Buddy')
#The phrase Keyword Arguments is often shortened to kwargs in Python documentation.

#Positional Arguments:When we call a function with arguments without using keywords, they are called positional arguments.Positional arguments must be in the correct order:
def my_function(animal, name):
    print('I have a',animal)
    print("My",animal+"'s name is",name)

my_function('dog','Buddy')

#Mixing Positional and Keyword Arguments: we can mix positional and keyword arguments in a function call.However, positional arguments must come before keyword arguments:
def my_function(animal, name, age):
    print("I have a",age, "year old", animal, "named",name)

my_function("dog",name="Buddy",age=5)

#Passing Different Data Types:You can send any data type as an argument to a function (string, number, list, dictionary, etc.).

def my_function(fruits):
    for x in fruits:
        print(x)

my_fruits=['apple','banana','cherry']
my_function(my_fruits)

#Sending a dictionary as an argument:
def my_function(person):
    print("Name:",person['name'])
    print("Age:",person['age'])

my_person={
    'name':'Emil',
    'age':25
}
my_function(my_person)

#Return Values:Functions can return values using the return statement:
def my_function(x,y):
    return x+y
result= my_function(5,3)
print(result)

#Returning Different Data Types:Functions can return any data type, including lists, tuples, dictionaries, and more.
#A function that returns a list.

def my_function():
    return ['aplle','banana','cherry']

fruits= my_function()
print(fruits[0])
print(fruits[1])

#A function that returns a tuple:
def my_function():
    return (10,20)
x,y= my_function()
print("x:",x)
print("y:",y)

#Positional-Only Arguments: we can specify that a function can have ONLY positional arguments.To specify positional-only arguments, add ( , / ) after the arguments:
def my_function(name, /):
    print("Hello",name)
    
my_function("Emil")

#Without the , / we are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(name):
    print("Hello",name)

my_function(name="Emil")

'''
With (, /) we will get an error if you try to use keyword arguments:

Example
def my_function(name, /):
  print("Hello", name)

my_function(name = "Emil")
'''
#Keyword-Only Arguments:To specify that a function can have only keyword arguments, add (*,) before the arguments:
def my_function(*, name):
    print('Hello', name)
    
my_function(name = "Emil")

#Combining Positional-Only and Keyword-Only: we can combine both argument types in the same function.Arguments before / are positional-only, and arguments after * are keyword-only:

def my_function(a,b,/,*,c,d):
    return a+b+c+d
result=my_function(5,10,c=15,d=20)
print(result)

