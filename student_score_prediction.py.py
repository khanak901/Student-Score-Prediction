import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,root_mean_squared_error
import numpy as np

data = pd.read_csv("Sample_Short_Data_student.csv")

X = data[["Hours"]]
y=data["Score"]

model = LinearRegression()
model.fit(X,y)
predicted_Score = model.predict(X)

mae = mean_absolute_error(y, predicted_Score)
mse = mean_squared_error(y, predicted_Score)
rmse = root_mean_squared_error(y, predicted_Score)

print("MAE IS:",mae)#Mean Absolute error
print("MSE IS:",mse)#Mean Suqared Error
print("RMSE IS:",rmse)#Root Mean Squared Error

new_hour = float(input("Enter an hour: "))

new_pred = model.predict(
    pd.DataFrame([[new_hour]], columns=["Hours"])
)

print(f"Prediction for Studying {new_hour} is score = {new_pred[0]:.2f}")