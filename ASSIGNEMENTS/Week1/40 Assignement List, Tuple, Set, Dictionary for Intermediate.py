#Part 1 List
#Create a list comprehension that returns the squares of only the even numbers
#from 0–20.
Squares = [x**2 for x in range(21) if x % 2 == 0]
print(Squares)

#Given nums = [3, 1, 4, 1, 5, 9], sort the list without modifying the original.
Nums = [3, 1, 4, 1, 5, 9]
SortedNums = sorted(Nums)
print("Original list:", Nums)
print("Sorted list:", SortedNums)

#Remove duplicates from a list while preserving the original order.
Nums = [1, 2, 2, 3, 1, 4, 5, 4]
unique = []
for item in Nums:
    if item not in unique:
        unique.append(item)
        print(unique)

#Flatten the nested list [[1, 2], [3, 4], [5]] into a single list using a list comprehension.
flat = [item for sublist in "nested" for item in sublist]
print(flat)      

#Given names = ['alice', 'Bob', 'charlie', 'DAVID'], sort them alphabetically but ignore
#case.
Names = ['alice', 'Bob', 'charlie', 'DAVID']
SortedNames = sorted(Names, key=str.lower)
print(SortedNames)

#Replace items from index 2–4 in a list with [100, 200] using slice assignment.
Nums = [10, 20, 30, 40, 50, 60]
Nums[2:5] = [100, 200]
print(Nums)

#Write a program to find all indices of a value in a list (e.g., all indices of 7).
Nums= [7, 3, 7, 5, 7, 9]
value = 7
Indices = [i for i, x in enumerate(Nums) if x == value]
print(Indices)

#Create a new list containing only elements that appear exactly once in the original
#list.
Nums = [1, 2, 2, 3, 4, 4, 5, 6]
UniqueOnce = [x for x in Nums if Nums.count(x) == 1]
print(UniqueOnce)

# Rotate a list right by one position (e.g., [1,2,3,4] → [4,1,2,3]).
Nums= [1, 2, 3, 4]
Rotated = [Nums[-1]] + Nums[:-1]
print(Rotated)

#Split a list into two lists: one with even numbers, one with odd numbers.
Nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even = [x for x in Nums if x % 2 == 0]
Odd = [x for x in Nums if x % 2 != 0]
print("Even numbers:", Even)
print("Odd numbers:", Odd)


#Part 2 Tuple
#Convert the list [1, 2, 3, 4] into a tuple and then unpack it into four variables.
Nums = [1, 2, 3, 4]
TupleNums = tuple(Nums)

a, b, c, d = TupleNums

print("Tuple:", TupleNums)
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


#Given t = (('a', 1), ('b', 2), ('c', 3)), create a list of all second elements.
t = (('a', 1), ('b', 2), ('c', 3))

SecondElements = [x[1] for x in t]

print("Second elements:", SecondElements)


#Write a function that returns multiple values (sum, min, max) using a tuple.
def Calculate(Nums):

    Sum = sum(Nums)
    Minimum = min(Nums)
    Maximum = max(Nums)

    return (Sum, Minimum, Maximum)


Nums = (10, 20, 30, 40, 50)

Result = Calculate(Nums)

Sum, Minimum, Maximum = Result

print("Sum:", Sum)
print("Minimum:", Minimum)
print("Maximum:", Maximum)


#Combine two tuples (1, 2, 3) and (4, 5) then convert the result to a list.
Tuple1 = (1, 2, 3)
Tuple2 = (4, 5)

Combined = Tuple1 + Tuple2

List = list(Combined)

print("Combined tuple:", Combined)
print("Converted list:", List)


#Given a tuple of numbers, find the element with the highest frequency.
Nums = (1, 2, 2, 3, 3, 3, 4)

Highest = None
HighestCount = 0

for x in set(Nums):

    Count = Nums.count(x)

    if Count > HighestCount:

        HighestCount = Count
        Highest = x

print("Element with highest frequency:", Highest)
print("Frequency:", HighestCount)


#Check if two tuples contain the same elements regardless of order.
Tuple1 = (1, 2, 3, 4)
Tuple2 = (4, 3, 2, 1)

if sorted(Tuple1) == sorted(Tuple2):

    print("Both tuples contain the same elements")

else:

    print("Tuples do not contain the same elements")


#Extract the last three items from a tuple using slicing.
Nums = (10, 20, 30, 40, 50, 60)

LastThree = Nums[-3:]

print("Last three items:", LastThree)


#Concatenate a tuple with itself three times.
Nums = (1, 2, 3)

Repeated = Nums * 3

print("Repeated tuple:", Repeated)


#Convert a nested tuple ((1,2),(3,4)) into a flat tuple (1,2,3,4).
Nested = ((1, 2), (3, 4))

Flat = tuple(x for subtuple in Nested for x in subtuple)

print("Flat tuple:", Flat)


#Store coordinates in tuples and calculate the Manhattan distance.
Point1 = (2, 3)
Point2 = (5, 7)

x1, y1 = Point1
x2, y2 = Point2

Distance = abs(x1 - x2) + abs(y1 - y2)

print("Point 1:", Point1)
print("Point 2:", Point2)
print("Manhattan Distance:", Distance)

#Part 3 Set...
#Given two sets, find elements that are in the first set but not the second.
Set1 = {1, 2, 3, 4, 5}
Set2 = {4, 5, 6, 7, 8}

Difference = Set1 - Set2

print("Elements in first set but not second:", Difference)


#Find common items between three sets using intersection.
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 3, 4, 6, 7}
Set3 = {2, 3, 8, 9}

Common = Set1 & Set2 & Set3

print("Common items:", Common)


#Given a sentence, return all unique words in lowercase.
Sentence = "Python is Easy and Python is Powerful"

Words = Sentence.lower().split()

UniqueWords = set(Words)

print("Unique words:", UniqueWords)


#Convert a list with duplicates into a set, then back to a sorted list.
Nums = [5, 2, 3, 2, 1, 5, 4, 3]

SortedNums = sorted(set(Nums))

print("Sorted list without duplicates:", SortedNums)


#Check if one set is a strict subset of another.
Set1 = {1, 2, 3}
Set2 = {1, 2, 3, 4, 5}

if Set1 < Set2:

    print("Set1 is a strict subset of Set2")

else:

    print("Set1 is not a strict subset of Set2")


#Use a set comprehension to collect all squares of numbers from 1–15
#that are divisible by 3.
Squares = {x*x for x in range(1, 16) if x % 3 == 0}

print("Squares divisible by 3:", Squares)


#Count how many duplicate values exist in a list using sets.
Nums = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]

Duplicates = len(Nums) - len(set(Nums))

print("Number of duplicate values:", Duplicates)


#Write a program to remove all vowels from a string using a set.
Text = "Hello Python World"

Vowels = {'a', 'e', 'i', 'o', 'u'}

Result = ''.join(x for x in Text if x.lower() not in Vowels)

print("String without vowels:", Result)


#Find the symmetric difference between two sets.
Set1 = {1, 2, 3, 4, 5}
Set2 = {4, 5, 6, 7, 8}

Difference = Set1 ^ Set2

print("Symmetric difference:", Difference)


#Check if two strings are anagrams using set comparison
#(unique characters only).
String1 = "listen"
String2 = "silent"

if set(String1) == set(String2):

    print("Both strings are anagrams")

else:

    print("Strings are not anagrams")


#Part 4 Dictionary...
#Count word frequencies in a sentence and store the results in a dictionary.
Sentence = "python is easy and python is powerful"

Words = Sentence.split()

Frequency = {}

for word in Words:

    Frequency[word] = Frequency.get(word, 0) + 1

print("Word frequencies:", Frequency)


#Invert a dictionary where all values are unique.
Dict = {"a": 1, "b": 2, "c": 3}

Inverted = {}

for key, value in Dict.items():

    Inverted[value] = key

print("Original dictionary:", Dict)
print("Inverted dictionary:", Inverted)


#Merge two dictionaries where second dictionary overrides first.
Dict1 = {"a": 10, "b": 20, "c": 30}
Dict2 = {"b": 50, "d": 40}

Merged = {**Dict1, **Dict2}

print("Merged dictionary:", Merged)


#Group words by their first letter into a dictionary of lists.
Words = ["apple", "ant", "banana", "ball", "cat", "car"]

Grouped = {}

for word in Words:

    FirstLetter = word[0]

    Grouped.setdefault(FirstLetter, []).append(word)

print("Grouped words:", Grouped)


#Filter a dictionary to keep only entries with values greater than 50.
Marks = {
    "Ali": 45,
    "Ahmed": 75,
    "Zain": 90,
    "Usman": 40,
    "Hamza": 65
}

Filtered = {key: value for key, value in Marks.items() if value > 50}

print("Values greater than 50:", Filtered)


#Given a nested dictionary, safely access a deeply nested key.
Student = {
    "student": {
        "name": "Zain",
        "details": {
            "age": 22,
            "city": "Lahore"
        }
    }
}

City = Student.get("student", {}).get("details", {}).get("city")

print("City:", City)


#Write a dictionary comprehension that maps numbers 1–10 to their cubes.
Cubes = {x: x**3 for x in range(1, 11)}

print("Numbers and their cubes:", Cubes)


#Find the key with the highest value in a dictionary.
Marks = {
    "Ali": 75,
    "Ahmed": 88,
    "Zain": 95,
    "Usman": 82
}

Highest = max(Marks, key=Marks.get)

print("Key with highest value:", Highest)
print("Highest value:", Marks[Highest])


#Combine two lists into a dictionary.
Keys = ["Name", "Age", "City"]
Values = ["Zain", 22, "Lahore"]

Result = dict(zip(Keys, Values))

print("Dictionary:", Result)


#Remove all keys from a dictionary whose values are None.
Data = {
    "Name": "Zain",
    "Age": None,
    "City": "Lahore",
    "Phone": None,
    "Country": "Pakistan"
}

Result = {key: value for key, value in Data.items() if value is not None}

print("Dictionary without None values:", Result)