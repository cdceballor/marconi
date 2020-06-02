import numpy as np
import utiles

def pivoteo(matrix_pr,i,x):
    sub = np.array(matrix_pr[i:len(matrix_pr),i:len(matrix_pr)])
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
        print("El sistema no tiene solucion")
        return 0
    else :
        print(mayor)
        print(i)
        if i != filamayor+i: 
            swap=matrix_pr[i+filamayor,len(matrix_pr[0])-1]
            matrix_pr[i+filamayor,len(matrix_pr[0])-1]=matrix_pr[i,len(matrix_pr[0])-1]
            matrix_pr[i,len(matrix_pr[0])-1]=swap
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
    for x in range(i,len(matrix_pr)):
        for y in range(i,len(matrix_pr)):
            matrix_pr[x][y]=sub[a][b]
            b+=1
        b=0
        a+=1
    return mat





def total(self):
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
    
    
    x=np.array(range(len(matrix_pr)))
    x=[y+1 for y in x]
    for i in range(0,len(matrix_pr)):
        matrix_pr = pivoteo(matrix_pr,i,x)
        for j in range(i+1,len(matrix_pr)):
            mult = matrix_pr[j][i]/matrix_pr[i][i]
            
            for k in range(i,len(matrix_pr[0])):
                matrix_pr[j][k]= matrix_pr[j][k]-(mult*matrix_pr[i][k])

    p+=str(utiles.printmat(matrix_pr))
    p+=str(utiles.susre(matrix_pr))
    return p


    




