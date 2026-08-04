'''can we  have a set with 18(int)and '18' str as a value init'''
a={18}
a.add('18')
print(a)




'''Create a set that contains integer, string, and float values. 
Add one more value using add() and 
display the final set.'''
s=set()
s.add(18)
s.add("18")
s.add(23.8)
print(s)


'''Create a set from a list containing duplicate values. 
Display the set and explain why duplicate values are removed.
numbers = [10, 20, 10, 30, 20, 40]'''
numbers={10,20,10,30,20,40}
print(numbers)

'''Create two sets. 
Add all elements of the second set into the first set using update(). 
Display the final set.'''
a={1,2,3}
b={5,4,3}
a.update(b)
print(a)


'''Create two sets of students who like different sports. Display:

Students who like any sport (Union)
Students who like both sports (Intersection)'''
a={1,2,3}
b={5,4,3}
print("students who like any sport:",a.union(b))
print("student who like both sports:",a.intersection(b))

'''Create two sets:
Elements only in A
Elements only in B
Common elements
All elements together'''
a= {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("Elements only in a:",a.difference(b))
print("Elenets only in b:",b.difference(a))
print("All elements:",a.union(b))
print("common elements:",a.intersection(b))


s={}
print(type(s))