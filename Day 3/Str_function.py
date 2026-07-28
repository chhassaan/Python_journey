#upper string ko upper bana adta ha
name="hassaan"
print(name.upper())

name="ali"
print(name.upper())

#lower string ko lower kr data ha 
name="HASSAAN"
print(name.lower())

name="ALI"
print(name.lower())

#tittle har word ka first word ko capital kr dta ha 
name="hassaan"
print(name.title())

name="ali"
print(name.title())

#replace string ko replcae krta ha 
name="i love ""python"
print(name.replace("python","java"))

name="Ali is a good boy"
print(name.replace("Ali is a good boy","Ali is a bad boy"))

#find index ko find krta ha 
name="Hassaan"
print(name.find('s'))

name="ali"
print(name.find("i"))

#count character or word count krta ha
name="Hassaan"
print(name.count("a"))

name="ali","ali","suban","ali"
print(name.count("ali"))

#strip strat or end ka extra spaces hata data haa
name=" Hassaan"
print(name.strip())

name="     subhan    "
print(name.strip())

#split string ko list ma convert krta haa
name="Hassaan"
print(name.split())

name="subhan"
print(name.split())

#join list ka all items ko mila ka ak string baa data haa
name=['hassaan ali subhan']
print(','.join(name))