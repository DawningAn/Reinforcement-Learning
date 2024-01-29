'''
通过发布随机动作，让智能体探索环境，时不时地偏离它原先策略的轨迹
'''
import gym
from typing import TypeVar
import random

Action = TypeVar('Action')


class RandomActionWrapper(gym.ActionWrapper):
    def __init__(self, env, epsilon=0.1):
        super(RandomActionWrapper, self).__init__(env)
        self.epsilon = epsilon

    def action(self, action: Action) -> Action:
        if random.random() < self.epsilon:
            print("Random!")
            return self.env.action_space.sample()
        return action


if __name__ == "__main__":
    # 创建一个普通的CartPole环境，并将其传入Wrapper构造函数。然后，将Wrapper类当成一个普通的Env实例，用它来取代原始的CartPole。
    # 因为Wrapper类继承自Env类，并且暴露了相同的接口，可以任意地嵌套包装器
    env = RandomActionWrapper(gym.make("CartPole-v0"))
    obs = env.reset()
    total_reward = 0.0

    while True:
        obs, reward, done, _ = env.step(0)
        total_reward += reward
        if done:
            break

    print("Reward got: %.2f" % total_reward)
