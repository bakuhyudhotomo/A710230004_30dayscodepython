# Program sederhana untuk menghitung luas dan keliling persegi

# Fungsi untuk menghitung luas persegi
def luas_persegi(sisi):
    return sisi * sisi

# Fungsi untuk menghitung keliling persegi
def keliling_persegi(sisi):
    return 4 * sisi

# Input sisi dari pengguna
sisi = float(input("Masukkan panjang sisi persegi: "))

# Hitung luas dan keliling persegi
luas = luas_persegi(sisi)
keliling = keliling_persegi(sisi)

# Tampilkan hasil
print("Luas persegi:", luas)
print("Keliling persegi:", keliling)