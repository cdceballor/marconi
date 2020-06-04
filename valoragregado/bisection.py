import math


class bisection:
    def __init__(self, Fx, nIter, tolerance, X0, X1):
        self.Fx = Fx
        self.nIter = nIter
        self.tolerance = tolerance
        self.X0 = X0
        self.X1 = X1

    #Method where the function is evaluated
    def funcion(self,x):
        fx1=self.Fx.replace("x",str(x))
        print("xi: "+str(fx1))
        print("f: "+str(eval(fx1)))
        return eval(fx1)
        

    def biseccion(self):
        a=float(self.X0)
        print(a)
        b=float(self.X1)
        print(b)
        iteraciones=int(self.nIter)
        print(iteraciones)
        tolerancia=float(self.tolerance)
        print(tolerancia)

        #definicion de variables
        x0=0 
        y0=0 
        i=1
        medio = (a+b)/2
        resultado=self.funcion(medio)
        p=""
        #control de entrada de datos
        if iteraciones<1:
            p="Iterations must be greater than 0 (Error)"
            
        elif resultado == 0:
            p=str(medio)+" Its a root (Success)"
            
        elif self.funcion(a)*self.funcion(b)>0:
            p="There is no root in this interval (Error) "
              
    #First iteration
        #This algorithm stores all the data in a txt called biseccion.txt,
        #f=open("biseccion.txt","w+") 
        #Loop start
        else:

            while resultado!=0 and i<=iteraciones and math.fabs(x0-resultado)>tolerancia:
            #Control of process

            #las partes del write no estan en el pseudo codigo ya que esto
            #es un adicional, no hace parte del algoritmo
            #f.write("--------")
            #f.write(
                p+="Iteration- "+str(i)+"Range: ["+str(a)+","+str(b)+"]  M= "+str(medio)+"  f(m)= "+str(resultado)+"\n"                    

                if i>1:
                    p+="Error: "+str(math.fabs(x0-medio))+"\n"
                #print(resultado*self.funcion(a))
                
                if resultado*self.funcion(a)>0:
                    a=medio
                else:
                    b=medio

                x0 = medio
                y0=resultado
                medio=(a+b)/2
                resultado=self.funcion(medio)
                i+=1   
        
            p+="\n"

        #Controles de salida (Exito/Fracaso)
            if resultado==0:
                p+="The root is: " +str(medio)+" (Success)"
            elif i>iteraciones:
                p+="Iteration limit reached (Failure)"
            elif math.fabs(x0-medio)<tolerancia:
                p+="The maximum tolerance permitted "+str(tolerancia)+ " But in the iteration "+str(i)+"\n"
                +"the maximum tolerance was reached "+str(math.fabs(x0-medio))+" (Fracaso)"

        return p