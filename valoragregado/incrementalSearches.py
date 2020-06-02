import math
import numpy as np
class incrementalSearches:

    def __init__(self,Fx,nIter,delta,X0):
        self.Fx = Fx
        self.nIter = nIter
        self.delta = delta
        self.X0 = X0


    def run(self):
        
        x=self.X0
        Y0=eval(self.Fx)
        #INPUT CONTROLS#
        p = ""
        if Y0 == 0:
            p= str(self.X0) + " is a root"
        elif self.delta == 0:
            p="Inappropriate Delta, It must be different from 0"
        elif self.nIter <= 0:
            p="Iterations must be greater than 0"
        else:                           #INPUT#
            X1 = self.X0 + self.delta
            Y1 = eval(self.Fx)
            count=1
            p="n    x    F(x)\n"
            p+=str(count)+"  "+str(X1)+"   "+str(Y1)+"\n"


            #CONTROL OF PROCESS#
            while Y0*Y1 >0 & count<self.nIter:
                #PROCESS#
                self.X0 = X1
                Y0 = Y1
                X1 = self.X0 + self.delta
                x = X1
                Y1 = eval(self.Fx)
                
                p+=str(count)+"   " +str(X1)+"   "+ str(Y1)+"\n"
                #a+=(x+"\n")
                print(count, "   ", X1,"   ", Y1)
                count=count+1
                
                
            p+="\n"  

            
            #OUTPUTS CONTROLS#
            if Y0*Y1 <0:
                p+="("+str(self.X0)+","+ str(X1)+ ")  define an interval"
            elif Y1 == 0:
                p+=str(X1)+" is a root"
            else: 
                p+="Failed in: "+str(self.nIter)

        print(p)                                                                                                                             
        return p



