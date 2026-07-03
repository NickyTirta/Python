<div align="center">

# 📊 Customer Personality Analysis
## K-Means Clustering for Customer Segmentation

**Ujian Akhir Semester (UAS) Data Mining**

Mengelompokkan pelanggan berdasarkan karakteristik demografi dan perilaku pembelian menggunakan algoritma **K-Means Clustering**.

---

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.x-blue?logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange?logo=scikitlearn)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![VS Code](https://img.shields.io/badge/VS_Code-Editor-blue?logo=visualstudiocode)

</div>

---

# 📖 Table of Contents

- Project Overview
- Dataset
- Objectives
- Workflow
- Technologies
- Project Structure
- Data Preprocessing
- Clustering Process
- Results
- Cluster Analysis
- How to Run
- References

---

# 📌 Project Overview

Customer segmentation merupakan salah satu penerapan Data Mining yang bertujuan untuk mengelompokkan pelanggan berdasarkan karakteristik yang dimiliki.

Pada proyek ini dilakukan proses:

- Data Cleaning
- Data Preprocessing
- Feature Engineering
- Data Transformation
- K-Means Clustering
- Cluster Evaluation
- Cluster Visualization

Dataset yang digunakan adalah **Customer Personality Analysis** dari Kaggle.

---

# 📂 Dataset

| Item | Value |
|------|------|
| Dataset | Customer Personality Analysis |
| Source | Kaggle |
| Total Records | 2240 |
| Total Features | 29 |
| Learning Type | Unsupervised Learning |
| Algorithm | K-Means |

---

# 🎯 Objectives

Project ini bertujuan untuk:

✅ Membersihkan dataset

✅ Menangani missing value

✅ Melakukan Feature Engineering

✅ Mengubah data kategorikal menjadi numerik

✅ Melakukan standardisasi data

✅ Menentukan jumlah cluster terbaik

✅ Mengelompokkan pelanggan

✅ Mengevaluasi kualitas cluster

---

# 🔄 Workflow

```text
Raw Dataset (Dataset Mentah)
            │
            ▼
Exploratory Data Analysis (EDA)
            │
            ▼
Missing Value Handling (Data Cleaning)
            │
            ▼
Feature Engineering
            │
            ▼
Penyederhanaan Kategori
            │
            ▼
One-Hot Encoding
            │
            ▼
Standardization (Standarisasi Data)
            │
            ▼
Menentukan Jumlah Cluster (Elbow Method) 
            │
            ▼
K-Means Clustering
            │
            ▼
Silhouette Score (Evaluasi Clustering)
            │
            ▼
PCA Visualization (Visualisasi Cluster)
            │
            ▼
Analisis Cluster & Interpretasi Hasil
```

---

# 🛠 Technologies

| Library | Fungsi |
|----------|---------|
| Pandas | Data Manipulation |
| NumPy | Numerical Computing |
| Matplotlib | Visualization |
| Scikit-Learn | Machine Learning |
| PCA | Dimensionality Reduction |

---

# 📁 Project Structure

```text
Python/Data-Mining/UAS/
│
├── README.md (Dokumen Laporan)
├── Jawaban_UAS_Data_Mining.ipynb (SourceCode Disertai Penjelasan)
├── marketing_campaign.csv (Dataset Mentah/Dataset Asli)
└── images/
   ├── elbow_method.png
   ├── pca_cluster.png
   ├── distribusi_income.png
   └──boxplot_income.png
    
```

---

# 🧹 Data Preprocessing

Tahapan preprocessing yang dilakukan:

| Tahapan | Status |
|----------|--------|
| Missing Value Handling | ✅ |
| Duplicate Checking | ✅ |
| Drop Unused Columns | ✅ |
| Feature Engineering | ✅ |
| Category Simplification | ✅ |
| One-Hot Encoding | ✅ |
| StandardScaler | ✅ |

---

# 📊 Exploratory Data Analysis

Analisis awal meliputi:

- Struktur Dataset
- Statistik Deskriptif
- Missing Value
- Duplicate Data
- Distribusi Income
- Outlier Detection

Visualisasi yang digunakan:

- Histogram
- Boxplot

---

# ⚙ Feature Engineering

Dilakukan pembuatan fitur baru:

### Customer_Tenure

Menghitung lama pelanggan menjadi member berdasarkan:

```
Tanggal terakhir dataset
-
Tanggal bergabung pelanggan
```

---

# 🔤 Encoding

Kolom kategorikal yang diubah menjadi numerik:

- Education

- Marital_Status

Metode:

```
One Hot Encoding
```

---

# 📈 Standardization

Menggunakan:

```python
StandardScaler()
```

Tujuan:

- Mean = 0

- Standard Deviation = 1

Sehingga seluruh fitur memiliki skala yang sama.

---

# 📉 Elbow Method

Dilakukan pengujian:

```
K = 1 sampai K = 10
```

Hasil:

```
Jumlah Cluster Terbaik = 4
```

> **Gambar Elbow Method**

*(Gambar)*

---

# 🤖 K-Means Clustering

Parameter yang digunakan:

```python
KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)
```

Output:

- Label Cluster

- Cluster Summary

---

# 📌 Evaluation

Metode evaluasi:

```
Silhouette Score
```

Hasil:

```
0.1078
```

Interpretasi:

- Cluster berhasil terbentuk.

- Masih terdapat overlap antar cluster.

- Segmentasi masih dapat digunakan untuk analisis pelanggan.

---

# 📈 PCA Visualization

Visualisasi menggunakan:

```
Principal Component Analysis
```

Tujuan:

Mereduksi dimensi menjadi 2 dimensi agar cluster mudah diamati.

> **Gambar PCA**

*(Tambahkan gambar PCA di sini.)*

---

# 👥 Cluster Analysis

| Cluster | Nama | Karakteristik |
|---------|------|---------------|
| 0 | Medium Value Customers | Pendapatan menengah, pembelian cukup aktif |
| 1 | Low Value Customers | Pendapatan rendah, pembelian sedikit |
| 2 | High Value Customers | Pendapatan tinggi, pembelian aktif |
| 3 | Premium Customers | Pendapatan tertinggi, pembelian terbesar |

---

# 📊 Final Result

| Item | Hasil |
|------|--------|
| Dataset | 2240 pelanggan |
| Feature Awal | 29 |
| Feature Setelah Preprocessing | 34 |
| Jumlah Cluster | 4 |
| Silhouette Score | 0.1078 |

---

# 🚀 How to Run

1. Install Python 3.x

2. Install seluruh library

```bash
pip install pandas numpy matplotlib scikit-learn
```

3. Jalankan

```
Customer_Personality_Analysis.ipynb
```

menggunakan:

- Visual Studio Code

- Jupyter Notebook Extension

---

# 📚 References

- Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques.*

- Bramer, M. (2016). *Principles of Data Mining.*

- Pedregosa et al. (2011). *Scikit-Learn: Machine Learning in Python.*

- Pandas Documentation

- Scikit-Learn Documentation

- Kaggle — Customer Personality Analysis (https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

---

<div align="center">

## ⭐ Thank You

**Customer Personality Analysis using K-Means Clustering**

Data Mining Final Project

</div>
