
import pandas as pd

df=pd.read_csv("Week6/FastFoodRestaurants.csv",delimiter=",")
print(df)

print("df - Data Types", df.dtypes)
print("df - info",df.info())

# display the last three rows
print("Last 3 rows=")
print(df.tail(3))

#Display the first three rows
print("First 3 rows :",df.head(3))

#Summary of Statistics of DataFrame using describe() method.
print("#Summary of Statistics of DataFrame using describe() method:",df.describe())

#Counting the rows and columns in DataFrame using shape().
print("#Counting the rows and columns in DataFrame using shape():",df.shape)
print()

# access the Name column
status=df["name"]
print("Access the Name Coloumn: df: ",status)
print()

#Access multiple coloumn
bed_bath=df[["city","province"]]
print("Multiple coloumn", bed_bath)
print()

#selecting a single row using .loc
second_row=df.loc[1]
print("Second Row :",second_row)
print()

#selecting multiple rows using .loc
MultipleRows=df.loc[[2,3]]
print("Multiple Rows :",MultipleRows)

#selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("Slice of rows :",second_row3)

#conditional selection of row using .loc
second_row4=df.loc[df["country"]=="US"]
print("Conditional row is :",second_row4)

#selecting a single coloumn using .loc
second_row5=df.loc[:1,"city"]
print("single coloumn is :",second_row5)

#Selecting multiple columns using .loc
second_row6=df.loc[:,["city","province"]]
print("Multiple coloumns are :",second_row6)

#Selecting a slice of columns using .loc
second_row7=df.loc[:1,"address":"name"]
print("Slicing colouns are :",second_row7)

#Combined row and column selection using .loc
second_row8=df.loc[df["province"]=="NY","city"]
print("Combined row and column selection :",second_row8)


print("Part 2 with using index coloumn Starts here:")

# Case 2 : using .loc with index_col - starts here
df_index_col=pd.read_csv("Week6/FastFoodRestaurants.csv",delimiter=",",index_col=("name"))

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

#Selecting a single row using .loc
SingleRow=df_index_col.loc["McDonald's"]
print("Selecting a single row :",SingleRow)

#Selecting multiple rows using .loc
MultipleRows2=df_index_col.loc[["Wendy's","Subway"]]
print(MultipleRows2)

#Selecting a slice of rows using .loc
SliceRow=df_index_col.iloc[0:5]
print(SliceRow)

#Conditional selection of rows using .loc
SelectionRow=df_index_col.loc[df_index_col["province"]=="NY"]
print("Conditional selection of rows using .loc")
print(SelectionRow)

#Selecting a single column using .loc
SingleColoumn=df_index_col.loc[:,"city"]
print("Selecting a single column using .loc")
print(SingleColoumn)

#Selecting multiple columns using .loc
MultipleColoumns=df_index_col.loc[:,["city","province"]]
print("Selecting multiple columns using .loc")
print(MultipleColoumns)

#Selecting a slice of columns using .loc
SliceColoumn=df_index_col.loc[:,"address":"name"]
print("Selecting a slice of columns using .loc")
print(SliceColoumn)

#Combined row and column selection using .loc
Combined=df_index_col.loc[df_index_col["province"]=="CA","city":"postalCode"]
print("Combined row and column selection using .loc")
print(Combined)


#Case 3 .iloc Starts Here.....

#Selecting a single row using .iloc
SingleRow=df_index_col.iloc[0]
print("Selecting a single row using .iloc")
print(SingleRow)

#Selecting multiple rows using .iloc
MultipleRows = df_index_col.iloc[[1,3,5]]
print("Selecting multiple rows using .iloc")
print(MultipleRows)

#Selecting a slice of rows using .iloc
SliceRow = df_index_col.iloc[2:5]
print("Selecting a slice of rows using .iloc")
print(SliceRow)

#Selecting a single column using .iloc
SingleColoumn = df_index_col.iloc[:,2]
print("Selecting a single column using .iloc")
print(SingleColoumn)

#Selecting multiple columns using .iloc
MultipleColoumns = df_index_col.iloc[:,[2,4]]
print("Selecting multiple columns using .iloc")
print(MultipleColoumns)

#Selecting a slice of columns using .iloc
SliceColoumn = df_index_col.iloc[:,2:4]
print("Selecting a slice of columns using .iloc")
print(SliceColoumn)

#Combined row and column selection using .iloc
RowAndColoumn= df_index_col.iloc[[1,3,5],2:4]
print("Combined row and column selection using .iloc")
print(RowAndColoumn)


#Add a New Row to a Pandas DataFrame
df.loc[len(df.index)]= [
    "100 Main Street",
    "Lahore",
    "PK",
    "pk/punjab/lahore/100mainstreet",
    31.5204,
    74.3587,
    "New Restaurant",
    "54000",
    "Punjab",
    "http://example.com"
]

print("Modified Dataframe")
print(df)

# delete row with index 1
df.drop(1, axis=0, inplace=True)
print("Delete Row =")
print(df)

# delete row with index 2
df.drop(index=2, inplace=True)
print(df)

# delete rows with index 3 and 5
df.drop([3,5], axis=0, inplace=True)
print(df)

# delete websites column
df.drop("websites",axis=1,inplace=True)
print(df)

#delete address and keys coloumn
df.drop(["address","keys"], axis=1, inplace=True)
print(df)

#Rename Labels in a DataFrame
#Rename column name to restaurant_name
df.rename(columns={"name":"restaurant_name"},inplace=True)
print(df)
