import numpy as np
import math
from tabulate import tabulate


class MultipleR:

    def __init__(self, Fx, deriv, deriv2, nIter, tolerance, X0):
        self.Fx = Fx
        self.deriv = deriv
        self.deriv2 = deriv2
        self.nIter = nIter
        self.tolerance = tolerance
        self.X0 = X0

    def f(self, x):
        fx1 = self.Fx.replace("x", str(x))
        return eval(fx1)

    def dfx1(self, x):
        fx1 = self.deriv.replace("x", str(x))
        return eval(fx1)

    def dfx2(self, x):
        fx1 = self.deriv2.replace("x", str(x))
        return eval(fx1)

    def raices(self):

        x0 = float(self.X0)
        tolerancia = float(self.tolerance)
        niter = float(self.nIter)

        data_to_table = []

        fx = self.f(x0)
        fx1 = self.dfx1(x0)
        fx2 = self.dfx2(x0)

        den = (math.pow(fx1, 2)-fx*fx2)

        contador = 0
        error = tolerancia + 1

        data_to_table.append([contador, x0, fx, fx1, fx2, error])
        p = ""
        while error > tolerancia and fx != 0 and den != 0 and contador < niter:
            x1 = x0 - fx*fx1 / den
            print("fxantes: "+str(fx))
            fx = self.f(x1)
            print("fxdesp: "+str(fx))
            fx1 = self.dfx1(x1)
            fx2 = self.dfx2(x1)
            error = abs(x1 - x0)
            contador += 1
            x0 = x1
            data_to_table.append([contador, x0, fx, fx1, fx2, error])

        if fx == 0:
            p = str("x0={} es una raiz".format(x0))
            p += str("numero de iteraciones={}:".format(contador)+"\n")
        elif error < tolerancia:
            p = str("x1={} es una proximación a una raiz con una tolerancia={}".format(
                x1, tolerancia)+"\n")
        elif error < tolerancia:
            p = str("den={} " + "Denominador es 0"+"\n")
        else:
            p = str("Fracaso en niter={} iteraciones".format(niter)+"\n")

        p += "\n"
        p += (tabulate(data_to_table,
                       headers=["N", "X0", "F(X)", "F'(X)", "F''(X)", "error"]))

        return p
