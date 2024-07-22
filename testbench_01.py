from package.maths.terms import SegReta
from package.maths.terms import Point


ponto1 = Point(0,0)
ponto2= Point(1,1)
segmento_1 = SegReta(ponto1,ponto2)
segmento_1.model()
print(f'o tamanho do segmento de reta é: {segmento_1.tamanho()}')

