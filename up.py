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
else:
    print("kallu dengaya ra")

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
