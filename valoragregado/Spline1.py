class Spline1:

    def __init__(self,x,y,n):
        self.x=x
        self.y=y
        self.n=n


    def SplineLineal(self):
        
        p="\n"
        x = self.x.split(",")
        fx = self.y.split(",")
        n = int(self.n)

        for i in range(len(x)):
            x[i] = float(x[i])

        for j in range(len(fx)):
            fx[j] =float(fx[j])


        for i in range(1,n):
            pendiente = (fx[i] - fx[i-1])/(x[i] - x[i-1])
            resultado = (pendiente * -x[i]) + fx[i]
            p+="P(X" + str(i) + ") = " + str(pendiente) + "X + " + str(resultado) + "        " + str(x[i-1]) + " <= X <= " + str(x[i])+"\n"

        return p