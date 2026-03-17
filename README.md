# Sistem Pakar Rekomendasi Laptop

Program yang dibuat ini adalah program sederhana dengan konsep Sistem Pakar yang pernah diajarkan pada mata kuliah Kecerdasan Buatan.

Program ini berjalan menggunakan Flask, dan juga menggunakan library JSON untuk membaca data statis yang berasal dari file eksternal.

## Konsep Sistem:
Pertama, sistem akan meminta pengguna memilih Data Budget dan Kebutuhan yang nantinya akan digunakan untuk mencari data Laptop yang ada pada file JSON. Lalu sistem akan memberikan output berdasarkan hasil pencarian, Jika Data yang dicari sesuai dengan Budget dan Kebutuhan maka sistem akan memberikan Data tersebut sebagai output, Namun jika tidak ada Data yang sesuai dengan Kombinasi Budget dan Kebutuhan maka sistem akan memberikan Pesan Error sebagai output.

1. **Struktur Kontrol**
   - Menggunakan perulangan (`for loop`) untuk mengecek setiap data laptop di dalam *database*.
   - Menggunakan percabangan logika berbasis aturan / *Rule-Based* (`if` dan `and`) untuk mencocokkan input pengguna (budget & kebutuhan) dengan kriteria laptop.

2. **Struktur Data**
   - Menggunakan format **List of Dictionaries** yang disimpan dalam file eksternal `data.json`.
   - Menggunakan struktur **List** di dalam data kategori (contoh: `"kategori": ["ringan", "menengah"]`) untuk menangani laptop dengan fungsi ganda.

3. **Penggunaan Library**
   - `flask`: Sebagai *framework* untuk menjalankan aplikasi berbasis web (menerima input form dan me-render HTML).
   - `json`: Untuk membaca dan mem- *parsing* basis pengetahuan (*knowledge base*) statis dari file eksternal.
