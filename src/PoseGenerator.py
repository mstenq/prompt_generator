
import random
from .poses import SITTING_ON_GROUND, SITTING_ON_A, CROUCHING, KNEELING, ON_ALL_FOURS, LYING, STANDING, WALKING, RUNNING, JUMPING, DANCING, POSING, LEANING


class PoseGenerator:

    @staticmethod
    def generate_pose():
        return random.choice(SITTING_ON_GROUND + SITTING_ON_A + CROUCHING + KNEELING + ON_ALL_FOURS + LYING + STANDING + WALKING + RUNNING + JUMPING + DANCING + POSING + LEANING)
        
    @staticmethod
    def generate_sitting_on_ground_pose():
        return random.choice(SITTING_ON_GROUND)
    
    @staticmethod
    def generate_sitting_on_a_pose():
        return random.choice(SITTING_ON_A)
    
    @staticmethod
    def generate_crouching_pose():
        return random.choice(CROUCHING)
    
    @staticmethod
    def generate_kneeling_pose():
        return random.choice(KNEELING)
    
    @staticmethod
    def generate_on_all_fours_pose():
        return random.choice(ON_ALL_FOURS)
    
    @staticmethod
    def generate_lying_pose():
        return random.choice(LYING)
    
    @staticmethod
    def generate_standing_pose():
        return random.choice(STANDING)
    
    @staticmethod
    def generate_walking_pose():
        return random.choice(WALKING)
    
    @staticmethod
    def generate_running_pose():
        return random.choice(RUNNING)
    
    @staticmethod
    def generate_jumping_pose():
        return random.choice(JUMPING)
    
    @staticmethod
    def generate_dancing_pose():
        return random.choice(DANCING)
    
    @staticmethod
    def generate_posing_pose():
        return random.choice(POSING)
    
    @staticmethod
    def generate_leaning_pose():
        return random.choice(LEANING)