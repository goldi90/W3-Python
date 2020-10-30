print("This is sets")
Set={"Kaushik","Harsh","Reena","Abhinesh","Umesh","Deepak","Anju","Rahul","Rohit"}
print(Set,"\n")

print("Acess item")
for x in Set:
    print(x)


print("\ncheck if item exists")
if "Reena" in Set:
    print("Yes Reena exist\n")


'''To add one item to a set use the add() method.

To add more than one item to a set use the update() method.'''

print("change  one item insets")
Set.add("Anand")
print(Set,"\n")

print("change  multiple item insets")
Set.update(["Kaushik", "Abhinesh"])
print(Set,"\n")

print("Remove  item from sets")
Set.discard("Umesh")
print(Set,"\n")

print("pop method")
Yaar={"Sanjay","chintu","Pardip"}
nikal=Yaar.pop()
print(nikal)

# The clear() method empties the set
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# The del keyword will delete the set completely:
# union function
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)





