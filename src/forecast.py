


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor


dates = pd.date_range(
    start="2024-01-07",
    end="2025-12-28",
    freq="W"
)
#len(dates)


products = [f"Product_{i:03d}" for i in range(1, 11)]


df = pd.MultiIndex.from_product(
    [dates, products],
    names=["Date", "Product"]
).to_frame(index=False)

df.head(10)
#print(df.head(10))
df.shape
#print(df.shape)

np.random.seed(42)

base_demand = {
    product: np.random.randint(80, 500)
    for product in products
}

df["Week_Number"] = df.groupby("Product").cumcount()

trend = 1 + 0.002 * df["Week_Number"]

seasonality = 1 + 0.15 * np.sin(
    2 * np.pi * df["Week_Number"] / 52
)

noise = np.random.normal(
    loc=0,
    scale=20,
    size=len(df)
)

df["Demand"] = (
    df["Product"].map(base_demand)
    * trend
    * seasonality
    + noise
)

df["Demand"] = df["Demand"].round().clip(lower=0)


product_data = df[df["Product"] == "Product_001"]

plt.figure(figsize=(12, 5))

plt.plot(
    product_data["Date"],
    product_data["Demand"]
)

plt.title("Demand – Product_001")
plt.xlabel("Date")
plt.ylabel("Demand")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


df["Promotion"] = np.random.choice(
    [0, 1],
    size=len(df),
    p=[0.85, 0.15]
)


df["Demand"] = (
    df["Demand"]
    * (1 + 0.30 * df["Promotion"])
).round()


df["Price"] = np.random.choice(
    [79, 89, 99, 109, 119],
    size=len(df)
)

df.to_csv(
    r"C:\Users\erik_\Desktop\Demand_Forecasting\dataset\raw\demand_data.csv",
    index=False
)