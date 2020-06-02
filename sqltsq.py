from matplotlib import pyplot as plt
from scipy.optimize import leastsq
import numpy as np
from scipy.io import wavfile

sample_rate, sample = wavfile.read('songs/hakuna_matata.wav')
datos_x = np.array(range(0, 100))
y = np.array(sample[5000000:5000100])  # We can change here to make the wave with more amplitude or not

datos_y = y.copy()

# Defino la funcion de residuos
def residuos(p, y, x):
    error = y -p[0]*x + p[1]
    return error

# Parámetros iniciales
# la solución no convergerá
p0 = [1.0, 0.0]

# hacemos  el ajuste por minimos cuadrados
ajuste = leastsq(residuos, p0, args=(datos_y, datos_x))

# El resultado es una lista, cuyo primer elemento es otra
# lista con los parámetros del ajuste.
print(ajuste[0])
# array([ -9.787095  ,  32.91201348,  -2.3390355 ]

# Ahora muestro los datos y el ajuste gráficamente

plt.plot(datos_x, datos_y, 'o')  # datos

# Defino la funcion modelo, para representarla gráficamente
def funcion(x, p):
    return p[0]*x - p[1]

# genero datos a partir del modelo para representarlo
x1 = np.arange(0, datos_x.max(), 0.001)  # array con muchos puntos de x
y1 = funcion(x1, ajuste[0])           # valor de la funcion modelo en los x

plt.plot(x1, y1,)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Ajuste del problema con leastsq')
plt.legend(('Datos', 'Ajuste lineal'))
plt.show()