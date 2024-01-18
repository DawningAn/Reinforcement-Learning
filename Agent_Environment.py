import random
from typing import List
'''
智能体：主动行动的人或物。实际上，智能体只是实现了某些策略的代码片段而已。这个策略根据观察决定每一个时间点执行什么动作。
环境：某些世界的模型，它在智能体外部，负责提供观察并给予奖励。而且环境会根据智能体的动作改变自己的状态
'''
class Environment:
    # 环境初始化内部状态
    def __init__(self):
        self.steps_left = 10  # 记录智能体还能和环境交互的步数

    def get_observation(self) -> List[float]:
        return [0.0, 0.0, 0.0]  # 给智能体返回当前环境的观察。它通常被实现为有关环境内部状态的某些函数

    def get_actions(self) -> List[int]:
        return [0, 1]

    def is_done(self) -> bool:
        return self.steps_left == 0

    def action(self, action: int) -> float:
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random()


class Agent:
    def __init__(self):
        self.total_reward = 0.0

    def step(self, env: Environment):
        current_obs = env.get_observation()
        actions = env.get_actions()
        reward = env.action(random.choice(actions))
        self.total_reward += reward


if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print("Total reward got: %.4f" % agent.total_reward)