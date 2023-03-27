import numpy as np

import neuronaMCP as mpc


neuronaA = mpc.NeuronMCP(3, 100)

neuronaA.mostrarTabla()
neuronaA.solve()
neuronaA.status()

