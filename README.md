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

So for our purposes, the sigmoid function will be:

```
1 / 1 + e^-(*NeuronInput*)
```

