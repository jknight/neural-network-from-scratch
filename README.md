## Problem

Given a input sequence of 4 numbers (0 or 1) that outputs a single number (0 or 1),
create a neural network that can predict the output.

Sample:

|               | Input | Ouput |
| --            | --    | --    |
| Example 1     | 0 0 1 | 0     |
| Example 2     | 1 1 1 | 1     |
| Example 3     | 1 0 1 | 1     |
| Example 4     | 0 1 1 | 1     |
| New Situation | 1 0 0 | ?     |

## Architecture

Three inputs and one output. Each input corresponds to an input digit:

Input 1 \
Input 2  --> neuron --> output
Input 3 /

## Weights

Weights are used to increase or reduce the strength of the signal.
Weights can be positive or negative. Negative weights inhibit the neuron from firing.

```
Incoming signal to neuron = (Input1 * Weight1) + (Input2 * Weight2) + (Input3 * Weight3)
```

or:

```
Σ(Inputᵢ * Weightᵢ)
```

## Activation Function

The activation function takes the incoming signal to the neuron and translates it 
to the neuron's output.

```
neuron output = ActivationFunction(incomingSignal)
```

For this demo, we'll use the *sigmoid function* as our activation function.
The sigmoid function uses Euler's number (e): 1 / 1+e^-x, where x is the input.

<img height="200" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Logistic-curve.svg/640px-Logistic-curve.svg.png" />  
(source: wikipedia)

So our functions will be:

```
Neuron input: Σ(Inputᵢ*Weightᵢ)
Neuron output:  1 / 1 + e^(-NeuronInput)
```

## Training Process

We start by assigning *random* numbers to our weights. We'll use values ranging
between 0 and 1 for our random weights.

We first predict the output for a training set example and check the output
against the expected value. The difference between the predicted value and the 
expected value is the `error`. We then adjust our weights to reduce the error,
and this feeds back into the network. This is now the network learns.
We'll repeat this process thousands of time and by the end of the training,
the neural network will have learned from the readjusted weights.


## Error Cost Function

The error cost function, also known as a "loss function", is the correct output
minus the predicted output, squared, for each example in the training set:

```
Σ 1/2(correctOutput - predictedOutput)^2
```

This gives us a measure of the total error of the neural network.

We can use the *gradient descent* to find the minimum by taking steps proportional
to the negative gradient.


## Formula for adjusting weights

Adjust weights by = Input * ErrorInOutput * SigmoidCurve Gradient

where:

Sigmoid gradient = NeuronOutput * (1 - NeuronOuput)


