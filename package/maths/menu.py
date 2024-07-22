from .terms import *

class Interferencia():#classe auxiliar para calculos da interferencia

    @staticmethod
    def verificarTriangulo(lado1,lado2,lado3):

        if (lado1 + lado2 )> lado3 and (lado3 + lado2 )> lado1 and (lado1 + lado3 )> lado2:
            return True
        else:
            return False

    @staticmethod
    def areaTriangulo(ponto1,ponto2,ponto3):

        area = abs(0.5*(ponto1.x*(ponto2.y - ponto3.y) + ponto2.x*(ponto3.y - ponto1.y) + ponto3.x*(ponto1.y - ponto2.y)))

        return area
    
    @staticmethod
    def verificacaoTriangulo(ponto1,ponto2,ponto3,pontoVer):

        areaTotal=Interferencia.areaTriangulo(ponto1,ponto2,ponto3)
        area1=Interferencia.areaTriangulo(ponto1,ponto2,pontoVer)
        area2=Interferencia.areaTriangulo(ponto3,ponto2,pontoVer)
        area3=Interferencia.areaTriangulo(ponto1,ponto3,pontoVer)

        if area1+area2+area3==areaTotal:
            return True
        else:
            return False

    @staticmethod
    def verificacaoQuadradoRetangulo(p1,p2,p3,p4,pVer):
        
        areaTotal1= Interferencia.areaTriangulo(p1,p2,p4)
        area1= Interferencia.areaTriangulo(p1,p2,pVer)
        area2= Interferencia.areaTriangulo(p1,p4,pVer)
        area3= Interferencia.areaTriangulo(p2,p4,pVer)

        areaTotal2= Interferencia.areaTriangulo(p2,p3,p4)
        area4= Interferencia.areaTriangulo(p2,p3,pVer)
        area5= Interferencia.areaTriangulo(p3,p4,pVer)

        areaSoma1= area1+area2+area3
        areaSoma2 = area4+area5+area3

        if areaSoma1 == areaTotal1 or areaSoma2==areaTotal2:
            return True
        else:
            return False

    @staticmethod   
    def verificacaoCirculo(raio,pVer,centro):

        distancePoints = math.sqrt((centro.x - pVer.x)**2 + (centro.y - pVer.y)**2)

        if distancePoints<= raio:
            return True
        else:
            return False
        
    @staticmethod
    def verificacaoSegReta(ponto,segReta):

        dis1= ((ponto.x-segReta.point_origem.x)**2+(ponto.y-segReta.point_origem.y)**2)**0.5
        dis2= ((ponto.x-segReta.point_final.x)**2+(ponto.y-segReta.point_final.y)**2)**0.5

        dis12= ((segReta.point_origem.x-segReta.point_final.x)**2+(segReta.point_origem.y-segReta.point_final.y)**2)**0.5

        if (dis1+dis2)<=1.1*dis12:
            return True
        else:
            return False
        
class Control():

    def __init__(self):
        
        self.figuras = {}
        self.contagem = 0

    def inserirFigura(self,figura):
         
        self.figuras[figura.nome + str(self.contagem)] = figura
        print(f"A {figura.nome + str(self.contagem)} figura foi adicionada")
        self.contagem += 1

    def printFormas(self):

        if len(self.figuras)==0:
            print("Nao ha formas armazenadas")

            return
        
        print('\nArmazenamos as seguintes formas :\n')
        for shape in self.figuras.keys():
            print(shape + self.figuras[shape].model())

class Menu:

    def __init__(self):

        self.dashboard = Control()
        self.actions = {
            'Criar_forma' : self.criar,
            'Interferencia_entre_formas': self.crash,
            'Imprimir_formas': self.printarFormas,
            'atualizar_forma': self.atualizar,
            'calculos_forma': self.calculos,
            'distancia_entre_pontos': self.distanciaPontos,
            'Sair' : exit
        }


    def embelezador(self):
        print('\n')
        print('=='*50)

    @staticmethod
    def eh_numero(entrada):
        try:
            float(entrada) 
            return True
        except ValueError:
            return False

    def criar(self):
        print('\n')
        print('Você pode criar as seguintes Formas:')
        print('1. Ponto')
        print('2. Segmento de reta')
        print('3. Circulo')
        print('4. Quadrado')
        print('5. Retangulo')
        print('6. Triangulo equilatero')
        print('7. Triangulo isoceles')
        escolha = input("Digite o numero da forma que deseja criar: ")
        print('\n')

        if escolha == "1":

            x=input("digite a coordenada X: ")
            y=input("digite a coordenada Y: ")

            if self.eh_numero(x) and self.eh_numero(y):
                if float(x)>=0 and float(y)>=0:
                    ponto = Point(float(x),float(y),self.dashboard.contagem)

                    print('\n')
                    print('=='*50)
                    self.dashboard.inserirFigura(ponto)                    
                    self.dashboard.printFormas()
                    print('\n')
                    print('=='*50)
                else:
                    print('\n')
                    print('=='*50)
                    print("digitos inválidos, as coordenadas devem estar no primeiro quadrante")  
                    print('\n')
                    print('=='*50)
            else:
                print('\n')
                print('=='*50)
                print("digitos inválidos")
                print('\n')
                print('=='*50)
        elif escolha =="2":

            x1=input("digite a coordenada X de origem: ")
            y1=input("digite a coordenada Y de origem: ")
            x2=input("digite a coordenada X do final: ")
            y2=input("digite a coordenada Y do final: ")

            if self.eh_numero(x1) and self.eh_numero(y1) and self.eh_numero(x2) and self.eh_numero(y2):
                if float(x1)>=0 and float(y1)>=0 and float(x2)>=0 and float(y2)>=0 and (float(x1)!=float(x2) or float(y1)!=float(y2)):   
                    ponto1 = Point(float(x1),float(y1),None)
                    ponto2= Point(float(x2),float(y2),None)
                    segReta = SegReta(ponto1,ponto2,self.dashboard.contagem)
                    print('\n')
                    print('=='*50)
                    self.dashboard.inserirFigura(segReta)
                    self.dashboard.printFormas()
                    print('\n')
                    print('=='*50)
                else:
                    print('\n')
                    print('=='*50)
                    print("digitos inválidos, as coordenadas devem estar no primeiro quadrante")
                    print('\n')
                    print('=='*50)
            else:
                print('\n')
                print('=='*50)
                print("digitos invalidos")
                print('\n')
                print('=='*50)
        elif escolha =="3":
            x=input("digite a coordenada X: ")
            y=input("digite a coordenada Y: ")
            raio = input("digite o valor do raio: ")

            if self.eh_numero(x) and self.eh_numero(y) and self.eh_numero(raio):
                if float(x)>=0 and float(y)>=0 and float(raio)>=0:
                    centro = Point(float(x),float(y),None)
                    circulo = Circle(centro,float(raio),self.dashboard.contagem)
                    print('\n')
                    print('=='*50)
                    self.dashboard.inserirFigura(circulo)
                    self.dashboard.printFormas()
                    print('\n')
                    print('=='*50)                 
                else:
                    print('\n')
                    print('=='*50)
                    print("digitos inválidos, as coordenadas devem estar no primeiro quadrante e o raio deve ser positivo")
                    print('\n')
                    print('=='*50)
            else:
                print('\n')
                print('=='*50)
                print("digitos invalidos")
                print('\n')
                print('=='*50)
        elif escolha =="4":
            lado = input("digite o valor do lado do quadrado: ")
            print("\nA origem do quadrado é o lado inferior esquerdo")
            origemX = input("Digite a coordenada X da origem:")
            origemY = input("Digite a coordenada y da origem:")

            if self.eh_numero(lado) and self.eh_numero(origemY) and self.eh_numero(origemX):
                if float(lado)>=0 and float(origemY)>=0 and float(origemX)>=0:
                    origem = Point(float(origemX), float(origemY), None)
                    quadrado = Quadrado(float(lado),origem,self.dashboard.contagem)
                    print('\n')
                    print('=='*50)
                    self.dashboard.inserirFigura(quadrado)
                    self.dashboard.printFormas()
                    print('\n')
                    print('=='*50)
                else:
                    print('\n')
                    print('=='*50)
                    print("digitos inválidos, as coordenadas devem estar no primeiro quadrante e o lado deve ser positivo")
                    print('\n')
                    print('=='*50)   
            else:
                print('\n')
                print('=='*50)
                print("Digitos invalidos")
                print('\n')
                print('=='*50)
        elif escolha =="5":
            lado = input("digite o valor do comprimento do retangulo: ")
            lado2 = input("digite o valor da altura do retangulo: ")
            print("\nA origem do retangulo é o lado inferior esquerdo")
            origemX = input("Digite a coordenada X da origem: ")
            origemY = input("Digite a coordenada y da origem: ")

            if self.eh_numero(lado) and self.eh_numero(origemY) and self.eh_numero(origemX) and self.eh_numero(lado2):
                if float(lado)>=0 and float(origemY)>=0 and float(origemX)>=0 and float(lado2)>=0:
                    origem = Point(float(origemX), float(origemY), None)
                    retangulo = Retangulo(float(lado),float(lado2),origem,self.dashboard.contagem)
                    print('\n')
                    print('=='*50)
                    self.dashboard.inserirFigura(retangulo)
                    self.dashboard.printFormas()
                    print('\n')
                    print('=='*50)
                else:
                    print('\n')
                    print('=='*50)
                    print("digitos inválidos, as coordenadas devem estar no primeiro quadrante e o lado deve ser positivo")
                    print('\n')
                    print('=='*50)   
            else:
                print('\n')
                print('=='*50)
                print("Digitos invalidos")
                print('\n')
                print('=='*50)
        elif escolha =="6":
            x1 = input("Digite a coordenada x do ponto 1: ")
            y1 = input("Digite a coordenada y do ponto 1: ")
            x2 = input("Digite a coordenada x do ponto 2: ")
            y2 = input("Digite a coordenada y do ponto 2: ")
            x3 = input("Digite a coordenada x do ponto 3: ")
            y3 = input("Digite a coordenada y do ponto 3: ")

            if self.eh_numero(x1) and self.eh_numero(y1) and self.eh_numero(x2) and self.eh_numero(y2) and self.eh_numero(x3) and self.eh_numero(y3):
                if float(x1)>= 0 and float(y1)>= 0 and float(x2)>= 0 and float(y2)>= 0 and float(x3)>=0 and float(y3)>=0:
                    ponto1 = Point(float(x1),float(y1),None)
                    ponto2 = Point(float(x2),float(y2),None)
                    ponto3 = Point(float(x3),float(y3),None)
                    lado1= math.sqrt((ponto2.x - ponto1.x)**2 + (ponto2.y - ponto1.y)**2)
                    lado2= math.sqrt((ponto2.x - ponto3.x)**2 + (ponto2.y - ponto3.y)**2)
                    lado3= math.sqrt((ponto3.x - ponto1.x)**2 + (ponto3.y - ponto1.y)**2)
                    if Interferencia.verificarTriangulo(lado1,lado2,lado3) and round(lado1, 4)==round(lado2, 4)==round(lado3, 4):
                        triangulo = TrianguloEquilatero(ponto1,ponto2,ponto3,self.dashboard.contagem)
                        print('\n')
                        print('=='*50)
                        self.dashboard.inserirFigura(triangulo)
                        self.dashboard.printFormas()
                        print('\n')
                        print('=='*50)
                    else:
                        print('\n')
                        print('=='*50)
                        print("digitos validos, porem nao formam um triangulo equilatero")
                        print('\n')
                        print('=='*50)
                else:
                    print('\n')
                    print('=='*50)
                    print("digitos inválidos, as coordenadas devem estar no primeiro quadrante ")
                    print('\n')
                    print('=='*50)
            else:
                print('\n')
                print('=='*50)
                print("Digitos invalidos")
                print('\n')
                print('=='*50)
        elif escolha =="7":
            x1 = input("Digite a coordenada x do ponto 1: ")
            y1 = input("Digite a coordenada y do ponto 1: ")
            x2 = input("Digite a coordenada x do ponto 2: ")
            y2 = input("Digite a coordenada y do ponto 2: ")
            x3 = input("Digite a coordenada x do ponto 3: ")
            y3 = input("Digite a coordenada y do ponto 3: ")

            if self.eh_numero(x1) and self.eh_numero(y1) and self.eh_numero(x2) and self.eh_numero(y2) and self.eh_numero(x3) and self.eh_numero(y3):
                if float(x1)>= 0 and float(y1)>= 0 and float(x2)>= 0 and float(y2)>= 0 and float(x3)>=0 and float(y3)>=0:
                    ponto1 = Point(float(x1),float(y1),None)
                    ponto2 = Point(float(x2),float(y2),None)
                    ponto3 = Point(float(x3),float(y3),None)
                    lado1= math.sqrt((ponto2.x - ponto1.x)**2 + (ponto2.y - ponto1.y)**2)
                    lado2= math.sqrt((ponto2.x - ponto3.x)**2 + (ponto2.y - ponto3.y)**2)
                    lado3= math.sqrt((ponto3.x - ponto1.x)**2 + (ponto3.y - ponto1.y)**2)
                    if Interferencia.verificarTriangulo(lado1,lado2,lado3) and ( round(lado1, 4)==round(lado2, 4) or round(lado1, 4)==round(lado3,2) or round(lado2, 4)==round(lado3,2) ):
                        triangulo = TrianguloIsoceles(ponto1,ponto2,ponto3,self.dashboard.contagem)
                        print('\n')
                        print('=='*50)
                        self.dashboard.inserirFigura(triangulo)
                        self.dashboard.printFormas()
                        print('\n')
                        print('=='*50)
                    else:
                        print('\n')
                        print('=='*50)
                        print("digitos validos, porem nao formam um triangulo isoceles")
                        print('\n')
                        print('=='*50)
                else:
                    print('\n')
                    print('=='*50)
                    print("digitos inválidos, as coordenadas devem estar no primeiro quadrante ")
                    print('\n')
                    print('=='*50)
            else:
                print('\n')
                print('=='*50)
                print("Digitos invalidos")
                print('\n')
                print('=='*50)
        else:
            print('\n')
            print('=='*50)
            print("opcao invalida")
            print('\n')
            print('=='*50)
        
    def crash(self):
        if len(self.dashboard.figuras)==0:
            print('\n')
            print('=='*50)
            print("não há nenhuma figura armazenada para atualizar")
            print('\n')
            print('=='*50)
        else:
            print('\n')
            print('=='*50)
            self.dashboard.printFormas()
            while True:
                try:
                    escolha = input("digite o nome da classe que quer verificar interferencia com o numero identificador dele EX: Point0: ")
                    if escolha == 'EXIT':
                        break
                    else:
                        control = 0
                        for i in self.dashboard.figuras.keys():
                            if i == escolha:
                                control =+ 1
                                if self.dashboard.figuras[i].nome == 'Point':

                                    x=input("digite a coordenada X: ")
                                    y=input("digite a coordenada Y: ")

                                    if self.eh_numero(x) and self.eh_numero(y):
                                        if float(x)>=0 and float(y)>=0:
                                            if self.dashboard.figuras[i].x == float(x) and self.dashboard.figuras[i].y == float(y):
                                                print("Seus pontos são iguais")
                                                print('\n')
                                                print('=='*50)
                                            else:
                                                print("Seus pontos são diferentes")
                                                print('\n')
                                                print('=='*50)
                                        else:
                                            print("digitos inválidos, as coordenadas devem estar no primeiro quadrante")
                                            print('\n')
                                            print('=='*50) 
                                    else:
                                        print("digitos inválidos")
                                        print('\n')
                                        print('=='*50)
                                elif self.dashboard.figuras[i].nome == 'SegReta':
                                    print("\nEssa função não verifica se o ponto está dentro de um Segmento de reta, mas sim se ele está dentro ou nas proximidades")

                                    x=input("digite a coordenada X: ")
                                    y=input("digite a coordenada Y: ")

                                    if self.eh_numero(x) and self.eh_numero(y):
                                        if float(x)>=0 and float(y)>=0:
                                            ponto = Point(float(x),float(y), None)
                                            z= Interferencia.verificacaoSegReta(ponto,self.dashboard.figuras[i])
                                            if z == True:
                                                print("o ponto está no dominio da figura")
                                                print('\n')
                                                print('=='*50)
                                            else:
                                                print("o ponto nao está no dominio da figura")
                                                print('\n')
                                                print('=='*50)
                                        else:
                                            print("digitos inválidos, as coordenadas devem estar no primeiro quadrante") 
                                            print('\n')
                                            print('=='*50) 
                                    else:
                                        print("digitos inválidos")
                                        print('\n')
                                        print('=='*50)
                                elif self.dashboard.figuras[i].nome == 'Circle':
                                    x=input("digite a coordenada X: ")
                                    y=input("digite a coordenada Y: ")

                                    if self.eh_numero(x) and self.eh_numero(y):
                                        if float(x)>=0 and float(y)>=0:
                                            ponto = Point(float(x),float(y), None)
                                            z=Interferencia.verificacaoCirculo(self.dashboard.figuras[i].raio,ponto,self.dashboard.figuras[i].centro)
                                            if z == True:
                                                print("o ponto está no dominio da figura")
                                                print('\n')
                                                print('=='*50)
                                            else:
                                                print("o ponto nao está no dominio da figura")
                                                print('\n')
                                                print('=='*50)
                                        else:
                                            print("digitos inválidos, as coordenadas devem estar no primeiro quadrante")
                                            print('\n')
                                            print('=='*50) 
                                    else:
                                        print("digitos inválidos")
                                        print('\n')
                                        print('=='*50)
                                elif self.dashboard.figuras[i].nome == 'Quadrado' or self.dashboard.figuras[i].nome == 'Retangulo':
                                    x=input("digite a coordenada X: ")
                                    y=input("digite a coordenada Y: ")

                                    if self.eh_numero(x) and self.eh_numero(y):
                                        if float(x)>=0 and float(y)>=0:
                                            ponto = Point(float(x),float(y), None)
                                            z=Interferencia.verificacaoQuadradoRetangulo(self.dashboard.figuras[i].inf_esq,self.dashboard.figuras[i].sup_esq,self.dashboard.figuras[i].sup_dir,self.dashboard.figuras[i].inf_dir,ponto)

                                            if z == True:
                                                print("o ponto está no dominio da figura")
                                                print('\n')
                                                print('=='*50)
                                            else:
                                                print("o ponto nao está no dominio da figura")
                                                print('\n')
                                                print('=='*50)
                                        else:
                                            print("digitos inválidos, as coordenadas devem estar no primeiro quadrante")
                                            print('\n')
                                            print('=='*50)  
                                    else:
                                        print("digitos inválidos")
                                        print('\n')
                                        print('=='*50)
                                elif self.dashboard.figuras[i].nome == 'TrianguloEquilatero' or self.dashboard.figuras[i].nome == 'TrianguloIsoceles':
                                    x=input("digite a coordenada X: ")
                                    y=input("digite a coordenada Y: ")

                                    if self.eh_numero(x) and self.eh_numero(y):
                                        if float(x)>=0 and float(y)>=0:
                                            ponto = Point(float(x),float(y), None)
                                            z=Interferencia.verificacaoTriangulo(self.dashboard.figuras[i].ponto1,self.dashboard.figuras[i].ponto2,self.dashboard.figuras[i].ponto3,ponto)

                                            if z == True:
                                                print("o ponto está no dominio da figura")
                                                print('\n')
                                                print('=='*50)
                                            else:
                                                print("o ponto nao está no dominio da figura")
                                                print('\n')
                                                print('=='*50)
                                        else:
                                            print("digitos inválidos, as coordenadas devem estar no primeiro quadrante")
                                            print('\n')
                                            print('=='*50)  
                                    else:
                                        print("digitos inválidos")
                                        print('\n')
                                        print('=='*50)
                        if control>0:
                            break
                        else:
                            print("Tem que digitar Extamente o que aparece antes do primeiro underline, EX: SegReta0, caso deseja sair digite EXIT")
                except KeyError:
                    print("Tem que digitar Extamente o que aparece antes do primeiro underline, EX: SegReta0, caso deseja sair digite EXIT")

    def printarFormas(self):
        print('\n')
        print('=='*50)
        self.dashboard.printFormas()
        print('\n')
        print('=='*50)

    def atualizar(self):
        if len(self.dashboard.figuras)==0:
            print('\n')
            print('=='*50)
            print("não há nenhuma figura armazenada para atualizar")
            print('\n')
            print('=='*50)
        else:
            print('\n')
            print('=='*50)
            self.dashboard.printFormas()
            while True:
                try:
                    escolha = input("digite o nome da classe com o numero identificador dele EX: Point0 ")
                    if escolha == 'EXIT':
                        break
                    else:
                        control = 0
                        for i in self.dashboard.figuras.keys():
                            if i == escolha:
                                control =+ 1
                                if self.dashboard.figuras[i].nome == 'Point':
                                    x=input("digite a nova coordenada X: ")
                                    y=input("digite a nova coordenada Y: ")

                                    if self.eh_numero(x) and self.eh_numero(y):
                                        if float(x)>=0 and float(y)>=0:
                                            self.dashboard.figuras[i].x= float(x)
                                            self.dashboard.figuras[i].y = float(y)
                                            self.embelezador()
                                            print("Forma atualizada com sucesso")
                                            print('\n')
                                            print('=='*50)
                                        else:
                                            self.embelezador()
                                            print("digitos inválidos, as coordenadas devem estar no primeiro quadrante")
                                            print('\n')
                                            print('=='*50)  
                                    else:
                                        self.embelezador()
                                        print("digitos inválidos")
                                        self.embelezador()
                                elif self.dashboard.figuras[i].nome == 'SegReta':
                                    x1=input("digite a nova coordenada X de origem: ")
                                    y1=input("digite a nova coordenada Y de origem: ")
                                    x2=input("digite a nova coordenada X do final: ")
                                    y2=input("digite a nova coordenada Y do final: ")

                                    if self.eh_numero(x1) and self.eh_numero(y1) and self.eh_numero(x2) and self.eh_numero(y2):
                                        if float(x1)>=0 and float(y1)>=0 and float(x2)>=0 and float(y2)>=0 and (float(x1)!=float(x2) or float(y1)!=float(y2)):   

                                            self.dashboard.figuras[i].point_origem.x = float(x1)
                                            self.dashboard.figuras[i].point_origem.y = float(y1)
                                            self.dashboard.figuras[i].point_final.x = float(x2)
                                            self.dashboard.figuras[i].point_final.y = float(y2)
                                            self.embelezador()
                                            print("Forma atualizada com sucesso")
                                            self.embelezador()
                                        else:
                                            self.embelezador()
                                            print("digitos inválidos, as coordenadas devem estar no primeiro quadrante")
                                            self.embelezador()
                                    else:
                                        self.embelezador()
                                        print("digitos invalidos")
                                        self.embelezador()
                                elif self.dashboard.figuras[i].nome == 'Circle':
                                    x=input("digite a nova coordenada X do centro: ")
                                    y=input("digite a nova coordenada Y do centro: ")
                                    raio = input("digite o novo valor do raio: ")

                                    if self.eh_numero(x) and self.eh_numero(y) and self.eh_numero(raio):
                                        if float(x)>=0 and float(y)>=0 and float(raio)>=0:

                                            self.dashboard.figuras[i].centro.x = float(x)
                                            self.dashboard.figuras[i].centro.y = float(y)
                                            self.dashboard.figuras[i].raio = float(raio)
                                            self.embelezador()
                                            print("Forma atualizada com sucesso")
                                            self.embelezador()                    
                                        else:
                                            self.embelezador()
                                            print("digitos inválidos, as coordenadas devem estar no primeiro quadrante e o raio deve ser positivo")
                                            self.embelezador()
                                    else:
                                        self.embelezador()
                                        print("digitos invalidos")
                                        self.embelezador()
                                elif self.dashboard.figuras[i].nome == 'Quadrado':
                                    lado = input("digite o novo valor do lado do quadrado: ")
                                    print("\nA origem do quadrado é o lado inferior esquerdo")
                                    origemX = input("Digite a nova coordenada X da origem: ")
                                    origemY = input("Digite a nova coordenada y da origem: ")

                                    if self.eh_numero(lado) and self.eh_numero(origemY) and self.eh_numero(origemX):
                                        if float(lado)>=0 and float(origemY)>=0 and float(origemX)>=0:

                                            self.dashboard.figuras[i].lado = float(lado)
                                            self.dashboard.figuras[i].origem.x = float(origemX)
                                            self.dashboard.figuras[i].origem.y = float(origemY)
                                            self.embelezador()
                                            print("Forma atualizada com sucesso")
                                            self.embelezador()
                                        else:
                                            self.embelezador()
                                            print("digitos inválidos, as coordenadas devem estar no primeiro quadrante e o lado deve ser positivo")
                                            self.embelezador()   
                                    else:
                                        self.embelezador()
                                        print("Digitos invalidos")
                                        self.embelezador()
                                elif self.dashboard.figuras[i].nome == 'Retangulo':
                                    lado = input("digite o valor do novo comprimento do retangulo: ")
                                    lado2 = input("digite o valor da nova altura do retangulo: ")
                                    print("\nA origem do retangulo é o lado inferior esquerdo")
                                    origemX = input("Digite a nova coordenada X da origem: ")
                                    origemY = input("Digite a nova coordenada y da origem: ")

                                    if self.eh_numero(lado) and self.eh_numero(origemY) and self.eh_numero(origemX) and self.eh_numero(lado2):
                                        if float(lado)>=0 and float(origemY)>=0 and float(origemX)>=0 and float(lado2)>=0:
                                            self.dashboard.figuras[i].lado = float(lado)
                                            self.dashboard.figuras[i].lado2 = float(lado2)
                                            self.dashboard.figuras[i].origem.x = float(origemX)
                                            self.dashboard.figuras[i].origem.y = float(origemY)
                                            self.embelezador()
                                            print("Forma atualizada com sucesso")
                                            self.embelezador()
                                        else:
                                            self.embelezador()
                                            print("digitos inválidos, as coordenadas devem estar no primeiro quadrante e o lado deve ser positivo")
                                            self.embelezador()   
                                    else:
                                        self.embelezador()
                                        print("Digitos invalidos")
                                        self.embelezador()
                                elif self.dashboard.figuras[i].nome == 'TrianguloEquilatero':
                                    x1 = input("Digite a nova coordenada x do ponto 1: ")
                                    y1 = input("Digite a nova coordenada y do ponto 1: ")
                                    x2 = input("Digite a nova coordenada x do ponto 2: ")
                                    y2 = input("Digite a nova coordenada y do ponto 2: ")
                                    x3 = input("Digite a nova coordenada x do ponto 3: ")
                                    y3 = input("Digite a nova coordenada y do ponto 3: ")

                                    if self.eh_numero(x1) and self.eh_numero(y1) and self.eh_numero(x2) and self.eh_numero(y2) and self.eh_numero(x3) and self.eh_numero(y3):
                                        if float(x1)>= 0 and float(y1)>= 0 and float(x2)>= 0 and float(y2)>= 0 and float(x3)>=0 and float(y3)>=0:
                                            ponto1 = Point(float(x1),float(y1),None)
                                            ponto2 = Point(float(x2),float(y2),None)
                                            ponto3 = Point(float(x3),float(y3),None)
                                            lado1= math.sqrt((ponto2.x - ponto1.x)**2 + (ponto2.y - ponto1.y)**2)
                                            lado2= math.sqrt((ponto2.x - ponto3.x)**2 + (ponto2.y - ponto3.y)**2)
                                            lado3= math.sqrt((ponto3.x - ponto1.x)**2 + (ponto3.y - ponto1.y)**2)
                                            if Interferencia.verificarTriangulo(lado1,lado2,lado3) and round(lado1, 4)==round(lado2, 4)==round(lado3, 4):

                                                self.dashboard.figuras[i].ponto1.x= float(x1)
                                                self.dashboard.figuras[i].ponto1.y= float(y1)
                                                self.dashboard.figuras[i].ponto2.x= float(x2)
                                                self.dashboard.figuras[i].ponto2.y= float(y2)
                                                self.dashboard.figuras[i].ponto3.x= float(x3)
                                                self.dashboard.figuras[i].ponto3.y= float(y3)
                                                self.embelezador()
                                                print("Forma atualizada com sucesso")
                                                self.embelezador()
                                            else:
                                                self.embelezador()
                                                print("digitos validos, porem nao formam um triangulo equilatero")
                                                self.embelezador()
                                        else:
                                            self.embelezador()
                                            print("digitos inválidos, as coordenadas devem estar no primeiro quadrante ")
                                            self.embelezador()
                                    else:
                                        self.embelezador()
                                        print("Digitos invalidos")
                                        self.embelezador()
                                elif self.dashboard.figuras[i].nome == 'TrianguloIsoceles':
                                    x1 = input("Digite a coordenada x do ponto 1: ")
                                    y1 = input("Digite a coordenada y do ponto 1: ")
                                    x2 = input("Digite a coordenada x do ponto 2: ")
                                    y2 = input("Digite a coordenada y do ponto 2: ")
                                    x3 = input("Digite a coordenada x do ponto 3: ")
                                    y3 = input("Digite a coordenada y do ponto 3: ")

                                    if self.eh_numero(x1) and self.eh_numero(y1) and self.eh_numero(x2) and self.eh_numero(y2) and self.eh_numero(x3) and self.eh_numero(y3):
                                        if float(x1)>= 0 and float(y1)>= 0 and float(x2)>= 0 and float(y2)>= 0 and float(x3)>=0 and float(y3)>=0:
                                            ponto1 = Point(float(x1),float(y1),None)
                                            ponto2 = Point(float(x2),float(y2),None)
                                            ponto3 = Point(float(x3),float(y3),None)
                                            lado1= math.sqrt((ponto2.x - ponto1.x)**2 + (ponto2.y - ponto1.y)**2)
                                            lado2= math.sqrt((ponto2.x - ponto3.x)**2 + (ponto2.y - ponto3.y)**2)
                                            lado3= math.sqrt((ponto3.x - ponto1.x)**2 + (ponto3.y - ponto1.y)**2)
                                            if Interferencia.verificarTriangulo(lado1,lado2,lado3) and ( round(lado1, 4)==round(lado2, 4) or round(lado1, 4)==round(lado3,2) or round(lado2, 4)==round(lado3,2) ):
                                                self.dashboard.figuras[i].ponto1.x= float(x1)
                                                self.dashboard.figuras[i].ponto1.y= float(y1)
                                                self.dashboard.figuras[i].ponto2.x= float(x2)
                                                self.dashboard.figuras[i].ponto2.y= float(y2)
                                                self.dashboard.figuras[i].ponto3.x= float(x3)
                                                self.dashboard.figuras[i].ponto3.y= float(y3)
                                                self.embelezador()
                                                print("Forma atualizada com sucesso")
                                                self.embelezador()
                                            else:
                                                self.embelezador()
                                                print("digitos validos, porem nao formam um triangulo equilatero")
                                                self.embelezador()
                                        else:
                                            self.embelezador()
                                            print("digitos inválidos, as coordenadas devem estar no primeiro quadrante ")
                                            self.embelezador()
                                    else:
                                        self.embelezador()
                                        print("Digitos invalidos")
                                        self.embelezador() 
                        if control>0:
                            break
                        else:
                            print("Tem que digitar Extamente o que aparece antes do primeiro underline, EX: SegReta0, caso deseja sair digite EXIT")
                except KeyError:
                    print("Tem que digitar Extamente o que aparece antes do primeiro underline, EX: SegReta0, caso deseja sair digite EXIT")

    def calculos(self):
        if len(self.dashboard.figuras)==0:
            self.embelezador()
            print("não há nenhuma figura armazenada para realizar calculos")
            self.embelezador()
        else:
            self.embelezador()
            self.dashboard.printFormas()
            while True:
                try:
                    escolha = input("digite o nome da classe com o numero identificador dele EX: Point0 ")
                    if escolha == 'EXIT':
                        break
                    else:
                        control = 0
                        for i in self.dashboard.figuras.keys():
                            if i == escolha:
                                control =+ 1
                                if self.dashboard.figuras[i].nome == 'Point':
                                   print("Para um ponto podemos fazer as seguinte operações:")
                                   print("1. Distancia do Centro")
                                   print("2. Angulo em relação ao eixo X")
                                   escolha = input("Digite o numero do calculo que deseja realizar: ")

                                   if escolha == "1":
                                       print(f'a distancia do ponto à origem é {self.dashboard.figuras[i].distanceFC()}')
                                       self.embelezador()
                                   elif escolha =="2":
                                       print(f'o angulo entre a reta que passa pela origem e pelo ponto em relação e o eixo x é {self.dashboard.figuras[i].anguloX()} rad e em graus é {self.dashboard.figuras[i].anguloX()*180/math.pi}')
                                       self.embelezador()
                                   else:
                                       print("digite opções válidas")
                                       self.embelezador()
                                elif self.dashboard.figuras[i].nome == 'SegReta':
                                    print("Para um segmento de reta podemos fazer as seguinte operações:")
                                    print("1. Tamanho do segmento")
                                    escolha = input("Digite o numero do calculo que deseja realizar: ")

                                    if escolha =="1":
                                        print(f'o tamanho do segmento de reta é: {self.dashboard.figuras[i].tamanho()}')
                                        self.embelezador()
                                    else:
                                        print("digite opções válidas")
                                        self.embelezador()      
                                elif self.dashboard.figuras[i].nome == 'Circle':
                                    
                                    print("Para um circulo podemos fazer as seguinte operações:")
                                    print("1. Area do circulo")
                                    print("2. Equacao do circulo")
                                    print("3. perimetro")
                                    escolha = input("Digite o numero do calculo que deseja realizar: ")

                                    if escolha =="1":
                                        print(f'Sua area é {self.dashboard.figuras[i].area()} U.A')
                                        self.embelezador()
                                    elif escolha == "2":
                                        print("\nA equação do seu círculo é:")
                                        self.dashboard.figuras[i].equation()
                                        self.embelezador()
                                    elif escolha == "3":
                                        print(f'seu perimetro é {self.dashboard.figuras[i].perimetro()} U.C')
                                        self.embelezador()
                                    else:
                                        print("digite opções válidas")
                                        self.embelezador()  
                                    
                                elif self.dashboard.figuras[i].nome == 'Quadrado' or self.dashboard.figuras[i].nome == 'Retangulo':
                                    print("Para um Quadrado/retangulo podemos fazer as seguinte operações:")
                                    print("1. Area ")
                                    print("2. diagonal")
                                    print("3. perimetro")
                                    print("4. centro")
                                    escolha = input("Digite o numero do calculo que deseja realizar: ")

                                    if escolha =="1":
                                        print(f'Sua area é {self.dashboard.figuras[i].area()} U.A')
                                        self.embelezador()
                                    elif escolha == "2":
                                        print(f'sua diagonal é {self.dashboard.figuras[i].diagonal()} U.C')
                                        self.embelezador()
                                    elif escolha == "3":
                                        print(f'seu perimetro é {self.dashboard.figuras[i].perimetro()} U.C')
                                        self.embelezador()
                                    elif escolha == "4":
                                        print(f'a coordenada do centro é {self.dashboard.figuras[i].getCentro()}')
                                        self.embelezador()
                                    else:
                                        print("digite opções válidas")
                                        self.embelezador()
                                elif self.dashboard.figuras[i].nome == 'TrianguloEquilatero' or self.dashboard.figuras[i].nome == 'TrianguloIsoceles':
                                    print("Para um Triangulo podemos fazer as seguinte operações:")
                                    print("1. Area ")
                                    print("2. Baricentro")
                                    print("3. perimetro")
                                    print("4. altura")
                                    escolha = input("Digite o numero do calculo que deseja realizar: ")

                                    if escolha =="1":
                                        print(f'Sua area é {self.dashboard.figuras[i].area()} U.A')
                                        self.embelezador()
                                    elif escolha == "2":
                                        print(f'seu baricentro tem coordenadas[{self.dashboard.figuras[i].baricentro()}] ')
                                        self.embelezador()
                                    elif escolha == "3":
                                        print(f'seu perimetro é {self.dashboard.figuras[i].perimetro()} U.C')
                                        self.embelezador()
                                    elif escolha == "4":
                                        print(f'a a altura do triangulo é {self.dashboard.figuras[i].altura()}')
                                        self.embelezador()
                                    else:
                                        print("digite opções válidas") 
                                        self.embelezador()   
                        if control>0:
                            break
                        else:
                            print("Tem que digitar Extamente o que aparece antes do primeiro underline, EX: SegReta0")
                except KeyError:
                    print("Tem que digitar Extamente o que aparece antes do primeiro underline, EX: SegReta0")

    def distanciaPontos(self):
        contagemPontos = 0
        for i in self.dashboard.figuras.keys():
                if self.dashboard.figuras[i].nome =='Point':                                   
                    contagemPontos += 1
        if len(self.dashboard.figuras)==0:
            self.embelezador()
            print("não há nenhuma figura armazenada para realizar calculos")
            self.embelezador()
        elif contagemPontos<2:
            self.embelezador()
            print("é necessario ter pelo menos 2 pontos criados")
            self.embelezador()    
        else:
            self.embelezador()
            self.dashboard.printFormas()
            while True:
                try:
                    escolha = input("digite o nome do primeiro ponto com o numero identificador dele EX: Point0 ")
                    escolha2 = input("digite o nome do segundo ponto com o numero identificador dele EX: Point1 ")

                    if escolha == 'EXIT' or escolha2 =='EXIT':
                        break
                    else:

                        control = 0
                        for j in self.dashboard.figuras.keys():
                            if j == escolha:
                                for k in self.dashboard.figuras.keys():
                                    if k == escolha2:
                                        control+=1
                                        print(f"a distancia é {self.dashboard.figuras[j].distancePoints(self.dashboard.figuras[k])} U.C")
                                        self.embelezador()           
                    if control>0:
                        break
                    else:
                        print("Tem que digitar Extamente o que aparece antes do primeiro underline, EX: SegReta0")
                except KeyError:
                    print("Tem que digitar Extamente o que aparece antes do primeiro underline, EX: SegReta0")

    def run(self):

         while True:
             print("Escolha uma opção:")
             print("1. Criar forma geométrica")
             print("2. Verificar interferências")
             print("3. Imprimir as formas no sistema")
             print("4. Atualizar forma")
             print("5. Calculos da forma")
             print("6. Distancia entre 2 pontos existentes")
             print("7. Sair")
             escolha = input("Digite o número da opção selecionada: ")

             if escolha.isdigit() and int(escolha) in range(1,8):
                 selecao = list(self.actions.keys())[int(escolha)-1]
                 self.actions[selecao]()
             else:
                 self.embelezador()
                 print("Digite uma opçao válida.")
                 self.embelezador()



