import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv("data_urban-growth-HW2.csv")
X = data[['Distance to Highways', 'Distance to Major Roads', 'Slope',
          'Distance to CBD', 'Distance to MIDC', 'Distance to Stations',
          'Distance to Hospitals', 'Distance to Airport']]
y = data['Built-up']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

selected_features_model1 = ['Distance to Highways', 'Slope', 'Distance to CBD']
X_train_model1 = X_train[selected_features_model1]
X_val_model1 = X_val[selected_features_model1]

model1 = LogisticRegression()
model1.fit(X_train_model1, y_train)
y_pred1 = model1.predict(X_val_model1)
accuracy1 = accuracy_score(y_val, y_pred1)

print("Logistic Regression Model 1 Accuracy:", accuracy1)

selected_features_model2 = ['Distance to Major Roads', 'Slope', 'Distance to MIDC']
X_train_model2 = X_train[selected_features_model2]
X_val_model2 = X_val[selected_features_model2]

model2 = LogisticRegression()
model2.fit(X_train_model2, y_train)
y_pred2 = model2.predict(X_val_model2)
accuracy2 = accuracy_score(y_val, y_pred2)

print("Logistic Regression Model 2 Accuracy:", accuracy2)

if accuracy1 > accuracy2:
    print("Model 1 outperforms Model 2.")
elif accuracy1 < accuracy2:
    print("Model 2 outperforms Model 1.")
else:
    print("Model 1 and Model 2 have the same accuracy.")