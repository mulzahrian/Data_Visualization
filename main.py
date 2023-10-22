import pandas as pd
import matplotlib.pyplot as plt

# Membaca file CSV
df = pd.read_csv('csv/bike_share.csv')

# Menampilkan 5 baris pertama data
print(df.head())


plt.hist(df['temp'], bins=20, edgecolor='k')
plt.title('Distribusi Suhu')
plt.xlabel('Suhu (Celsius)')
plt.ylabel('Jumlah Data')
plt.show()


