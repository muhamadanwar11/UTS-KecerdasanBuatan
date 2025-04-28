# UTS-KecerdasanBuatan


Sistem Pakar Identifikasi Hama Tanaman
Deskripsi
Sistem ini menggunakan aturan logika sederhana untuk menentukan jenis hama tanaman berdasarkan gejala yang muncul, seperti daun menguning, bercak hitam, daun berlubang, dan tanaman layu.
Aturan
•	Daun menguning dan tanaman layu → Hama Aphids
•	Daun menguning dan bercak hitam → Jamur Daun
•	Bercak hitam dan daun berlubang → Hama Ulat
•	Daun berlubang dan tanaman layu → Hama Kumbang
Cara Kerja
1.	Input kondisi gejala tanaman.
2.	Sistem mencocokkan gejala dengan aturan.
3.	Sistem menampilkan jenis hama atau pesan "perlu pemeriksaan lebih lanjut".
Contoh Implementasi (Python)
def identifikasi_hama(daun_menguning, bercak_hitam, daun_berlubang, tanaman_layu):
    if daun_menguning and tanaman_layu:
        return "Hama Aphids"
    elif daun_menguning and bercak_hitam:
        return "Jamur Daun"
    elif bercak_hitam and daun_berlubang:
        return "Hama Ulat"
    elif daun_berlubang and tanaman_layu:
        return "Hama Kumbang"
    else:
        return "Hama tidak diketahui, perlu pemeriksaan lanjut"

# Contoh penggunaan
gejala = {
    "daun_menguning": True,
    "bercak_hitam": False,
    "daun_berlubang": False,
    "tanaman_layu": True
}

hasil = identifikasi_hama(**gejala)
print("Jenis Hama:", hasil)
Output
Jenis Hama: Hama Aphids


Penulis
•	Nama: Muhamad Anwar Sanusi
•	NIM: 2306016
•	Kelas: Informatika-A
•	Institusi: Institut Teknologi Garut
•	Mata Kuliah: Kecerdasan Buatan
•	Dosen Pengampu: Leni Fitriani, S.T., M.Kom.



