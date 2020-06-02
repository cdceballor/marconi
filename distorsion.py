import matplotlib.pyplot as plt
from scipy.io import wavfile

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
samples = samples[5000000:5000100]

sample_badRate, badSample = wavfile.read('songs/bad_songs/not_good_song.wav')
badSample = badSample[5000000:5000100]

plt.subplot(211)

plt.title('Our song vs bad song')
plt.ylabel('Amplitude')
plt.plot(samples, label='real')
plt.plot(badSample, label='damaged')
plt.legend(loc='best')

plt.show()