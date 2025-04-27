def identifikasi_hama(daun_menguning, bercak_hitam, daun_berlubang, tanaman_layu):
    if daun_menguning and tanaman_layu:
        return "Ulat Grayak"
    elif daun_menguning and bercak_hitam:
        return "Kutu Daun"
    elif bercak_hitam and daun_berlubang:
        return "Kumbang Daun"
    elif daun_berlubang and tanaman_layu:
        return "Wereng Batang"
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