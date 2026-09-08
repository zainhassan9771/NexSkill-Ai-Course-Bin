import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("Week6/FastFoodRestaurants.csv",delimiter=",",index_col="address")
print(df.dtypes)
dffilter=df.head(40)
dffilter100=df.head(100)
sns.set_theme(style="darkgrid")

g=sns.displot(data=dffilter,x="address",y="name")
g.figure.suptitle("sns.displot(data=dffilter,x=Address,y=name)")
g.figure.show()
read=input("Wait for me...")

g=sns.barplot(data=dffilter,x="address",y="keys")
g.figure.suptitle("sns.barplot(data=dffilter,x=address,y=keys)")
g.figure.show()
read=input("WAit for me...")

g=sns.catplot(data=dffilter,x="keys",y="name")
g.figure.suptitle("sns.catplot(data=dffilter,x=keys,y=name)")
g.figure.show()
read=input("WAit for me...")

g=sns.scatterplot(data=dffilter,x="latitude",y="name")
g.figure.suptitle("sns.scatterplot(data=dffilter,x=latitude,y=name)")
g.figure.show()
read=input("Wait for me...")

g=sns.boxplot(data=dffilter,x="latitude",y="name")
g.figure.suptitle("sns.boxplot(data=dffilter,x=latitude,y=name)")
g.figure.show()
read=input("wait for me...")

g=sns.histplot(data=dffilter,x="longitude",y="latitude")
g.figure.suptitle("sns.histplot(data=dffilter,x=longitude,y=latitude)")
g.figure.show()
read=input("Wait for me...")

sns.set_theme(style="darkgrid", rc={"axes.facecolor":"grey","grid.color":"white"})
sns.lineplot(x="x",y="y",data="data")
plt.show()
