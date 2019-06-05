from ple.games.flappybird import FlappyBird
from ple import PLE
import numpy as np
from nnagent import NNAgent


class NEAT:

    def __init__(self, game, size=10, mutationrate=0.1, crossoverrate=0.1):
        p = PLE(game, fps=30, display_screen=False)
        p.init()

        self.population = np.array([NNAgent(inputs=p.getGameState().keys(), actions=p.getActionSet()) for i in range(size)])
        for agent in self.population:
            agent.fitness = None

        self.fitness = []*size
        self.generation = 0
        self.popsize = size
        self.mutationrate = mutationrate
        self.crossoverrate = crossoverrate

    def advance(self):
        """ Do one iteration of the evolutionary algorithm including fitness calculation,
        selection, crossover, mutation, creating a new population out of the parents and the generated children.
        The provided function stubs for crossover, mutate, determine_fitness and selection can be changes if you want.

        :return: (best_agent, fitness_values) best agent in the current population and the fitness values
        """
        return best_agent, fitness_values

    def crossover(self, indvididual, pop):
        """ apply crossover to the selected invidual and a random individual of the population

        :return: modified parent  (or modified parent and child)
        """
        raise NotImplementedError("implement a crossover, "
                                  "you can change the signature of this function")

        return indvididual

    def mutate(self, individual):
        """ apply mutation to the selected invidual

        :return: modified individual  (or modified parent and child)
        """
        raise NotImplementedError("implement a mutation, "
                                  "you can change the signature of this function")

        return individual

    def determine_fitness(self, individual):
        """ determine the fitness of the given individual by running a simulation of the game with its encoded agent

        :param individual:
        :return:
        """
        if individual.fitness is None:
            game = FlappyBird()
            p = PLE(game, fps=30, display_screen=False)
            p.init()

            raise NotImplementedError("add your code to determine the fitness of the individual, "
                                      "you can change the signature of this function")
        else:
            return individual.fitness

    def selection(self, fitness, n=None):
        """ implement a selection of fit individuals using tournament or random selection

        :param fitness:  fitness values of individuals
        :param n: number of individuals to select of the given population
        :return: indices of selected individuals
        """
        raise NotImplementedError("add your code to select a set of individuals, "
                                  "you can change the signature of this function")
