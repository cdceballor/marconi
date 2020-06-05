import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16,12]
plt.rcParams.update({'font.size' : 18})


def main():
    s_rate, signal =wavfile.read('songs/bad_songs/not_good_song.wav')
    sample_badRate, badSample = wavfile.read('songs/bad_songs/not_good_song.wav')
    sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')


    dt = 0.001
    t = np.arange(0,1,dt)
    f_clean = samples[5000000:5001000]
    f = badSample[5000000:5001000]



    n = len(t)
    fhat = np.fft.fft(f,n)
    psd = fhat * np.conj(fhat) / n
    print(psd)
    freq = (1/(dt*n)) * np.arange(n)
    l = np.arange(1,np.floor(n/2),dtype = 'int')
    print(freq)
    fig,axs = plt.subplots(2,1)

    #Mismo calculos de arriba pero para la cancion limpia, esto para mostrar como es la solucion con respecto a la original
    Lhat = np.fft.fft(f_clean,n)
    lsd = Lhat * np.conj(Lhat) / n
#Crear varias inversas con filtros en lugares distintos para ver distintos posibles resultados
#---------Filtro 1------------------------
    indices1 = psd >100000000
    psdclean1 = psd * indices1
    fhat1 = indices1 * fhat
    
    ffilt1 = np.fft.ifft(fhat1)
#---------Filtro 2------------------------
    indices2 = psd >150000000
    psdclean2 = psd * indices2
    fhat2 = indices2 * fhat
    
    ffilt2 = np.fft.ifft(fhat2)
#---------Filtro 3------------------------
    indices3 = psd >200000000
    psdclean3 = psd * indices3
    fhat3 = indices3 * fhat
    
    ffilt3 = np.fft.ifft(fhat3)

    plt.sca(axs[0])
    plt.plot(freq[l],psd[l],color = 'c', LineWidth = 2, label = "Noisy")
    plt.plot(freq[l],lsd[l],color = 'k', LineWidth = 2, label = "Clean")
    plt.axhline(y=1000000000,color = 'y', LineWidth = 2, label = 'Filtered1')
    plt.axhline(y=1500000000,color = 'b', LineWidth = 2, label = 'Filtered2')
    plt.axhline(y=2000000000,color = 'r', LineWidth = 2, label = 'Filtered3')
    plt.xlim(freq[l[0]],freq[l[-1]])
    plt.ylabel("Espectro de poder")
    plt.xlabel("Frecuencia")
    plt.legend()

    plt.sca(axs[1])
    plt.plot(t,f_clean,color = 'k', LineWidth = 1.5,label = 'Clean')
    plt.plot(t,ffilt1,color = 'y', LineWidth = 2, label = 'Filtered1')
    plt.plot(t,ffilt2,color = 'b', LineWidth = 2, label = 'Filtered2')
    plt.plot(t,ffilt3,color = 'r', LineWidth = 2, label = 'Filtered3')
    plt.ylabel("Amplitud")
    plt.xlabel("Tiempo")
    plt.legend()









    fig,axs = plt.subplots(2,1)

    plt.sca(axs[0])
    plt.plot(t,f_clean,color = 'g', LineWidth = 2, label = 'clean')
    plt.plot(t,f,color = 'r', LineWidth = 1.5, label = 'noisy')
    plt.xlim(t[0],t[-1])
    plt.ylabel("Amplitud")
    plt.xlabel("Tiempo")
    plt.legend()


    plt.sca(axs[1])
    plt.plot(t,Lhat,color = 'c', LineWidth = 2, label = 'Clean')
    plt.plot(t,fhat,color = 'k', LineWidth = 2, label = 'Noisy')
    plt.xlim(t[0],t[-1])
    plt.ylabel("Amplitud")
    plt.xlabel("Frecuencia")
    plt.legend()

    # plt.sca(axs[1])
    # plt.plot(freq[l],psd[l],color = 'c', LineWidth = 1.5, label = 'noisy')
    # plt.plot(freq[l],psdclean1[l],color = 'k', LineWidth = 2, label = 'Filtered')
    # plt.xlim(freq[0],freq[-1])
    # plt.legend()    





    plt.show()


if __name__ == "__main__": 
    main()
