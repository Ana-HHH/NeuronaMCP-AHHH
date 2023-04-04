import numpy as np
import neuronaMCP as mpc
from Perceptron import PerceptronSimple as p

# neuronaA = mpc.NeuronMCP(3, 100, "OR")

# neuronaA.mostrarTabla()
# neuronaA.solve()
# neuronaA.status()

## datos de entrenamientos sacados de CodigoMaquina 
# Datos de 10 personas -> [edad, ahorro]
personas = np.array([[0.3, 0.4], [0.4, 0.3],
                     [0.3, 0.2], [0.4, 0.1], 
                     [0.5, 0.2], [0.4, 0.8],
                     [0.6, 0.8], [0.5, 0.6], 
                     [0.7, 0.6], [0.8, 0.5]])
# 1 : aprobrada    0 : denegada
clases = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

perceprtronA = p(X=personas, Y=clases)

resultado = perceprtronA.fit()

print(resultado)