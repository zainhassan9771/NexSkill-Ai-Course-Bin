BookList=[328,"Think and gro rich","Zain",50.5]
print(BookList)
print(type(BookList))
print(len(BookList))
for x in BookList:
    print(x)

print(BookList[2])
print(type(BookList[2]))
print(BookList[3])
print(type(BookList[3]))

BookList.append("Husnain Shafiq")
print(BookList)
BookList.insert(1,2026)
print(BookList)
BookList.extend([2,5,"Red"])
print(BookList)
BookList.remove(50.5)
print(BookList)
BookList.pop(4)
print(BookList)