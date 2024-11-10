import numpy as np
import pandas as pd

np.random.seed(42)
data = np.random.randint(0, 101, size=(10, 3))
df = pd.DataFrame(data, columns=['Matematika', 'Kalkulus', 'Fisika'])

print("Data yang di hasilkan:", df)

print("\n5 Data Teratas:")
print(df.head())

print("\n5 Data Terbawah:")
print(df.tail())