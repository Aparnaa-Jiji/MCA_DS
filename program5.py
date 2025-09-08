import matplotlib.pyplot as plt
import pandas as pd

#Read csv file
data = pd.read_csv("fruit_sales.csv")

#display bar chart
plt.figure(figsize=(10,10))
plt.bar(data["Fruits"],data["Sales"],color="blue",edgecolor="black")
plt.title("fruit_sales - Bar Chart")
plt.xlabel("Fruits")
plt.ylabel("Sales")
plt.show()

#display scatter plot
plt.figure(figsize=(10,10))
plt.scatter(data["Fruits"],data["Sales"],color="skyblue")
plt.title("fruit_sales - Scatter Chart")
plt.xlabel("Fruits")
plt.ylabel("Sales")
plt.show()