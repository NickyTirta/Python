## Soal 1: Python list and Slicing
# List suhu dalam Celsius
temperatures = [25, 28, 30, 22, 35, 40, 18, 24]

# Tulis jawaban Anda di bawah ini
# 1. Konversi ke Fahrenheit menggunakan list comprehension
temp_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures]

# 2. Mengambil 3 data suhu terakhir
last_three = temp_fahrenheit[-3:]

# Menampilkan hasil
print("Suhu Fahrenheit:", temp_fahrenheit)
print("3 suhu terakhir:", last_three)
print("\n\n\n")


## Soal 2: Dictionary Operasi
inventory = {
    "laptop": {"stok": 10, "harga": 15000000},
    "mouse": {"stok": 50, "harga": 250000},
    "monitor": {"stok": 20, "harga": 3000000}
}

# Tulis jawaban Anda di bawah ini
# 1. Tambahkan produk baru: keyboard
inventory["keyboard"] = {"stok": 30, "harga": 500000}

# 2. Perbarui harga laptop menggunakan .update()
inventory["laptop"].update({"harga": 14500000})

# 3. Hitung total nilai aset gudang
total_aset = 0

for item in inventory.values():
    total_aset += item["stok"] * item["harga"]

print("Inventory:", inventory)
print("Total nilai aset:", total_aset)
print("\n\n\n")


## Soal 3: NumPy Array & Aggregation
import numpy as np

scores = np.array([
    [80, 85, 90],
    [70, 60, 75],
    [95, 90, 100],
    [40, 50, 45]
])

# Tulis jawaban Anda di bawah ini
# 1. Rata-rata setiap mahasiswa (baris)
avg_scores = np.mean(scores, axis=1)

# 2. Nilai tertinggi dari seluruh data
max_value = np.max(scores)

# 3. Label Lulus / Gagal menggunakan np.where
result = np.where(avg_scores >= 70, "Lulus", "Gagal")

print("Rata-rata tiap mahasiswa:", avg_scores)
print("Nilai tertinggi:", max_value)
print("Status:", result)
print("\n\n\n")



## Soal 4: Pandas DataFrame Manipulation
import pandas as pd
import numpy as np

# Data awal
df_data = {
    'Nama': ['Andi', 'Budi', 'Caca', 'Dedi', 'Euis'],
    'Departemen': ['IT', 'HR', 'IT', 'Sales', 'Sales'],
    'Gaji': [8000000, 7000000, 8500000, np.nan, 6000000],
    'Pengalaman_Tahun': [5, 3, 6, 2, 1]
}

df = pd.DataFrame(df_data)

# Tulis jawaban Anda di bawah ini
# 1. Isi NaN pada Gaji dengan median
median_gaji = df['Gaji'].median()
df['Gaji'] = df['Gaji'].fillna(median_gaji)

# 2. Kolom Kategori_Senioritas
df['Kategori_Senioritas'] = np.where(
    df['Pengalaman_Tahun'] > 4,
    'Senior',
    'Junior'
)

# 3. Rata-rata gaji per departemen
rata_gaji = df.groupby('Departemen')['Gaji'].mean()

print(df)
print("\nRata-rata Gaji per Departemen:")
print(rata_gaji)