import tkinter as tk
from tkinter import ttk
from incrementalSearches import *
from bisection import *
from falsePosition import *
from fixedPoint import *
from newton import *
from secante import *
from MultipleR import *
from PivotP import*
from pivoteoSimple import*

class IntroFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Bienvenidos al aplicativo de analisis numerico 2020-1 \n\n Los miembros del equipo son los siguientes: \n    -Luis Bernardo Zuluaga\n    -Juan Felipe Londono Gaviria\n    -Cristian Dario Ceballos\n    -Juan Pablo Giraldo Restrepo")
        self.label.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("\n\nSi desea realizar los calculos en alguno de los metodos\n haga click en su respectiva casilla.")
        self.label.pack()
        
        

class Incremental_Searches(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the equation")
        self.label.pack()

        self.X = ttk.Entry(self)
        self.X.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the number of iterations")
        self.label.pack()

        self.nIter = ttk.Entry(self)
        self.nIter.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the delta")
        self.label.pack()

        self.delta = ttk.Entry(self)
        self.delta.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the initial value for x")
        self.label.pack()

        self.x0 = ttk.Entry(self)
        self.x0.pack()
        


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = incrementalSearches(self.X.get(),int(self.nIter.get()),float(self.delta.get()),float(self.x0.get()))
        self.label["text"] = I1.run()



class Bisec(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the equation")
        self.label.pack()

        self.X = ttk.Entry(self)
        self.X.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the number of iterations")
        self.label.pack()

        self.nIter = ttk.Entry(self)
        self.nIter.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the tolerance")
        self.label.pack()

        self.tolerance = ttk.Entry(self)
        self.tolerance.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the inferior limit of the interval")
        self.label.pack()

        self.x0 = ttk.Entry(self)
        self.x0.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the superior limit of the interval")
        self.label.pack()

        self.x1 = ttk.Entry(self)
        self.x1.pack()
        


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()
        

    def answer(self):
         I1 = bisection(self.X.get(),int(self.nIter.get()),float(self.tolerance.get()),float(self.x0.get()),float(self.x1.get()))
         self.label["text"] = I1.biseccion()



class Falsep(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the equation")
        self.label.pack()

        self.X = ttk.Entry(self)
        self.X.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the number of iterations")
        self.label.pack()

        self.nIter = ttk.Entry(self)
        self.nIter.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the tolerance")
        self.label.pack()

        self.tolerance = ttk.Entry(self)
        self.tolerance.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the inferior limit of the interval")
        self.label.pack()

        self.x0 = ttk.Entry(self)
        self.x0.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the superior limit of the interval")
        self.label.pack()

        self.x1 = ttk.Entry(self)
        self.x1.pack()
        


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()
        

    def answer(self):
         I1 = falsePosition(self.X.get(),int(self.nIter.get()),float(self.tolerance.get()),float(self.x0.get()),float(self.x1.get()))
         self.label["text"] = I1.FalseP()



class Fixedp(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the Fx equation")
        self.label.pack()

        self.Fx = ttk.Entry(self)
        self.Fx.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the Gx equation")
        self.label.pack()

        self.Gx = ttk.Entry(self)
        self.Gx.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the number of iterations")
        self.label.pack()

        self.nIter = ttk.Entry(self)
        self.nIter.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the tolerance")
        self.label.pack()

        self.tolerance = ttk.Entry(self)
        self.tolerance.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the X0")
        self.label.pack()

        self.x0 = ttk.Entry(self)
        self.x0.pack()

        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()
        

    def answer(self):
         I1 = fixedPoint(self.Fx.get(),self.Gx.get(),int(self.nIter.get()),float(self.tolerance.get()),float(self.x0.get()))
         self.label["text"] = I1.fixed_point()



class Newton(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the Fx equation")
        self.label.pack()

        self.Fx = ttk.Entry(self)
        self.Fx.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the derivative")
        self.label.pack()

        self.derivative = ttk.Entry(self)
        self.derivative.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the number of iterations")
        self.label.pack()

        self.nIter = ttk.Entry(self)
        self.nIter.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the tolerance")
        self.label.pack()

        self.tolerance = ttk.Entry(self)
        self.tolerance.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the X0")
        self.label.pack()

        self.x0 = ttk.Entry(self)
        self.x0.pack()

        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()
        

    def answer(self):
        I1 = newton(self.Fx.get(),self.derivative.get(),int(self.nIter.get()),float(self.tolerance.get()),float(self.x0.get()))
        self.label["text"] = I1.newton1()



class Secant(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the Fx equation")
        self.label.pack()

        self.Fx = ttk.Entry(self)
        self.Fx.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the number of iterations")
        self.label.pack()

        self.nIter = ttk.Entry(self)
        self.nIter.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the tolerance")
        self.label.pack()

        self.tolerance = ttk.Entry(self)
        self.tolerance.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the X0")
        self.label.pack()

        self.x0 = ttk.Entry(self)
        self.x0.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the X1")
        self.label.pack()

        self.x1 = ttk.Entry(self)
        self.x1.pack()

        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()
        

    def answer(self):
        I1 = Secante(self.Fx.get(),int(self.nIter.get()),float(self.tolerance.get()),float(self.x0.get()),float(self.x1.get()))
        self.label["text"] = I1.secante()



class Root(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the Fx equation")
        self.label.pack()

        self.Fx = ttk.Entry(self)
        self.Fx.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the first derivative")
        self.label.pack()

        self.deriv = ttk.Entry(self)
        self.deriv.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the second derivative")
        self.label.pack()

        self.deriv2 = ttk.Entry(self)
        self.deriv2.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the number of iterations")
        self.label.pack()

        self.nIter = ttk.Entry(self)
        self.nIter.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the tolerance")
        self.label.pack()

        self.tolerance = ttk.Entry(self)
        self.tolerance.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the X0")
        self.label.pack()

        self.x0 = ttk.Entry(self)
        self.x0.pack()


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()
        

    def answer(self):
        I1 = MultipleR(self.Fx.get(),self.deriv.get(),self.deriv2.get(),int(self.nIter.get()),float(self.tolerance.get()),float(self.x0.get()))
        self.label["text"] = I1.raices()



class Gauss(ttk.Frame):

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the n")
        self.label.pack()

        self.n = ttk.Entry(self)
        self.n.pack()
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the Matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()
        
        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        self.label = ttk.Label(self)
        self.label.pack()


    def answer(self):
        I1 = pivoteoSimple(int(self.n.get()), self.mat.get())
        self.label["text"] = I1.pivoteoS()



class PivotParc(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()


    def answer(self):
        I1 = PivotP(int(self.n.get()),self.mat.get())
        self.label["text"] = I1.main()



class PivotTot(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class PPivot(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class Crout(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class Doolittle(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class Cholesky(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class Jacobi(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class GausS(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class JacobS(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class GausR(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class Integ(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class NumericDif(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class NewtonD(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class Lagr(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class Spline1(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class Spline2(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class Spline3(ttk.Frame):
    #Phased Pivot
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the matrix")
        self.label.pack()

        self.mat = ttk.Entry(self)
        self.mat.pack()  

        self.label = ttk.Label(self)
        self.label["text"] = ("Insert the size of the matrix")
        self.label.pack()

        self.size = ttk.Entry(self)
        self.size.pack() 


        self.calculate = ttk.Button(
            self, 
            text="Calculate", 
            command = self.answer
            )
        self.calculate.pack()

        
        
        self.label = ttk.Label(self)
        self.label.pack()

    def answer(self):
        I1 = PivotP(self.mat.get(),self.size.get())
        self.label["text"] = I1.main()



class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Numerical Analysis")
        
        self.notebook = ttk.Notebook(self)
        self.intro_frame = IntroFrame(self.notebook)
        self.notebook.add(
            self.intro_frame,
            text="Introduction", 
            padding=10
            )

        self.incremental_searches = Incremental_Searches(self.notebook)
        self.notebook.add(
            self.incremental_searches, 
            text="Incremental Searches", 
            padding=10
            )
        
        self.bisecc = Bisec(self.notebook)
        self.notebook.add(
            self.bisecc,
            text="Bisection",
            padding=10
            )

        self.falsep = Falsep(self.notebook)
        self.notebook.add(
            self.falsep,
            text="False Position",
            padding=10
            )

        self.fixedp = Fixedp(self.notebook)
        self.notebook.add(
            self.fixedp,
            text="Fixed point",
            padding=10
            )

        self.newton = Newton(self.notebook)
        self.notebook.add(
            self.newton,
            text="Newton",
            padding=10
            )

        self.secante = Secant(self.notebook)
        self.notebook.add(
            self.secante,
            text="Secant",
            padding=10
            )

        self.root = Root(self.notebook)
        self.notebook.add(
            self.root,
            text="Multiple Roots",
            padding=10
            )

        self.gauss = Gauss(self.notebook)
        self.notebook.add(
            self.gauss,
            text="Gauss",
            padding=10
            )

        self.Pivot = PivotParc(self.notebook)
        self.notebook.add(
            self.Pivot,
            text="Partial Pivoting",
            padding=10
            )

        self.PivotT = PivotTot(self.notebook)
        self.notebook.add(
            self.PivotT,
            text="Complete Pivoting",
            padding=10
            )

        self.pPivot = PPivot(self.notebook)
        self.notebook.add(
            self.pPivot,
            text="Phased Pivoting",
            padding=10
            )

        self.crout = Crout(self.notebook)
        self.notebook.add(
            self.crout,
            text="Crout",
            padding=10
            )

        self.doolittle = Doolittle(self.notebook)
        self.notebook.add(
            self.doolittle,
            text="Doolittle",
            padding=10
            )

        self.cholesky = Cholesky(self.notebook)
        self.notebook.add(
            self.cholesky,
            text="Cholesky",
            padding=10
            )


        self.jacobi = Jacobi(self.notebook)
        self.notebook.add(
            self.jacobi,
            text="Jacobi",
            padding=10
            )

        self.gausS = GausS(self.notebook)
        self.notebook.add(
            self.gausS,
            text="Gauss Seidel",
            padding=10
            )

        self.jacobs = JacobS(self.notebook)
        self.notebook.add(
            self.jacobs,
            text="Relaxed Jacobi",
            padding=10
            )

        self.gausr = GausR(self.notebook)
        self.notebook.add(
            self.gausr,
            text="Relaxed Gauss-Seidel",
            padding=10
            )

        self.numericdif = NumericDif(self.notebook)
        self.notebook.add(
            self.numericdif,
            text="Numeric Diferentiation",
            padding=10
            )


        self.trap = Integ(self.notebook)
        self.notebook.add(
            self.trap,
            text="Numerical Integration",
            padding=10
            )

        self.newtond = NewtonD(self.notebook)
        self.notebook.add(
            self.newtond,
            text="Newton Divided Differences",
            padding=10
            )


        self.lagr = Lagr(self.notebook)
        self.notebook.add(
            self.lagr,
            text="Lagrange",
            padding=10
            )


        self.spline1 = Spline1(self.notebook)
        self.notebook.add(
            self.spline1,
            text="Linear Spline",
            padding=10
            )


        self.spline2 = Spline2(self.notebook)
        self.notebook.add(
            self.spline2,
            text="Squared Spline",
            padding=10
            )


        self.spline3 = Spline3(self.notebook)
        self.notebook.add(
            self.spline3,
            text="Cubic Spline",
            padding=10
            )

        self.notebook.pack(padx=10, pady=10)
        self.pack()

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()



