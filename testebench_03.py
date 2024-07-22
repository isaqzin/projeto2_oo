from package.maths.terms import Point
import math


ponto = Point(2,2,0)
ponto1= Point(0,0,3)

print(ponto.model())

print(f'a distancia do ponto à origem é {ponto.distanceFC()}')

print(f'o angulo entre a reta que passa pela origem e pelo ponto em relação e o eixo x é {ponto.anguloX()} rad e em graus é {ponto.anguloX()*180/math.pi}')

print(f'a distancia entre ponto e ponto1 é {ponto.distancePoints(ponto1)} ')



