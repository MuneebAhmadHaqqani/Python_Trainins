# Python code
# Technology Academy
# Mohammed Marwan

''' 

Python
Technology Academy
Etisalat

''' 

"""
Python
Technology Academy
Etisalat
"""

'''
Python
Technology Academy
Etisalat
'''
'''
print("Etisalat")# print function --> show/display a value

print("python")# int  # str # variable , function
print   ( "python" ) 
print   ( 'python' ) 

print(2020)

print("technology")
print("academy")
print("---------------------")
print("technology\nacademy")# \n is a special char which can print new line
print("---------------------")
print("technology\tacademy")# \t is a special char which can print (tab space)
print("new line")

a="m"
print(a)
a=10
print(a)
'''
'''
a=1
print(a)

a=1
b=2
c=3
print(a ,b ,c )

a,b,c=1,2,3
print(a ,b ,c )

a=b=c=10
print(a,b,c)
'''
'''
# Data Types 
# String 
a="Technology Academy"
print("value:",a,",Data Type:",type(a))

# int 
a=2020
print("value:",a,",Data Type:",type(a))

#float
a=5.5
print("value:",a,",Data Type:",type(a))

# boolean
a=True
print("value:",a,",Data Type:",type(a))

# list
a=["Python",2020,6.6,True,["ali",20]]
print("value:",a,",Data Type:",type(a))

# tuple 
a=("Python",2020,6.6,True,["ali",20],"new")
print("value:",a,",Data Type:",type(a))

# dic/json
a={"name":"mohammed","Age":35}
print("value:",a,",Data Type:",type(a))

# set
a={"python",20,5.5,"python",5.5,"Ta","mohammed"}
print("value:",a,",Data Type:",type(a))
'''

#string - index/slicing

a="Technology Academy"
#  0123456789   +ve index 
#  -ve index        -1
'''
print(a[2])# c --> single char
print(a[11])# A --> single char
print(a[2:4]) #ch
#  a[starting index : ending index+1]
# Technology
print(a[0:10])
#Aca
print(a[11:14])
print(a[:11])
print(a[11:])
print(a[:])
print(a[::2])
print(a[::3])
print(a[0:10:3])
print(a[-1])
print(a[-6:-3]) # cad
# Academy --> -ve index 
print(a[-7:])
# dem --> +ve and -ve index
print(a[-4:17])
#print(a[-7::-1])
'''
# string functions
'''
a="Technology Technology Academy Technology"
# string is imutable

print(a.upper())#converting all the string char into an upper case
print(a.lower())# converting all string into lower case
print(a.capitalize())# converting only the first char into upper case rest into lower case
print(a.replace("Technology","Etisalat",1))
#help(a.replace)
print(a.count("Technology"))# return the total count of an argument
print(a.index("Academy"))# return index of an argument
print(a.split(" "))#return list of strings item
print(len(a))# return number of char in a string
print("----")
print(a.find("cad"))

print(a)
'''
       
# list - index/slicing
'''
a="Technology"
#012345678
#  a[starting index : ending index+1]

a=["Python",2020,6.6,True,["ali",20]]
#    0        1   2   3        4
print(a[1])
print(a[0:2])   #["Python",2020]
print(a[:3])
#["ali",20]
print(a[4])
print(a[-1])
# ali
print(a[4][0])
# "l"
print(a[4][0][1])
# 20
print(a[4][1])
# 2
#print(a[4][1][0]) --> error !! you can not slice int value
'''
'''
# list functions 
a=["Python",2020,6.6,True,["ali",20]]
# lists are mutable

a.append(2021)# adding new single item
print(a)

a.append("mohammed")
print(a)

a.append(["Covid-19","Delta"])# adding nested list
print(a)

# add multiple items to a list
a.extend(["new1",2020])
print(a)

print(a.count(2020))

a.insert(2,2021)# add item to a list in a particular place
print(a)

print(len(a))# returning num of items in a list

print("---------")
del a[0]
print(a)

# changing the item value
a[2]=12
print(a)

a.clear()# removing all items from a list
print(a)

del a # delete the list itself
print(a)
'''

# tuple
#a=("Python",2020,6.6,True,["ali",20],6.6)
#print(a)

#print(a[0])

#print(a.index(True))
#print(a.count(6.6))

#supporting functions:
#print(list(("Python",2020,6.6,True,["ali",20],6.6)))
#print(set(("Python",2020,6.6,True,("ali",20),6.6)))
#print(type(str(1234)))
#print(type(int("2020")))

'''
a=["Python",2020,6.6,True,("ali",20),6.6]
b=("Python",2020,6.6,True,["ali",20],6.6)
# you can change the nested list inside a tuple
b[4][0]="mohammed"
print(b)
'''
# you can not change the nested tuple inside a list
#a[4][0]="mohammed"
#print(a)

# dic/json

a={"name":"mohammed","Age":35}
#print(a)

#ATM application
a={"co1":["mohammed",1000000],"co2":["ahmad",50000]}

# slicing for Dic:

#print(a["name"])
#print(a["Age"])
#print(a["co2"][1])

# changing item value:

#a["key"] = new value
#a["co1"]="error"
#print(a)

#a["co1"][0] ="Ali"
#print(a)

#dic functions:
'''
# add new item to a Dic
a.update({"co3":["Omar",5000000],"co4":["Sultan",500000]})
print(a)

# returning all values in a list
print(a.values())

# returning all keys in a list
print(a.keys())

# delete a certain item in a dic
#del a["co1"]
#print(a)

del a["co1"][0]
print(a)
print(len(a))


# delete all items in a dic
a.clear()
print(a)

#delete the dic itself from the memory
del a
print(a)
'''


# HW
'''
a_list= [1, "hello", [1,2,3 ] , True]

#Find the value stored at index 1 of 'a_list'.
print(a_list[1])
#Retrieve the elements stored at index 1,2, and 3 of 'a_list'.
print(a_list[1:])

#Concatenate the following lists A=[1,'a'] abd B=[2,1,'d']:
A=[1,'a']
B=[2,1,'d']


c=A+B
print(c)
'''
'''

a={"a1":50,"a2":50,"a3":65}
print(a)
print(a["a3"])
print(a.keys())
print(a.values())
'''

'''

album_sales_dict={'Back in Black':50, 'The Bodyguard':50,'Thriller':65}
print(album_sales_dict)
#Use the dictionary to find the total sales of "Thriller":
print(album_sales_dict['Thriller'])
#Find the names of the albums from the dictionary using the method "keys":
print(album_sales_dict.keys())
#Find the names of the recording sales from the dictionary using the method "values":
print(album_sales_dict.values())
'''
'''
a= {
    "update_id":646911460,
    "message":{
        "message_id":93,
        "from":{
            "id":"10000xxxx",
            "is_bot":False,
            "first_name":"Marwan",
            "username":"jiayu",
            "language_code":"en-US"
        },
        "chat":{
            "id":"10000xxxx",
            "first_name":"Jiayu",
            "username":"jiayu",
            "type":"private"
        },
        "date":1509641174,
        "text":"eevee"
    }
}

#646911460
print(a["update_id"])

#93
print(a["message"]['message_id'])

# Marwan
print (a["message"]["from"]["first_name"])

print(a["message"].keys())

'''

# Operators

'''
print(10%2)
print(9%2)
print(2**3)
print(9//2)
print(9/2)
'''
'''
a="m"
b="x"

print(a+b)
print(a*5)
#print(a*b)# not possible
#print(a/b)# not possible
#print(a-b)# not possible
'''
'''
a=True
b=False

print(a and b)
print(a or b)
print( not a)

a=1

print(a==10)
'''
# the output of relational and logic operator are True and false

# thats why we use it in conditional statement (if) and for loops

'''
a="Technology"

print("z" not in a)# T or F

'''
'''
Fname="Mohammed"
Lname="Shahin"
'''
'''
# note: input() function will always return a (str)
Fname=input("Enter your first name: ")
Lname=input("Enter your last name: ")

print("Hello there,",Fname,Lname)
print("Hello there, "+Fname+" "+Lname)
print("Hello there, %s %s"%(Fname,Lname))# FYI
'''


# if statement



#using if
'''
# check if x value is greater than 0
x=7
if x>0:
    print("yes")

print("the end")
'''
# if , else
'''
x=7
if x>0:
    print("yes")
else:
    print("no")
    

print("the end")
'''
# if , elif ,else
'''
x=6

# check if x is greater than 5 or less than 10

if x>7:
    print("Greater than 7")
elif x<5:
    print("less than 5")
else:
    pass

print("rest of code")
'''
# you can use if statement with the following operators:
# relational operator: > < >= <= == !=
# membership operator: in , not in
# identity operator: is ,  is not 
# logical operator: and or not 

# (if) with (and)
# check if x is greater than 5 and less than 10

HR= 200
'''
if HR>80 and HR<110:
    print("normal")
else:
    print("check with doctor")
'''
'''
#(if) with (or)
if HR>80 or HR<110:
    print("normal")
else:
    print("check with doctor")
'''

#(if) with (in)
'''
a=["mohammed","ali","sultan","ahmad"]

# enable the user to input the value 
# check if the user will insert the name in a upper case
user=input("Enter your name: ")
user=user.lower()

if user in a:
    print("you are eligible")
else:
    print("you are not eligible")

'''
# example for (nested if)
'''
experience = input("Enter your exp")
experience=int(experience)

if experience >=15:
    education = input("Enter your education")
    
    if education == "PhD":
        print("you are Eligible!!")
    else:
        print("PhD Required")
        
else:
    print("mini 15 years of experience required")
'''
'''
# Ex1.

day="Friday"

if day=="monday" or day=="Tuesday":
    print("Today is sunny")
else:
    print("today it will rain")'''

#Find the greatest number among two
'''
a=10
b=20

if a>b:
    print(a, "a is the greatest")
else:
    print(b, " b is the greatest")
'''
#Check whether a number is even or odd
'''
a=7

if a%2==0:
    print(a,"is even")
else:
    print(a,"is odd")
'''
#.    Find the grade of a student
'''
mark=70

if mark>80:
    print(" A - Grade")
elif mark>60:
    print(" B - Grade")
elif mark>40:
    print(" C - Grade")
else:
    print(" D - Grade")
        

print("the end")
'''
#loops
'''
print(list(range(10)))

print(list(range(5,10)))

print(list(range(5,20,2)))
'''
# for loop
'''
for i in range(10):
    print("OK")
'''
'''
print(list(range(15,20)))

for i in range(15,20):
    print("OK")
    print(i)
'''
'''
for i in ["mohammed","ali","sultan","majed"]:
    print("OK")
    print(i)
    
'''
'''
for i in "mohammed":
    print("OK")
    print(i)

'''
'''
#Ex1.
a=[10,20,30,40,50]
#a=[1,1,1,1,1]

# manualy
'''
'''
a[0]=1
a[1]=1
a[2]=1
a[3]=1
a[4]=1
'''
'''

n=len(a)# n=5

for i in range(n):
    a[i]=1
    
print(a)
'''

# for loop with (if)
'''
a=["ahmad","sultan","majed","ahmad"]
print(a)
#a=["mohammed","sultan","majed","mohammed"]


n=len(a)# n=4

for i in range(n):
    if a[i]=="ahmad":
        a[i]="mohammed"

print(a)
'''

#while loop
'''
a=5
b=0

while a>b:
    print("OK")

    b=b+1
    #b+=1
'''
'''
a=[10,20,30,40,50]
#a=[1,1,1,1,1]

n=len(a) # n=5
b=0

while n>b:
    a[b]=1

    b=b+1

print(a)
'''
# normal loop
'''
for i in range(10):
    print("i")    
'''
# loop with pass
'''
for i in range(10):

    if i==5:
        pass # nothing
    
    print("i")
'''
# loop with continue
'''
for i in range(10):

    if i==5:
        continue # nothing
    
    print(i)
'''
# loop with break
'''
for i in range(10):

    if i==5:
        break # nothing
    
    print(i)


print("code")

'''

'''
while True:
    n= input("select an option:")
    if n=="exit":
        break # nothing

'''
# functions

'''
print()
len()
type()
a.upper()
a.lower()
....


print()# --> display a value 
'''
# functions
'''
def add (a=10,b=0):
    "enter a number , result will be a+b+1"
    z=input("enter your name")
    c=a+b+1# local variable
    global c
    d=a*b+1
    return c,d,z

print(add(b=50))

#a="123" # global variable
print(c)
'''
# class 
'''
# funstions works with all data types 
print()
len()
type()

# below functions work with specifc data type
a.append()
a.clear()
a.find()
a.upper()
'''
# class = data type

'''
you don't need to create a class,
but you need to use a class

that's why you need to understand the class
:)

'''
# Class way 1
'''
class student:
    name=""
    age=0

    def display(self):
        print("student name:",self.name,",Age:",self.age)


a=student()
a.age=25
a.name="mohammed"
a.display()


a2=student()
a2.name="ahmad"
a2.age=30
a2.display()

'''
# Class way 2
'''
class student:
    def __init__(self,a,b):
        self.name=a
        self.age=b

    def display(self):
        print("student name:",self.name,",Age:",self.age)


a=student("mohammed",25)
a.display()

a2=student("ahmed",30)
a2.display()

'''
