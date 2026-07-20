"""s = "AB1[+2@pq631$mn9!"

uppercase = ""
lowercase = ""
number = ""
specialchar = ""

i = 0
while i < len(s):
    char = s[i]
    if 'A' <= char <= 'Z':
        uppercase += char
    elif 'a' <= char <= 'z':
        lowercase += char
    elif '0' <= char <= '9':
        number += char
    else:
        specialchar += char

    i += 1

print(uppercase)
print(lowercase)
print(number)
print(specialchar)"""
    

"""n = 153
ch = str(n)

sum = 0
i = 0

while(i <= len(ch) - 1):
    char = int(ch[i])
    sum += char ** len(ch)
    i += 1

if(sum == n):
    print("armstrong")
else:
    print("not armstrong")"""

"""p=145
n = int(p)
sum=0
while(n>0):
    rem =  n%10
    i=0
    mul =1 
    while(i<=rem):
        mul = mul*i
        i+=1
    sum += mul
    n = n/10
if(sum == n):
    print("strong")
else:
    print("weak")"""

""""i = 1
j = 50

while i <= j:
    m = 1
    count = 0

    while m <= i:
        if i % m == 0:
            count += 1
        m += 1

    if count == 2:
        print(i)

    i += 1"""


"""a = "subbu"
for i in a:
    print(i)"""


"""n = int(input("Enter a number"))
sum=0
for i in range(n+1):
    sum+=i
print(sum)"""


"""a = [10,61,31,96,102,35]
for i in a:
    if(i%2==0):
        print(i)"""


"""a = "ab12@3sdk61!&5pq"

alphabets = 0
number = 0
special = 0

for i in a:
    if (i >= "A" and i <= "Z") or (i >= "a" and i <= "z"):
        alphabets += 1
    elif i >= "0" and i <= "9":
        number += 1
    else:
        special += 1

print(alphabets)
print(number)
print(special)"""

"""a = ["pen","appless","mango","banana"]
result = {}

for i in a:
    result[len(i)] = i

print(result)"""



"""value = int(input("Enter the number"))
count =0
for i in range(1,value+1):
    if(value % i == 0):
        count+=1
    
if(count ==2):
    print("prime")
else:
    print("not prime")"""

"""a = [10,45,65,72,91,306]
l=[]
count =0
for i in a:
    count+=1
    if(count %2 !=0):
        l.append(i)
print(l)"""


"""a=['raja5','rani6']
result = {}

for i in a:
    name = ""
    for j in i:
        if('1'<=j<='9'):
            result[name] = j
        else: 
            name+=j
    
print(result)"""

"""a = [24, 108, 364, 123, 32]
result = []

for i in a:
    sum = 0
    for j in str(i):
        sum += int(j)
    result.append(sum)
print(result) """      



"""a = int(input("Enter start number: "))
b = int(input("Enter end number: "))

for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if(i % j == 0):
            count += 1

    if(count == 2):
        print(i)"""
        

"""FUNCTIONS:"""
"""1 FUNCTION WITH ARGUMENTS AND RETURN VALUE"""


"""def add_num(a,b):
    sum = a+b
    return sum

print(add_num(10,20))
"""
"""2 FUNCTION WITH ARGUMENTS AND NO RETURN VALUE
def add_num(a,b):
    sum = a+b
    print(sum)

add_num(10,20)"""

"3 FUNCTION WITHOUT ARGUMENTS AND NO RETURN VALUE"
"""def add_two():
    n = int(input("enter number one"))
    m = int(input("enter other number"))
    sum = n+m
    print(sum)

add_two"""

"4 FUNCTION WITHOUT ARGUMENTS AND  RETURN VALUE"
"""def add_two():
    n = int(input("enter number one"))
    m = int(input("enter other number"))
    sum = n+m
    return sum

print(add_two)"""
"""while True:
    def lengthstring(a):
        s = len(a)
        return s

    print(lengthstring("subbu"))

    def add_two(n,m):
        
        sum = n+m
        return sum

    def sub_two(n,m):
    
        sum = n-m
        return sum


    def mul_two(n,m):
    
        sum = n*m
        return sum


    def div_two(n,m):
        sum = n/m
        return sum


    a = int(input("enter number one :"))
    b = int(input("enter other number :"))

    choice = int(input("1.add,2.sub,3.mul,4.div:"))
    if(choice == 1):
        print(f"sum of {a} and {b} is:-",add_two(a,b))
    elif(choice==2):
        print(f"sub of {a} and {b} ",sub_two(a,b))
    elif(choice==3):
        print(f"mul of {a} and {b} ",mul_two(a,b))
    elif(choice ==4):
        print(f"div of {a} and {b} ",div_two(a,b))
    elif(choice ==5):
        break+"""
"""arguments are the neccesary values to perform functions
1.positional argument
2.keyword argument
3.default argument
4.variable length argument


1. These are the arguments which takes the argument according to positions"""


"""def sample(a,b):
    for i in a:
        print(i)
    print(b)
sample("hello",10)"""

"""4.variable length arguments:
packing and unpacking
packing:-
packing multiple values into  a single variable is known as packing
def sample(*a):
    print(a)

sample(1,2)"""

"""
unpacking is used to unpack functions from collections and distribute among arguments
def sample(a,b,c):
    print(a)
    print(b)
    print(c)

sample(*[10,20,30])"""


"""def prabhas(a,b):
    sum = a+b
    
    def bhagya(x,y):
        sum = x+y
        return sum14
    return sum
print(prabhas(50,60))"""


"""
decorator is a function which is used to add some additional functionality to the function 
in decorator there are of 2 types

built in 
user defined decorators

built in:-These are the decorators which is developed by developers to doo some specific task

example:- @classmethod
@staticmethod
@properties


userdefined decorators:- these are the decorators which are created by users according to their requirments


syntax:-
def sample(func):
    def inner():
        pre_task
        func()
        post_task
    return inner
"""


"""def recharge():
    print("recharge successful")


def shop(func):
    print("checking amount is credited or not")
    print("amount credited")
    func()
    print("thank you for the recharge ")

shop(recharge)"""


"15-july"

"""global and local variable
global variable it can bee accesible every where inside the function or outside function or nested functio
anywhere
local variable can be accesible inside the function and nested function
non local variable cannot be accessed outside function
"""

"""a= 100
def sample():
    a=10
    print(a)
    def sample1():
        c=12
        print(a)    
    sample1()
    
sample()
print(a)"""

"""
global variable inside function
use a keyword called global :
a= 100
def sample():
    global a
    a=10
    print(a)
    def sample1():
        c=12
        print(a)    
    sample1()
    
sample()
print(a)"""


"""
modification of local variable by being inside nested function nonlocal inside function
use a keyword called nonlocal :"""
"""a= 100
def sample():  
    b=10 
    def sample1():
        nonlocal b
        b=900
        print(b)    
    sample1()
    print(b)
sample()
print()"""


"""def strong(n):
    temp = n
    total = 0
    while n > 0:
        rem = n % 10
        i = 1
        fact = 1
        while i <= rem:
            fact = fact * i
            i += 1
        total += fact
        n = n // 10
    if total == temp:
        print("Strong Number")
    else:
        print("Not a Strong Number")

strong(145)
strong(143)"""

"modification of global variable inside function"


"***key word arguments "
"""" it Is used to take key words arguments pair as input it will store the values in dictionary formats
def sample(**a):
    print(a)

sample(name = "subbu",age=21,phone = 3333333)
output:{'name': 'subbu', 'age': 21, 'phone': 3333333}
"""

"""def sample2(*a):
    print(a)
sample2(10,20,30,b=20)
this actually throw  an error soo we are using 
the keywords arguments on above """

"""example for both postional arguments and keyword arguments"""
"""def sample(*a,**b):
    print(a)
    print(b)

sample(10,20,40,name = "subbu" ,age = 21)
output format = (10, 20, 40)
{'name': 'subbu', 'age': 21}"""


without decorator function calling
def jiofamily(func):
    def inner():
        print("Checking amount credited or not")
        print("Amount credited successfully")
        func()                   
        print("Thank you for using Jio")
    return inner



def recharge1():
    print("Recharge of 149 is successful")
recharge1 = jiofamily(recharge1)


def recharge2():
    print("Recharge of 299 is successful")
recharge2 = jiofamily(recharge2)



def recharge3():
    print("Recharge of 549 is successful")
recharge3 = jiofamily(recharge3)


print("1. 149 plan")
print("2. 299 plan")
print("3. 549 plan")

choice = int(input("Enter the plan to select: "))

if choice == 1:
    recharge1()
elif choice == 2:
    recharge2()
elif choice == 3:
    recharge3()
else:
    print("Invalid Choice")"""

"""class and object creation

class subbu:
    ename  =  "subbu"
    age  =20
    father = "xxxx"
    mom = "yyyy"


sri = subbu()


print(sri.age)
"""

class car:

    wheels = 4
    fueltank = 1
    engine = 1
    steering = 1
    sidemirrors = 2
    headlights = 2

    def addval(self, key, value):
        self.__dict__[key] = value
       


tata = car()
bmw = car()

"""tata.speed = 150
bmw.speed = 250

tata.spoiler = 0
bmw.spoiler = 1

tata.horsepower = "5000hp"
bmw.horsepower = "9000hp"

tata.torque = 2000
bmw.torque = 3000
"""

n = int(input("Enter the no of changes: "))

for i in range(n):
    cls = input("Enter cls: ")
    key = input("Enter key: ")
    value = input("Enter value: ")

    if cls == "tata":
        tata.addval(key, value)

    elif cls == "bmw":
        bmw.addval(key, value)

    else:
        print("Invalid car")


print("tata = ",tata.__dict__)
print("bmw = ",bmw.__dict__)
