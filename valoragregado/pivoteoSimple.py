import utiles
import numpy
# Metodo para gauss simple


class pivoteoSimple:

    def __init__(self, n, mat):
        self.n = n
        self.mat = mat

    def pivoteoS(self):
        a=self.mat.split(";")
        n=self.n
        cont = 0
        p = ""


        if(n==3):
            arr0 = a[0].split(",")
            arr1 = a[1].split(",")
            arr2 = a[2].split(",")
            matrix_pr = arr0, arr1, arr2
        elif(n==4):
            arr0 = a[0].split(",")
            arr1 = a[1].split(",")
            arr2 = a[2].split(",")
            arr3 = a[3].split(",")
            matrix_pr = arr0, arr1, arr2, arr3
        elif(n==5):
            arr0 = a[0].split(",")
            arr1 = a[1].split(",")
            arr2 = a[2].split(",")
            arr3 = a[3].split(",")
            arr4 = a[4].split(",")
            matrix_pr = arr0, arr1, arr2, arr3,arr4
        elif(n==6):
            arr0 = a[0].split(",")
            arr1 = a[1].split(",")
            arr2 = a[2].split(",")
            arr3 = a[3].split(",")
            arr4 = a[4].split(",")
            arr5 = a[5].split(",")
            matrix_pr = arr0, arr1, arr2, arr3,arr4, arr5

        for i in range(len(matrix_pr)):
            for j in range(i+1, len(matrix_pr)):
                mult = float(matrix_pr[j][i])/float(matrix_pr[i][i])
                for k in range(i, len(matrix_pr[0])):
                    matrix_pr[j][k] = float(matrix_pr[j][k])-(mult*float(matrix_pr[i][k]))
                    cont += 1
                    p += str(utiles.printmat(matrix_pr))
        p += "-----------------------------\n"
        p += "Sustitución Regresiva\n"
        p+= str(utiles.susre(pivoteoS(matrix_pr)))
        print(p)
        return p

