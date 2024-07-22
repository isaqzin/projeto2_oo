from package.maths.terms import TrianguloIsoceles
from package.maths.terms import Point

ponto1 = Point(5,0.43,None)
ponto2 = Point(4.5,-0.43,None)
ponto3 = Point(5.5,-0.43,None)

# ponto1 = Point(0,0)
# ponto2 = Point(0,1)
# ponto3 = Point(0,2)

triangulo = TrianguloIsoceles(ponto1,ponto2,ponto3,None)


print(f' a area é {triangulo.area()}, a altura é {triangulo.altura()}, o baricentro é {triangulo.baricentro()} e o perimetro é {triangulo.perimetro()}')

triangulo.model()