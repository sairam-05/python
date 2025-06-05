"""file=open("./names.txt" ,"r")
#print(file.read())#r
#d=file.readline()
#d=file.write("\nhi")#a,w
#print(d)
#d=file.readline()#one line
#print(file.split("\n"))
#file.close()
data=file.readlines()
#data=data.split("\n")
age_dict={}
for item in data:
    split_data=item.split( )
    age_dict[split_data[0]]=split_data[1]
print(age_dict)"""
try:
    n1=int(input())
    n2=int(input())
    result=n1/n2
except Exception as e:
 print(f"erroe occured is{e}")
else:
   print("try executed succesfully")
finally:
   print("completed")
print(result)