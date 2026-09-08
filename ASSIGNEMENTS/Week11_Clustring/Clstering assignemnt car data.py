import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df=pd.read_csv("Week11/car_data.csv")
X=df[["Present_Price", "Kms_Driven"]].values
df=df.dropna()
plt.figure(figsize=(7.5,3.5))
plt.scatter(X[:,0],X[:,1],s=20)
plt.show()

KMeans=KMeans(n_clusters=3,max_iter=300,random_state=42)
KMeans.fit(X)

plt.figure(figsize=(7.5,3.5))
plt.scatter(X[:,0], X[:,1], c=KMeans.labels_, s=20, cmap='summer')
plt.scatter(KMeans.cluster_centers_[:,0], KMeans.cluster_centers_[:,1],
marker='x', c='r', s=50, alpha=0.9)
plt.show()
