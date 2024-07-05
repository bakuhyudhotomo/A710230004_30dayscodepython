class Mobil:
  def move(self):
    print("Mobil berjalan di jalan raya.")

class Pesawat:
  def move(self):
    print("Pesawat terbang di udara.")

class Kapal:
  def move(self):
    print("Kapal berlayar di laut.")

# Example Usage
mobil = Mobil()
pesawat = Pesawat()
kapal = Kapal()

mobil.move()  # Output: Mobil berjalan di jalan raya.
pesawat.move()  # Output: Pesawat terbang di udara.
kapal.move()  # Output: Kapal berlayar di laut.