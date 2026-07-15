import isaacgym

from legged_gym.envs import *
from legged_gym.envs.go2 import *
from legged_gym.utils import get_args, task_registry


DEFAULT_GO2_TASK = "go2_pos_rough"


def train(args):
    env, env_cfg = task_registry.make_env(name=args.task, args=args)
    ppo_runner, train_cfg = task_registry.make_alg_runner(env=env, name=args.task, args=args)
    ppo_runner.learn(num_learning_iterations=train_cfg.runner.max_iterations, init_at_random_ep_len=True)


if __name__ == "__main__":
    args = get_args()
    if args.task == "anymal_c_flat":
        args.task = DEFAULT_GO2_TASK
    train(args)
