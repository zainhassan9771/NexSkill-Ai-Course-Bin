import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso,LinearRegression,Ridge
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from sklearn.ensemble import RandomForestRegressor

df=pd.read_csv("Week11/StudentsPerformance.csv")
Y=df["math score"]
X=df.drop("math score",axis=1)

Oe=OrdinalEncoder()
X[["gender", "race/ethnicity", "parental level of education","lunch", "test preparation course"]]=Oe.fit_transform(X[["gender", "race/ethnicity", "parental level of education","lunch", "test preparation course"]]
)

X_train,X_Test,Y_train,Y_Test=train_test_split(X,Y,test_size=0.2,random_state=42)
print(f"Train Size: {round((len(X_train)/len(X)) * 100)}%")
print(f"Test Size: {round((len(Y_Test)/len(Y)) * 100)}%")

scaler=StandardScaler()
X_Train_Scaled=scaler.fit_transform(X_train)
X_Test_Scaled=scaler.transform(X_Test)

linear_model = LinearRegression()
nn_model = MLPRegressor(hidden_layer_sizes=(100, 50),activation="relu",alpha=0.01,learning_rate_init=0.001,max_iter=1000,early_stopping=True,random_state=42)
tree_model = DecisionTreeRegressor(max_depth=9, min_samples_split=15, min_samples_leaf=5, random_state=42)
lasso_model = Lasso(alpha=0.1, max_iter=2000, random_state=42)
ridge_model = Ridge(alpha=100.0, random_state=42)
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

linear_model.fit(X_Train_Scaled,Y_train)
nn_model.fit(X_Train_Scaled,Y_train)
lasso_model.fit(X_Train_Scaled,Y_train)
ridge_model.fit(X_Train_Scaled,Y_train)
tree_model.fit(X_Train_Scaled,Y_train)
rf_model.fit(X_Train_Scaled, Y_train)

linear_predict=linear_model.predict(X_Test_Scaled)
nn_model_predict=nn_model.predict(X_Test_Scaled)
lasso_model_predict=lasso_model.predict(X_Test_Scaled)
ridge_model_predict=ridge_model.predict(X_Test_Scaled)
tree_model_predict=tree_model.predict(X_Test_Scaled)
rf_predict = rf_model.predict(X_Test_Scaled)

print("1. Linear Regression R2:", r2_score(Y_Test, linear_predict))
print("2. Neural Network Regression R2:", r2_score(Y_Test, nn_model_predict))
print("3. Decision Tree Regression R2:", r2_score(Y_Test, tree_model_predict))
print("4. Lasso Regression R2:", r2_score(Y_Test, lasso_model_predict))
print("5. Ridge Regression R2:", r2_score(Y_Test, ridge_model_predict))
print("6. Random Forest R2:", r2_score(Y_Test, rf_predict))


