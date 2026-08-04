s={1,3,45,4,3,45,67,35,67,43,65,"harry"}
print(s,type(s))

#add 
s={1,3,45,4,3,45,67,35,67,43,65,"harry"}
s.add("hassan")
print(s)


d={34,89,"hassan"}
d.add(78)
print(d)

#remove 
s={1,3,45,4,3,45,67,35,67,43,65,"harry"}
s.remove("harry")
print(s)


# d={34,89,"hassan"}
# d.remove(56)
# print(d)


#discard 
s={1,3,45,4,3,45,67,35,67,43,65,"harry"}
s.discard("hassaan")
print(s)


d={34,89,"hassan"}
d.discard(56)
print(d)

#update set ma add krnaa
s={1,5,6,"harry"}
s.update([2,3,4])
print(s)

a={1,3,5}
b={2,4}
a.update(b)
print(a)

#union set ka tamam unique elements ko add kr data ha 
a={1,3,5}
b={2,4}
a.update(b)
print(a)


a={"ahmad","hasssaan"}
b={"hassaan","ali"}
a.union(b)
print(a)


#intersection common nikalna
a={1,3,5}
b={1,3,2,4,5}
a.intersection(b)
print(a)


b={"ali","subhan","hassaan","faizan"}
c={"hassaan","subhan","ali"}
print(b.intersection(c))
print(b)

#diffrence sirf unique element 
a={1,3,5,6,7}
b={1,3,2,4,5}
print(a.difference(b))

b={"ali","subhan","hassaan","faizan"}
c={"hassaan","subhan","ali"}
print(b.difference(c))
