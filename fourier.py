import numpy as np
import scipy as cp
from scipy.io import wavfile
from scipy import fftpack
import matplotlib.pyplot as plt
from pandas import DataFrame
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error, r2_score

def metricas(y_verdad,y_predic):
    return mean_squared_error(y_verdad, y_predic, squared = False)
    #print("R^2: "+str(r2_score(y_verdad,y_predic)))


def main():
    '''
    cargando las canciones
    '''
    sample_badRate, badSample = wavfile.read('marconi-master/songs/bad_songs/bad_song.wav')
    sample_rate, samples = wavfile.read('marconi-master/songs/hakuna_matata.wav')
     #definicion de los puntos
    x = np.array(range(0,1000))
    y = badSample[5000000:5001000] #cancion mala
    buena=samples[5000000:5001000]   
    producto=np.array([])
    #pendiente determinar si se debe dividir la funcion por un periodo, pendiente determinar un periodo adecuado

    time_step = 0.05

    time_vec = np.arange(0,1000, time_step)
    y_fit = fftpack.fft(y)
    amplitude = np.abs(y_fit)
    poder = amplitude**2
    angulo = np.angle(y_fit)
    sample_freq = fftpack.fftfreq(y.size, d=time_step)
    amp_freq = np.array([amplitude , sample_freq])
    amp_position = amp_freq[0,:].argmax()
    peak_freq = amp_freq[1, amp_position]
    high_freq_fft = y_fit.copy()
    high_freq_fft[abs(sample_freq) > 0.8 ] = 0

    y_filtro = fftpack.ifft(high_freq_fft)
    print(amp_freq)
    print(peak_freq)
    #graficar(x,y)
    p15 = cp.polyfit(x,y,71)
    '''
    vamos a calcular el RMSe buenos de una de los p calculados
    '''
    promedio=metricas(y,cp.polyval(p15,x))
    yrmas=[x+promedio for x in cp.polyval(p15,x)]
    yrmenos=[x-promedio for x in cp.polyval(p15,x)]

    '''
    vamos a calcular el RMSe malos de una de los p calculados

    '''
    #graficamos los puntos y cada una de las regressiones
    plt.figure(1)
    plt.plot(buena,"r",label="Original")
    plt.plot(y,'y', label="Dañada")
    plt.plot(x,yrmas,'b', label="Mas promedio")
    plt.plot(x,yrmenos,'b', label="Menos promedio")
    plt.plot(y_filtro.real,'g',label = "Inversa")

    plt.figure(2)
    plt.plot(amplitude,'b',label = "Amplitud sin filtrar")
    plt.plot(high_freq_fft,'r',label = "Amplitud filtrada")
    plt.legend()
    plt.show()

    

if __name__ == "__main__": 
    main()
