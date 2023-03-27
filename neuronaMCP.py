import numpy as np


class NeuronMCP:
    def __init__(self, s=2, n_inter=1000) -> None:
        self.s = s
        self.n_iter = n_inter
        self.tablasV = self.tabla(s)
        self.threshold = 0
        self.weights = []
        self.combinacion = []
        self.active = False

    def tabla(self, n=2):
        if n < 1:
            return [[]]
        subtabla = self.tabla(n-1)
        return [ fila + [v] for fila in subtabla for v in [0,1] ]
    
    def mostrarTabla(self):
         print(self.tablasV)
            
    def solve(self):
        for i in range(self.n_iter):
            temp_threshold =  np.random.randint(1, 100, 1)
            temp_weights = np.random.randint(-100, 100, size=self.s)

            for i in range(2**self.s):
                multiply_n = np.multiply(self.tablasV[i], temp_weights)
                sum_n = np.sum(multiply_n)

                if sum_n > temp_threshold:
                    self.threshold = temp_threshold
                    self.weights = temp_weights
                    self.combinacion = self.tablasV[i]
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





