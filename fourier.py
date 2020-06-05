import scipy.io.wavfile as wavfile
import numpy as np


def main():
    s_rate, signal =wavfile.read('songs/bad_songs/bad_song.wav')
    sample_badRate, badSample = wavfile.read('songs/bad_songs/bad_song.wav')
    sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
    producto =[]

    dt = 0.001
    t = np.arange(0,3,dt)
    print(len(badSample))
    for a in range(0,int(len(badSample)-3000),3000):
        f = badSample[a:a+3000]
        n = len(t)
        fhat = np.fft.fft(f,n)
        psd = fhat * np.conj(fhat) / n
        freq = (1/(dt*n)) * np.arange(n)
        indices = psd >150000000
        psdclean = psd * indices
        fhat = indices * fhat
        ffilt = (np.fft.ifft(fhat))/10000
        producto = np.append(producto,ffilt.real)

    wavfile.write("furier.wav",sample_badRate,producto)


if __name__ == "__main__": 
    main()
