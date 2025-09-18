import random
from .enums import OutfitType, OUTFIT_TYPE_NAMES, LOCATION_TYPE_NAMES
from .OutfitGenerator import OutfitGenerator
from .SceneGenerator import SceneGenerator
from .CharacterGenerator import CharacterGenerator
from .PoseGenerator import PoseGenerator

class PromptGenerator:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "A photo of <<woman>> wearing <<femaleOutfit>> in <<scene>>"}),
                "outfit_type": (OUTFIT_TYPE_NAMES, {}),
                "location": (LOCATION_TYPE_NAMES, {}),
            },
            "optional": {
                "seed": ("INT", {"default": -1, "min": -1, "max": 2147483647}),
                "force_barefoot": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "generate_prompt"

    CATEGORY = "examples"



    def _substitute_template(self, template, outfit_type_enum, location, force_barefoot=False):
        """Replace template placeholders with generated outfit and scene data"""
        result = template
        
        ##############################################################################
        # CHARACTER
        ##############################################################################
        while "<<femaleChar>>" in result:
            character = CharacterGenerator.generate_character(outfit_type_enum, "female")
            result = result.replace("<<femaleChar>>", character, 1)
            
        while "<<woman>>" in result:
            character = CharacterGenerator.generate_character(outfit_type_enum, "female")
            result = result.replace("<<woman>>", character, 1)
            
        while "<<maleChar>>" in result:
            character = CharacterGenerator.generate_character(outfit_type_enum, "female")
            result = result.replace("<<maleChar>>", character, 1)
            
        while "<<man>>" in result:
            character = CharacterGenerator.generate_character(outfit_type_enum, "female")
            result = result.replace("<<man>>", character, 1)
            
        ##############################################################################
        # POSES
        ##############################################################################
        while "<<anyPose>>" in result:
            pose = PoseGenerator.generate_pose()
            result = result.replace("<<anyPose>>", pose, 1)
            
        while "<<sitting>>" in result:
            pose = PoseGenerator.generate_sitting_on_ground_pose()
            result = result.replace("<<sitting>>", pose, 1)
            
        while "<<sittingOnGround>>" in result:
            pose = PoseGenerator.generate_sitting_on_ground_pose()
            result = result.replace("<<sittingOnGround>>", pose, 1)
            
        while "<<sittingOnA>>" in result:
            pose = PoseGenerator.generate_sitting_on_a_pose()
            result = result.replace("<<sittingOnA>>", pose, 1)
            
        while "<<crouching>>" in result:
            pose = PoseGenerator.generate_crouching_pose()
            result = result.replace("<<crouching>>", pose, 1)
            
        while "<<kneeling>>" in result:
            pose = PoseGenerator.generate_kneeling_pose()
            result = result.replace("<<kneeling>>", pose, 1)
            
        while "<<onAllFours>>" in result:
            pose = PoseGenerator.generate_on_all_fours_pose()
            result = result.replace("<<onAllFours>>", pose, 1)
            
        while "<<lying>>" in result:
            pose = PoseGenerator.generate_lying_pose()
            result = result.replace("<<lying>>", pose, 1)
            
        while "<<standing>>" in result:
            pose = PoseGenerator.generate_standing_pose()
            result = result.replace("<<standing>>", pose, 1)
            
        while "<<walking>>" in result:
            pose = PoseGenerator.generate_walking_pose()
            result = result.replace("<<walking>>", pose, 1)
            
        while "<<running>>" in result:
            pose = PoseGenerator.generate_running_pose()
            result = result.replace("<<running>>", pose, 1)
            
        while "<<jumping>>" in result:
            pose = PoseGenerator.generate_jumping_pose()
            result = result.replace("<<jumping>>", pose, 1)
            
        while "<<dancing>>" in result:
            pose = PoseGenerator.generate_dancing_pose()
            result = result.replace("<<dancing>>", pose, 1)
            
        while "<<posing>>" in result:
            pose = PoseGenerator.generate_posing_pose()
            result = result.replace("<<posing>>", pose, 1)
            
        while "<<leaning>>" in result:
            pose = PoseGenerator.generate_leaning_pose()
            result = result.replace("<<leaning>>", pose, 1)
            
        ##############################################################################
        # OUTFIT
        ##############################################################################
        while "<<femaleOutfit>>" in result:
            female_outfit = OutfitGenerator.generate_outfit(outfit_type_enum, "female", force_barefoot)
            result = result.replace("<<femaleOutfit>>", female_outfit, 1)
        
        while "<<maleOutfit>>" in result:
            male_outfit = OutfitGenerator.generate_outfit(outfit_type_enum, "male", force_barefoot)
            result = result.replace("<<maleOutfit>>", male_outfit, 1)
        
        ##############################################################################
        # SCENE
        ##############################################################################
        while "<<scene>>" in result:
            scene = SceneGenerator.generate_scene(outfit_type_enum, location)
            result = result.replace("<<scene>>", scene, 1)
        
        while "<<location>>" in result:
            scene = SceneGenerator.generate_scene(outfit_type_enum, location)
            result = result.replace("<<location>>", scene, 1)
        
        return result

    def generate_prompt(self, prompt, outfit_type, location, seed=-1, force_barefoot=False):
        """Generate a merged prompt with outfit and scene data substituted for placeholders"""
        
        # Use seed for randomization - if -1, use random seed
        if seed != -1:
            random.seed(seed)
        # If seed is -1, let Python use its default random behavior
        
        # If random is selected, pick a random style
        if outfit_type == "random":
            outfit_type_enum = random.choice(list(OutfitType))
        else:
            # Find the matching enum value
            outfit_type_enum = None
            for ot in OutfitType:
                if ot.value == outfit_type:
                    outfit_type_enum = ot
                    break
            if outfit_type_enum is None:
                outfit_type_enum = OutfitType.CASUAL_CHIC  # Default fallback

        # Substitute template placeholders with generated data
        final_prompt = self._substitute_template(prompt, outfit_type_enum, location, force_barefoot)
        
        # Debug logging
        print(f"DEBUG - original prompt: {prompt}")
        print(f"DEBUG - final_prompt: {final_prompt}")
        
        return (final_prompt,)

NODE_CLASS_MAPPINGS = {
    "prompt-generator": PromptGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "prompt-generator": "Prompt Generator"
}