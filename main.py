from ple.games.flappybird import FlappyBird
from ple import PLE
import time
from nnagent import NNAgent
from randomagent import RandomAgent
from naiveagent import NaiveAgent
from population import NEAT


def view_agent(agent):
    game = FlappyBird()
    p = PLE(game, fps=30, display_screen=True)
    p.init()

    for i in range(200000):
        if p.game_over():
            p.reset_game()

        time.sleep(0.03)
        action = agent.pick_action(p.getGameState())
        p.act(action)

        if p.game_over():
            break


class HeuristicAgent:
    """
            This is our naive agent. It picks actions at random!
    """

    def __init__(self, inputs, actions):
        self.actions = actions

    def pick_action(self, gameState):
        if gameState["player_y"] > gameState["next_pipe_bottom_y"] - 30:
            return self.actions[0]
        else:
            return None


game = PLE(FlappyBird(), fps=30, display_screen=False)
game.init()
agent = HeuristicAgent(game.getGameState(), game.getActionSet())
# you can use the view_agent function to see the agent playing the game
if agent is not None:
    view_agent(agent)


pop = NEAT(FlappyBird(), size=100, mutationrate=0.5, crossoverrate=0.5)
print("Start evolutionary process")
for i in range(100):
    agent, fitness = pop.advance()
    print("highest fitness " + str(max(fitness)))

# (optional) the neat implementation could also be tested with some other games
# see: https://pygame-learning-environment.readthedocs.io/en/latest/user/games.html
# for a list of other simple games
