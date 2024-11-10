import pandas as pd

data = {'buah': ['apel', 'pisang', 'anggur'],
        'jumlah': [10, 15, 20],
        'harga_per_buah': [2000, 1500, 3000]}
df = pd.DataFrame(data)

# Operasi aritmatika
total_penjualan = df['jumlah'] * df['harga_per_buah']
rata_rata_harga = df['harga_per_buah'].mean()
selisih_jumlah = df.loc[df['buah'] == 'apel', 'jumlah'] - df.loc[df['buah'] == 'pisang', 'jumlah'].values[0]

# Tampilkan hasil
print("Total Penjualan:\n", total_penjualan)
print("Rata-rata Harga:\n", rata_rata_harga)
print("Selisih Jumlah Apel dan Pisang:\n", selisih_jumlah)