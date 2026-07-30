#append method list ma element add krta haa
friend=["ALi","Subhan","hassaan"]
friend.append("Faizan")
print(friend)

numbers=[34,89,90]
numbers.append(56)
print(numbers)

#extend dosre list k sara elemnt add krta ha
friend=["ALi","Subhan","hassaan"]
numbers=[34,89,90]
friend.extend(numbers)
print(friend)

list1=[1,2,3,4]
list2=[4,3,2,1]
list2.extend(list1)
print(list2)
#insert kisi bi position pir elements ko add krta ha
friend=["ALi","Subhan","hassaan"]
friend.insert(2,"banana")
print(friend)

number=[1,2,4,5,]
number.insert(4,3)
print(number)

#remove value ko del krta ha

friend=["ALi","Subhan","hassaan"]
friend.remove("Subhan")
print(friend)

number=[1,2,4,5,]
number.remove(4)
print(number)

#pop index sa element remove krta ha or return bi lata ha
number=[90,100,110,120,130]
number.pop()    #python agr koi index na mila too default last index ko remove kr da g
print(number)


number=[90,100,110,120,130]
number.pop(3)   
print(number)

#clear poori list ko khali kr data haa
number=[90,100,110,120,130]
number.clear()   
print(number)

friend=["ALi","Subhan","hassaan"]
friend.clear()
print(friend)


#count kon se value kitni bar ae ha is ka pata lagat ha
number=[34,87,56,33,56,33,33,33]
print(number.count(33))


word=["I LOVE PYTHON"]
print(word[0].count("O"))

#sort list ko asending order ma store krtaaa haaa
word=["banana","mango","apple"]
word.sort()
print(word)

num=[1,2,3,4,3,2,1]
num.sort()
print(num)

#reverse list ko ulta kr data haa
num=[3,2,1]
num.reverse()
print(num)

word=["a","b","c","d","e","f"]
word.reverse()
print(word)

#copy list ki copy banata 

word=["a","b","c","d","e","f"]
print(word.copy())