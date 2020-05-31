import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16,12]
plt.rcParams.update({'font.size' : 18})


def main():
    s_rate, signal =wavfile.read('marconi-master/songs/bad_songs/bad_song.wav')
    sample_badRate, badSample = wavfile.read('marconi-master/songs/bad_songs/bad_song.wav')
    sample_rate, samples = wavfile.read('marconi-master/songs/hakuna_matata.wav')


    dt = 0.001
    t = np.arange(0,1,dt)
    f_clean = samples[5000000:5001000]


    f = badSample[5000000:5001000]
    n = len(t)
    fhat = np.fft.fft(f,n)
    psd = fhat * np.conj(fhat) / n

    freq = (1/(dt*n)) * np.arange(n)
    l = np.arange(1,np.floor(n/2),dtype = 'int')

    fig,axs = plt.subplots(2,1)
    plt.ticklabel_format(style='plain')

    plt.sca(axs[0])
    plt.plot(t,f,color = 'c', LineWidth = 1.5,label = 'Ruido')
    plt.plot(t,f_clean,color = 'k', LineWidth = 2,label = 'Limpia')
    plt.legend()
    plt.sca(axs[1])
    plt.plot(freq[l],psd[l],color = 'c', LineWidth = 2, label = "Ruido")
    plt.xlim(freq[l[0]],freq[l[-1]])
    plt.legend

    indices = psd >210000000
    psdclean = psd * indices
    fhat = indices * fhat
    ffilt = np.fft.ifft(fhat)

    fig,axs = plt.subplots(3,1)

    plt.sca(axs[0])
    plt.plot(t,f,color = 'r', LineWidth = 1.5, label = 'Ruido')
    plt.plot(t,f_clean,color = 'g', LineWidth = 2, label = 'Limpia')
    plt.xlim(t[0],t[-1])
    plt.legend()

    plt.sca(axs[1])
    plt.plot(t,f,color = 'c', LineWidth = 2, label = 'Ruido')
    plt.plot(t,f_clean,color = 'g', LineWidth = 1.5, label = 'Limpia')
    plt.plot(t,ffilt,color = 'k', LineWidth = 2, label = 'Filtrada')

    plt.xlim(t[0],t[-1])
    plt.legend()

    plt.sca(axs[2])
    plt.plot(freq[l],psd[l],color = 'c', LineWidth = 1.5, label = 'Ruido')
    plt.plot(freq[l],psdclean[l],color = 'k', LineWidth = 2, label = 'Filtrada')
    plt.xlim(freq[0],freq[-1])
    plt.legend()    





    plt.show()



if __name__ == "__main__": 
    main()
