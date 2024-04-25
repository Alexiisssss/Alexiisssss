class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def weighted_sum(self, inputs):
        if len(inputs) != len(self.weights):
            return "Number of input must match numbers of weights"
        weighted_sum = self.bias
        for i in range(len(inputs)):
            weighted_sum += inputs[i] * self.weights[i]
        return weighted_sum

    def step_function(self, weighted_sum):
        return 1 if weighted_sum >= 0 else 0

    def sigmoid_function(self, weighted_sum):
        import math
        return 1 / (1 + math.exp(-weighted_sum))

    def relu_function(self, weighted_sum):
        return max(0, weighted_sum)


weights = [0.5, 0.3, 0.2]
bias = 0.1
neiron = Neuron(weights, bias)

inputs = [0.7, 0.2, 0.9]
weighted_sum = neiron.weighted_sum(inputs)
print("Weighted_sum:", weighted_sum)
print("Step function output:", neiron.step_function(weighted_sum))
print("Sigmoid function output", neiron.sigmoid_function(weighted_sum))
print("Relu function output", neiron.relu_function(weighted_sum))
