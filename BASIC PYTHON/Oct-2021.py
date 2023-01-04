# Python Training
# Etisalat


#a=5 #comment for this line


'''
Python Training
Technology Academy
Mohammed Marwan

'''
"""
Python Training
Technology Academy
Mohammed Marwan

"""

"""
Python Training
Technology Academy
Mohammed Marwan

"""
# print()
'''
print("Etisalat") # display a value 
print(2021)


# all functions need to be in lowercase
print("-------------")  

print("mohammed")
print("marwan")

print("-------------")

print("mohammed\nmarwan")

print("mohammed\tmarwan")
'''

'''
a=10
print(a)
a="M"
print(a)

'''
'''

a=10
b=20
c=30

print(a,b,c)
'''
'''
a,b,c=10,20,30

print(a,b,c)

a=10
b=10
c=10

a,b,c=10,20,30 # !!!!!!
a=b=c=10

print(a,b,c)

'''
# Data types
'''
# string
a="Technology Academy"
print(a,",Data type:",type(a))

'''
'''
print(10)
print("m")
print(10,20,30)
print(a,b,c)
print(type())
'''
'''

# int
a=10
print(a,",Data type:",type(a))

# float
a=10.5
print(a,",Data type:",type(a))

#boolean
a=True
print(a,",Data type:",type(a))

#list
a=["etisalat",2021,True,5.5,["ali",2020]]
print(a,",Data type:",type(a))

#tuple
a=("etisalat",2021,True,5.5,["ali",2020])
print(a,",Data type:",type(a))

#dic
a={"name":"mohammed","status":True}

a={"temp":30,
   "Hum":70,
   "power":True}

print(a,",Data type:",type(a))

#set
a={"marwan",2020,"marwan"}
print(a,",Data type:",type(a))
print(a)
'''

# string 

#slicing !!!!!!!!!!!!!!!!!!!!!!!

a=      "technology Academy"
#index   01234567 ..... +ve
'''
print(a)

# var[index] >> single char slicing
print(a[0]) # >>t

# var[statring index : ending index +1] >> multiple slicing
print(a[2:5]) # >> chn
print(a[-1]) # >> y

# Extract "technology" using +ve index
print(a[ 0 :10 ])#>>technology
print(a[:10 ]) # >> technology
print(a[:]) #>> technology Academy

# Extract "Academy" using -ve index

print(a[-7: ]) # >> Academy
print(a[-7: 18]) # >> Academy
print(a[::2]) 
print(a[0:10:2])
'''

# string functions
'''
a="technology Academy"
# string is imutable
print(len(a))
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.count("o"))
print("a.find("o"))
#print("a.find("ogy Academy"))
print(a.replace("technology","Etisalat"))
print(a.split(" "))
#print(a.index("o"))
print(a)
'''

# list

'''
a=[True,"Etisalat",2020,5.5,["ali",2021]]
print(a)

print(a[0])
print(a[1])
print(a[0:2])
print(a[-1])
print(a[:3])
print(a[:])
print(a[::2])
print(a[::3])

print(a[4]) # ['ali', 2021]
print(a[4][0]) #ali
print(a[4][1]) #2021
# l
print(a[4][0][1])
'''
'''
b=a[4][1]
b=str(b)
print(b[0])

a="2021"
b=int(a)
print(type(b))
'''
'''
#list functions : list is mutable
a=[True,"Etisalat",2020,5.5,["ali",2021]]


# change item values 
a[0]=False
print(a)

# add new single item to a list
a.append("Expo")
print(a)

# add a nested list
a.append(["Expo",2021])
print(a)

# add multiple items into a list
a.extend([[1,2,3]])
print(a)
#print("------------")

# insert will add new item in a certain index of a list
a.insert(1,"marwan")
print(a)

# it will count the freq. of a certain item in a list
print(a.count(2020))

# delete an item in a list
del a[3]
print(a)

# it will count the number of items inside a list
print(len(a))

# delete multiple items in a list 
del a[3:5]
print(a)

# delete all items inside a list
a.clear()
print(a)

# delete the list itself
del a
print(a)
'''
'''
# tuples 
a=(True,"Etisalat",2020,2020,5.5,["ali",2021])


# slicing
print(a[1:3])

#tuple functions
# a[0]="Etisalat" >> error

print(a.count(2020))
print(a.index("Etisalat"))

del a[5][1]
a[5].clear()

print(a)

#list() function to convert tuple to list
b=list(a)
print(b)

#tuple() function to convert list to tuple
'''

# dic/json
'''
a={"hum":70,"power":True,"temp":30}
print(a)

# the index for the dic is the (key)
print(a["temp"])


# change the existing items inside a dic
a["power"]=False
print(a)


# add new single item into a dic
a["GPS"]="1234234:762345"
print(a)


print("------------")
# add new multiple items into a dic
a.update({"device ID":123  , "region": "DXB"})
print(a)
print(a.keys())
print(a.values())


# delete item in a dic
#del a["device ID"]
#print(a)

# delete all items inside a deic
#a.clear()
#print(a)


# delete the dic itself
#del a
#print(a)

'''
#HW1
'''
a=[1, "hello", [1,2,3 ] , True]
print(a[1])
print(a[1:])


A=[1,'a']
B=[2,1,'d']
c=A+B
print(c)

#--------------------
# HW2

album_sales_dict={'Back in Black':50,
   'The Bodyguard':50,
   'Thriller':64}

print(album_sales_dict["Thriller"])
print(album_sales_dict.keys())
print(album_sales_dict.values())
'''
#arthmatic operators
'''
print(10%2)
print(9%2)
print(2**3)
print(9//2)

a="Mohammed "
b="Marwan"

print(a+b)
#print(a/b)
#print(a*b)
#print(a-b)


c=10
print(a*c)
'''
# logical operators
'''
a=True
b=False

print(a and b)
print(a or b)
print( not a )


#relaational operators

a=10
print(a)
print(a==10)

'''

# EX !!!!!!!!!!!!
'''
fn="mohammed"
ln="marwan"

print("Hi there,", fn , ln)
print("Hi there,"+ " "+fn +" "+ ln)
print("Hi there, %s %s " %(fn,ln)) #FYI
'''
'''
fn= input("Enter your first name:")
ln= input("Enter your last name:")

print("Hi there,", fn , ln)
print("Hi there,"+ " "+fn +" "+ ln)
print("Hi there, %s %s " %(fn,ln)) #FYI

'''

# if statement

# if
'''
x=-7 # i want to confirm x value is +ve

if x>0:
    print(x,"is a +ve number")

print("code")
'''

# if , else 
'''
x=-7 # i want to confirm x value is +ve or -ve

if x>0:
    print(x,"is a +ve number")
    
else:
    print(x,"is a -ve number")


print("code")
'''
# if ,elif, else
'''
x=7 # i want to confirm x value is +ve or -ve

if x>0:
    print(x,"is a +ve number")

elif x==0:
    print(x,"is zero")
    
else:
    print(x,"is a -ve number")


print("code")
'''

# if , and 

'''
x=17 # i want to perform action if x value between 5 to 10

if x>=5 and x<=10:
    print(x,"between 5 and 10")

print("code")
'''

#if , or
'''
x=17

if x>=10 or x<=5:
    print("True")

else:
    print("False")

print("code")
'''

# if , not
'''
a="mohammed"

if a!="mohammed":
    print("not equal")
else:
    print("equal")
'''

# if , in
'''
a=["mohammed","ali","ahmad","mostafa"]

# obj: confirm if "mohammed" value is part of the lsit


# task: try to solve the issue of using upper case
# task2: get the value from the user

x=input("Enter your value: ")
z=x.lower()

if z in a:
    print("Available")
else:
    print("Not Available")
'''

# Nested if 

#experience= input("Enter your experience")
#exp=int(experience)



# obj: create a code to select applicants based on
# their experience and education,
# min_exp>=15, min_education=PhD

# task1: Get the values for exp and edu
# from a users ---> input()

# task2:make the code smarter 

'''
if exp >=15:
    education= input("Enter your education level")
    
    if education =="PhD":
        print("Eligible")
    else:
        print("PhD required")
else:
    print("mini experience required is 15 years")

'''

#ex1
'''
day="friday"

if day=="tuesday" or day=="monday":

    print("today is sunny")

else:
    print("today it will rain")



day="friday"

if day in ["tuesday", "monday"]:

    print("today is sunny")

else:
    print("today it will rain")

'''
#ex2
'''
a=20
b=20

if a>b:
    print(a,"is the greatest")

elif a==b:
    print("equal")
else:
    print(b,"is the greatest")

'''
#ex3
'''
a=15

if a%2==0:
    print(a,"is even number")

else:
    print(a,"is odd number")

'''

#Ex4.
'''
a=30

if a>80:
    print("Grade A")
elif a>60:
    print("Grade B")
elif a>40:
    print("Grade C")
else:
    print("Grade D")

'''
#Ex5
'''
a=10
b=20
c=30

if a>b and a>c:
    print(a, " is the greatest")
elif b>a and b>c:
    print(b, " is the greatest")
elif c>a and c>b:
    print(c, " is the greatest")    

'''

# loops
'''
print(range(1,10))
print(list(range(1,10)))
print(list(range(10)))
print(list(range(5,10)))
print(list(range(1,15,2)))
print("-------------")
# for loop
# loop to run for 10 times

#for loop is not working with conditions 

for i in range(10):
    
    #print("OK1")
    print(i)

print("-------------")
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    
    #print("OK2")
    print(i)

print(list(range(10,20,2)))

# important note:
# loop will run based on number of items in range() or list
# i will take a different value from range () or list sequentialy

for i in range(10,20,2):
    
    #print("OK1")
    print(i)

'''

# loop with str
'''
for i in "Etisalat":
    print("OK")
    print(i)
'''
# loop with dic
'''
a={"name":"mohammed","status":True}

b=list(a.keys())

for i in b:
    print(i)
    print(a[i])
    print("OK")

'''
'''
#Ex1
a=[100,22,13,4,5,6]
# a=[1,1,1,1,1,1]

'''
'''
a[0]=1
a[1]=1
a[2]=1
a[3]=1
a[4]=1
a[5]=1
'''
'''
n=len(a)

for i in range(n):
    a[i]=1

print(a)
'''


#Ex2 loop with if statement 
'''
a=["mohammed","ahmad","hasan","abdullah","mohammed"]

# Obj: replace mohammed with ali

n=len(a)

for i in range(n):
    if a[i]=="mohammed":
        a[i]="ali"

print(a)
'''
# while loop
# in (while loop) we define the loop iteration using a condition

'''
a=10
b=0

while a>b:
    print("OK")

    #b=b+1
    b+=1

'''
#Ex1
a=[100,22,13,4,5,6]
# a=[1,1,1,1,1,1]


'''
a[0]=1
a[1]=1
a[2]=1
a[3]=1
a[4]=1
a[5]=1
'''
'''

c=0
b=len(a)

while b>c:
    a[c]=1

    c=c+1

print(a)
'''


#Ex2 loop with if statement 
'''
a=["mohammed","ahmad","hasan","abdullah","mohammed"]
# Obj: Replace "mohammed" with "ali"

n=len(a)
b=0

while n>b:
    if a[b]=="mohammed":
        a[b]="ali"

    b=b+1

print(a)
'''
# pass
'''
print("____pass_____")

for i in range(10):

    if i==5:
        pass

    print(i)

    
print("____Continue_____")

#continue

for i in range(10):

    if i==5:
        continue

    print(i)

#break
print("____break_____")

for i in range(10):

    if i==5:
        break

    print(i)


print("code")
'''

# functions 
'''
def hello():
    print("mohammed marwan")
    aa=5 #local var
    global aa
    
    return aa

x=hello()


print(x+5)


#a="m" ==> global variable
print(aa)

# use print() to get the value of the function return
'''

def hello():
    print("mohammed marwan")

    
#hello()

'''
def add(a):
    "int (a) value will ba added to 10"
    b=a+10
    return b

print(add(10))
'''

'''
def add(a,b):
    "int (a) value will ba added to 10"
    c=a+b
    return c

print(add(10,20))
'''
'''
def add(a,b):
    "int (a) value will ba added to 10"
    c=a+b
    #print(c)
    return c

var=add(10,20)
print(add(10,20))
'''
#final=add(10,20)+10
#print(final)

'''
def add(a=10,b=20):
    "int (a) value will ba added to 10"
    c=a+b
    #print(c)
    return c


print(add())
print(add(100,50))
#print(add(,100))
print(add(100,))
'''

'''
def add(a,b,c):

    return a,b

j,h=add(10,20,30)
print(j)
print(h)

'''
#create a class

class student:
    def __init__(self,a,b):
        self.name=a
        self.age=b


    def display(self):
        print("student name" , self.name, self.age)

        
# use a class

st1=student("mohammed",30)
st1.display()


st2=student("ali",300)
st2.display()

























