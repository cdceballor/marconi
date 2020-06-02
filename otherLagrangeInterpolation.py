from scipy.io import wavfile
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import dangerzone as dz
import recognize
import numpy as np

def otherLagrangeInterpolation():
    sample_rate, sample = wavfile.read('songs/hakuna_matata.wav')
    x = np.array(range(0, 100))
    y = np.array(sample[5000000:5000100])

    sample_rateBAD, sampleBAD = wavfile.read('songs/bad_songs/not_good_song.wav')
    sampleBAD = sampleBAD[5000000:5000100]

    BadSample = y.copy()

    dz.theEvilMethod(BadSample, 0.5, blocksize=2)
    matches = recognize.cheat(y, BadSample)
    f = lagrange(x,y)
    IwannaSee(y, BadSample, sampleBAD)
    

def IwannaSee(sample, BadSample, sampleBAD):

    plt.title('Other Lagrange interpolation')
    plt.xlabel('Frame')
    plt.ylabel('Amplitude')
    plt.plot(sample, label='real')
    plt.plot(sampleBAD, label='Bad')
    plt.plot(BadSample, label='interpolated')
    plt.legend(loc='best')
    plt.show()

otherLagrangeInterpolation()