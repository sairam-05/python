"""gradebook={ }
def newstudent():
    student_name=input("enter the student name")
    print("enter the marks by sep with ,")
    marks=list(map(int,input().split(",")))
    
    gradebook[student_name]=marks
def update():
 name=input("enter the name")
 if name in gradebook:
  print("enter the marks by sep with ,")
  marks=list(map(int,input().split(",")))
  gradebook[name]=marks
 else:
  print("no such name is found") 
def view():
 sum=0
 for i in gradebook:
  for j in range(len(gradebook[i])):
   sum+=gradebook[i][j]
 print(f"{i}={gradebook[i]}", "avg=",sum/len(gradebook[i]))
  #print(f"{i}={gradebook[i]} avg marks={(sum(gradebook[i])/len(gradebook[i]))}")
def remove():
 name=input("enter name to remove")
 if name in gradebook:
  del gradebook[name]
 else:
  print("no name is found")"""
"""def avg():
 sum=0
 name=input("enter the name for whom yo want to calculate")
 if name in gradebook:
  for i in gradebook[name]:
   sum+=i
 avg=sum/len(gradebook[name])
 print(avg)"""
# """for i in range(10):
#     n=list(map(int,input("enter the n value").split(",")))
#     print(n)"""
"""
print("grade marks of students")
while True:
    try:
        print("choice")
        print("1.add the new student\n2.update the marksn\n3.view all students\n4.remove the student\n5.avg\n6.exit")
        choice=int(input("enter your choice"))
        if choice==1:
            a.newstudent()
        elif choice==2:
                a.update()
        elif choice==3:
                a.view()
        elif choice==4:
                a.remove()
        elif choice==5:
                a.avg()
        else:
                print("end")
                break         

    except Exception as e:
            print(f"error occured{e}")
    finally:
           print("contact added")"""

"""student={
    "name":"sai" ,
    "age":19,
    "marks":[91,96,87],
    "present":True

}
sum=0
for i in student["marks"]:
 sum+=i
student["average"]=sum/len(student['marks'])
student["name"]="nani"
print(student["name"]) 
student["village"]="gdp"
print(student)
for i in student:
 print(f"{i}={student[i]}")

student["contact"]=9948784999
print(student["name"])

print(student["contact"])
student["name"]=None
print(student)

n=input("enter name")
num=int(input())
if num==range(10):
    print(num)
else:
    print("valid value")
print(f"{n},{num}")"""