from package.maths.terms import TrianguloEquilatero
from package.maths.terms import Point
from package.maths.terms import *

ponto1 = Point(10.0, 12.165063509461097,None)
ponto2 = Point(7.5, 7.834936490538903,None)
ponto3 = Point(12.5, 7.834936490538903,None)

triangulo = TrianguloEquilatero(ponto1,ponto2,ponto3,None)

print(f' a area é {triangulo.area()}, a altura é {triangulo.altura()}, o baricentro é {triangulo.baricentro()} e o perimetro é {triangulo.perimetro()}')


print(f'{Interferencia.areaTriangulo(ponto1,ponto2,ponto3)}')

triangulo.model()