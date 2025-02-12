from tutorial1_skeleton_creation import CustomSkeletonEnvironment
from tutorial2_adding_game_logic import CustomEnvironment
from tutorial3_action_masking import CustomActionMaskedEnvironment

from pettingzoo.test import api_test

if __name__ == "__main__":
    env = CustomSkeletonEnvironment()
    api_test(env, num_cycles=1_000_000)

    env = CustomEnvironment()
    api_test(env, num_cycles=1_000_000)

    env = CustomActionMaskedEnvironment()
    api_test(env, num_cycles=1_000_000)
