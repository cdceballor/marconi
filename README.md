# Marconi: reparación de audio por medio de métodos numéricos.

El siguiente proyecto se trabajó y elaboró en la universidad Eafit el semestre 2020-1 para la asignatura de Análisis numérico dictada por el maestro Francisto José Correa Zabala quien fue nuestro guía y tutor para la elaboración del mismo.
Los métodos trabajados se ejecutan uno por uno por medio del comando python3 (Ya que fueron elaborados en python) seguido del nombre del archivo con extensión .py

Librerías trabajadas en los métodos:

* 1DInterpolateShow.py
```sh
from scipy.io import wavfile, para leer la canción como archivo.

import matplotlib.pyplot as ply, para poder generar una gráfica graficar 
```
* Interpolation1D.py 
```sh
from scipy.io import wavfile, para leer la canción como archivo.
from scipy.interpolate import interp1d, para poder utilizar el método de interpolación de 1 grado en python.
```

* akimaInterpolation.py
```sh
from scipy.interpolate import Akima1DInterpolator, para utilizar el método de interpolación de Akima.
```

* cubicSplineInterpolation.py
```sh
from scipy.interpolate import CubicSpline, para implementar el spline cúbico en python.
```

* cubicSplineShow.py
```sh
from scipy.io import wavfile
import matplotlib.pyplot as plt
```

* dangerZone.py
```sh
import random, para poder generar valores aleatorios.
from scipy.io import wavfile
import matplotlib.pyplot as plt
```

* distorsion.py
```sh
import matplotlib.pyplot as plt
from scipy.io import wavfile
```

* fourier.py
```sh
import scipy.op.wavfile as wavefile
import numpy as np
import matplotlib.pyplot as plt
```
Es importante recalcar que para poder leer la canción, se debe tener en la raíz de jerarquías, o sea, se debe tener cuidado con la ruta que se coloca.

* fouriergraph.py
```sh
from scipy.io.wavfile as wavefile
import numpy as np
import matplotlib.pyplot as plt
```

* kroghInterpolator.py
```sh
from scipy.interpolate import KroghInterpolator, para utilizar la interpolación de Krogh en python.
from scipy.io import wavfile
import matplotlib.pyplot as plt
```
* lagrangeInterpolate.py
```sh
from scipy.io import wavfile
from scipy.interpolate import BarycentricInterpolator, para trabajar con la transformada de Lagrange.
import matplotlib.pyplot as plt
```

* otherLagrangeInterpolation.py
```sh
from scipy.io import wavfile
from scipy.interpolate import lagrange, para utilizar el polinomio interpolante de Lagrange.
import matplotlib.pyplot as plt
```

* pchip.py
```sh
from scipy.io import wavfile
from scipy.interpolate import pchip_interpolate, para utilizar el polinomio de Hermite de manera sencilla.
import matplotlib.pyplot as plt
```

* polinomialRegression.py
```sh
import scipy as cp, lo usamos para utiizar la librería polyfit que provee python para hacer regresión de n polinomios.
```

* recognize.py
```sh
import random, para poder generar valores aleatorios.
```

* splineUnivariableInterpolation.py
```sh
from scipy.io import wavfile
from scipy.interpolate import InterpolatedUnivariateSpline, para utilizar la interpolación no variante.
import matplotlib.pyplot as plt
```

* splineUnivariateShow.py
```sh
from scipy.io import wavfile
import matplotlib.pyplot as plt
```

* sqltsq.py
```sh
from matplotlib import pyplot as plt
from scipy,optimize import leastsq, implementamos un método de optimización que busca un conjunto de puntos dados relacionarlos con una funciin dada.
import numpy as np
```
