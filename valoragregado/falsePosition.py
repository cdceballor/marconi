import math
class falsePosition:

    def __init__(self, Fx, nIter, tolerance, X0, X1):
        self.Fx = Fx
        self.nIter = nIter
        self.tolerance = tolerance
        self.X0 = X0
        self.X1 = X1   

    #Method where the function is evaluated
    def funcion(self,x):
        fx1=self.Fx.replace("x",str(x))
        print(fx1)
        print("f: " + str(eval(fx1)))
        return eval(fx1)
        

    def FalseP(self):
        a=float(self.X0)
        b=float(self.X1)
        iteraciones=int(self.nIter)
        tolerancia=float(self.tolerance)
        
        #definicion de variables
        x0 = 0 #el m anterior
        y0 = 0 #el resultado de la funcion anterior
        i=1
        medio = a-((self.funcion(a)*(b-a))/(self.funcion(b)-self.funcion(a)))
        
        #medio = (a+b)/2
        resultado=self.funcion(medio)
        #control de entrada de datos
        p = ""
        if iteraciones<1:
            p = "Iterations must be greater than 0 (Error)"

        if resultado == 0:
            p = str(medio)+" Its a root (Success)"
            

        if self.funcion(a)*self.funcion(b)>0:
            p ="There is no root in this interval (Error) "
              
    #First iteration
        #This algorithm stores all the data in a txt called FalsePosition.txt, 
         #Loop start
        while resultado!=0 and i<=iteraciones and math.fabs(x0-medio)>tolerancia:
            #Control of process

            #las partes del write no estan en el pseudo codigo ya que esto
            #es un adicional, no hace parte del algoritmo
            p+="Iteration-"+str(i)+" Range: ["+str(a)+","+str(b)+"]  M= "+str(medio)+" f(m)= "+str(resultado)                        

            if i>1:
                p+=" Error: "+str(math.fabs(x0-medio))+"\n"
                #print(resultado*self.funcion(a))
            if resultado*self.funcion(a)>0:
                a=medio
            else:
                b=medio
            
            x0 = medio
            y0=resultado
            medio=a-((self.funcion(a)*(b-a))/(self.funcion(b)-self.funcion(a)))
            resultado=self.funcion(medio)
            i+=1 


        #Controles de salida (Exito/Fracaso)
        if resultado==0:
            p+= "The root is: " +str(medio)+" (Success)"
        elif i>iteraciones:
            p+= "Iteration limit reached (Failure)"
        elif math.fabs(x0-medio)<tolerancia:
            p+= "The maximum tolerance permitted "+str(tolerancia)+ " But in the iteration "+str(i)+"\n"
            +"the maximum tolerance was reached "+str(math.fabs(x0-medio))+" (Fracaso)"

        #print("\n\nData in the last iteration")
        #print("Iteration-"+str(i)+"\n"+"Range: ["+str(a)+","+str(b)+"]\nM= "+str(medio)+"\nf(m)= "+str(resultado)+"\n")
        #print("Tolerance: "+str(math.fabs(x0-medio))+"\n")
# i=Incremental()
# i.FalsePosition()
        return p