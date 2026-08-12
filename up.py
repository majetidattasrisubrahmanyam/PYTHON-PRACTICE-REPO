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



"""class Bank:
    bank_name = "Union Bank"
    bank_location = "KPHB"
    ifsc_code = "1234"
    manager = "Arjun"
    roi = "6.26%"


def add_data(self, key, val):
    self.__dict__[key] = val


def printv(obj):
    print("\nObject Data:")
    print(obj.__dict__)

    print("\nClass Data:")
    print(Bank.__dict__)


subbu = Bank()


print("1. Add Data")
print("2. Modify Data")
print("3. Display Data")

s = int(input("Enter the option: "))

if s == 1:
    changes = int(input("Enter number of changes: "))
    for i in range(changes):
        key = input("Enter key: ")
        value = input("Enter value: ")
        add_data(subbu, key, value)
        printv(subbu)

elif s == 2:
    key = input("Enter key value: ")
    value = input("Enter new value: ")
    add_data(subbu, key, value)
    printv(subbu)

elif s == 3:
    printv(subbu)

else:
    print("Invalid option")
"""



data = {
    "name": "Subbu",
    "age": 20,
    "city": "Hyderabad"
}

class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

obj = Student(**data)

print(obj.__dict__)


##CONSTRUCTER METHOD
"""class student:
    ins = "spider"
    loc = "jntu"

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(self.name)
        print(self.age)

subbu = student("subbu",20)"""

##static method

class student:
    ins = "pyspider"
    loc = "jntu"

    def __init__(self):
        self.name = self.get_name()
        self.age = self.get_age()

    @staticmethod
    def get_name():
        return input("Enter the name")
    
    @staticmethod
    def get_age():
        return int(input("Enter the age"))

    def display(self):
        print(self.name,self.age)


class A:
    a=10
    b=20
    def __init__(self,c,d):
        self.c = c
        self.d = d

    def display(self):
        print(self.c,self.d)


class B(A):
    a=90
    def __init__(self,c,d,e,f,g):
        super().__init__(c,d)
        self.e = e
        self.f=f
        self.g=g

    def display(self):
        super().display()
        print(self.e,self.f,self.g)

oa = B(10,2,3,4,5)
print(oa.display())


"""class A:
    a=10
    b=20
    def __init__(self,c,d):
        self.c = c
        self.d = d

    def display(self):
        print(self.c,self.d)


class B(A):
    a=90
    def __init__(self,c,d,e,f,g):
        super().__init__(c,d)
        self.e = e
        self.f=f
        self.g=g

    def display(self):
        super().display()
        print(self.e,self.f,self.g)

class C(B):
    def __init__(self,c,d,e,f,g,h,i):
        super().__init__(c,d,e,f,g)
        self.h = h
        self.i = i
    
    def display(self):
        super().display()
        print(self.h,self.i)

oa = C(10,2,3,4,5,0,100)
print(oa.display())"""

class Resume10th:
    def __init__(self, name, marks10):
        self.name = name
        self.age = 15
        self.marks10 = marks10

    def display(self):
        print(self.name, self.age, self.marks10)


class Resume12th(Resume10th):
    def __init__(self, name, marks10, marks12, phone):
        super().__init__(name, marks10)
        self.age = 17
        self.marks12 = marks12
        self.phone = phone

    def display(self):
        super().display()
        print(self.age, self.marks12, self.phone)


class ResumeEngineering(Resume12th):
    def __init__(self, name, marks10, marks12, phone, cgpa):
        super().__init__(name, marks10, marks12, phone)
        self.age = 21
        self.cgpa = cgpa

    def display(self):
        super().display()
        print(self.age, self.cgpa)



obj1 = Resume10th("Subrahmanyam", 600)
obj2 = Resume12th("Subrahmanyam", 600, 921, "918278XXX")
obj3 = ResumeEngineering("Subrahmanyam", 600, 921, "919978XXX", 8.5)

print("10th Resume")
obj1.display()

print("\n12th Resume")
obj2.display()

print("\nEngineering Resume")
obj3.display()



class ShoppingCart:
    products = {
        "iphone": 6,
        "imac": 3,
        "ipad": 2,
        "iwatch": 1
    }

    prices = {
        "iphone": 900,
        "imac": 500,
        "ipad": 300,
        "iwatch": 400
    }

    def __init__(self):
        self.cart = []

    def add_user(self):
        self.name = input("Enter your name")
        self.email = input("Enter your email")
        self.phoneno = input("Enter your number")

    def display(self):
        print(self.name)
        print(self.email)
        print(self.phoneno)

    def add_items(self, name, quantity):
        if name not in ShoppingCart.products:
            raise Exception(f"Cannot add product '{name}'")

        if quantity > ShoppingCart.products[name]:
            raise Exception("Quantity out of stock")

        item = {
            "name": name,
            "quantity": quantity,
            "price": ShoppingCart.prices[name] * quantity
        }

        self.cart.append(item)
        ShoppingCart.products[name] -= quantity 

    

    def remove_item(self, name):
        for item in self.cart:
            if item["name"] == name:
                if item["quantity"] == 1:
                    self.cart.remove(item)
                else:
                    item["quantity"] -= 1
                    item["price"] -= ShoppingCart.prices[name]

                ShoppingCart.products[name] += 1
                return

        print("Item not found in cart.")



subbu = ShoppingCart()
subbu.add_user()
subbu.display()
subbu.add_items("iphone", 5)
subbu.add_items("ipad", 2)

subbu.remove_item("iphone")

##subbu.display_cart()

print("\nRemaining Stock:")
print(ShoppingCart.products)


"""def bubble_sort(l):
    n= len(l)
    for i in range(n-1):
        for j in range(n-1):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    print(l)

l = [10,25,33,2,7]
bubble_sort(l)

a = ['apple','mangoshake','banana','ant']
bubble_sort(a)"""


from abc import ABC , abstractmethod

class payment(ABC):
    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def pay(self):
        pass

    def receipt(self,amount):
        return f"payment of ${amount} sucessfull"


class creditcardpayment(payment):
    def validate(self):
        print("validating the credit card.....")

    def pay(self,amount):
        print(f"paying ${amount} via credit card")


class paypalpayment(payment):
    def validate(self):
        print("logging into paypal....")

    def pay(self,amount):
        print(f"paying ${amount} via paypal")

class paymentservice:
    def process_payment(self,payment,amount):
        payment.validate()
        payment.pay(amount)
        print(payment.receipt(amount))


service = paymentservice()
cred_payment = creditcardpayment()
paypal_payment = paypalpayment()

pay = service.process_payment(paypal_payment,1000)


a = [1,2,3,4,5,6,7,8,9]

def even_number(a, i=0, b=[]):

    if i == len(a):
        return b

    if a[i] % 2 == 0:
        b.append(a[i])

    return even_number(a, i + 1, b)

print(even_number(a))


z = "12hello24"

def sum_number_string(a,i=0,sum=0):
    if i == len(z):
        return sum

    if '0' <= z[i] <= '9':
        sum += int(z[i])

    return sum_number_string(a,i+1,sum)

print(sum_number_string(z))

x = "ab932@$mn6pq#!*rs"
alpha = ''
number = ''
special = ''

def seperate(x, alpha, number, special, i=0):
    if i == len(x):
        return alpha,number,special

    if('0' <= x[i] <= '9'):
        number+=x[i]
    elif('a' <= x[i] <= 'z'):
        alpha+=x[i]
    else:
        special+=x[i]

    return seperate(x,alpha,number,special,i=i+1)

print(seperate(x,'','',''))
    
fruit = "banana"
ch = "a"
count =0
def find(fruit,ch,count,i=0,):
    if(i == len(fruit)):
        return count

    if(fruit[i] == ch):
        count+=1

    return find(fruit,ch,count,i=i+1)

print(find(fruit,ch,count))
##private public and protected
"""class s:
    __a=10
    _b=20

    def __init__(self,c):
        self.c=c

    def __display(self):
        print(self.a,self.b,self.c)

    @classmethod
    def ch_a(cls,new_a):
        cls.a = new_a
    @staticmethod
    def msg():
        print("hello")

oa = s(30)

print(s._s__display)

print(s._s__a)"""

"""class teacher:
    
    def __init__(self,teacher):
        self.teacher = teacher

    def display(self):
        print("teacher name is ", self.teacher)

class student(teacher):
    def __init__(self,tecaher,studentname):
        super().__init__(teache r)
        self.studentname = studentname

    def display(self):
        super().display()
        print("student name is ",self.studentname)

s=student("ramesh","subbu")
s.display()"""

"""s = "aaabbbccdd"
dict = {}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i] =1

print(dict)

def number(i=0):
    if i==10:
        return i
    print(i)

    return number(i=i+1)

print(number(0))"""

#specific exception
"""def fun():
    try:
        a = int(input("Enter the first number :"))
        b = int(input("Enter the second number :"))
        res = a/b
        print(res)
    except ZeroDivisionError:
        print("Input should  not be zero")
        fun()
    
fun()"""

##Generic Exception
"""def fun():
    try:
        a = int(input("Enter the first number :"))
        b = int(input("Enter the second number :"))
        res = a/b
        print(res)
    except Exception:
        print("handled")
        fun()
    
fun()"""


##default exception

"""def fun():
    try:
        a = int(input("Enter the first number :"))
        b = int(input("Enter the second number :"))
        res = a/b
        print(res)
    except:
        print("handled")
        fun()
    
fun()"""


##custom exception

"""a=10
b=20


if(a>b):
    print("a is greater")
else:
    raise ZeroDivisionError("A should be greater")"""

##assert

"""a=10
b=20
assert a>b,("a is smaller")
print("a is bigger")"""


##user defined error

"""class lengtherror(Exception):
    pass

n = input("Enter the name :")
if len(n) != 10:
    raise lengtherror("Enter 10 chararcter name")"""

##higher order functions

##syntax varname = lambda args1,args2,...argsn:return value
##print(varname(args1))
"""res = lambda n:n%2==0
print(res(10))"""


"""res = lambda st,ch,count : ch in st
print(res("banana","a"))"""

"""res = lambda a,b,c:a+b+c
print(res(1,2,3))"""

"""res = lambda a,b,c,d=1,e=1 :a*b*c*d*e
print(res(1,2,3))
print(res(1,2,3,4,5))"""

"""res = lambda a:not(a.isalnum())
print(res('9'))
print(res("A"))
print(res('a'))
print(res('@'))
print(res('$'))"""

