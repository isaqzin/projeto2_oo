import math
from abc import ABC, abstractmethod

class Point():

    def __init__(self,x,y,n):

        self.n=n
        self.x=x
        self.y=y
        self.nome = __class__.__name__

    def distanceFC(self):

        distanceFC = math.sqrt(self.x**2 + self.y**2)
        return distanceFC
    
    def distancePoints(self, point):
        x2 = point.x
        y2 = point.y
        distancePoints = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        return distancePoints  
     
    def anguloX(self):

        if self.x != 0:
            anguloX = math.atan(self.y/self.x)
        else:
            anguloX=0
            
        return anguloX
    def model(self):

        model = f"_X={self.x}_y={self.y}"
        return model

class SegReta():


    def __init__(self,point_origem, point_final,n):
        self.n=n
        self.point_origem = point_origem
        self.point_final = point_final
        self.nome = __class__.__name__


    def tamanho(self):

        tamanho = math.sqrt((self.point_final.x - self.point_origem.x)**2 + (self.point_final.y - self.point_origem.y)**2)
        return tamanho

    
    def model(self):

        model =f'_origem=[{self.point_origem.x},{self.point_origem.y}]_fim=[{self.point_final.x},{self.point_final.y}]'
        return model

class Circle():

    #centro é um ponto
    def __init__(self,centro,raio,n):
        self.n=n
        self.raio=raio
        self.centro = centro
        self.nome = __class__.__name__

    def area(self):

        area= 3.14*self.raio**2
        return area

    def equation(self):

        print(f'{self.raio}²= (y-{self.centro.y})² + (x-{self.centro.x})²')

    def perimetro(self):

        perimetro=2*3.14*self.raio
        return perimetro
    
    def model(self):
        model = f'_raio={self.raio}_centro[{self.centro.x},{self.centro.y}]'
        return model

class Quadrado():
        
        def __init__(self,lado,ponto,n):
            self.n=n
            self.nome = __class__.__name__
            self.lado = lado
            self.origem = ponto
            self.centro = Point(0,0,None)
            self.sup_dir = Point(self.origem.x + self.lado,self.origem.y + self.lado,None)
            self.sup_esq = Point(self.origem.x,self.origem.y + self.lado,None)
            self.inf_dir = Point(self.origem.x + self.lado,self.origem.y,None)
            self.inf_esq = self.origem

        def _setPoints(self):

            self.sup_dir.y = self.origem.y + self.lado
            self.sup_dir.x = self.origem.x + self.lado
            self.sup_esq.x = self.origem.x
            self.sup_esq.y = self.origem.y + self.lado
            self.inf_dir.x = self.origem.x + self.lado
            self.inf_dir.y = self.origem.y 
            self.inf_esq = self.origem
 
        def setOrigem(self,ponto):

            self.origem= ponto

        def area(self):

            area= self.lado**2
            return area
    
        def perimetro(self):

            perimetro= 4*self.lado
            return perimetro

        def model(self):

            model = f'_lado={self.lado}_origem[{self.origem.x},{self.origem.y}]'
            return model

        def diagonal(self):
            diagonal= math.sqrt(2*(self.lado**2))
            return diagonal
        
        def getCentro(self):
            diagonal= math.sqrt(2*(self.lado**2))
            self.centro.x= (diagonal/2) + self.origem.x
            self.centro.y= (diagonal/2) + self.origem.y
            return self.centro.x, self.centro.y
            
class Retangulo(Quadrado):

    #lado é a altura Y, lado 2 é o comprimento X    
    def __init__(self,lado,lado2,origem,n):

        super().__init__(lado,origem,n)
        self.nome = __class__.__name__
        self.lado2= lado2
        self.origem = origem
        self.sup_dir = Point(0,0,None)
        self.sup_esq = Point(0,0,None)
        self.inf_dir = Point(0,0,None)
        self.inf_esq = Point(0,0,None)
        self.sup_dir.y = self.origem.y + self.lado
        self.sup_dir.x = self.origem.x + self.lado2
        self.sup_esq.x = self.origem.x
        self.sup_esq.y = self.origem.y + self.lado
        self.inf_dir.x = self.origem.x + self.lado2
        self.inf_dir.y = self.origem.y 
        self.inf_esq = self.origem

    def area(self):

        area= self.lado * self.lado2
        return area
    
    def perimetro(self):

        perimetro= 2*self.lado + 2*self.lado2
        return perimetro
    
    def model(self):

        model =f'_lados={self.lado}_{self.lado2}_origem[{self.origem.x},{self.origem.y}]'
        return model

    def diagonal(self):
        diagonal = math.sqrt(self.lado**2 + self.lado2**2)
        return diagonal
    
    def getCentro(self):
        self.centro.x= (self.lado/2) + self.origem.x
        self.centro.y= (self.lado2/2) + self.origem.y
        return self.centro.x, self.centro.y
    
#Eu sei que daria pra fazer todos os tipos de triangulo em uma só classe
#mas estudando vi a abstração e quis por, n tive muita ideia 
#se pareceu forçado, releve :) 
#ai vou mudar só a formula de calculo de area em cada triangulo ou algo que 
#achar de diferente em cada 
class Triangulo(ABC):

    def __init__(self, ponto1, ponto2,ponto3,n):
        self.n=n
        self.nome = __class__.__name__
        self.ponto1=ponto1
        self.ponto2=ponto2
        self.ponto3=ponto3
        self.lado1= math.sqrt((ponto2.x - ponto1.x)**2 + (ponto2.y - ponto1.y)**2)
        self.lado2= math.sqrt((ponto2.x - ponto3.x)**2 + (ponto2.y - ponto3.y)**2)
        self.lado3= math.sqrt((ponto3.x - ponto1.x)**2 + (ponto3.y - ponto1.y)**2)

    def perimetro(self):

        perimetro= self.lado1 + self.lado2 + self.lado3
        return perimetro

    def baricentro(self):

        x= (self.ponto1.x + self.ponto2.x + self.ponto3.x)/3
        y =(self.ponto1.y + self.ponto2.y + self.ponto3.y)/3
        return x,y
       
    
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def altura(self):
        pass
    @abstractmethod
    def model(self):
        pass

class TrianguloEquilatero(Triangulo):

    def __init__(self, ponto1, ponto2, ponto3,n):
        super().__init__(ponto1, ponto2, ponto3,n)
        self.nome = __class__.__name__

    def area(self):
        area = ((self.lado1**2)*math.sqrt(3))/4
        return area
  

    def altura(self):

        altura =(self.lado1*math.sqrt(3))/2
        return altura
   
        
    def model(self):

        model = f'_coordenadas[{self.ponto1.x},{self.ponto1.y}],[{self.ponto2.x},{self.ponto2.y}],[{self.ponto3.x},{self.ponto3.y}]_lado={self.lado1}'
        return model
   
class TrianguloIsoceles(Triangulo):

    def __init__(self, ponto1, ponto2, ponto3,n):
        super().__init__(ponto1, ponto2, ponto3,n)
        self.nome = __class__.__name__
        
    def altura(self):
        if self.lado1 == self.lado2:
            altura = (self.lado1**2 - (self.lado3**2)/4)**0.5
            return altura
        elif self.lado1 == self.lado3:
            altura = (self.lado1**2 - (self.lado2**2)/4)**0.5
            return altura
        elif self.lado2 == self.lado3:
            altura = (self.lado2**2 - (self.lado1**2)/4)**0.5
            return altura 
        else:
            print("suas opções são invalidas")
            altura=0.00
            return altura 
  

    def area(self):

        h = self.altura()
        if self.lado1 == self.lado2:
            base= self.lado3
        elif self.lado1 == self.lado3:
            base=self.lado2
        elif self.lado2 == self.lado3:
            base= self.lado1
        else:
            print("suas opções são invalidas")
            base=0.00 

        area = (base*h)/2
        return area


    def model(self):

        model =f'_coordenadas[{self.ponto1.x},{self.ponto1.y}],[{self.ponto2.x},{self.ponto2.y}],[{self.ponto3.x},{self.ponto3.y}]_lados={self.lado1}_{self.lado2}_{self.lado3}'
        return model
 




        
