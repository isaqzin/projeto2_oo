from package.maths.terms import Circle
from package.maths.terms import Point

centro = Point(0,0)
circulo = Circle(centro,5)

print("\nA equação do seu círculo é:")
circulo.equation()

print(f'Sua area é {circulo.area()} U.A')
print(f'seu perimetro é {circulo.perimetro()} U.C')