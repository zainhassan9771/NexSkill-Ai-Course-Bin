#Part 1 List
#Create a list nums = [3, 1, 4, 1, 5] and print the first and last elements.
Numbers=[3,1,4,1,5]
print("First Element :",Numbers[0])
print("Last Element :",Numbers[-1])

#Find the length of the list colors = ['red', 'blue', 'green'].
Colours=["Red", "Blue", "Green"]
print(len(Colours))

#Append 'yellow' to the list colors = ['red', 'blue']
Colours=["Red", "Blue"]
Colours.append("Yellow")
print(Colours)

#Insert 'orange' at index 1 in fruits = ['apple', 'banana'].
Fruits= ["Apple", "Banana"]
Fruits.insert(1,"Orange")
print(Fruits)

# Remove 'banana' from fruits = ['apple', 'banana', 'grapes'].
Fruits=["Apple", "Banana", "Grapes"]
Fruits.remove("Banana")
print(Fruits)

#Pop the last element from items = [10, 20, 30] and print the popped value.
Items=[10,20,30]
PoppedValue=Items.pop()
print("Popped Value :",PoppedValue)

#Check if 3 is in the list nums = [1, 2, 3, 4].
Numbers=[1,2,3,4]
if 3 in Numbers:
    print("3 in the list.")
else:
    print("3 not in the list")

#Print the slice [2, 3] from the list [0, 1, 2, 3, 4].
List=[0,1,2,3,4]
print(List[2:4]) 

#Replace the element at index 1 in a = [5, 10, 15] with 12.
List=[5,10,15]
List[1]=12
print(List)

# Count how many times 2 appears in [1, 2, 2, 3, 2].
List=[1,2,2,3,2]
Count=List.count(2)
print(Count)



#Part 2 Tuple
#Create a tuple t = (10, 20, 30) and print the second element.
Tuple=(10,20,30)
print(Tuple[1])

#Find the length of tuple ('a', 'b', 'c').
Touple=("a","b","c")
print(len(Touple))

#Unpack the tuple (4, 5) into variables x and y.
Tuple=(4,5)
x,y = Tuple
print("x",x)
print("y",y)

#Check if 'b' is in the tuple ('a', 'b', 'c')
Tuple=("a","b","c")
if "b" in Tuple:
    print("Touple is correct.")
else:
    print("Not Correct.")

#Create an empty tuple and print its type.
Tuple=()
print(type(Tuple))

#Concatenate (1, 2) and (3, 4) into a new tuple.
Tuple1=(1,2)
Tuple2=(3,4)
NewTuple=Tuple1+Tuple2
print(NewTuple)

#Repeat (7,) three times.
Tuple=(7,)
NewTuple=Tuple*3
print(NewTuple)

#Find the index of 2 in (1, 2, 3, 2).
Tuple=(1,2,3,2)
print(Tuple[2])

#Count how many times 2 appears in (1, 2, 3, 2).
Tuple=(1,2,3,2)
Count=Tuple.count(2)
print(Count)

#Create a single‑ element tuple containing the value 5
Tuple=(5,)
print(Tuple)



#Part 3 Set
#Create a set from [1, 2, 2, 3] and print it.
Numbers=[1,2,2,3]
NewSet=set(Numbers)
print(NewSet)

#Add element 4 to the set {1, 2, 3}.
Numbers={1,2,3}
Numbers.add(4)
print(Numbers)

#Remove element 2 from the set {1, 2, 3}.
Numbers={1,2,3}
Numbers.remove(2)
print(Numbers)

#Check if 5 is in the set {1, 3, 5}
Numbers={1,3,5}
if 5 in Numbers:
    print("Set is complete.")
else:
    print("Not Complete.")


#Find the length of set {10, 20, 30}.
Set={10,20,30}
print(len(Set))

#Clear all elements from the set {1, 2, 3}.
Set={1,2,3}
Set.clear()
print(Set)

#Create a set {'a', 'b'} and add 'c' only if it’s missing.
Set={"a","b"}
if "c" not in Set:
    Set.add("c")
    print(Set)

#Convert list ['a', 'a', 'b'] into a set to remove duplicates.
List=["a","a","b"]
MySet=set(List)
print(MySet)

#Create two sets and print their union
Set1={1,2,3,4}
Set2={3,4,5,6}
print(Set1.union(Set2))

#Create two sets and print their intersection.
Set1={1,4,6,8,7}
Set2={2,5,7,8}
print(Set1.intersection(Set2))


#Part 4 Dictionary
#Create a dictionary {'name': 'Ali', 'age': 25} and print the name.
Dictionary={"Name":"Ali","Age":"25"}
print(Dictionary["Name"])

#Add key 'city': 'Lahore' to a dictionary.
Dictionary["City"]="Lahore"
print(Dictionary)

#Change 'age' in {'name': 'Ali', 'age': 25} to 30.
Dictionary={"Name":"Ali","Age":25}
Dictionary["Age"]=30
print(Dictionary)

#Delete key 'age' from a dictionary.
Dictionary={"Name":"Ali","Age":25}
del Dictionary["Age"]
print(Dictionary)

#Check if key 'salary' exists in a dictionary
if "Salary" in Dictionary:
    print("Salary exist.")
else:
    print("Not exist.")

#Print all keys from {'a': 1, 'b': 2}.
Dictionary={"a":1,"b":2}
for key in Dictionary:
    print(key)

#Print all values from a dictionary
for values in Dictionary.values():
    print(values)    

#Iterate and print key‑ value pairs from {'x': 10, 'y': 20}.
Dictionary= {"x": 10, "y": 20}
for key, value in Dictionary.items():
    print(key, value)

#Use get() to safely read key 'score' from an empty dictionary.
Dictionary={}
Score=Dictionary.get("Score")
print("Score")

# Create a dictionary from two lists: keys = ['a','b'], values = [1,2]
Key=["a","b"]
Values=[1,2]
Dictionary=dict(zip(Key,Values))
print(Dictionary)
