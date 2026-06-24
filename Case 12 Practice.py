List=[2,"zain",36.1,False]
print(List[0])
print(List[2])
print(List[1])
print(List[3])

print(type(List[1]))
print(type(List[2]))
print(type(List[0]))
print(type(List[3]))

a=[3,"Ali",37.2]
b=[5,"ahmad",20.7]
c=[6,"Azam",15.3]

print(a)
print(b)
print(c)

a=[5]
a.append(10)
print("After append Value :",a)

a.insert(1,4)
print("After insert Value :",a)

a.extend([5,10,15,20,25,30])
print("after extend value :",a)

a=[1,3,5,7,9]
a[1]=13
print("After replace Value",a)
a.remove (5)
print("After remove value :",a)
a.pop(2)
print("After pop value :",a)
del a [1]
print("After del:",a)
matrix=[[12,16,18],[22,24,26],[32,34,36]]
print(matrix[1],[2])