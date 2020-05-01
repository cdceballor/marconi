import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import dangerzone as distorsion

archivo = 'hakuna_matata.wav' #Archivo
muestreo, sonido = waves.read(archivo) #muestreo = frecuencia de datos por segundo, sonido = datos del sonido
# canales: monofónico o estéreo
tamano = np.shape(sonido)
muestras = tamano[0]
m = len(tamano)
canales = 1  # monofónico
if (m>1):  # estéreo
    canales = tamano[1]
# experimento con un canal
if (canales>1):
    canal = 0
    uncanal = sonido[:canal]
else:
    uncanal = sonido
    # rango de observación en segundos
inicia = 1.000
termina = 3.002
# observación en número de muestra
a = int(inicia*muestreo)
b = int(termina*muestreo)
parte = uncanal[a:b]
# Salida # Archivo de audio.wav
print('archivo de parte[] grabado...')
waves.write('salidaProcesada.wav', muestreo, parte)
# tiempos en eje x
dt = 1/muestreo
ta = a*dt
tb = (b-1)*dt
tab = np.arange(ta,tb,dt)
plt.plot(tab,parte)
plt.xlabel('tiempo (s)')
plt.ylabel('Amplitud')
plt.show()

