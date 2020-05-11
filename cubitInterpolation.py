from scipy.io import wavfile
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import dangerzone as dz

sample_rate, sample = wavfile.read('songs/hakuna_matata.wav')
sample = sample[5000000:5000100]

BadSample = sample.copy()
#sample_rate, BadSample = wavfile.read('../songs/bad_songs/bad_song.wav')
#BadSample = BadSample[5000000:5000100]

dz.theEvilMethod(BadSample, 0.5, blocksize=2)

f = interp1d(BadSample, sample, kind='cubic', fill_value='interpolation')

plt.title('Cubic interpolation')
plt.xlabel('Frame')
plt.ylabel('Amplitude')
plt.plot(sample, label='real')
plt.plot(BadSample, label='interpolated')
plt.legend(loc='best')
plt.show()