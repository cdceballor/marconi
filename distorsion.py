import matplotlib.pyplot as plt
from scipy.io import wavfile
#import dangerzone, posibleSolution

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
samplesDanger = samples[5000040:5000140] #We can change here to make the wave with more amplitude or not #We can change here to make the wave with more amplitude or not
samples = samples[5000000:5000100] #We can change here to make the wave with more amplitude or not

plt.subplot(211)

plt.title('Our song vs bad song')
plt.ylabel('Amplitude')
plt.plot(samples, label='real')
plt.plot(samplesDanger, label='damaged')
plt.legend(loc='best')

plt.show()