x=int(input("enter number ", ))
s=x%10
print("last digit from number",s)

# it works for negative
x=int(input("enter number ", ))
s=abs(x)%10
print("last digit from number",s)

d=int(input("enter d", ))
n= int(input("enter n", ))
print((d-n)%7)

txt="rajesh koredla, koredla lakshmi, rama lakshmi kore"
pat="kore"
pos=txt.find(pat)
print(pos)

txt=input("enter text", )
pat=input("enter pattern", )
pos = txt.find(pat)
while pos>=0:
    print(pos)
    pos=txt.find(pat,pos+1)

#reverse string
def reverse(a):
    a=a[::-1]
    return a
a="rajesh"
print(reverse(a))

def reverse(a):
    str=" "
    for i in a:
        str= i + str
    return str
a="rajesh"
print(reverse(a))

# pallindrome or not
def pallindrome(a):
    str=a[::-1]
    if str==a:
        return True
    else:
        return False
a="madam"
print(pallindrome(a))

def capital_first_letter(a):
    a=a[0].upper() + a[1:]
    return a
a="rajesh"
print(capital_first_letter(a))

# print alphabets from c1 to c2 in one line
def alphabets(c1,c2):
    a=ord(c1)
    b=ord(c2)
    for i in range(a,b+1):
        print(chr(i),end=" ")
x,y = "c","n"
print(alphabets(x,y))

l1=[x for x in range(10) if x%2==0]
print(l1)

l2= [x for x in range(20) if x%2==1]
print(l2)

#get smaller than x
l1=[1,44,55,2,3,4,3,2,45,55,77,89]
x=30
l3= [y for y in l1 if y<x]
print(l3)

s="geeks for geeks"
l4=[i for i in s if i in "aeiou"]
print(l4)

s1=["geeks","ide","courses","rajesh","lanched","data science","data engineer","data scientist"]
l5 = [i for i in s1 if i.startswith("data")]
print(l5)

s6=[x*2 for x in range(10)]
print(s6)

d1={x:f"id{x}" for x in range(5)}
print(d1)

l1=[101,102,103]
l2=["hi","rajesh","how are you"]
d1={l1[i]:l2[i] for i in range(len(l1))}
print(d1)

l1={1:"hi",2:"rajesh",3:"how are you"}
d2={k:v for (k,v) in l1.items()}
d3={k for (k,v) in l1.items()}
d4={v for (k,v) in l1.items()}
print(d2)
print(d3)
print(d4)

# Given two integers a and b, you need to concatenate them so the output is ab.
a=5
b=6
l1 = str(a)+str(b)
print(int(l1))

a={2,5,6}
b={1,4,3,2}
ans=set(a).add(b)
print(ans)
'''
Given a dictionary, and a list of queries(keys), 
you have to find and print the value of each query 
from the dictionary if present else it prints "None".
Input:
dict = {1:"abc", 2: "cde", 3: "fgh"}
query = [2, 3, 4]
Output:
cde
fgh
None
'''
def Query(dict, query):
    for i in query:
        if i in dict.keys():
            print(dict[i])
        else:
            print("None")
dict = {1:"abc", 2: "cde", 3: "fgh"}
query = [2, 3, 4]
Query(dict,query)

def palindrom_number(a):
    temp=a
    rev=0
    while temp!=0:
        b=temp%10
        rev=rev*10 + b
        temp=temp//10
    print(rev)
    if rev == a:
        return "palindrome"
    else:
        return "not palindrome"
a=78987
print(palindrom_number(a))

def factorial(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def fact(n):
    res=1
    for i in range(2,n+1):
        res=res*i
    return res
print(fact(6))

def factorial(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n * factorial(n-1)
def trailing_zero(n):
    res=factorial(n)
    print("res",res)
    temp=res
    count=0
#print(temp)
    while temp!=0 and temp%10==0:
        temp=temp//10
        count=count+1
    return count
print(trailing_zero(24))

def gcd(a,b):
    if a<b:
        bigger=b
    else:
        bigger=a
    n=int(bigger/2)
    #print(n)
    i=2
    c=[1]
    while i<n:
        if a%i==0 and b%i==0:
            c.append(i)
            i=i+1
        else:
            i=i+1
    return c[-1]
print(gcd(12,17))
#Ecuilidean algorithm
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    if a>b:
        return gcd(a-b,b)
    return gcd(a,b-a)
print(gcd(12,17))

def lcm(a,b):
    res=max(a,b)
    while True:
        if res % a ==0 and res % b == 0:
            return res
        res+=1
    return res
print(lcm(4,9))

def absolute_val(a):
    if a<0:
        return -1 * (a)
    else:
        return a
print(absolute_val(-12))

121%10

12%10

def fun(n):
    if n==0:
        return
    print("gfg")
    fun(n-1)
fun(6)

def sum_digit(a):
    temp1=0
    while a>0:
        temp=a
        a=a//10
        b=temp%10
        temp1=temp1+b
    return temp1
a=984
print(sum_digit(a))

def sum_digit1(a):
    temp=0
    if a<0:
        return
    else:
        #temp=a
        a=a%10
        temp=a+sum_digit1(temp)
        return temp
a=984
print(sum_digit1(a))


