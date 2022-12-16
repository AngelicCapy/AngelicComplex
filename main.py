class Complexe:
    def __init__(self, reel, imaginaire):
        self.__reel = reel
        self.__imaginaire = imaginaire
    def reel(self):return self.__reel
    def imaginaire(self):return self.__imaginaire
    def __add__(self, autre):return Complexe(self.reel() + autre.reel(), self.imaginaire() + autre.imaginaire())
    def __sub__(self, autre):return Complexe(self.reel() - autre.reel(), self.imaginaire() - autre.imaginaire())
    def __mul__(self, autre):return Complexe(self.reel() * autre.reel() - self.imaginaire() * autre.imaginaire(), self.reel() * autre.imaginaire() + self.imaginaire() * autre.reel())
    def __truediv__(self, autre):return Complexe((self.reel() * autre.reel() + self.imaginaire() * autre.imaginaire()) / (autre.reel() ** 2 + autre.imaginaire() ** 2), (self.imaginaire() * autre.reel() - self.reel() * autre.imaginaire()) / (autre.reel() ** 2 + autre.imaginaire() ** 2))
    def __str__(self):
        if self.imaginaire() < 0:
            return str(self.reel()) + " - " + str(-self.imaginaire()) + "i"
        return str(self.reel()) + " + " + str(self.imaginaire()) + "i"
