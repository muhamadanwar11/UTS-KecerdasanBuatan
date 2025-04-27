# UTS-KecerdasanBuatan

Sistem Pakar Diagnosa Tanaman
Deskripsi
Sistem pakar ini dirancang untuk membantu mendiagnosa hama atau penyakit pada tanaman berdasarkan gejala yang terdeteksi. Sistem menggunakan aturan berbasis logika proposisional untuk mencocokkan kombinasi gejala dengan diagnosis yang sudah ditentukan sebelumnya.

Fitur Sistem
•	Diagnosa berdasarkan 6 aturan yang ditetapkan.
•	Input berupa gejala tanaman yang dapat dipilih oleh pengguna.
•	Proses inferensi otomatis berdasarkan gejala yang dimasukkan.
•	Hasil diagnosa berupa jenis hama atau penyakit tanaman.
•	Penanganan kesalahan input (hanya menerima jawaban 'y' atau 'n').

Langkah Pengerjaan
1. Penentuan Gejala
Gejala yang digunakan dalam sistem ini adalah:
•	Daun Menguning
•	Terdapat Bercak Hitam
•	Daun Berlubang
•	Tanaman Layu
2. Penyusunan Aturan Diagnosa
Berdasarkan kombinasi gejala, sistem akan menghasilkan diagnosis sesuai dengan 6 aturan berikut:
1.	Jika daun menguning dan tanaman layu, maka diagnosis adalah Hama Aphids.
2.	Jika terdapat bercak hitam dan daun menguning, maka diagnosis adalah Jamur Daun.
3.	Jika daun berlubang dan terdapat bercak hitam, maka diagnosis adalah Hama Ulat.
4.	Jika tanaman layu dan daun berlubang, maka diagnosis adalah Hama Kumbang.
5.	Jika daun menguning saja, maka diagnosis adalah Kekurangan Nutrisi.
6.	Jika terdapat bercak hitam saja, maka diagnosis adalah Penyakit Bercak Daun.
3. Penyusunan Algoritma Inferensi
•	Menggunakan logika proposisional, sistem akan memeriksa kombinasi gejala yang diberikan pengguna.
•	Berdasarkan kombinasi gejala tersebut, hasil diagnosis akan disampaikan kepada pengguna.
4. Implementasi Program
•	Program ini ditulis dalam bahasa Python.
•	Input gejala diambil dari pengguna menggunakan fungsi input().
•	Sistem kemudian memeriksa kombinasi gejala menggunakan struktur if-elif-else.
•	Program akan memberikan hasil diagnosis berdasarkan aturan yang sudah ditentukan.

Langkah Penggunaan
1.	Persyaratan Sistem:
o	Pastikan Python sudah terinstal di sistem Anda. (Disarankan Python versi 3.x)
2.	Cara Menjalankan Program:
o	Unduh atau salin kode Python berikut ke dalam file diagnosa_tanaman.py.
o	Jalankan program menggunakan terminal atau command prompt dengan perintah:
o	python diagnosa_tanaman.py
o	Program akan meminta input berupa gejala yang dialami oleh tanaman.
o	Setelah memasukkan informasi gejala, sistem akan memberikan diagnosis.
3.	Contoh Penggunaan:
4.	Apakah daun menguning? (y/n): y
5.	Apakah terdapat bercak hitam? (y/n): n
6.	Apakah daun berlubang? (y/n): n
7.	Apakah tanaman layu? (y/n): y
8.	Diagnosis: Hama Aphids

Fitur Tambahan:
•	Penanganan Kesalahan Input: Jika pengguna memasukkan input selain 'y' atau 'n', sistem akan meminta ulang input hingga yang benar dimasukkan.
•	Pengecekan Diagnosa: Sistem dapat mengidentifikasi berbagai hama atau penyakit tanaman berdasarkan kombinasi gejala yang ada.

Struktur Kode
diagnosa_tanaman.py
│
├── Fungsi get_input()          # Menangani input gejala dengan validasi
├── Input Gejala                # Pengguna memasukkan informasi gejala
├── Logika Inferensi            # Proses pengecekan kombinasi gejala
└── Output Diagnosis            # Menampilkan hasil diagnosis

Kontribusi
Jika Anda ingin berkontribusi atau melakukan pengembangan lebih lanjut terhadap sistem ini, Anda dapat mengajukan pull request atau memberikan masukan melalui Issues pada repositori ini.

Lisensi
Proyek ini dilisensikan di bawah lisensi MIT License.

