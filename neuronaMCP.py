import numpy as np


class NeuronMCP:
    def __init__(self, s=2, n_inter=100, gate="AND") -> None:
        self.s = s
        self.n_iter = n_inter
        self.gate = gate
        self.tablasV = self.gateTabla()
        self.threshold = 0
        self.weights = []
        self.combinacion = []
        self.active = False

    def tabla(self, n=2):
        if n < 1:
            return [[]]
        subtabla = self.tabla(n-1)
        return [ fila + [v] for fila in subtabla for v in [0,1] ]
    
    def gateTabla(self):
        tabla = self.tabla(self.s)
        for t in tabla:
            if self.gate == "AND":
                if t.count(1) == self.s:
                    t.append(1)
                else:
                    t.append(0)
            elif self.gate == "OR":
                if t.count(1) >= 1:
                    t.append(1)
                else:
                    t.append(0)
            elif self.gate == "NOT":
                if t.count(1) >= 1:
                    t.append(0)
                else:
                    t.append(1)
        return tabla

    
    def mostrarTabla(self):
         print(self.tablasV)
            
    def solve(self):
        self.threshold = 0
        self.weights = []
        self.combinacion = []
        self.active = False

        for i in range(self.n_iter):
            temp_threshold =  np.random.randint(-100, 100, 1)
            temp_weights = np.random.randint(-100, 100, size=self.s)

            for t in self.tablasV:
                if t[-1] == 0:
                    continue
                else:
                    multiply_n = np.multiply(t[:-1], temp_weights)
                    sum_n = np.sum(multiply_n)
                
                    if sum_n >= temp_threshold:
                        self.threshold = temp_threshold
                        self.weights = temp_weights
                        self.combinacion = t
                        self.active = True
                        print('Se encontro el umbral y pesos para la neurona')
                        break
            if self.active:
                break

    def status(self):
        print('Combinacion: ', self.combinacion )       
        print('Umbral: ', self.threshold )       
        print('Peso: ', self.weights )       
        print('Estatus: ', self.active )       





