class Volume(): 
    def __init__(self):
        self.volume_level = 5 # Volume level default

    def volumeUp(self):
        if self.volume_level < 10: #Maksimum volume adalah 10
            self.volume_level += 1
            print("Volume increased to level:", self.volume_level)
        else:
            print("Volume is already at maximum level.")

    def volumeDown(self):
        if self.volume_level > 0: #Minimum volume adalah 0
            self.volume_level -= 1
            print("Volume decreased to level:", self.volume_level)
        else:
            print("Volume is already at minimum level.")

    def get_volume_level(self):
        return self.volume_level

    # Extra method for debugging
    def show(self): 
        print('Switch is up ?', self.volumeUp) 
        print('Switch is down ?', self.volumeDown) 

# Contoh penggunaan
volume = Volume()
print("Initial volume level:", volume.get_volume_level())
volume.volumeUp()
volume.volumeUp()
volume.volumeDown()
volume.volumeDown()