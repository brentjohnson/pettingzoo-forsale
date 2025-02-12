from pettingzoo import AECEnv
from pettingzoo.utils import agent_selector
from gymnasium.spaces import Discrete, Box
import numpy as np
import functools




class CustomEnvironment(AECEnv):
    metadata = {
        "name": "custom_environment_v0",
    }

    def __init__(self):
        self.possible_agents = ["player_" + str(r) for r in range(4)]

    def reset(self, seed=None, options=None):
        self.agents = self.possible_agents[:]
        self.rewards = {agent: 0 for agent in self.agents}
        self._cumulative_rewards = {agent: 0 for agent in self.agents}
        self.terminations = {agent: False for agent in self.agents}
        self.truncations = {agent: False for agent in self.agents}
        self.infos = {agent: {} for agent in self.agents}
        self._agent_selector = agent_selector(self.agents)
        self.agent_selection = self._agent_selector.next()


    def step(self, actions):
        pass

    def render(self):
        print("hi")

    def close(self):
        pass

    def observe(self, agent):
        """
        Observe should return the observation of the specified agent. This function
        should return a sane observation (though not necessarily the most up to date possible)
        at any time after reset() is called.
        """
        # observation of one agent is the previous state of the other
        obs = np.array([1, 2, 3, 4])
        return obs

    @functools.lru_cache(maxsize=None)
    def observation_space(self, agent):
        b = Box(low=-1, high=17, shape=(4,), dtype=int)
        return b

    @functools.lru_cache(maxsize=None)
    def action_space(self, agent):
        return Discrete(17)
