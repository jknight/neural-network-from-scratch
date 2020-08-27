#!/usr/bin/python
import math
import random

class NeuralNetwork(): 
    def __init__(self):
        # seed the random number generator, so we get the 
        # same numbers each time
        random.seed(1) 

        # create 3 weights & set them to random between -1 and 1
        self.weights = [random.uniform(-1, 1),
                        random.uniform(-1, 1),
                        random.uniform(-1, 1)]

    def think(self, neuron_inputs):
        sum_of_weighted_inputs = self.__sum_of_weighted_inputs(neuron_inputs)
        neuron_output = self.__sigmoid(sum_of_weighted_inputs)
        return neuron_output 

    def train(self, training_set_examples, number_of_iterations):
        for it in range(number_of_iterations):
            for training_set_example in training_set_examples:
                # predict the output based on inputs
                predicted_output = self.think(training_set_example["inputs"])

                # how much was the prediction wrong by ?
                # calculate error as diff b/t desired output & predicted output
                error_in_output = training_set_example["output"] - predicted_output

                # now start adjusting for weights - minimize total error
                for index in range(len(self.weights)): 
                    # get neuron input associated with this weight
                    neuron_input = training_set_example["inputs"][index]

                    # calculate how much to adjust the weights by using the detail rule 
                    #  (gradient descent)
                    # The idea is that if the prediction is way off, adjust a lot
                    #   but if the error is small, make a smaller adjustment
                    adjust_weight = neuron_input * error_in_output * self.__sigmoid_gradient(predicted_output)
                       
                    # adjust the weight
                    self.weights[index] += adjust_weight



    # there are different types of activation functions in neural networks - 
    # we're using a sigmod function here
    def __sigmoid(self, sum_of_weighted_inputs):
        # Todo: is this correct ? 1 / 1 + e^(-NeuronInput)
        #  - where's the e ? 
        return 1 / (1 + math.exp(-sum_of_weighted_inputs))

    def __sigmoid_gradient(self, neuron_output):
        return neuron_output * (1 - neuron_output)

    def __sum_of_weighted_inputs(self, neuron_inputs):
        # Could use matrix algebra instead
        sum_of_weighted_inputs = 0
        for index, neuron_input in enumerate(neuron_inputs):
            sum_of_weighted_inputs += self.weights[index] * neuron_input
        return sum_of_weighted_inputs


nn = NeuralNetwork()
print("Random starting weights", str(nn.weights))

training_set = [ 
        {"inputs": [0,0,1], "output": 0},
        {"inputs": [1,0,1], "output": 1},
        {"inputs": [0,1,1], "output": 0},
        {"inputs": [1,0,1], "output": 1},
        ]

# Now train the network so it can learn from this training set
nn.train(training_set, number_of_iterations = 10000)
print("Weights after training", str(nn.weights))

# Make a prediction for a new situation
new_situation = [1,1,1]
prediction = nn.think(new_situation)
print("Prediction for a new situation" + str(new_situation) + "==>" + str(prediction))
