import mod as c
print("CONTACT")
while True:
 try:
        print("CHOICES")
        print("1.add new number\n 2.delete the number\n3.view the data\n4.search\n5.update number\n6.exit")
        choice=int(input("enter the choice"))
        if choice==1:
            c.add()
        elif choice==2:
            c.delete()
        elif choice==3:
            c.view()
        elif choice==4:
            c.search()
        elif choice==5:
           c.update( )
        else:
            print("thankyou")
            break
 except Exception as e:
  print(f"exception occured is{e}")
 else:
  print("try block exected sucessfully")
 finally:
   print("contact block final stage")
 

