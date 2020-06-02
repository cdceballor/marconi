from scipy.io import wavfile
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import dangerzone as dz
import recognize, utils

def cubicSplineInterpolation():
    sample_rate, sample = wavfile.read('songs/hakuna_matata.wav')
    #sample = sample[5000000:5000100]

    BadSample = sample.copy()

    dz.theEvilMethod(BadSample, 0.5)
    matches = recognize.cheat(sample, BadSample)
    x, y = utils.tovalidxy(BadSample, matches)
    f = CubicSpline(x,y)

    xNotValid = utils.invalidx(matches)
    fixedy = f(xNotValid)
    utils.replace(BadSample, xNotValid, fixedy)
    wavfile.write('songs/generator_song/regen_cubitSpline_song.wav', sample_rate, BadSample)

cubicSplineInterpolation()