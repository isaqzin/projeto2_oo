from package.maths.terms import Point
from package.maths.terms import Quadrado

origem = Point(20,30,None)
quadrado = Quadrado(10,origem,None)

quadrado.model()
quadrado.diagonal()

print(f'sua diagonal é {quadrado.diagonal()}, a coordenada do centro é {quadrado.getCentro()}')

print(f'Sua area é {quadrado.area()} U.A')
print(f'seu perimetro é {quadrado.perimetro()} U.C')
