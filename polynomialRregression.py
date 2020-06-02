import scipy as cp
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

def polynomialReg():
    sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
    x = np.array(range(0,100))
    y = np.array(samples[5000000:5000100])
    plt.subplot(211)
    p1=cp.polyfit(x,y,1)
    p2 = cp.polyfit(x,y,2)
    p3 = cp.polyfit(x,y,3)
    p20 = cp.polyfit(x,y,20)
    #graficamos
    plt.plot(x,y,'r',label="Original")
    plt.plot(x,cp.polyval(p1,x),'b--',label="Grado 1")
    plt.plot(x,cp.polyval(p2,x),'m--',label="Grado 2")
    plt.plot(x,cp.polyval(p3,x),'g--',label="Grado 3")
    plt.plot(x,cp.polyval(p20,x),'k--',label="Grado 20")
    plt.legend()
    plt.show()

polynomialReg()
