import numpy as np

class Integracion:

    def __init__(self,n, fx):
        self.n=n
        self.fx=fx


    def main(self):
        n = self.n.split(",")
        fx = self.fx.split(",")

        for i in range(len(n)):
            n[i] = float(n[i])

        for j in range(len(fx)):
            fx[j] =float(fx[j])

        print(n)
        print("\n")
        print(fx)
        print("\n")

        p=""

        if (len(n)-1)%2 == 0:
            print("Entre 13\n")
            p+="Simpson 1/3: "+ str(self.Simpson13(n, fx))+"\n"
            p+="Simpson 1/3 Generalizado: "+ str(self.Simpson13Gen(n, fx))+"\n"


        if (len(n)-1)%3 == 0:
            print("Entre 38\n")
            p+="Simpson 3/8: "+ str(self.Simpson38(n, fx))+"\n"
            p+="Simpson 3/8 Gen: = "+ str(self.Simpson38Gen(n, fx))+"\n"

        p+="Trapecio: "+ str(self.Trapecio(n,fx))+"\n"
        print(str(self.Trapecio(n,fx)))
        p+="Trapecio Generalizado: "+str(self.TrapecioGen(n, fx))+"\n"
        print(str(self.TrapecioGen(n, fx)))
        return p


#Metodos para hallar las H de cada método de integral
    def getHGen(self,n):
        a1 = n[0]
        a2 = n[1]
        h=int(a2)-int(a1)
        return h

    def getHTrap(self,n):
        lastN = len(n)-1

        a1 = n[0]
        a2 = n[lastN]
        h = float(a2)-float(a1)
        return h

    def getHSim13(self, n):
        a1 = n[0]
        center = len(n)/2
        a2 = n[int(center)]
        h = float(a2) - float(a1)
        return h

    def getHSim38(self, n):
        a1 = n[0]
        a2 = n[int(len(n)/3)]
        h = float(a2)-float(a1)
        return h


#metodos para calcular las integrales.
    def Trapecio(self, n, fx):
        lastN = len(fx)-1
        firstF = float(fx[0])
        lastF = float(fx[lastN])

        den = 2*(firstF+lastF)
        num = self.getHTrap(n)

        resultT = num/den
        return resultT

    def TrapecioGen(self, n, fx):
        suma = 0
        for i in fx:
            suma = suma + i


        lastN = len(fx)-1
        firstF = float(fx[0])
        lastF = float(fx[lastN])
        suma = suma - firstF - lastF
        num = self.getHGen(n)
        den = 2*(firstF+lastF+2*suma)
        resultTG = float(num)/float(den)
        return resultTG

    def Simpson13(self, n, fx):
        lastN = len(fx)-1
        firstF = float(fx[0])
        lastF = float(fx[lastN])
        centerN = len(n)/2
        centerF = float(fx[int(centerN)])
        num = self.getHSim13(n)
        den = 3*(firstF+lastF+4*centerF)
    

        resultS13 = float(num)/float(den)
        return resultS13

    def Simpson13Gen(self, n, fx):

        lastN = len(fx)-1
        firstF = float(fx[0])
        lastF = float(fx[lastN])
        sumaP = sum(fx[::2])-firstF-lastF
        sumaImp = sum(fx[1::2])

        num = self.getHGen(n)
        sumaImp = 4*sumaImp
        sumaP = 2*sumaP
        den = 3*(firstF+lastF+sumaP+sumaImp)
        resultS13G = float(num)/float(den)
        return resultS13G


    def Simpson38(self, n, fx):
        lastN = len(fx)-1
        firstF = float(fx[0])
        lastF = float(fx[lastN])
        ot = float(fx[int(len(n)/3)])
        st = float(fx[int(len(n)*2/3)])

        num = 3*self.getHSim38(n)
        den = 8*(firstF+lastF+3*(ot+st))
        results38 = float(num)/float(den)
        return results38

    def Simpson38Gen(self, n, fx):
        lastN = len(fx)-1
        firstF = float(fx[0])
        lastF = float(fx[lastN])
        suma3 = sum(fx[::3])-lastF-firstF
        sumaR = 0
        for i in fx:
            sumaR = sumaR + i
    
        sumaR=sumaR-suma3-firstF-lastF
        num = 3*self.getHGen(n)
        den = 8*(firstF+lastF+2*suma3+3*sumaR)
        resultss38gen = float(num)/float(den)
        return resultss38gen

