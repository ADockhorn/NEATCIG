import numpy as np
import random


class NNAgent(object):

    def __init__(self, inputs: list, actions: list, size_hidden_layer=5, nr_hidden_layers=0):
        self.inputs = inputs
        self.size_input_layer = len(inputs)

        self.nr_hidden_layers = nr_hidden_layers
        self.size_hidden_layer = size_hidden_layer

        self.actions = actions
        self.size_output_layer = len(actions)

        self.weights = self.initialize_weights()

    @classmethod
    def from_agent(cls, other):
        agent = cls(other.inputs, other.actions, other.size_hidden_layer, other.nr_hidden_layers)
        for i, weights in enumerate(agent.weights):
            agent.weights[i] = np.copy(other.weights[i])
        agent.fitness = other.fitness
        return agent

    def initialize_weights(self):
        weights = []
        # or use np.random.normal(0, 2, (self.size_hidden_layer, self.size_input_layer))
        if self.nr_hidden_layers > 0:
            weights.append(np.random.normal(0, 2, (self.size_hidden_layer, self.size_input_layer)))
        for i in range(self.nr_hidden_layers-1):
            weights.append(np.random.normal(0, 2, (self.size_hidden_layer, self.size_hidden_layer)))
        if self.nr_hidden_layers > 0:
            weights.append(np.random.normal(0, 2, (self.size_output_layer, self.size_hidden_layer)))
        else:
            weights.append(np.random.normal(0, 2, (self.size_output_layer, self.size_input_layer)))
        return weights

    def run(self, inputs):
        input_vector = np.array(inputs, ndmin=2).T
        for weightmatrix in self.weights:
            output_vector = np.dot(weightmatrix, input_vector)
            input_vector = 1/(1+np.exp(-output_vector))
        return input_vector

    def pick_action(self, gameState):
        inputvals = [gameState[val] for val in self.inputs]
        result = self.run(inputvals)
        return self.actions[result.argmax()]

    def crossover(self, other: "NNAgent"):
        m_idx = random.choice(range(len(self.weights)))

        a = self.weights[m_idx]
        b = other.weights[m_idx]
        shape = a.shape

        a = a.flatten()
        b = b.flatten()
        swap_idx = random.sample(range(len(a)), random.randint(1, len(a)-1))
        t = a[swap_idx]
        a[swap_idx] = b[swap_idx]
        b[swap_idx] = t

        self.weights[m_idx] = a.reshape(shape)
        other.weights[m_idx] = b.reshape(shape)
        pass

    def mutate(self):
        weightmatrix = random.choice(self.weights)
        weightmatrix[random.randint(0, weightmatrix.shape[0]-1), random.randint(0, weightmatrix.shape[1]-1)] = random.gauss(0,2)
