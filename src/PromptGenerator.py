import random
import math
import re
from .enums import OutfitType, OUTFIT_TYPE_NAMES, LOCATION_TYPE_NAMES
from .OutfitGenerator import OutfitGenerator
from .SceneGenerator import SceneGenerator
from .CharacterGenerator import CharacterGenerator
from .PoseGenerator import PoseGenerator
from .ColorGenerator import ColorGenerator

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
                "ratio": (["1:1 square", "2:3 portrait", "3:4 portrait", "4:7 portrait", "3:2 landscape", "4:3 landscape", "7:4 landscape"], {"default": "1:1 square"}),
                "megapixels": ("FLOAT", {"default": 1.00, "min": 0.1, "max": 10.0, "step": 0.1}),
            },
            "optional": {
                "seed": ("INT", {"default": -1, "min": -1, "max": 2147483647}),
                "force_barefoot": ("BOOLEAN", {"default": False}),
                "var_1": ("PROMPT_VAR", {}),
                "var_2": ("PROMPT_VAR", {}),
                "var_3": ("PROMPT_VAR", {}),
                "var_4": ("PROMPT_VAR", {}),
                "var_5": ("PROMPT_VAR", {}),
                "var_6": ("PROMPT_VAR", {}),
            },
        }

    RETURN_TYPES = ("STRING", "INT", "INT")
    RETURN_NAMES = ("prompt", "width", "height")

    FUNCTION = "generate_prompt"

    CATEGORY = "prompt_generator"
    OUTPUT_NODE = True

    def _calculate_dimensions(self, ratio, megapixels):
        """Calculate width and height based on ratio and megapixels"""
        # Parse ratio string to get width:height ratio
        ratio_map = {
            "1:1 square": (1, 1),
            "2:3 portrait": (2, 3),
            "3:4 portrait": (3, 4),
            "4:7 portrait": (4, 7),
            "3:2 landscape": (3, 2),
            "4:3 landscape": (4, 3),
            "7:4 landscape": (7, 4)
        }
        
        width_ratio, height_ratio = ratio_map.get(ratio, (1, 1))
        
        # Calculate total pixels from megapixels (using 1024² as base megapixel)
        # 1.0 megapixel = 1024 x 1024 = 1,048,576 pixels
        total_pixels = megapixels * 1024 * 1024
        
        # Calculate dimensions based on ratio
        # width * height = total_pixels
        # width / height = width_ratio / height_ratio
        # So: width = height * (width_ratio / height_ratio)
        # Therefore: height * (width_ratio / height_ratio) * height = total_pixels
        # height^2 * (width_ratio / height_ratio) = total_pixels
        # height = sqrt(total_pixels / (width_ratio / height_ratio))
        
        height = math.sqrt(total_pixels / (width_ratio / height_ratio))
        width = height * (width_ratio / height_ratio)
        
        # Round to nearest multiple of 8 (common requirement for AI image generation)
        width = int(round(width / 8) * 8)
        height = int(round(height / 8) * 8)
        
        return width, height

    def _substitute_template(self, template, outfit_type, location, force_barefoot=False, vars = []):
        """Replace template placeholders with generated outfit and scene data"""
        result = template
        
        # Resolve outfit_type to enum
        # If outfit type is "random" AND location is specified,
        # generate scene first and derive outfit type from it
        outfit_type_enum = None
        generated_scene = None
        
        if outfit_type == "random" and location and location != "anything":
            # Scene-first logic: Generate scene based on location, then pick outfit type
            generated_scene = SceneGenerator.generate_scene(location)
            
            # Get compatible outfit types for this scene and pick one randomly
            compatible_outfit_types = SceneGenerator.get_outfit_types_for_scene(generated_scene)
            if compatible_outfit_types:
                outfit_type_enum = random.choice(compatible_outfit_types)
            else:
                # Fallback if scene has no types
                outfit_type_enum = random.choice(list(OutfitType))
        elif outfit_type == "random":
            # Random outfit type without location constraint
            outfit_type_enum = random.choice(list(OutfitType))
        else:
            # Specific outfit type requested - find the matching enum
            for ot in OutfitType:
                if ot.value == outfit_type:
                    outfit_type_enum = ot
                    break
            if outfit_type_enum is None:
                outfit_type_enum = OutfitType.CASUAL_CHIC  # Default fallback
        
        ##############################################################################
        # VARS
        ##############################################################################
        while "<<var1>>" in result and len(vars) >= 1 and vars[0] is not None:
            result = result.replace("<<var1>>", vars[0], 1)
        while "<<var_1>>" in result and len(vars) >= 1 and vars[0] is not None:
            result = result.replace("<<var_1>>", vars[0], 1)
        while "<<var2>>" in result and len(vars) >= 2 and vars[1] is not None:
            result = result.replace("<<var2>>", vars[1], 1)
        while "<<var_2>>" in result and len(vars) >= 2 and vars[1] is not None:
            result = result.replace("<<var_2>>", vars[1], 1)
        while "<<var3>>" in result and len(vars) >= 3 and vars[2] is not None:
            result = result.replace("<<var3>>", vars[2], 1)
        while "<<var_3>>" in result and len(vars) >= 3 and vars[2] is not None:
            result = result.replace("<<var_3>>", vars[2], 1)
        while "<<var4>>" in result and len(vars) >= 4 and vars[3] is not None:
            result = result.replace("<<var4>>", vars[3], 1)
        while "<<var_4>>" in result and len(vars) >= 4 and vars[3] is not None:
            result = result.replace("<<var_4>>", vars[3], 1)
        while "<<var5>>" in result and len(vars) >= 5 and vars[4] is not None:
            result = result.replace("<<var5>>", vars[4], 1)
        while "<<var_5>>" in result and len(vars) >= 5 and vars[4] is not None:
            result = result.replace("<<var_5>>", vars[4], 1)
        while "<<var6>>" in result and len(vars) >= 6 and vars[5] is not None:
            result = result.replace("<<var6>>", vars[5], 1)
        while "<<var_6>>" in result and len(vars) >= 6 and vars[5] is not None:
            result = result.replace("<<var_6>>", vars[5], 1)
        
        ##############################################################################
        # CHARACTER
        ##############################################################################
        while "<<femaleChar>>" in result:
            character = CharacterGenerator.generate_character("female")
            result = result.replace("<<femaleChar>>", character, 1)
        
        while "<<simpleFemaleChar>>" in result:
            character = CharacterGenerator.generate_simple_character("female")
            result = result.replace("<<simpleFemaleChar>>", character, 1)
            
        while "<<woman>>" in result:
            character = CharacterGenerator.generate_character("female")
            result = result.replace("<<woman>>", character, 1)
            
        while "<<simpleWoman>>" in result:
            character = CharacterGenerator.generate_simple_character("female")
            result = result.replace("<<simpleWoman>>", character, 1)
            
        while "<<maleChar>>" in result:
            character = CharacterGenerator.generate_character("male")
            result = result.replace("<<maleChar>>", character, 1)
            
        while "<<simpleMaleChar>>" in result:
            character = CharacterGenerator.generate_simple_character("male")
            result = result.replace("<<simpleMaleChar>>", character, 1)
            
        while "<<man>>" in result:
            character = CharacterGenerator.generate_character("male")
            result = result.replace("<<man>>", character, 1)
            
        while "<<simpleMan>>" in result:
            character = CharacterGenerator.generate_simple_character("male")
            result = result.replace("<<simpleMan>>", character, 1)
            
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
            
        while "<<laying>>" in result:
            pose = PoseGenerator.generate_lying_pose()
            result = result.replace("<<laying>>", pose, 1)
            
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
        # COLOR
        ##############################################################################
        # Handle color substitutions with regex to support both <<color>> and <<color:categories>>
        def replace_color(match):
            full_match = match.group(0)
            if ':' in full_match:
                # Extract categories from <<color:category1,category2>>
                categories_str = full_match[8:-2]  # Remove "<<color:" and ">>"
                categories = [cat.strip() for cat in categories_str.split(',')]
                return ColorGenerator.generate_color(categories)
            else:
                # Simple <<color>> case
                return ColorGenerator.generate_color()
        
        # Use regex to find and replace all color patterns
        color_pattern = r'<<color(?::[^>]+)?>>'
        result = re.sub(color_pattern, replace_color, result)
        
        ##############################################################################
        # SCENE
        ##############################################################################
        while "<<scene>>" in result:
            # Use pre-generated scene if available, otherwise generate new one
            if generated_scene:
                scene = generated_scene
                generated_scene = None  # Use it only once
            else:
                scene = SceneGenerator.generate_scene(location)
            result = result.replace("<<scene>>", scene, 1)
        
        while "<<location>>" in result:
            # Use pre-generated scene if available, otherwise generate new one
            if generated_scene:
                scene = generated_scene
                generated_scene = None  # Use it only once
            else:
                scene = SceneGenerator.generate_scene(location)
            result = result.replace("<<location>>", scene, 1)
        
        return result

    def generate_prompt(self, prompt, outfit_type, location, ratio, megapixels, seed=-1, force_barefoot=False, var_1=None, var_2=None, var_3=None, var_4=None, var_5=None, var_6=None):
        """Generate a merged prompt with outfit and scene data substituted for placeholders"""
        
        # Use seed for randomization - if -1, use random seed
        if seed != -1:
            random.seed(seed)
        # If seed is -1, let Python use its default random behavior

        # Calculate dimensions based on ratio and megapixels
        width, height = self._calculate_dimensions(ratio, megapixels)
        
        vars = [var_1, var_2, var_3, var_4, var_5, var_6]

        # Substitute template placeholders with generated data
        # Note: outfit_type resolution happens inside _substitute_template
        final_prompt = self._substitute_template(prompt, outfit_type, location, force_barefoot, vars)
        
        # Debug logging
        print(f"DEBUG - original prompt: {prompt}")
        print(f"DEBUG - final_prompt: {final_prompt}")
        print(f"DEBUG - ratio: {ratio}, megapixels: {megapixels}")
        print(f"DEBUG - calculated dimensions: {width}x{height}")
        
        return {
            "ui": {"text": (final_prompt,)},
            "result": (final_prompt, width, height)
        }