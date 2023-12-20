import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/deaths_covid.csv')

# Convert 'Total_deaths_England_2022' to float
df['Total_deaths_England_2022'] = df['Total_deaths_England_2022'].str.replace(',', '').astype(float)

# Convert 'Total_deaths_Wales_2022' to float
df['Total_deaths_Wales_2022'] = df['Total_deaths_Wales_2022'].astype(str).str.replace(',', '').astype(float)

# Group by 'Week_number' and calculate the mean
england_weekly_mean = df.groupby('Week_number')['Total_deaths_England_2022'].mean()
wales_weekly_mean = df.groupby('Week_number')['Total_deaths_Wales_2022'].mean()

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(england_weekly_mean.index, england_weekly_mean.values, marker='o', linestyle='-', color='b', label='England')
plt.plot(wales_weekly_mean.index, wales_weekly_mean.values, marker='o', linestyle='-', color='r', label='Wales')
plt.title('Weekly Mean Total Deaths in England and Wales (2022)')
plt.xlabel('Week Number')
plt.ylabel('Mean Total Deaths')
plt.legend()
plt.grid(True)
plt.show()

# Print the overall mean values
england_average = df['Total_deaths_England_2022'].mean()
wales_average = df['Total_deaths_Wales_2022'].mean()

print("England Average:", england_average)
print("Wales Average:", wales_average)
