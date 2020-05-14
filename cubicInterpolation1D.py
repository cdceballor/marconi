from scipy.io import wavfile
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import dangerzone as dz
import recognize, utils

def cubitInterpolation1D():
    sample_rate, sample = wavfile.read('songs/hakuna_matata.wav')
    sample = sample[5000000:5000100]

    BadSample = sample.copy()
    dz.theEvilMethod(BadSample, 0.5, blocksize=2)

    matches = recognize.cheat(sample, BadSample)
    x, y = utils.tovalidxy(BadSample, matches)
    f = interp1d(x, y, kind='cubic', fill_value='extrapolate')
    utils.repair(BadSample, matches, f)
    wavfile.write('songs/generator_song/regen_song.wav', sample_rate, BadSample)
    IwannaSee(sample, BadSample)


def IwannaSee(sample, BadSample):

    plt.title('Cubic interpolation 1D')
    plt.xlabel('Frame')
    plt.ylabel('Amplitude')
    plt.plot(sample, label='real')
    plt.plot(BadSample, label='interpolated')
    plt.legend(loc='best')
    plt.show()

cubitInterpolation1D()
