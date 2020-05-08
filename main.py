import numpy as np

trainInput = np.array([[0,0,1],
                       [0,0,1],
                       [1,0,1],
                       [0,1,1]])

trainOutput = np.array([[0,1,1,0]]).T

def sig(x):
    return 1 / (1 + np.exp(-x))


def sigD(x):
    return x * (1 - x)




np.random.seed(1)

#randomly assigned weights
synapticWeights = 2 * np.random.random((3,1)) - 1

#record orignal random weights
print('Random starting synaptic weights: ')
print(synapticWeights)

#training weights for 1k iterations
for iteration in range(1000):
	#store input
    inputLayer = trainInput
	#element wise multiplication of inputLayer* weights
    outputs = sig(np.dot(inputLayer, synapticWeights))

    error = trainOutput - outputs

    
    adjustments = error * sigD(outputs)

    # revise weights
    synapticWeights += np.dot(inputLayer.T, adjustments)

print('Synaptic weights after training: ')
print(synapticWeightseights)

print("Output After Training:")
print(outputs)
