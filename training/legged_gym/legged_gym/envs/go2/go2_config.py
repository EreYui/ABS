from legged_gym.envs.go1.go1_config import (
    Go1RoughCfg,
    Go1RoughCfgNoPenalty,
    Go1RoughCfgPPO,
    Go1RoughCfgPPOLagrangian,
)
from legged_gym.envs.go1.go1_pos_config import (
    Go1PosRoughCfg,
    Go1PosRoughCfgNoPenalty,
    Go1PosRoughCfgPPO,
    Go1PosRoughCfgPPOLagrangian,
)
from legged_gym.envs.go1.go1_rec_config import Go1RecRoughCfg, Go1RecRoughCfgPPO


GO2_URDF = "{LEGGED_GYM_ROOT_DIR}/resources/robots/go2/urdf/go2.urdf"

GO2_DEFAULT_JOINT_ANGLES = {
    "FL_hip_joint": 0.0,
    "RL_hip_joint": 0.0,
    "FR_hip_joint": 0.0,
    "RR_hip_joint": 0.0,
    "FL_thigh_joint": 0.8,
    "RL_thigh_joint": 0.8,
    "FR_thigh_joint": 0.8,
    "RR_thigh_joint": 0.8,
    "FL_calf_joint": -1.5,
    "RL_calf_joint": -1.5,
    "FR_calf_joint": -1.5,
    "RR_calf_joint": -1.5,
}


class Go2RoughCfg(Go1RoughCfg):
    class init_state(Go1RoughCfg.init_state):
        pos = [0.0, 0.0, 0.4]
        default_joint_angles = GO2_DEFAULT_JOINT_ANGLES

    class control(Go1RoughCfg.control):
        stiffness = {"joint": 30.0}
        damping = {"joint": 0.6}

    class asset(Go1RoughCfg.asset):
        file = GO2_URDF
        name = "go2"
        foot_name = "foot"
        penalize_contacts_on = ["thigh", "calf"]
        terminate_after_contacts_on = ["base"]
        self_collisions = 0

    class sensors(Go1RoughCfg.sensors):
        class depth_cam:
            enable = False

    class domain_rand(Go1RoughCfg.domain_rand):
        randomize_dof_bias = False
        max_dof_bias = 0.0
        randomize_init_dof = False
        init_dof_factor = [1.0, 1.0]
        stand_bias3 = [0.0, 0.0, 0.0]

        erfi = False
        erfi_torq_lim = 0.0

        randomize_xy = False
        init_x_range = [0.0, 0.0]
        init_y_range = [0.0, 0.0]
        randomize_yaw = False
        init_yaw_range = [0.0, 0.0]
        randomize_roll = False
        init_roll_range = [0.0, 0.0]
        randomize_pitch = False
        init_pitch_range = [0.0, 0.0]
        randomize_velo = False
        init_vlinx_range = [0.0, 0.0]
        init_vliny_range = [0.0, 0.0]
        init_vlinz_range = [0.0, 0.0]
        init_vang_range = [0.0, 0.0]

    class rewards(Go1RoughCfg.rewards):
        base_height_target = 0.34


class Go2RoughCfgNoPenalty(Go2RoughCfg, Go1RoughCfgNoPenalty):
    class rewards(Go2RoughCfg.rewards):
        class scales(Go2RoughCfg.rewards.scales):
            collision = 0.0
            termination = 0.0


class Go2RoughCfgPPO(Go1RoughCfgPPO):
    class runner(Go1RoughCfgPPO.runner):
        run_name = ""
        experiment_name = "go2_rough"


class Go2RoughCfgPPOLagrangian(Go1RoughCfgPPOLagrangian):
    class runner(Go1RoughCfgPPOLagrangian.runner):
        run_name = ""
        experiment_name = "go2_rough"


class Go2PosRoughCfg(Go1PosRoughCfg):
    class init_state(Go1PosRoughCfg.init_state):
        pos = [0.0, 0.0, 0.4]
        default_joint_angles = GO2_DEFAULT_JOINT_ANGLES

    class control(Go1PosRoughCfg.control):
        stiffness = {"joint": 30.0}
        damping = {"joint": 0.6}

    class asset(Go1PosRoughCfg.asset):
        file = GO2_URDF
        name = "go2"
        foot_name = "foot"
        penalize_contacts_on = ["thigh", "calf"]
        terminate_after_contacts_on = ["base"]
        self_collisions = 0

    class rewards(Go1PosRoughCfg.rewards):
        base_height_target = 0.34


class Go2PosRoughCfgNoPenalty(Go2PosRoughCfg, Go1PosRoughCfgNoPenalty):
    class domain_rand(Go2PosRoughCfg.domain_rand):
        init_x_range = [-0.3, 0.3]
        init_y_range = [-0.3, 0.3]

    class rewards(Go2PosRoughCfg.rewards):
        class scales(Go2PosRoughCfg.rewards.scales):
            collision = 0.0
            feet_collision = 0.0
            termination = 0.0


class Go2PosRoughCfgPPO(Go1PosRoughCfgPPO):
    class runner(Go1PosRoughCfgPPO.runner):
        run_name = ""
        experiment_name = "go2_pos_rough"


class Go2PosRoughCfgPPOLagrangian(Go1PosRoughCfgPPOLagrangian):
    class runner(Go1PosRoughCfgPPOLagrangian.runner):
        run_name = ""
        experiment_name = "go2_pos_rough_lag"


class Go2RecRoughCfg(Go1RecRoughCfg):
    class init_state(Go1RecRoughCfg.init_state):
        pos = [0.0, 0.0, 0.4]
        default_joint_angles = GO2_DEFAULT_JOINT_ANGLES

    class control(Go1RecRoughCfg.control):
        stiffness = {"joint": 30.0}
        damping = {"joint": 0.6}

    class asset(Go1RecRoughCfg.asset):
        file = GO2_URDF
        name = "go2"
        foot_name = "foot"
        penalize_contacts_on = ["calf"]
        terminate_after_contacts_on = ["base"]
        self_collisions = 0
        load_dynamic_object = False
        test_mode = False

    class rewards(Go1RecRoughCfg.rewards):
        base_height_target = 0.34


class Go2RecRoughCfgPPO(Go1RecRoughCfgPPO):
    class runner(Go1RecRoughCfgPPO.runner):
        run_name = ""
        experiment_name = "go2_rec_rough"
        num_steps_per_env = 24
