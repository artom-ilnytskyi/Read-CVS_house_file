import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

csv_content = """rooms,square_meters,age,floor,price
1,35.5,5,3,45000
2,62.0,12,5,78000
3,89.3,2,8,125000
1,40.2,25,2,38000
2,55.0,1,12,90000
3,78.5,8,4,110000
1,29.0,40,1,28000
2,48.0,15,9,65000
4,120.0,3,2,210000
2,60.5,6,14,85000"""

with open("house_prices.csv", "w") as f:
    f.write(csv_content)

df = pd.read_csv("house_prices.csv")
X = df[["rooms", "square_meters", "age", "floor"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
House_rooms = input("how much rooms?: ")
House_meters = input("how much meters²: ")
House_age = input("  how much age: ")
House_floor = input("how much floors: ")
Your_house =[House_rooms, House_meters, House_age, House_floor]
Your_house =["rooms, square_meters, age"]
