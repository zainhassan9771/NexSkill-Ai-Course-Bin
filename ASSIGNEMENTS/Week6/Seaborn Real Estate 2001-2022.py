import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("Week6/Real_Estate_Sales_2001-2022_GL-Short.csv",delimiter=",",index_col="Serial Number")
print(df.dtypes)
dffilter=df.head(40)
dffilter100=df.head(100)
sns.set_theme(style="darkgrid")

g=sns.displot(data=dffilter,x="List Year",y="Address")
g.figure.suptitle("sns.displot(data=dffilter,x=List Year,y=Address)")
g.figure.show()
read=input("Wait for me ...")

g=sns.kdeplot(data=dffilter,x="List Year",y="Sale Amount")
g.figure.suptitle("sns.kdeplot(data=dffilter,x=List Year,y=Sale Amount)")
g.figure.show()
read=input("Wait for me...")

g=sns.histplot(data=dffilter,x="List Year",y="Address")
g.figure.suptitle("sns.histplot(data=dffilter,x=List Year,y=Address)")
g.figure.show()
read=input("Wait for me...")

g=sns.barplot(data=dffilter,x="List Year",y="Sale Amount")
g.figure.suptitle("sns.barplot(data=dffilter,x=List Year,y=Sale Amount)")
g.figure.show()
read=input("Wait for me....")

g=sns.boxplot(data=dffilter,x="List Year",y="Address")
g.figure.suptitle("sns.boxplot(data=dffilter,x=List Year,y=Address)")
g.figure.show()
read=input("Wait for me...")

g=sns.scatterplot(data=dffilter,x="Sale Amount",y="Address")
g.figure.suptitle("sns.scatterplot(data=dffilter,x=Sale Amount,y=Address)")
g.figure.show()
read=input("Wait for me....")

glue=dffilter.pivot(columns="List Year",values="Sale Amount")
g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue) - glue=dffilter.pivot(columns=List Year, values=Sale Amoount)")
g.figure.show()
read=input("Wait for me....")

