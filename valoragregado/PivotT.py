import numpy as np
import utiles
from tabulate import tabulate

class PivotT:

    def __init__(self,mat):

        self.mat=mat


    def pivoteo(self,mat,i,x):
        sub = np.array(mat[i:len(mat),i:len(mat)])
        mayor = abs(sub[0][0])
        filamayor = 0
        columnamayor = 0
        for a in range(len(sub)):
            for b in range(len(sub)):
                if abs(sub[a][b]) > mayor:
                    mayor = abs(sub[a][b])
                    filamayor = a
                    columnamayor = b

        if mayor == 0:
            p="El sistema no tiene solucion"
            return p
        else :
            if i != filamayor+i: 
                swap=mat[i+filamayor,len(mat[0])-1]
                mat[i+filamayor,len(mat[0])-1]=mat[i,len(mat[0])-1]
                mat[i,len(mat[0])-1]=swap
                sub[[0,filamayor]] = sub[[filamayor,0]]
                
            if i != columnamayor+i:
                swap=x[i]
                x[i]=x[i+columnamayor]
                x[i+columnamayor]=swap
                for x in range(len(sub)):
                    swap=sub[x][0]
                    sub[x][0]=sub[x][columnamayor]
                    sub[x][columnamayor]=swap
        a=0
        b=0
        for x in range(i,len(mat)):
            for y in range(i,len(mat)):
                mat[x][y]=sub[a][b]
                b+=1
            b=0
            a+=1
        return mat

    def total(self):
        mat=self.mat.replace("[","")
        mat=mat.replace("]","")
        mat=mat.split(",")
        mat = np.array(mat)        
        mat = mat.astype(np.float)
        p=""

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

        x=np.array(range(len(mat)))
        x=[y+1 for y in x]
        for i in range(0,len(mat)):
            mat = self.pivoteo(mat,i,x)
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



