import pandas as pd
import matplotlib.pyplot as plt


file_path = '/content/death_data_england .csv'
df = pd.read_csv(file_path)


columns_of_interest = ['Week_number', 'Total_deaths_England_and_Wales_2022', 'Total_deaths_England_and_Wales_2021']
df_selected = df[columns_of_interest]


grouped_data = df_selected.groupby('Week_number').sum()


plt.figure(figsize=(12, 6))
bar_width = 0.35
bar_positions_2022 = grouped_data.index
bar_positions_2021 = bar_positions_2022 + bar_width

plt.bar(bar_positions_2022, grouped_data['Total_deaths_England_and_Wales_2022'], width=bar_width, label='Total deaths 2022')
plt.bar(bar_positions_2021, grouped_data['Total_deaths_England_and_Wales_2021'], width=bar_width, label='Total deaths 2021')

plt.xlabel('Week number')
plt.ylabel('Total deaths')
plt.title('Comparison of Total Deaths in England and Wales (2021 vs 2022)')
plt.legend()
plt.grid(True)
plt.show()
