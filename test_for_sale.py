from pettingzoo.test import api_test
from for_sale import CustomEnvironment
env = CustomEnvironment()
api_test(env, num_cycles=1000, verbose_progress=False)
