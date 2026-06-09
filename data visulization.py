import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
df = pd.read_csv("superstore_sales.csv")

print(df.head())
df = pd.read_csv("superstore_sales.csv")

print(df.head())
df = pd.read_csv("superstore_sales.csv")

print(df.head())
region_sales = df.groupby('Region')['Sales'].sum().reset_index()

plt.figure(figsize=(8,5))

sns.barplot(
    data=region_sales,
    x='Region',
    y='Sales'
)

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()
category_profit = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(7,7))

plt.pie(
    category_profit,
    labels=category_profit.index,
    autopct='%1.1f%%'
)

plt.title("Profit Distribution by Category")

plt.show()
plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x='Sales',
    y='Profit',
    hue='Category',
    s=100
)

plt.title("Sales vs Profit")

plt.show()
category_sales = df.groupby('Category')['Sales'].sum().reset_index()

plt.figure(figsize=(8,5))

sns.barplot(
    data=category_sales,
    x='Category',
    y='Sales'
)

plt.title("Category-wise Sales")

plt.show()
fig, axes = plt.subplots(2, 2, figsize=(12,8))

# Sales by Region
sns.barplot(
    data=region_sales,
    x='Region',
    y='Sales',
    ax=axes[0,0]
)
axes[0,0].set_title("Sales by Region")

# Profit by Category
category_profit.plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=axes[0,1]
)

# Scatter Plot
sns.scatterplot(
    data=df,
    x='Sales',
    y='Profit',
    hue='Category',
    ax=axes[1,0]
)
axes[1,0].set_title("Sales vs Profit")

# Category Sales
sns.barplot(
    data=category_sales,
    x='Category',
    y='Sales',
    ax=axes[1,1]
)
axes[1,1].set_title("Category Sales")

plt.tight_layout()
plt.show()
