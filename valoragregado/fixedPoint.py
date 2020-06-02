import math
class fixedPoint:
    
    def __init__(self, Fx, Gx, nIter, tolerance, X0):
        self.Fx = Fx
        self.Gx = Gx
        self.nIter = nIter
        self.tolerance = tolerance
        self.X0 = X0
            
    

    def f(self,x):
        fx1=self.Fx.replace("x",str(x))
        return eval(fx1)

    def g(self,x):
        gx1=self.Gx.replace("x",str(x))
        print(gx1)
        return eval(gx1)

    def fixed_point(self):
        X0=self.X0
        fx = self.f(X0)
        error = self.tolerance + 1
        tol=self.tolerance
        niter=self.nIter
        cont = 1
        p=("| n:  |" + "      " +"| X0: |" + "      "+"| F(x): |" +"      "+ "| error: |"+"\n")
        
        
        while fx != 0 and error > tol and cont < niter:
            xn = self.g(X0)
            fx = self.f(xn)
            # relative error
            error = abs((xn-X0)/xn)
            #abs error
            #error = abs(xn-x0)
            p+="| " + str(cont) + " | " + str(X0) + " | " + str(fx) + " | " + str(error) + " | "+"\n"
            cont = cont + 1
            X0 = xn
        
        if fx == 0:
            p+= str(X0) + " is a root"
            p+= " ,iterations: " + str(cont)
            p+= " ,F(X): " + str(fx)
            p+= " ,error: " + str(error)+"\n"
            p+= "This is the case that say - F(x) = 0 -"
        elif error <= tol:

            p+= str(X0) + " is a root with tolerance = " + str(tol)
            p+= " iterations: " + str(cont)
            p+= " F(X): " + str(fx)
            p+= " error: " + str(error)+"\n"
        else:
            p+= "failed in " + str(cont) + ": iterations"



        return p
    # 5 cifras: 5 * 10^-5
    # 5 decimales: 0.5 * 10^-5
    #fixed_point(-0.5, 5 * math.pow(10,-5), 20)