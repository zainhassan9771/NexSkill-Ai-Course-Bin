#Write a program to create a new string made of an input string’s first,
#middle, and last character.
String=input("Enter a string :")
print("First chracter :",String[0])
print("Middle character :",String[len(String)//2])
print("Last Character :",String[-1])

#Write a program to create a new string made of an input string’s first,
#middle, and last character.
Data=input("Enter a word :")
for x in Data:
    print(x, ":",Data.count(x))

#Reverse a given string
String=input("Enter a word :")
print(String[::-1])

#Split a string on hyphens
String=("Enter a string :")
print("Enter String :",String.split)
