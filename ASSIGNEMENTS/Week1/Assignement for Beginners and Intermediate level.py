#Length of a String
#Write a program that reads a string and prints its length.
Length=input("Enter your data :")
print(len(Length))

#Uppercase & Lowercase
#Convert the input string to uppercase and lowercase.
Text="ZaIn HaSsaN"
print("Converted String :")
print(Text.upper())
print("Converted String in lower is :")
print(Text.lower())

#Count a Character
#Count how many times a given character appears in a string (case-sensitive).
Text=input("Enter a Word :")
Char=input("Enter a character to count :")
count=Text.count(Char)
print("The Word",Char,"appears",count,"times..")

#First & Last Character
#Print the first and last character of a string; handle empty input.
Text=input("Enter a word :")
if len(Text)==0:
    print("The string is empty")
else:
    print("First character :",Text[0])
    print("Last character :",Text[-1])

#Check Substring Presence
#Check if a substring exists in a string
String=input("Enter a string :")
print(String[0:2:1])

#Replace Substring
#Replace all occurrences of a word with another (case-sensitive).
Text=input("Enter a String :")
OldWord=input("Enter a word to replace :")
NewWord=input("Enter a new word :")
Result=Text.replace(OldWord,NewWord)
print("The result :",Result)

#Reverse a String
#Reverse the string.
Text=input("Enter a string :")
print("The reverse string is :",Text[::-1])

#Split and Join
#Split a sentence on spaces and join with.
Sentence=input("Enter a sentence :")
Word=Sentence.split()
Result="-".join(Word)
print("Output :",Result)

#Strip Whitespace
#Remove leading and trailing spaces.
Text=input("Enter a string :")
Result=Text.strip()
print("Output :",Result)

#. Count Vowels & Consonants
#Count vowels and consonants (letters only; ignore digits/punctuation).
Text=input("Enter a string :")
Vowels="aeiouAEIOU"
VowelsCount=0
consonantCount=0
for ch in Text:
    if ch.isalpha():
        if ch in Vowels:
            VowelsCount +=1
        else:
            consonantCount+=1
print("Vowels :",VowelsCount)
print("Consonant :",consonantCount)

#Palindrome Check (Ignore Case & Non-alphanumerics)
#Determine if a string is a palindrome ignoring case and non-alphanumeric characters
Text=input("Enter a string :")
CleanText=""
for ch in Text:
    if ch.isalnum():
        CleanText += ch.lower()
if CleanText == CleanText[::-1]:
    print("Polindrome :")
else:
    print("Not a Polindrime :")
     
#Title Case (Manual)
#Convert a sentence to title case without using .title().     
Sentence=input("Enter a sentence :")
Words=Sentence.split()
Result=[]
for words in Word:
    if len(Word) >0:
     NewWord=Word[0].upper()+Word[1:].lower()
     Result.append(NewWord)
TitleCase=" ".join(Result) 
print("Output :",Result)

#Find All Indices of a Substring (Allow Overlaps)
#Return a list of starting indices where a substring occurs.
Text=input("Enter the main String :")
Sub=input("Enter the substring :")
indices=[]
for i in range (len(Text)+len(Sub)+1):
    if Text[i:i+len(Sub)]==Sub:
        indices.append(i)
print("Starting indices :",indices)   

#Character Frequency Dictionary
#Build a frequency dictionary for characters (case-insensitive, skip spaces).
Text=input("Enter a string :")
Text=Text.lower()
Frequency={}
for ch in Text:
    if ch !=" ":
        if ch in Frequency:
            Frequency[ch]+=1
        else:
            Frequency[ch]=1

print("Character Frequency :", Frequency)

#Anagram Checker
#Check if two strings are anagrams (ignore spaces, punctuation, and case).
Str1=input("Enter a string :")
Str2=input("enter a string :")
Clean1=" "
Clean2=" "

for ch in Str1:
    if ch.isalnum():
        Clean1+=ch.lower()

for ch in Str2:
    if ch.isalnum():
        Clean2+=ch.lower()

if sorted(Clean1)==sorted(Clean2):
    print("The strings are anagram :")
else:
    print("The strings are not anagram :")

#Compress Repeated Characters (RLE-lite)
#Compress runs of the same character as <char><count>
Text=input("Enter a string :")
Result=" "
Count=1
for i in range(len(Text)):
    if i < len(Text)-1 and Text[i]==Text[i+1]:
        count+= 1
    else:
        Result+= Text[i]+ str(count)
        count=1
print("Compressed String :",Result)

#Longest Word in a Sentence
#Find the longest word; if multiple, return the first. Consider words as alphabetic
#sequences.
Sentence=input("Enter a sentence :")
Word=" "
Longest=" "
for ch in Sentence:
    if ch.isalpha():
     Word += ch
else:
    if len(Word)>len(Longest):
        Longest=Word
        Word =" "
if len(Word)>len(Longest):
    Longest = Word
print("Longest word :",Longest)

#Remove Duplicate Characters but Keep Order
#Remove duplicates while preserving the first occurrence order.
Text=input("Enter a string :")
Result=" "
for ch in Text:
    if ch not in Result:
        Result += ch
print("Output :",Result) 

#Mask Email Username
#Mask all but the first and last character of the username with *; keep domain intact.
Email = input("Enter an email: ")
Username , domain = Email.split("@")
if len(Username) <= 2:
    masked = Username
else:
    masked = Username[0] + "*" * (len(Username) - 2) + Username[-1]
print("Masked Email:", masked + "@" + domain)
