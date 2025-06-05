def add():
    name=input("enter name")
    num=int(input('enter number'))
    # contact[name]=num
    file=open("./ncontact.txt","a")
    file.write(f"{name} {num}\n")

    
    file.close()
def delete():
    name=input("enter name to delete")
    file=open("./ncontact.txt","a")
    data=file.readlines()
    data1=""
    file.close()
    for d in data:
        k=d.split()
        if name==k[0]:
            continue
        else:  
         k=k[0]+" "+k[1]
         data1=data1+k+"\n"
    file=open("./ncontact.txt","r")
    file.write(data1)   
    file.close( )   
    
    # if name in contact:
    #     del contact[name]
    # file=open("./ncontact.txt","a")
def search():
    name=input("enter the name")
    file=open("./ncontact.txt","r")
    h=file.readlines()
    file.close()
    flag=False
    for k in h:
        a=k.split()
        if name==a[0]:
            print(f"{a[0]}:{a[1]}")
            flag=True
    if flag==False:
        print("not founnd")
def update():
    file=open(".\ncontact.txt","r")
    name=input()
    data=file.readlines()
    data1=""
    file.close()
    for d in data:
        k=d.split()
        if name==k[0]:
            phone_num=int(input())
            k[1]=str(phone_num) 
        k=k[0]+" "+k[1]
        data1=data1+k+"\n"
    file=open("./ncontact.txt","w")
    file.write(data1)   
    file.close( )     
def view():
    #print(contact)
    # for i in contact:
    #  print(f"{i}={contact[i]}")
     file=open("./ncontact.txt","r")
     print(file.read())   

#    #if name in contact:
#    # contact[name]=num
#    #else:
#    #print("no contact found")
#    file=open("./ncontact.txt","a")
#    file.write()