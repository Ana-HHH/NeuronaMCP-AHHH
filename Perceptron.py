import numpy as np
import neuronaMCP as mpc

class PerceptronSimple:
    def __init__(self, X, Y, epoch=100, learning_rate=0.01) -> None:
        self.X = X
        self.Y = Y
        self.epoch = epoch
        self.learning_rate = learning_rate

    def neurona(self, weights, x, treshhold):
        multiply_n = np.multiply(weights, x)
        sum_n = np.sum(multiply_n)

        if sum_n >= treshhold:
            return 1
        else: 
            return 0


    def fit(self):
        input_size = int(len(self.X))
        a = [0 for z in range(input_size)]

        temp_threshold =  np.random.randint(-100, 100, 1)
        temp_weights = np.random.randint(-100, 100, size=self.X.shape[1])

        for i in range(self.epoch):
            for n in range(input_size):
                a[n] = self.neurona(temp_weights, self.X[n], temp_threshold)
                
                error = self.Y[n] - a[n]

                if error>0:
                    temp_weights = temp_weights + self.X[n]
                    temp_threshold = temp_threshold + self.learning_rate * error
                elif error<0:
                    temp_weights = temp_weights - self.X[n]
                    temp_threshold = temp_threshold + self.learning_rate * error          
                else:
                    temp_weights = temp_weights
                 
        return temp_weights, a, temp_threshold

