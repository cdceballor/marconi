from scipy.io import wavfile
import matplotlib.pyplot as plt

def danger():
    sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
#samples = samples[5000000:5000100] #We can change here to make the wave with more amplitude or not
    samples = samples[5000010:5000230] #We can change here to make the wave with more amplitude or not
    plt.subplot(211)

    plt.title('Bad song')
    plt.ylabel('Amplitude')
    plt.plot(samples, label='real')

    plt.show()

danger()
