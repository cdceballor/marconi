import random
from scipy.io import wavfile
import matplotlib.pyplot as plt

def danger():
    sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')

    badSamples = samples.copy()

    theEvilMethod(badSamples, 0.2) #we can change the value that is the percent with the song is broked
    plt.subplot(211)

def theEvilMethod(y, percent, blocksize=1):
    i = 0
    while i < len(y):
        if random.random() < percent:
            m = min(blocksize, len(y) - i)
            y[i:i + m] = [0] * m
            i += m
        else:
            i += 1

danger()
