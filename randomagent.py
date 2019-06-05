import numpy as np


class RandomAgent:
    """
            This is our naive agent. It picks actions at random!
    """

    def __init__(self, inputs, actions):
        self.actions = actions

    def pick_action(self, gameState):
        return self.actions[np.random.randint(0, len(self.actions))]
