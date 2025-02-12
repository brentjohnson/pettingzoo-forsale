from pettingzoo import AECEnv

class CustomSkeletonEnvironment(AECEnv):
    metadata = {
        "name": "custom_environment_v0",
    }

    def __init__(self):
        pass

    def reset(self, seed=None, options=None):

        self.agents = {}
        self.possible_agents = {}
        self.agent_selection = {}
        self.terminations = {}
        self.truncations = {}
        self.rewards = {}
        self.infos = {}
        self.observation_spaces = {}
        self.action_spaces = {}


    def step(self, actions):
        pass

    def render(self):
        pass

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]
