import pandas as pd
df=pd.read_csv("Week6/Real_Estate_Sales_2001-2022_GL-Short.csv",delimiter=",")
print(df)
print('Data type of Dataframe =',df.dtypes)
print("Info of Dataframe =",df.info())

# Print Last three rows
print("Last three Rows =",df.tail(3))

# Print First three rows 
print("First three rows =",df.head(3))

# Summary of Statistic of Dataframe using describe() method 
print("Summary of Statistic of Dataframe =",df.describe())

# Counting the rows and columns of Dataframe by using shape() method
print("Counting the rows and columns of Dataframe =",df.shape)

# Access the column by name 
print("Access the column by using name =",df["List Year"])

# Access Multiple columns by name
print("Access Mjltiple columns =",df[["Date Recorded","Assessed Value"]])

# Selecting a single row by using .loc
print("Selecting a single row by using .loc =",df.loc[0])

# Selecting multiple rows by using .loc
print("Selecting Multiple rows by using .loc =",df.loc[[1,2]])

# Conditional selection of rows using .loc
print("Conditional selectin of rows using .loc =",df.loc[df["Town"]=="Beacon"])

# Selecting a single column using .loc
print("Selecting a single column using .loc =",df.loc[:7,'List Year'])

# Selecting multiple columns using .loc
print("Selecting multiple columns using .loc =",df.loc[:10,["Date Recorded","Town"]])

# Selecting a slice of columns using .loc
print("Selecting a slice of columns using .loc =",df.loc[:,"List Year":"Assessed Value"])

# Combined row and column selection using .loc
print("Combined rows and column selection using .loc =",df.loc[df["Town"]=="Beacon","Property Type"])

# Taking index column
df_index_col=pd.read_csv("Week6/Real_Estate_Sales_2001-2022_GL-Short.csv",delimiter=",",index_col="Serial Number")
print(df_index_col)
print("Data type of df_index_col",df_index_col.dtypes)
print("Info of df_index_col =",df_index_col.info())

# Selecting a single row using .loc
print("Selecting a single row by index_column =",df_index_col.loc[2020225])

# Selecting multiple rows using .loc
print("Selecting a multiple by index_column =",df_index_col.loc[[20058,2020360]])

# Selecting a slice of rows using .loc
print("Selecting a slice of rows by index_column =",df_index_col.loc[200008:200483])

# Conditional selection of rows using .loc
print("Conditional selection of rows using .loc =",df_index_col.loc[df_index_col["Town"]=="Barkhamsted"])

# Selecting a single column using .loc
print("Selecting a single column using .loc =",df_index_col.loc[:200483,"Address"])

# Selecting multiple columns using .loc
print("Selectiong multiple columns using .loc =",df_index_col.loc[:200016,["Town","List Year"]])

# Selecting a slice of columns using .loc
print("Selecting a slice of columns using .loc =",df_index_col.loc[:20058,"List Year":"Address"])

# Combined row and column selection using .loc
print("Combined rows and columns using .loc =",df_index_col.loc[df_index_col["List Year"]==2023,"Assessed Value"])

# Selecting a single row using .iloc
print('Selecting a single row using .iloc =',df_index_col.iloc[0])

# Selecting multiple rows using .iloc
print("Selecting multiple rows using .iloc =",df_index_col.iloc[[1,2]])

# Selecting a slice of rows using .iloc
print("Selecting a slice of rows using .iloc =",df_index_col.iloc[3:7])

# Selecting a single column using .iloc
print("Selecting a single column usiing .iloc =",df_index_col.iloc[:,1])

# Selecting multiple columns using .iloc
print("Selecting multiple columns using .iloc =",df_index_col.iloc[:,[2,6]])

# Selecting a slice of columns using .iloc
print("Selecting a slice of columns using .iloc =",df_index_col.iloc[:,1:4])

# Combined row and column selection using .iloc
print("Combining row and column using .iloc =",df_index_col.iloc[[2,3,4],2:4])

#Add a New Row to a Pandas DataFrame
# add a new row
df.loc[len(df.index)]=[2020090,2020,12/14/2020,"Ansonia","57 PLATT ST",127400.00,202500.00,0.6291,"Residential","Two Family","awais",33,89,344]
print(df)

# Remove Rows from a Pandas DataFrame using drop with axis
df.drop(40,axis=0,inplace=True)
df.drop(index=41,inplace=True)

# Remove Multiple Rows using drop with axis
df.drop([66,65],axis=0,inplace=True)
print("After removing multiple rows",df)

# Delete Columns from a pandas DataFrame using drop
df.drop("Location",axis=1,inplace=True)
df.drop(columns="OPM remarks",inplace=True)

# Delete Multiple columns using drop
df.drop(["Assessor Remarks","Non Use Code"],axis=1,inplace=True)
print("After removing multiple columns =",df)

# Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns={"Residential Type":"Residential_types"},inplace=True)
# rename multiple columns
df.rename(mapper={"Property Type":"Type_of_property","Sales Ratio":"Ratio_of_sales"},axis=1,inplace=True)
print(df)

#Example: Rename Row Labels
# rename row one index label
df.rename(index={200183:545454},inplace=True)
# remane multiple rows by index
df.rename(mapper={200111:2020202020,200183:94949494},axis=0,inplace=True)

# query() to Select Data
# The query() method in Pandas allows you to select data using a more SQL-like syntax.
# for example : select the rows where the age is greater than 25
Selection_row=df.query("Town== 'Barkhamsted' or 'Address'=='323 BEAVER ST' ")
print(Selection_row.to_string())
print(len(Selection_row))

# sort DataFrame by Funding Rounds in ascending order
sorted_value=df.sort_values(by="Sale Amount")
print(sorted_value.to_string(index=False))
print(sorted_value)

# sorted Dataframe by Funding Rounds and Country_Name
sorted_df=df.sort_values(by=["Assessed Value","Date Recorded"])
print(sorted_df.to_string(index=False))
print(sorted_df)

#Pandas groupby
# In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.
# group the DataFrame by the location_id column and
# calculate the sum of price for each category

grouped_df=df.groupby("Town")["Sale Amount"].sum()
print(grouped_df.to_string())
print(len(grouped_df))

# use dropna() to remove rows with any missing values
cleaned_data=df.dropna()
print("Cleaned Data: \n",cleaned_data)

# filling NaN values with '0'
text_cols=df.select_dtypes(include=['object','string']).columns
df[text_cols]=df[text_cols].fillna("missing")

num_cols=df.select_dtypes(include=['number']).columns
df[num_cols]=df[num_cols].fillna(0)

# create a list named data
data=[1,2,3,5]
array1=pd.array(data)
print(array1)

# creating a pandas.array of integers
int_array=pd.array([1,2,5,7,8],dtype="int")
print(int_array)