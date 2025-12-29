import pandas as pd
import numpy as np

# Generate synthetic retail data
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
data = {
    "Date": np.random.choice(dates, 1000),
    "Product_Category": np.random.choice(["Smartphones", "Laptops", "Audio", "Wearables"], 1000),
    "Region": np.random.choice(["North America", "Europe", "Asia", "LATAM"], 1000),
    "Sales": np.random.uniform(100, 1500, 1000).round(2),
    "Quantity": np.random.randint(1, 5, 1000)
}

df = pd.DataFrame(data)
df["Profit"] = (df["Sales"] * np.random.uniform(0.1, 0.3, 1000)).round(2)
df.to_csv("sales_data.csv", index=False)
print("Dataset 'sales_data.csv' created successfully!")