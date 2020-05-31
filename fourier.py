import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16,12]
plt.rcParams.update({'font.size' : 18})


def main():
    s_rate, signal =wavfile.read('marconi-master/songs/bad_songs/hakuna_rosa.wav')
    sample_badRate, badSample = wavfile.read('marconi-master/songs/bad_songs/hakuna_rosa.wav')
    sample_rate, samples = wavfile.read('marconi-master/songs/hakuna_matata.wav')
    producto =[]

    dt = 0.001
    t = np.arange(0,30,dt)
    print(len(badSample))
    for a in range(0,int(len(badSample)),30000):
        f = badSample[a:a+30000]
        n = len(t)
        fhat = np.fft.fft(f,n)
        psd = fhat * np.conj(fhat) / n
        freq = (1/(dt*n)) * np.arange(n)
        indices = psd >400000000
        psdclean = psd * indices
        fhat = indices * fhat
        ffilt = (np.fft.ifft(fhat))/30000
        producto = np.append(producto,ffilt.real)

    wavfile.write("furier.wav",sample_badRate,producto)


if __name__ == "__main__": 
    main()
