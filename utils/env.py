import gymnasium as gym
import gym_corrigible

def make_env(env_key, seed=None, render_mode=None, chigh=0, clow=0, prsht=None):
    if chigh or clow or prsht:
        env = gym.make(env_key, chigh=chigh, clow=clow, prsht=prsht, render_mode=render_mode)
    else:
        env = gym.make(env_key, render_mode=render_mode)
    env.reset(seed=seed)
    return env
