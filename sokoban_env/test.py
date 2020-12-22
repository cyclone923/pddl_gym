import gym
import pddlgym
import matplotlib.pyplot as plt

def test_env(env_name, num_problems, render=True, test=False, verbose=True):
    gym_name = env_name.capitalize()
    if test:
        gym_name += "Test"
    env = gym.make("PDDLEnv{}-v0".format(gym_name))
    if not render: env._render = None

    # for problem_index in range(num_problems):
    #     env.fix_problem_index(problem_index)

    plt.gca()

    for _ in range(10):
        obs, _ = env.reset()
        # perform 10 random action
        for _ in range(10):
            action = env.action_space.sample(obs)
            obs, reward, done, _ = env.step(action)
            print(action, reward, done)
            img = env.render()
            plt.imshow(img)
            plt.pause(0.001)


if __name__ == "__main__":
    test_env("sokoban", 10, test=False, render=True,  verbose=True)