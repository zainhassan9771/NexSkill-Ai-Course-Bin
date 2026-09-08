import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("Week6/startup_growth_investment_data.csv",delimiter=",",index_col="Startup Name")
print(df.dtypes)
dffilter=df.head(40)
dffilter100=df.head(100)
sns.set_theme(style="whitegrid")

g=sns.displot(data=dffilter,x="Startup Name",y="Industry")
g.figure.suptitle("sns.displot(data=dffilter,x=Startup Name,y=Industry)")
g.figure.show()
read=input("Wait for me ...")

g=sns.catplot(data=dffilter,x="Industry",y="Country")
g.figure.suptitle("sns.catplot(data=dffilter,x=Industry,y=Country)")
g.figure.show()
read=input("Wait for me...")

g=sns.boxplot(data=dffilter,x="Startup Name",y="Industry")
g.figure.suptitle("sns.boxplot(data=dffilter,x=Startup Name,y=Industry)")
g.figure.show()
read=input("Wait for me ..")

g=sns.barplot(data=dffilter,x="Funding Rounds",y="Valuation(USD)")
g.figure.suptitle("sns.barplot(data=dffilter,x=Funding Rounds,y=Valuation(USD))")
g.figure.show()
read=input("Wait for me...")

g=sns.scatterplot(data=dffilter,x="Country",y="Year Founded")
g.figure.suptitle("sns.scatterplot(data=dffilter,x=Country,y=Year Founded)")
g.figure.show()
read=input("Wait for me...")

sns.set_theme(style="whitegrid",rc={"axes.facecolor":"grey","grid.color":"white"})
sns.lineplot(x="x",y="y",data="data")
plt.show()
