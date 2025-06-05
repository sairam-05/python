"""list=[1,2,3,2,4,8]
x=4736
for i in list:
    if  x==i:
        print("found")
        break
else:
    print("not found")"""
"""list=[-1,-23,-242,-34,-234,-32,-32432,-3234322]
brain=list[1]
for i in list:
    if i>brain:
        brain=i
print(brain)"""
"""n=32
while n>0:
    x=n%10
    print(x,end="")
    n=n//10"""
"""n=432
n1=str(n)
n1=n1[::-1]
print(n1)
n1=int(n1)
print(n1)"""
"""n=2132
count=0
while n>0:
    x=n%10
    print(x,end=" ")
    count+=1
    n=n//10
print(" ")
print(count)"""
"""n=212
n1=n
y=0
while n>0:
     x=n%10
     y=y*10+x
     n=n//10
print(n1==y)"""
"""import time
x=23
y=0
z=1
c=time.perf_counter()
while x>0:
    n=x%10
    y+=n
    
    z*=x
    
    x=x//10
print(y)
print(z)
d=time.perf_counter()
print(d-c)"""
#print("HELLO,WORLD!")
"""a="sai"
print(a)"""
"""n=int(input())
op=input()
x=int(input())

if op== "+":
    print(n+x)
elif op=="-":
    print(n-x)"""
"""n=123
n=str(n)
print(type(n))"""

'''n=input("enter age")
print(f"your age is{n}")'''
'''a=int(input())
b=int(input())
sum=a+b
print(sum)'''
"""len=int(input())
width=int(input())
print(len*width)"""

"""a=int(input())

b=int(input())
for i in range(10):
 op=input()
 if op=="+":
        print(a+b)
 elif op=="-":
        print(a-b)
 elif op=='*':
        print(a*b)
 elif op=='/':
        print(a/b)
 elif op=="%":
        print(a%b)
 elif op=="//":
        print(a//b)"""
"""n=int(input())
if n%2==0:
    print("even")
else:
    print("odd")"""
"""a=12
b=8
if a>b:
    print(a)
else:

    print(b)"""
"""for i in range(10):
    print(i)"""
"""n=5
i=1
while i<=10: 
    print(n*i)
    i+=1"""
"""def sum(x,y):
    return x+y
a=sum(1,2)
print(a)"""
"""def prime(n):
    if n<=1:
        print("not prime")
    flag=False
    for i in range(2,n+1):
        if n%i==0:
            print("prime")
            flag=True
            break
        if flag==False:
            print("not prime")
            break
prime(1)"""
"""fruit=["banana","apple","orange","berry"]
for fruits in fruit:
    print(fruits)

fruit.append("straberry")
print(fruit)"""
"""str="saiAJK"
count=0
for i in str:
    if i in "aeiouAEIOU":
        count+=1
print(count)"""
"""str="sai ram"
for i in range(len(str)-1,-1,-1):
 print(str[i],end="")"""
dic={"ase":32,"sas":45,"rad":456}
flag=False
query=input("enter to find")
for item in dic:
 if query in item:
   print(f"{item}")
   flag=True
if  flag==False:
  print("no name")