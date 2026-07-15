import isaacgym

from legged_gym.envs import *
from legged_gym.envs.go2 import *
from legged_gym.scripts.testbed import play
from legged_gym.utils import get_args


DEFAULT_GO2_TASK = "go2_pos_rough"


if __name__ == "__main__":
    args = get_args()
    if args.task == "anymal_c_flat":
        args.task = DEFAULT_GO2_TASK
    play(args)
