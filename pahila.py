# username=input("Enter your name ")
# Password=input("Enter password ")
# if username in'kaushik' and Password in"kaushik":
#     print("done")
# else:
#     print("NO")
# --------------------------------------> DataType
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# ----------------------------------> LIST
name = ["kaushik", "Harsh", "Vinavy", "tej", "Vigo"]
print(name[3])
name[1] = "blackcurrant"
name.pop()
# --------> print all element using for loop
print("print all element using for loop")
for x in name:
    print(x)
# --------> check element in list
print("check element in list")
if "kaushik" in name:
    print("Yes Kaushik here")
else:
    print("Kaushik Not in List")
# --------> To determine how many items a list has, use the len() function
print("To determine how many items a list has, use the len() function")
print(len(name))
# --------> TO add item in last
print("To add item in last")
name.append("Reena")
print(name)
# --------> add item to list with insert() index number
print("Add item to list with index number")
name.insert(0,"ME")
print(name)
# ---------> The remove() method removes the specified item
print("The remove() method removes the specified item")
name.remove("ME")
print(name)