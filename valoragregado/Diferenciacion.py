import numpy as np
import matplotlib.pyplot as plt
class Diferenciacion:

    def __init__(self,n, fx):
        self.n = n
        self.fx = fx


    def main(self):
        n = self.n.split(",")
        fx = self.fx.split(",")

        for i in range(len(n)):
            n[i] = float(n[i])

        for j in range(len(fx)):
            fx[j] =float(fx[j])

        p=""
    
        if(len(fx) >=2):
            a,b,c = self.derivative2(fx,n)
            p+= "Adelante para 2 puntos: "+str(a)+"\n"
            p+= "Atrás para 2 puntos: "+str(b)+"\n"
            p+= "Centro para 2 puntos: "+str(c)+"\n"
        
        if(len(fx)>=3):
            d,e,f = self.derivative3(fx,n)
            p+= "Los de 3: \n"
            p+= "Adelante para 3 puntos: "+str(d)+"\n"
            p+= "Atrás para 3 puntos: "+str(e)+"\n"
            p+= "Centro para 3 puntos: "+str(f)+"\n"
        
        if(len(fx)>=5):
            g,h,k = self.derivative5(fx,n)
            p+="Los de 5: \n"
            p+= "Adelante para 5 puntos: "+str(g)+"\n"
            p+= "Atrás para 5 puntos: "+str(h)+"\n"
            p+= "Centro para 5 puntos: "+str(k)+"\n"
        
        return p

    def derivative5(self,fx,n):
        a1 = n[0]
        a2 = n[1]
        h=float(a2)-float(a1)
        forw=np.zeros((len(fx)-4))
        back=np.zeros((len(fx)-4))
        midd=np.zeros((len(fx)-5))
    
        for n in range(len(fx)-4):
            v=(-25*fx[n])
            w=(48*fx[n+1])
            x=(-36*fx[n+2])
            y=(16*fx[n+3])
            z=(-3*fx[n+4])

            forw[n]=((v+w+x+y+z)/(h*12))

        for n in range(len(fx)-3,0,-1):
            back[n-2]=(((3*fx[n])-(4*fx[n-1])+(fx[n-2]))/(h))
        back[len(back)-1]=(((3*fx[len(fx)-1])-(4*fx[len(fx)-2])+(fx[len(fx)-3]))/(h))

        for n in range(2,len(fx)-3):
            w=fx[n-2]
            x=-fx[n+2]
            y=(-8*fx[n-1])
            z=(8*fx[n+1])
            midd[n-2]=(w+x+y+z)/(12*h)

        return forw,back,midd
    
    def derivative2(self, fx,n):
        a1 = n[0]
        a2 = n[1]
        h=float(a2)-float(a1)
        forw=np.zeros((len(fx)-1))
        back=np.zeros((len(fx)-1))
        midd=np.zeros((len(fx)-2))
    
        for n in range(len(fx)-1):
            forw[n]=(fx[n+1]-fx[n])/h

        for n in range(len(fx)-1,-1,-1):
            back[n-1]=(fx[n]-fx[n-1])/h
        back[len(back)-1]=(fx[len(fx)-1]-fx[len(fx)-2])/h

        for n in range(1,len(fx)-1):
            midd[n-1]=(fx[n+1]-fx[n-1])/(2*h)


        return forw,back,midd

    def derivative3(self,fx,n):
        a1 = n[0]
        a2 = n[1]
        h=float(a2)-float(a1)
        forw=np.zeros((len(fx)-2))
        back=np.zeros((len(fx)-2))
        midd=np.zeros((len(fx)-2))
    
        for n in range(len(fx)-2):
            x=(-3*fx[n])
            y=(4*fx[n+1])
            z=(-fx[n+2])

            forw[n]=((x+y+z)/(h*2))

    
        for n in range(len(fx)-1,0,-1):
            back[n-2]=(((3*fx[n])-(4*fx[n-1])+(fx[n-2]))/(0.2))
        back[len(back)-1]=(((3*fx[len(fx)-1])-(4*fx[len(fx)-2])+(fx[len(fx)-3]))/(h*2))

        for n in range(1,len(fx)-1):
            midd[n-1]=((fx[n+1]-fx[n-1]))/(2*h)


        return forw,back,midd

