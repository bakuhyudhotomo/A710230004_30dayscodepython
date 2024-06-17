import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)  # Menghasilkan angka acak antara 1 dan 100
    tebakan = None
    percobaan = 0

    print("Halo! Saya telah memilih sebuah angka antara 1 dan 100. Coba tebak!")

    while tebakan != angka_rahasia:
        tebakan = int(input("Masukkan tebakan Anda: "))
        percobaan += 1

        if tebakan < angka_rahasia:
            print("Tebakan Anda terlalu rendah, coba lagi.")
        elif tebakan > angka_rahasia:
            print("Tebakan Anda terlalu tinggi, coba lagi.")
        else:
            print(f"Selamat! Anda menebak angka {angka_rahasia} dengan benar dalam {percobaan} percobaan.")

    return percobaan

tebak_angka()