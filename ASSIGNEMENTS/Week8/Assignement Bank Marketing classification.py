import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn .ensemble import RandomForestClassifier
import joblib

df=pd.read_csv("Week8/Bank_Marketing.csv")
feature=["age","job","marital","education","default","balance","housing","loan","contact","day","month","duration","campaign","pdays","previous","poutcome"]
raw_x=df[feature]
on=OrdinalEncoder()
X=on.fit_transform(raw_x)
y_raw=df["deposit"]

le=LabelEncoder()
Y=le.fit_transform(y_raw)
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
print(f"Train Size: {round((len(X_train)/len(X)) * 100)}%")
print(f"Train Test:{round((len(X_test)/len(X))*100)}%")

scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

svm=SVC(kernel="linear",C=10)
tree=DecisionTreeClassifier()
linear_model=LogisticRegression()
rdc=RandomForestClassifier()

svm.fit(X_train_scaled,y_train)
linear_model.fit(X_train_scaled,y_train)
tree.fit(X_train_scaled,y_train)
rdc.fit(X_train_scaled,y_train)

svm_predict=svm.predict(X_test_scaled)
linear_predict=linear_model.predict(X_test_scaled)
tree=tree.predict(X_test_scaled)
rdc_predict=rdc.predict(X_test_scaled)
model_preds = {
    "Logistic Regression": linear_predict,
    "Support Vector Machine": svm_predict,
    "Decision Tree": tree,
    "Random forest classifier":rdc_predict,
}
for model,preds in model_preds.items():
    print(f"{model} Results:\n{classification_report(y_test, preds)}", sep="\n\n")
