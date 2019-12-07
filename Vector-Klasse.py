#Ein sehr effektive Python-Klasse, um Vektoren auszurechnen

class Vec(tuple):
    """ Eigene Vektor-Klasse um 2D-nDimensionale Koordinaten zu hinterlegen"""

    def __new__(cls, *args):
        return tuple.__new__(cls, args)

    def __add__(self, other):
        return Vec(*tuple(a+b for a,b in zip(self, other)))

    def __sub__(self, other):
        return Vec(*tuple(a-b for a,b in zip(self, other)))

    def __mul__(self, faktor):
        return Vec(*tuple(a*faktor for a in self))

    def abstand(self, other):
        """"Liefert den Manhatten-Abstand zwischen zwei Koordinaten"""
        return sum(abs(a-b) for a,b in zip(self, other))
