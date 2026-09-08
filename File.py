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
X = df[["rooms","square_meters","age","floor"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size = 0.2, random_state = 43)

model = LinearRegression()
model.fit(X_train, y_train)

Predict = model.predict(X_test)
while True:
    try:
        Rooms = int(input("    how much you have rooms: "))
        Square_meters = float(input("how much square_meters you have: "))
        Age = int(input("     how is old your house: "))
        Floor = int(input( "how much you have a floars: "))
    except Exception:
        print("you write something wrong")
User_data = pd.DataFrame(
[[Rooms, Square_meters, Age, Floor ]] ,columns = X.columns)
predicted_price = model.predict(User_data)
print(predicted_price)
