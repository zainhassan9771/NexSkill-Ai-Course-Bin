import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
import joblib

df=pd.read_csv("Week8/Iris_Species.csv")
feature = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
X=df[feature]
y_raw = df['Species']

le=LabelEncoder()
Y=le.fit_transform(y_raw)

X_train,X_Test,Y_Train,Y_Test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
print(f"Train Size: {round((len(X_train)/len(X)) * 100)}%")
print(f"Test Size: {round((len(Y_Test)/len(Y)) * 100)}%")

scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_Test_scaled=scaler.transform(X_Test)

svm=SVC(kernel='linear', C=10)
tree=DecisionTreeClassifier()
liner_model=LogisticRegression()
rdc=RandomForestClassifier()

svm.fit(X_train_scaled,Y_Train)
liner_model.fit(X_train_scaled,Y_Train)
tree.fit(X_train_scaled,Y_Train)
rdc.fit(X_train_scaled,Y_Train)

svm_predict=svm.predict(X_Test_scaled)
liner_predict=liner_model.predict(X_Test_scaled)
tree_predict=tree.predict(X_Test_scaled)
random_rdc=rdc.predict(X_Test_scaled)

model_preds = {
    "Logistic Regression": liner_predict,
    "Support Vector Machine": svm_predict,
    "Decision Tree": tree_predict,
    "Random forest classifier":random_rdc
}

for model, preds in model_preds.items():
    print(f"{model} Results:\n{classification_report(Y_Test, preds)}", sep="\n\n")