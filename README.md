# Identitas
<table align="center">
  <tr><td>Nama</td><td>Rachma Nur Wulandari</td></tr> 
  <tr><td>NIM</td><td>12030122120003</td></tr>
  <tr><td>KELAS</td><td>E</td></tr>
  <tr><td>Mata Kuliah</td><td>Pengkodean dan Pemrograman</td></tr>
  <tr><td>Dosen</td><td>Dr. Totok Dewayanto, SE., M.Si, Ak, CA</td></tr>
</table>

# Urutan Tahapan analysis_data.py
## 1. Pengumpulan Data
Kumpulkan data dari ketiga file CSV dan gabungkan menjadi satu dataframe untuk analisis lebih lanjut.
## 2. Data Cleaning
Missing Values: Periksa nilai yang hilang dan isi dengan metode yang sesuai (misalnya, forward fill).
Duplicates: Hapus data duplikat yang tidak relevan.
Inconsistencies: Periksa harga satuan dan jumlah terjual yang tampak tidak wajar dan perbaiki jika diperlukan.
## 3. Data Transformation
Gabungkan ketiga file CSV menjadi satu dataframe.
Konversi kolom tanggal menjadi tipe data datetime.
Tambahkan kolom bulan untuk analisis bulanan.
## 4. Exploratory Data Analysis (EDA)
Visualisasi data (grafik batang, histogram, boxplot) untuk melihat distribusi penjualan per kategori produk.
Analisis tren penjualan bulanan untuk mengidentifikasi pola dan anomali.
Pengelompokan data berdasarkan kategori produk dan analisis performa masing-masing kategori.
## 5. Modelling Data
Persiapkan data untuk model prediktif dengan memilih fitur yang relevan (misalnya, Produk_ID, Bulan, Harga_Satuan).
Bagi data menjadi set pelatihan dan set pengujian.
Buat model regresi linear untuk memprediksi jumlah penjualan di bulan berikutnya.
Validasi model menggunakan metrik seperti Mean Squared Error (MSE) untuk menilai akurasi model.
## 6. Interpretasi dan Penyajian Hasil
Interpretasikan koefisien model untuk memahami pengaruh masing-masing fitur terhadap prediksi penjualan.
Buat laporan yang menjelaskan temuan utama dari analisis dan hasil model.
Berikan rekomendasi kepada manajemen berdasarkan hasil analisis dan model prediktif.
## 7. Deploy dan Monitoring
Simpan model yang sudah dilatih dan hasil prediksi dalam file untuk digunakan lebih lanjut (misalnya, menggunakan joblib untuk menyimpan model).
Deploy model untuk memprediksi penjualan di bulan-bulan berikutnya.
Monitor performa model secara berkala dan lakukan pembaruan jika diperlukan berdasarkan data baru yang masuk.

# Menjalankan Aplikasi
- Simpan file Flask app sebagai app.py.
- Buat direktori templates dan simpan file index.html di dalamnya.
- Buat direktori static dan simpan file penjualan_per_bulan.png dan Prediksi_Penjualan_Bulan_Depan.csv di dalamnya.

# Hasil Gambar
![Figure_1](https://github.com/rachmanurwulandari/Rachma-Nur-Wulandari_Data-Analitik/assets/152131726/c4b148ce-6a3b-4ea2-b4b8-b7c79154c945)

# Coding vscode
![Screenshot (2234)](https://github.com/rachmanurwulandari/Rachma-Nur-Wulandari_Data-Analitik/assets/152131726/4c26fb4f-e7d0-45aa-96aa-5093d92968e5)

