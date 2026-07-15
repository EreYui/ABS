from legged_gym.envs.base.legged_robot import LeggedRobot
from legged_gym.envs.base.legged_robot_pos import LeggedRobotPos
from legged_gym.envs.base.legged_robot_rec import LeggedRobotRec
from legged_gym.envs.go2.go2_config import (
    Go2PosRoughCfg,
    Go2PosRoughCfgNoPenalty,
    Go2PosRoughCfgPPO,
    Go2PosRoughCfgPPOLagrangian,
    Go2RecRoughCfg,
    Go2RecRoughCfgPPO,
    Go2RoughCfg,
    Go2RoughCfgPPO,
)
from legged_gym.utils.task_registry import task_registry


task_registry.register("go2_rough", LeggedRobot, Go2RoughCfg(), Go2RoughCfgPPO())
task_registry.register("go2_pos_rough", LeggedRobotPos, Go2PosRoughCfg(), Go2PosRoughCfgPPO())
task_registry.register("go2_rec_rough", LeggedRobotRec, Go2RecRoughCfg(), Go2RecRoughCfgPPO())
task_registry.register(
    "go2_pos_rough_ppo_lagrangian",
    LeggedRobotPos,
    Go2PosRoughCfgNoPenalty(),
    Go2PosRoughCfgPPOLagrangian(),
)
