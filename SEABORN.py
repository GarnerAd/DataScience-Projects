import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the CSV file
df = pd.read_csv('Cars93.csv')

# Box plot for revs per mile for selected manufacturers
plt.figure(figsize=(10, 6))
sns.boxplot(x='Manufacturer', y='Rev.per.mile', data=df[df['Manufacturer'].isin(['Audi', 'Hyundai', 'Suzuki', 'Toyota'])])
plt.title('Revs per Mile for Selected Manufacturers')
plt.xlabel('Manufacturer')
plt.ylabel('Revs per Mile')
plt.show()

# Histogram of MPG in the city and on the highway
plt.figure(figsize=(10, 6))
sns.histplot(df['MPG.city'], color='skyblue', label='MPG in City', kde=True)
sns.histplot(df['MPG.highway'], color='salmon', label='MPG on Highway', kde=True)
plt.title('Histogram of MPG in City vs. on Highway')
plt.xlabel('MPG')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# Line plot showing the relationship between Wheelbase and Turning circle
plt.figure(figsize=(10, 6))
sns.lineplot(x='Wheelbase', y='Turn.circle', data=df)
plt.title('Relationship between Wheelbase and Turning Circle')
plt.xlabel('Wheelbase')
plt.ylabel('Turning Circle')
plt.show()

# Bar plot showing the mean horsepower for each car Type
plt.figure(figsize=(10, 6))
sns.barplot(x='Type', y='Horsepower', data=df, estimator=pd.Series.mean)
plt.title('Mean Horsepower for Each Car Type')
plt.xlabel('Car Type')
plt.ylabel('Mean Horsepower')
plt.show()
