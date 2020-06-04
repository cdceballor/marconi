import numpy as np
import utiles
from tabulate import tabulate

class Crouty:

    def __init__(self,mat):
        self.mat=mat


    def crout(self):
        pr=""
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

        l=np.zeros((len(mat),len(mat[0])))
        u=np.zeros((len(mat),len(mat[0])))
        for a in range(len(mat)):
            u[a][a]=1

        for k in range(len(mat)):
            sum1=0
            for p in range(k):
                sum1+= l[k][p]*u[p][k]
            l[k][k]= mat[k][k]-sum1
            for i in range(k+1,len(mat)):
                sum2=0
                for p in range(k):
                    sum2+=l[i][p]*u[p][k]
                l[i][k]=(mat[i][k]-sum2)/u[k][k]
            
            for j in range(k+1,len(mat)):
                sum3=0
                for p in range(k):
                    sum3+=l[k][p]*u[p][j]
                u[k][j]=(mat[k][j]-sum3)/(l[k][k])

            for x in range(len(mat)):
                l[x][len(mat[0])-1]=mat[x][len(mat[0])-1]
            zx=utiles.suslu(l)
            
            for x in range(len(mat)):
                u[x][len(l[0])-1]=zx[x]


        pr+= "                  MATRIZ L:\n"
        pr+= (tabulate(l, stralign='decimal'))
        pr+= "\n"
        pr+= "                  MATRIZ U:\n"
        pr+= (tabulate(u, stralign='decimal'))
        pr+= "\n"
        pr+= "|        ZX1        |      ZX2         |         ZX3         |       ZX4        |\n"
        pr+= str(utiles.susre(l))+"\n"
        pr+= "|         X1        |       X2         |          X3         |        X4        |\n"
        pr+=  str(utiles.susre(u))
        pr+= "\n"

        return pr
                
            #x=utiles.susre(u)
            #l, u, zx, x