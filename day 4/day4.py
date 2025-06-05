"""list=[1,2,3,4,5,6,7]
x=int(input("enter the number to find"))
for i in range(len(list)):
    if x==list[i]:
        print("bffd")
        break
else:
    print("dfw")"""
"""def num(x,list):
    for i in range(len(list)):
        if x==list[i]:
            return "true"
    return "false"
c=int(input())
d=num(c,[2,3,7,8,9,0,4])
print(d)"""
"""list=[1,23,34,2,34343,3243,343,5544478877]
n=list[0]
for i in list:
   if n<i:
    n=i
print(n)"""
"""l=[1,2]
print(type(l))
l.append(43787)
l.insert(1,[1,2,3,22,1,233])
print(l)
l.remove(l[2])
print(l) 
l.pop(2)    
print(l)
l1=[233,2,4,5,2,1,7,9,65,4]
l1.sort()
print(l1)"""

"""list1=['s', 'a', 'i', 'r', 'a', 'm']
list1=str(list1)
list1=list1[::-1]
#list1=list(list1)
print(list1)
li=str(list1)
print(list1)"""
"""s=int(input())
while s>0:
    n=s%10
    print(n,end=" ")
    s=s//10"""
"""
s=1090
count=0
while s>0:
   s=s//10
   count+=1
   
print(count)"""
"""import time

import math
s=time.perf_counter()
n=123
print(int(math.log10(n))+1)
e=time.perf_counter()
print(e-s)"""
"""s=12324
count=0
while s>0:
 s=s//10
 count+=1
print(count)"""
"""n=123
y=0
z=1
while n>0:
    x=n%10
    y+=x
    z*=x

    n=n//10
print(y) 
q=y-z
print(q)"""
n1=121
n=n1
y=0
while n>0:
    x=n%10
    y=y*10+x
    n=n//10
print(n1==y) 



    
   



    

    

    

    
