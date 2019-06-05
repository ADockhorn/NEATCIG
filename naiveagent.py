
class NaiveAgent:
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
