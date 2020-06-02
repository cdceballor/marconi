from scipy.io import wavfile
from scipy.interpolate import Akima1DInterpolator
#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import dangerzone as dz
import recognize, utils
import numpy as np
sample_rate, sample = wavfile.read('songs/generator_song/regen_linear_song.wav')
sample = sample[5000000:5000100]

sample_rateOR, sampleOR = wavfile.read('songs/hakuna_matata.wav')
sampleOR = sampleOR[5000000:5000100]

sample_rateBAD, sampleBAD = wavfile.read('songs/bad_songs/not_good_song.wav')
sampleBAD = sampleBAD[5000000:5000100]

plt.title('1D interpolation solution')
plt.xlabel('Frame')
plt.ylabel('Amplitude')
plt.plot(sampleOR, label='Original')
plt.plot(sample, label='Interpolate')
plt.plot(sampleBAD, label='Bad')
plt.legend(loc='best')
plt.show()

