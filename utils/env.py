import gymnasium as gym
import gym_corrigible

def make_env(env_key, seed=None, render_mode=None, chigh=None, prsht=None):
    if chigh or prsht:
        env = gym.make(env_key, chigh = chigh, prsht = prsht, render_mode=render_mode)
    else:
        env = gym.make(env_key, render_mode=render_mode)
    env.reset(seed=seed)
    return env
