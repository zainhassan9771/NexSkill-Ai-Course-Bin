Set={1,3,5,6,8}
print(Set)
print(type(Set))

NewSet={"Banana","Apple","Orange"}
print(NewSet)

StudentID={10,20,30,50,60,40}
print("Student ID :", StudentID)
VowelLetters={"a","e","i","o","u"}
print("Vowel Letters :", VowelLetters)

MixedSet={"a",103,"Apple",2.5}
print("Mixed Set :", MixedSet)

emptyset=set()
EmptyDictionary={}
print("Data type of Empty Set :",type(emptyset))
print("Data type of Empty Dictionary :",type(EmptyDictionary))
set= {1,3,5,66,7}
print("Set :",set)
set.add(2)
print("updated set :",set)

Set1={1,2,3,5,6}
Set2={4,7,8,9}
Set1.update(Set2)
print("Updated Set :",Set1)

Set3={"Ali","Asoi","Ary"}
print(Set3)
RemoveValue=Set3.discard("Ali")
print("Remove Value :",Set3)