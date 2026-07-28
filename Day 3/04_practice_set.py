'''write a program to replace to double space to single space'''
name="My  name  is  Hassaan  "
print(name.replace("  "," "))


'''Write a Python program to take a sentence from the user and:

Count the total number of double spaces.
Replace all double spaces with single spaces.
Display the cleaned sentence.'''
sent="My  name  is  Hassaan  "
print(f'Total number of double spaces:{sent.count("  ")}')
clean=sent.replace("  "," ")
print(f"Replace double to single spaces:{clean}")
print(f"Cleaned Sentence:{clean}")




