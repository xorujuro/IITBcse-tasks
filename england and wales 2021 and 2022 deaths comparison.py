import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a DataFrame called 'df' with columns 'Week_number', 'Total_deaths_England_and_Wales_2021', and 'Total_deaths_England_and_Wales_2022'
# Replace 'your_dataset.csv' with the actual file or provide your data in another way

df = pd.read_csv('/content/deaths_covid.csv')

# Convert columns to float
df['Total_deaths_England_and_Wales_2021'] = df['Total_deaths_England_and_Wales_2021'].astype(str).str.replace(',', '').astype(float)
df['Total_deaths_England_and_Wales_2022'] = df['Total_deaths_England_and_Wales_2022'].str.replace(',', '').astype(float)

# Group by 'Week_number' and calculate the mean
mean_2021 = df.groupby('Week_number')['Total_deaths_England_and_Wales_2021'].mean()
mean_2022 = df.groupby('Week_number')['Total_deaths_England_and_Wales_2022'].mean()

# Plot the bar graph
plt.figure(figsize=(12, 6))
bar_width = 0.35
bar_positions_2021 = mean_2021.index - bar_width / 2
bar_positions_2022 = mean_2022.index + bar_width / 2

plt.bar(bar_positions_2021, mean_2021.values, width=bar_width, label='England and Wales 2021')
plt.bar(bar_positions_2022, mean_2022.values, width=bar_width, label='England and Wales 2022')

plt.title('Weekly Mean Total Deaths in England and Wales (2021 and 2022)')
plt.xlabel('Week Number')
plt.ylabel('Mean Total Deaths')
plt.legend()
plt.grid(True)
plt.show()
