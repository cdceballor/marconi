import numpy as np
import utiles
from tabulate import tabulate

class PivotP:
    

    def __init__(self,mat):

        self.mat=mat


    def pivoteo(self,mat,i):
        mayor = round(abs(mat[i][i]),3)
        filamayor = i
        for a in range(i+1,len(mat)):
            if abs(mat[a][i]) > mayor:
                mayor = round(abs(mat[a][i]))
                filamayor = a
        

        if mayor == 0:
            print("El sistema no tiene solucion")
            return 0
        elif i != filamayor: 
            mat[[i,filamayor]] = mat[[filamayor,i]]


        return mat

    def parcial(self):
        p=""
        mat=self.mat.replace("[","")
        mat=mat.replace("]","")
        mat=mat.split(",")
        mat = np.array(mat)        
        mat = mat.astype(np.float)
        print(mat)
        if len(mat) ==6:
            mat=mat.reshape(2,3)
        elif len(mat) ==12:
            mat = mat.reshape(3,4)
        elif len(mat) ==20:
            mat = mat.reshape(4,5)
        elif len(mat) ==30:
            mat = mat.reshape(5,6)
        elif len(mat) ==42:
            mat = mat.reshape(6,7)


        for i in range(0,len(mat)):
            mat =self.pivoteo(mat,i)
            for j in range(i+1,len(mat)):
                mult = round(mat[j][i]/mat[i][i],3)
                print("Multiplicador "+str(mult))
                for k in range(i,len(mat[0])):
                    mat[j][k]= round(mat[j][k]-(mult*mat[i][k]),3)

        
        
        p+= (tabulate(mat))
        p+= "\n"

        p+= "|         X1        |       X2         |          X3         |        X4        |\n"
        p+=  str(utiles.susre(mat)) 
        return p