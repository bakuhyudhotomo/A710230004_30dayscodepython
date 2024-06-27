# Menghitung rata-rata nilai dari daftar nilai
nilai_siswa = [80, 85, 78, 92, 88]

def hitung_rata_rata(nilai):
    total = sum(nilai)
    jumlah_nilai = len(nilai)
    rata_rata = total / jumlah_nilai
    return rata_rata

rata_rata_nilai = hitung_rata_rata(nilai_siswa)
print("Rata-rata nilai siswa:", rata_rata_nilai)