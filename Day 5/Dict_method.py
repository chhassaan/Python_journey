# Keys returns all  keys
marks={
    "name":"hassaan",
    "age":45
}
print(marks.keys())



student={
    'st1':"hassaaan",
    "st2":"ali"

}
print(student.keys())

#value return all values
marks={
    "name":"hassaan",
    "age":45
}
print(marks.values())


student={
    'st1':"hassaaan",
    "st2":"ali"

}
print(student.values())

#items return keys and values
marks={
    "name":"hassaan",
    "age":45
}
print(marks.items())

student={
    'st1':"hassaaan",
    "st2":"ali"

}
print(student.items())

#get retuen value safely
marks={
    "name":"hassaan",
    "age":45
}
print(marks.get("name"))
print(marks.get("age"))

student={
    'st1':"hassaaan",
    "st2":"ali"

}
print(student.get("st1"))
print(student.get("st2"))

#update adds or updates items 
student={
    "name":"hassaan",
    "name":"subhan"
}
student.update({"age":43})
print(student["name"],student["age"])


marks={
    "st1":34,
    "st2":56,
    "st3":554
}
marks.update({"st4":90})
print(marks["st4"],marks["st1"])




#pop removes a specific key
intro={
    "name":"hassaan",
    "age":34
}
intro.pop("age")
print(intro)



intro={
    "name":"subhan",
    "age":45
}
intro.pop("name")
print(intro)
#popitem remove the last key value pair

intro={
    "name":"ali",
    "age":78
}
intro.popitem()
print(intro)


intro={
    "name":"subhan",
    "age":45,
    "city":"chiniot"
}
intro.popitem()
print(intro)

#clear remove alll items

intro={
    "name":"subhan",
    "age":45,
    "city":"chiniot"
}
intro.clear()
print(intro)

intro={
    "name":"ali",
    "age":78
}
intro.clear()
print(intro)

#copy creates a copy
intro={
    "name":"ali",
    "age":78
}
intro2=intro.copy()
print(intro)


marks={
    "name":"hassaan",
    "age":45
}
marks2=marks.copy()
print(marks)


#set default adds key if it doesnt exist 
marks={
    "name":"hassaan",
    "age":45
}
marks.setdefault("city","chiniot")
print(marks)

student={
    'st1':"hassaaan",
    "st2":"ali"

}
student.setdefault("st4","subhan")
print(student.keys())
print(student)