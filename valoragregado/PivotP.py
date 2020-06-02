import numpy as np
import utiles

class PivotP:
    

    def __init__(self, n, mat): 
        self.n = n
        self.mat = mat
    
    def pivoteo(matrix_pr, i):
        mayor = round(abs(matrix_pr[i][i]), 3)
        filamayor = i
        for a in range(i+1, len(matrix_pr)):
            if abs(matrix_pr[a][i]) > mayor:
                mayor = round(abs(matrix_pr[a][i]))
                filamayor = a

        if mayor == 0:
            p+=("El sistema no tiene solucion")
        elif i != filamayor:
            matrix_pr[[i, filamayor]] = matrix_pr[[filamayor, i]]


    def parcial(self):
        a = self.mat.split(";")
        n = self.n
        cont = 0
        p = ""
        if(n == 3):
            arr0 = a[0].split(",")
            arr1 = a[1].split(",")
            arr2 = a[2].split(",")
            matrix_pr = arr0, arr1, arr2
        elif(n == 4):
            arr0 = a[0].split(",")
            arr1 = a[1].split(",")
            arr2 = a[2].split(",")
            arr3 = a[3].split(",")
            matrix_pr = arr0, arr1, arr2, arr3
        elif(n == 5):
            arr0 = a[0].split(",")
            arr1 = a[1].split(",")
            arr2 = a[2].split(",")
            arr3 = a[3].split(",")
            arr4 = a[4].split(",")
            matrix_pr = arr0, arr1, arr2, arr3, arr4
        elif(n == 6):
            arr0 = a[0].split(",")
            arr1 = a[1].split(",")
            arr2 = a[2].split(",")
            arr3 = a[3].split(",")
            arr4 = a[4].split(",")
            arr5 = a[5].split(",")
            matrix_pr = arr0, arr1, arr2, arr3, arr4, arr5

        for i in range(0,len(matrix_pr)):
            matrix_pr =pivoteo(matrix_pr,i)
            for j in range(i+1,len(matrix_pr)):
                mult = round(matrix_pr[j][i]/matrix_pr[i][i],3)
                p+=("Multiplicador "+str(mult))
                for k in range(i,len(matrix_pr[0])):
                    matrix_pr[j][k]= round(matrix_pr[j][k]-(mult*matrix_pr[i][k]),3)
            p+=str(utiles.printmat(matrix_pr))
        p+= str(utiles.printmat(utiles.susre(matrix_pr)))
        return p

        utiles.printmat(matrix_pr)



