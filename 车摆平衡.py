import gym

if __name__ == "__main__":
    '''
    创建了一个叫作CartPole（车摆系统）的环境。该环境来自经典的控制问题，其目的是控制底部附有木棒的平台
    '''
    env = gym.make("CartPole-v0")
    total_reward = 0.0  # 初始化了步数计数器和奖励累积器
    total_steps = 0
    # 观察是4个浮点数，包含了木棒质点的x坐标、速度、与平台的角度以及角速度的信息
    obs = env.reset()  # 重置环境
    # print(obs)
    while True:
        # 从动作空间中随机采样一个动作，然后让环境执行并返回下一个观察（obs）、reward和done标记
        action = env.action_space.sample()
        obs,reward,done,_ = env.step(action)
        total_steps +=1
        total_reward += reward
        if done:
            break

    print("Episode done in %d steps, total reward %.2f"%(total_steps,total_reward))



