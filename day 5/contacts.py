contacts={ }
def add():
 name=input("enter the name")
 num=int(input("enter number"))
 contacts[name]=num
def delete():
 name_to_delete=input("enter name to delete")
 if name_to_delete in contacts:
  del contacts[name_to_delete]
 else:
  print("no name found")
def view():
 for i in contacts:
  print(f"{i}={contacts[i]}")
def update():
  name=input()
  new_num=input("new num")
  contacts[name]=new_num
