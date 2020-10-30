print("Below is orginal list")
Mylist = ["Kaushik","Harsh","Reena","Abhinesh","Umesh","Deepak","Anju","Rahul","Rohit"]
print(Mylist)

print("Acessed items from list")
print(Mylist[4],"\n")

print("Change item in list")
Mylist[0]="Me"
print(Mylist,"\n")

print("print item one by oneLoop Thorugh List\n")
for x in Mylist:
    print(x)

print("\ncheck item exist")
if "Reena" in Mylist:
    print("Yes Reena Here\n")

print("Lenght of List")
print(len(Mylist),"\n")

print("append Or add item in last of list")
Mylist.append("Ramesh")
print(Mylist,"\n")

print("Insert iten in list without deleting items")
Mylist.insert(0,"Kaushik")
print(Mylist,"\n")

print("Remove Item from list")
Mylist.remove("Me")
print(Mylist,"\n")

print("Delete Last item from list using pop method")
Mylist.pop()
print(Mylist,"\n")

print("Delete Last item from list using del keyword")
del Mylist[0]
print(Mylist,"\n")

print("Delete whole list using del keyword Uncomment del statment to see")
# del Mylist
print(Mylist,"\n")

print("clear whole list with clear Method")
Mylist.clear()
print(Mylist,"\n")

print("Copy list")
mylist=Mylist.copy()
print("This is from mylist",mylist)

print("Other way to create list using list(( ...)) ")
AnoList=list(("Hello i am constructor of list","I am element of list","I am <--his brother"))
print(AnoList,"\n")

print("jointing to list")
Pen=["Lexi","Boll","Jell","Jupiter"]
Pencil=["Apsare","Natraj","Chalu"]
print(Pen+Pencil)

