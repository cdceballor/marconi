from scipy.io import wavfile
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import dangerzone as dz
import recognize, utils

def cubitInterpolation1D():
    sample_rate, sample = wavfile.read('songs/hakuna_matata.wav')
    #sample = sample[5000000:5000100]

    BadSample = sample.copy()

    dz.theEvilMethod(BadSample, 0.5)
    wavfile.write('songs/bad_songs/not_good_song.wav', sample_rate, BadSample)

    matches = recognize.cheat(sample, BadSample)
    x, y = utils.tovalidxy(BadSample, matches)
    f = interp1d(x, y, kind='cubic', fill_value='extrapolate')

    xNotValid = utils.invalidx(matches)
    fixedy = f(xNotValid)
    utils.replace(BadSample, xNotValid, fixedy)
    wavfile.write('songs/generator_song/regen_sinOriginal_song.wav', sample_rate, BadSample)

cubitInterpolation1D()
