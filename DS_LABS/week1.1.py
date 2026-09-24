#print
#print("Hello World")

#code for datatypes
"""name="Thamu"
age=19
weight=50.5
print(name,age,weight ,sep="**")"""

#input
"""name=input("Enter course name")
a=int(input())
b=float(input("enter number"))
print(name,a,b,sep=",")
print(type(name),type(a),type(b),sep=",")"""

#boolean using conditional statements
"""a=int(input("Enter a number"))
b=int(input("Enter b number"))
is_greater=False
if a>b:
    is_greater=True
print(is_greater)"""

#assign same value to multiple variables
"""a=b=c="hi"
print(a,b,c,sep=",")"""

#operators
"""a=int(input("enter a"))
b=int(input("enter b"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)"""

#type casting
"""a=5.88
#print(int(a))
#print(float(a))"""

#string slicing
"""name="Thanusree"
print(name[0:5])
print(name[:3])
print(name[4:])
print(name[-1])
print(name[1:4:9])
print(name[-1:9])"""

#string functions
"""name="meghna.P"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.swapcase())
print(name.title())
print(len(name))"""

#string concatination
"""a="Meghna"
b="Thanusree"
print(a+" "+b)"""

#string format method
"""txt1="my name is{name}".format(name=" tan")
print(txt1)"""

#greatest of three numbers
"""a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)"""

#even or not
"""a=int(input())
if a%2==0:
    print("even")
else:
    print("odd")"""

#grade of student
"""sub1=int(input())
sub2=int(input())
sub3=int(input())
avg=(sub1+sub2+sub3)/3
if avg>=90:
    print("A")
elif avg>=80:
    print("B")
elif avg>=70:
    print("C")
else:
    print("D")"""

#for loop s
"""n=int(input())
sum=0
for i in range(n+1):
    sum+=i

print(sum)"""

# number palindrome
"""n=int(input())
temp=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n//=10
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")"""

#function
"""def calculate_sum(a,b):
    c=a+b
    return c
print(calculate_sum(5,10))"""
