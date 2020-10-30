print("This is tuple")
tup=("Kaushik","Harsh","Reena","Abhinesh","Umesh","Deepak","Anju","Rahul","Rohit")
print(tup,"\n")

print("Acess item of tuples")
print(tup[0],"\n")

print("changing tuple value")
Tlist=list(tup)
Tlist[0]="Me"
tup=tuple(Tlist)
print(tup,"\n")

print("Loop through tuples")
for x in tup:
    print(x)

print("\nCheck if item exits")
if "Me" in tup:
    print("!!Yes Me exist\n")

print("Tuples length")
print(len(tup),"\n")

print("create tuple with one item")
SingleTup=("KAushikD",)
print(type(SingleTup),"\n")

print("delete whole tupple using del keyword")
# del tup
print(tup,"\n")

print("tuple constructor")
me=tuple(("Idont know",))
print(me,"\n")

print("add two tuple")
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)







