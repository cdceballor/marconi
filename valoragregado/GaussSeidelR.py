import  numpy as np

class GaussSeidelR:

    def __init__(self,mat, b, n,error,itera, lam):
        self.mat=mat
        self.b = b
        self.n = n
        self.error = error
        self.itera = itera
        self.lam = lam

    def GaussSR(self):
        mat=self.mat.replace("[","")
        mat=mat.replace("]","")
        mat=mat.split(",")
        mat = np.array(mat)        
        mat = mat.astype(np.float)
        err = float(self.error)
        n = int(self.n)
        iterat = int(self.itera)
        mat = mat.reshape(n, n)
        lambd = float(self.lam)
        p=""

        b = self.b.split(",")

        for i in range(len(b)):
            b[i] = float(b[i])

        x=np.zeros_like(b)

        for k in range(iterat):
            for i in range(len(b)):
                x[i]=lambd*((b[i]-np.sum(mat[i][:i]*x[:i])-np.sum(mat[i][i+1:]*x[i+1:]))/mat[i][i])+(1-lambd)*x[i-1]

            e=np.linalg.norm(mat@x-b)
            p+= str(k)+" "+str(x)+" "+str(e)+"\n"
            if e<err:
                break

        return p