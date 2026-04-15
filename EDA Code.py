# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df= pd.read_csv(r"C:\Users\Aryan Gupta\Downloads\SampleSuperstore.csv")
df.head(20)

#Basic Exploration
df.shape
df.columns
df.info()
df.describe()

# Checking Missing values
df.isnull().sum()

# Checking duplicates and removing duplicates
df.duplicated().sum()
df.drop_duplicates(inplace=True)

# Convert Columns names to lower case
df.columns=df.columns.str.lower()
df.columns

df.columns=df.columns.str.replace(' ','_')
df.head()

df.columns=df.columns.str.replace('-','_')
df.head()

# Sales Distribution
sns.histplot(df['sales'], bins=30)
plt.show()

# Profit Distribution
sns.histplot(df['profit'], bins=30)
plt.show()

# Category Analysis 
# Sales by Category
df.groupby('category')['sales'].sum().plot(kind='bar')
plt.show()

# Profit by Category
df.groupby('category')['profit'].sum().plot(kind='bar')
plt.show()

# Sub-Category Analysis
sub_profit = df.groupby('sub_category')['profit'].sum().sort_values()

sub_profit.plot(kind='barh', figsize=(10,8))
plt.show()

# Region Analysis
df.groupby('region')['sales'].sum().plot(kind='bar')
plt.show()

# State Analysis
state_profit = df.groupby('state')['profit'].sum().sort_values()

state_profit.tail(10).plot(kind='barh')
plt.show()

# Discount vs Profit
sns.scatterplot(x='discount', y='profit', data=df)
plt.show()

# Segment Analysis
df.groupby('segment')['sales'].sum().plot(kind='bar')
plt.show()

# Ship Mode Analysis
df.groupby('ship_mode')['sales'].sum().plot(kind='bar')
plt.show()

# Correlation Heatmap
sns.heatmap(df[['sales','profit','discount','quantity']].corr(), annot=True)
plt.show()
