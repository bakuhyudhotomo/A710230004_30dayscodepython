# Membuat dan memanipulasi daftar
buah = ["apel", "jeruk", "pisang", "mangga"]

# Menambahkan elemen ke dalam daftar
buah.append("anggur")

# Mengakses elemen dalam daftar
print("Buah pertama:", buah[0])
print("Buah terakhir:", buah[-1])

# Menghapus elemen dari daftar
buah.remove("pisang")

# Menggunakan loop untuk mengakses setiap elemen dalam daftar
print("\nDaftar buah:")
for item in buah:
    print(item)