from punto import *
from math import pi

class Figura:

    def __init__(self, p1, p2):
        self.origen = p1
        self.fin = p2
        self.area = 0 


class Cuadrado(Figura):

    def calcular_area(self):
        lado = self.origen.calcular_distancia(self.fin)
        self.area  = lado * lado
    def calcular_perimetro(self):
        lado = self.origen.calcular_distancia(self.fin)
        self.perimetro = lado * lado * lado * lado
    
        
class Circulo(Figura):
    def calcular_area(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.area = pi * (radio**2)

    def calcular_perimetro(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.perimetro = 2 * pi * radio


class Triangulo(Figura):

    def calcular_area(self):
        self.p3 = Punto(self.origen.x,self.fin.y)
        altura = self.origen.calcular_distancia(self.p3)
        base = self.p3.calcular_distancia(self.fin)
        self.area = ((base*altura)/2)
    def calcular_perimetro(self):
        self.p3 = Punto(self.origen.x,self.fin.y)
        altura = self.origen.calcular_distancia(self.p3)
        base = self.p3.calcular_distancia(self.fin)
        h= self.origen.calcular_distancia(self.fin)
        self.perimetro = altura + base + h 
        
        



         
    
