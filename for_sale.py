from pettingzoo import AECEnv
from pettingzoo.utils import agent_selector

class CustomEnvironment(AECEnv):
    metadata = {
        "name": "custom_environment_v0",
    }

    def __init__(self):
        self.agents = ["agent_0", "agent_1", "agent_2", "agent_3"]
        self.possible_agents = self.agents[:]

        self.terminations = {}
        self.truncations = {}

        self._agent_selector = agent_selector(self.agents)
        self.agent_selection = self._agent_selector.reset()

    def reset(self, seed=None, options=None):
        pass

    def step(self, actions):
        pass

    def render(self):
        pass

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]
