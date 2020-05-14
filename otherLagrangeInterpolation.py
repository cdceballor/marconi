from scipy.io import wavfile
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import dangerzone as dz
import recognize, utils
import numpy as np

def otherLagrangeInterpolation():
    sample_rate, sample = wavfile.read('songs/hakuna_matata.wav')
    #sample = sample[5000000:5000100]
    x = np.array(range(0, 100))
    y = np.array(sample[5000000:5000100])  # We can change here to make the wave with more amplitude or not

    BadSample = y.copy()

    dz.theEvilMethod(BadSample, 0.5, blocksize=2)
    matches = recognize.cheat(y, BadSample)
    #x, y = utils.tovalidxy(BadSample, matches)
    f = lagrange(x,y)
    #utils.repair(BadSample, matches, f)
    IwannaSee(y, BadSample)

def IwannaSee(sample, BadSample):

    plt.title('Other Lagrange interpolation')
    plt.xlabel('Frame')
    plt.ylabel('Amplitude')
    plt.plot(sample, label='real')
    plt.plot(BadSample, label='interpolated')
    plt.legend(loc='best')
    plt.show()

otherLagrangeInterpolation()