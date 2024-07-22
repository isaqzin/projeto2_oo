from package.maths.terms import Point
from package.maths.terms import Retangulo

origem = Point(30,20,None)
retangulo = Retangulo(4,3, origem, None)



retangulo.model()


retangulo.model()

print(f'sua diagonal é {retangulo.diagonal()}, a coordenada do centro é {retangulo.getCentro()}')
print(f'Sua area é {retangulo.area()} U.A')
print(f'seu perimetro é {retangulo.perimetro()} U.C')