import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("Week6/RealEstate-USA.csv", delimiter=",",index_col="brokered_by")
print(df.dtypes)
dffilter=df.head(40)
dffilter100=df.head(100)
sns.set_theme(style="whitegrid")

g=sns.displot(data=dffilter, x="price",y="city")
g.figure.suptitle("sns.displot(data=dffilter, x=price , y=city)")
g.figure.show()
read=input("Wait for me....")

g=sns.kdeplot(data=dffilter, x="price",y="zip_code")
g.figure.suptitle("sns.kdeplot(data=dffilter,x=price ,y=zip_code)")
g.figure.show()
read=input("Wait for me...")

g=sns.histplot(data=dffilter,x="price",y="bed")
g.figure.suptitle("sns.histplot(data=dffilter,x=price,y=bed)")
g.figure.show()
read=input("wait for me..")

g=sns.barplot(data=dffilter,x="price",y="bath")
g.figure.suptitle("sns.barplot(data=dffilter,x=price,y=bath)")
g.figure.show()
read=input("Wait for me...")

g=sns.boxplot(data=dffilter,x="price",y="street")
g.figure.suptitle("sns.boxplot(data=dffilter,x=price,y=street)")
g.figure.show()
read=input("wait for me...")

g=sns.scatterplot(data=dffilter,x="price",y="zip_code")
g.figure.suptitle("sns.scatterplot(data=dffilter,x=price ,y=zip_code)")
g.figure.show()
read=input("Wait for me ....")

g=sns.catplot(data=dffilter,x="price",y="status")
g.figure.suptitle("sns.catplot(data=dffilter,x=price,y=status)")
g.figure.show()
read=input("Wait for me ...")

g=sns.JointGrid(data=dffilter,x="price",y="street")
g.figure.suptitle("sns.JointGrid (data=dffilter,x=price,y=street)")
g.figure.show()
read=input("Wait for me...")

