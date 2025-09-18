
import random
from .poses import SITTING_ON_GROUND, SITTING_ON_A, CROUCHING, KNEELING, ON_ALL_FOURS, LYING, STANDING, WALKING, RUNNING, JUMPING, DANCING, POSING, LEANING


class PoseGenerator:

    def generate_pose(self):
        return random.choice(SITTING_ON_GROUND + SITTING_ON_A + CROUCHING + KNEELING + ON_ALL_FOURS + LYING + STANDING + WALKING + RUNNING + JUMPING + DANCING + POSING + LEANING)
        
    def generate_sitting_on_ground_pose(self):
        return random.choice(SITTING_ON_GROUND)
    
    def generate_sitting_on_a_pose(self):
        return random.choice(SITTING_ON_A)
    
    def generate_crouching_pose(self):
        return random.choice(CROUCHING)
    
    def generate_kneeling_pose(self):
        return random.choice(KNEELING)
    
    def generate_on_all_fours_pose(self):
        return random.choice(ON_ALL_FOURS)
    
    def generate_lying_pose(self):
        return random.choice(LYING)
    
    def generate_standing_pose(self):
        return random.choice(STANDING)
    
    def generate_walking_pose(self):
        return random.choice(WALKING)
    
    def generate_running_pose(self):
        return random.choice(RUNNING)
    
    def generate_jumping_pose(self):
        return random.choice(JUMPING)
    
    def generate_dancing_pose(self):
        return random.choice(DANCING)
    
    def generate_posing_pose(self):
        return random.choice(POSING)
    
    def generate_leaning_pose(self):
        return random.choice(LEANING)