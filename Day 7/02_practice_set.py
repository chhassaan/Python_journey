'''write a proggram to greet at all the person names stored in a list l and which starts 
with s'''
l=["harry","sohan","sachin","rahul"]
for i in range(len(l)):
    if l[i].startswith("s"):
        print("hello",l[i])

print(".......................First program..........................................")




names = ["ali", "ahmed", "subhan", "saad", "hassan"]
for i in range(len(names)):
    if names[i].startswith("a"):
        print("Hello",names[i])

for i in range(len(names)):
    if names[i].endswith("n"):
        print("hello",names[i])




print(".......................secound program..........................................")



'''Program likho jo sirf un cities ko print kare jinki length 7 se zyada ho.'''
cities = ["lahore", "islamabad", "karachi", "multan", "quetta"]
for i in range(len(cities)):
    if len(cities[i])>7:
        print(cities[i])





print(".......................third program..........................................")



'''Program likho jo sirf un names ko print kare jo:

"s" se start hote hon AND
unki length 5 ya us se zyada ho.'''
names = ["ali", "subhan", "sachin", "hassan", "saad", "umer"]
for i in range(len(names)):
    if names[i].startswith("s"):
        if len(names[i])>5:
            print(names[i])


print(".......................fourth program..........................................")



'''Program likho jo sirf un names ko print kare jo:

"s" se start hote hain AND
unki length 4 se zyada ho AND
naam ke andar "a" bhi موجود ho.'''
names = ["ali", "subhan", "sachin", "hassan", "saad", "umer", "sana", "usman"]
for i in range(len(names)):
    if names[i].startswith("s"):
        if len(names[i])>4:
            if "a" in names[i]:
                print(names[i])






print(".......................fifth program..........................................")