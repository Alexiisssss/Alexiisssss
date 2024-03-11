class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def weighted_sum(self, inputs):
        if len(inputs) != len(self.weights):
            raise ValueError("Number of input must match numbers of weights")
       weighted_sum = self.bias