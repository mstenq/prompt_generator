#!/usr/bin/env python3
"""
Standalone test script for PromptGenerator
Run this from the outfit_generator directory with: python test_prompt_generator.py
"""

import sys
import os

# Add the current directory to Python path so we can import src as a package
sys.path.insert(0, os.path.dirname(__file__))

# Import from the src package
from src.enums import OutfitType, OUTFIT_TYPE_NAMES, LOCATION_TYPE_NAMES
from src.OutfitGenerator import OutfitGenerator
from src.SceneGenerator import SceneGenerator
from src.CharacterGenerator import CharacterGenerator
from src.PoseGenerator import PoseGenerator
import random

class PromptGeneratorStandalone:
    """Standalone version of PromptGenerator for testing"""
    
    def __init__(self):
        # Create instances of all generators
        self.outfit_generator = OutfitGenerator()
        self.scene_generator = SceneGenerator()
        self.character_generator = CharacterGenerator()
        self.pose_generator = PoseGenerator()

    def _substitute_template(self, template, outfit_type_enum, location, force_barefoot=False):
        """Replace template placeholders with generated outfit and scene data"""
        result = template
        
        ##############################################################################
        # CHARACTER
        ##############################################################################
        while "<<femaleChar>>" in result:
            character = self.character_generator.generate_character("female")
            result = result.replace("<<femaleChar>>", character, 1)
            
        while "<<woman>>" in result:
            character = self.character_generator.generate_character("female")
            result = result.replace("<<woman>>", character, 1)
            
        while "<<maleChar>>" in result:
            character = self.character_generator.generate_character("male")
            result = result.replace("<<maleChar>>", character, 1)
            
        while "<<man>>" in result:
            character = self.character_generator.generate_character("male")
            result = result.replace("<<man>>", character, 1)
            
        ##############################################################################
        # POSES
        ##############################################################################
        while "<<anyPose>>" in result:
            pose = self.pose_generator.generate_pose()
            result = result.replace("<<anyPose>>", pose, 1)
            
        while "<<sitting>>" in result:
            pose = self.pose_generator.generate_sitting_on_ground_pose()
            result = result.replace("<<sitting>>", pose, 1)
            
        while "<<sittingOnGround>>" in result:
            pose = self.pose_generator.generate_sitting_on_ground_pose()
            result = result.replace("<<sittingOnGround>>", pose, 1)
            
        while "<<sittingOnA>>" in result:
            pose = self.pose_generator.generate_sitting_on_a_pose()
            result = result.replace("<<sittingOnA>>", pose, 1)
            
        while "<<crouching>>" in result:
            pose = self.pose_generator.generate_crouching_pose()
            result = result.replace("<<crouching>>", pose, 1)
            
        while "<<kneeling>>" in result:
            pose = self.pose_generator.generate_kneeling_pose()
            result = result.replace("<<kneeling>>", pose, 1)
            
        while "<<onAllFours>>" in result:
            pose = self.pose_generator.generate_on_all_fours_pose()
            result = result.replace("<<onAllFours>>", pose, 1)
            
        while "<<lying>>" in result:
            pose = self.pose_generator.generate_lying_pose()
            result = result.replace("<<lying>>", pose, 1)
            
        while "<<standing>>" in result:
            pose = self.pose_generator.generate_standing_pose()
            result = result.replace("<<standing>>", pose, 1)
            
        while "<<walking>>" in result:
            pose = self.pose_generator.generate_walking_pose()
            result = result.replace("<<walking>>", pose, 1)
            
        while "<<running>>" in result:
            pose = self.pose_generator.generate_running_pose()
            result = result.replace("<<running>>", pose, 1)
            
        while "<<jumping>>" in result:
            pose = self.pose_generator.generate_jumping_pose()
            result = result.replace("<<jumping>>", pose, 1)
            
        while "<<dancing>>" in result:
            pose = self.pose_generator.generate_dancing_pose()
            result = result.replace("<<dancing>>", pose, 1)
            
        while "<<posing>>" in result:
            pose = self.pose_generator.generate_posing_pose()
            result = result.replace("<<posing>>", pose, 1)
            
        while "<<leaning>>" in result:
            pose = self.pose_generator.generate_leaning_pose()
            result = result.replace("<<leaning>>", pose, 1)
            
        ##############################################################################
        # OUTFIT
        ##############################################################################
        while "<<femaleOutfit>>" in result:
            female_outfit = self.outfit_generator.generate_outfit(outfit_type_enum, "female", force_barefoot)
            result = result.replace("<<femaleOutfit>>", female_outfit, 1)
        
        while "<<maleOutfit>>" in result:
            male_outfit = self.outfit_generator.generate_outfit(outfit_type_enum, "male", force_barefoot)
            result = result.replace("<<maleOutfit>>", male_outfit, 1)
        
        ##############################################################################
        # SCENE
        ##############################################################################
        while "<<scene>>" in result:
            scene = self.scene_generator.generate_scene(outfit_type_enum, location)
            result = result.replace("<<scene>>", scene, 1)
        
        while "<<location>>" in result:
            scene = self.scene_generator.generate_scene(outfit_type_enum, location)
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
        
        return final_prompt


def test_basic_functionality():
    """Test basic PromptGenerator functionality"""
    print("=== Testing Basic PromptGenerator Functionality ===\n")
    
    generator = PromptGeneratorStandalone()
    
    # Test 1: Basic female outfit generation
    print("Test 1: Basic female outfit with template")
    template = "A photo of <<woman>> wearing <<femaleOutfit>> in <<scene>>"
    result = generator.generate_prompt(template, "casual chic", "indoors")
    print(f"Template: {template}")
    print(f"Result: {result}")
    print()
    
    # Test 2: Male outfit generation
    print("Test 2: Male outfit generation")
    template = "A photo of <<man>> wearing <<maleOutfit>> <<standing>> in <<location>>"
    result = generator.generate_prompt(template, "business wear", "outdoors")
    print(f"Template: {template}")
    print(f"Result: {result}")
    print()
    
    # Test 3: With poses
    print("Test 3: With various poses")
    template = "<<woman>> <<sitting>> wearing <<femaleOutfit>>"
    result = generator.generate_prompt(template, "beach wear", "beach")
    print(f"Template: {template}")
    print(f"Result: {result}")
    print()
    
    # Test 4: Random outfit type
    print("Test 4: Random outfit type")
    template = "<<woman>> wearing <<femaleOutfit>> <<anyPose>>"
    result = generator.generate_prompt(template, "random", "anything")
    print(f"Template: {template}")
    print(f"Result: {result}")
    print()
    
    # Test 5: With seed for reproducibility
    print("Test 5: With seed (should be reproducible)")
    template = "<<woman>> wearing <<femaleOutfit>>"
    seed = 12345
    result1 = generator.generate_prompt(template, "punk", "outdoors", seed=seed)
    result2 = generator.generate_prompt(template, "punk", "outdoors", seed=seed)
    print(f"Template: {template}")
    print(f"Seed: {seed}")
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
    print(f"Results match: {result1 == result2}")
    print()
    
    # Test 6: Force barefoot option
    print("Test 6: Force barefoot option")
    template = "<<woman>> wearing <<femaleOutfit>>"
    result = generator.generate_prompt(template, "casual chic", "indoors", force_barefoot=True)
    print(f"Template: {template}")
    print(f"Result (barefoot): {result}")
    print()


def test_all_outfit_types():
    """Test generation with all outfit types"""
    print("=== Testing All Outfit Types ===\n")
    
    generator = PromptGeneratorStandalone()
    template = "<<woman>> wearing <<femaleOutfit>>"
    
    for outfit_type in OUTFIT_TYPE_NAMES:
        if outfit_type == "random":
            continue
        result = generator.generate_prompt(template, outfit_type, "indoors")
        print(f"{outfit_type.title()}: {result}")
    print()


def test_all_locations():
    """Test generation with all location types"""
    print("=== Testing All Location Types ===\n")
    
    generator = PromptGeneratorStandalone()
    template = "<<woman>> wearing <<femaleOutfit>> in <<scene>>"
    
    for location in LOCATION_TYPE_NAMES:
        result = generator.generate_prompt(template, "casual chic", location)
        print(f"{location.title()}: {result}")
    print()


def interactive_test():
    """Interactive testing mode"""
    print("=== Interactive Testing Mode ===")
    print("Available outfit types:", ", ".join(OUTFIT_TYPE_NAMES))
    print("Available locations:", ", ".join(LOCATION_TYPE_NAMES))
    print("Available template placeholders:")
    print("  Characters: <<woman>>, <<man>>, <<femaleChar>>, <<maleChar>>")
    print("  Outfits: <<femaleOutfit>>, <<maleOutfit>>")
    print("  Scenes: <<scene>>, <<location>>")
    print("  Poses: <<anyPose>>, <<standing>>, <<sitting>>, <<walking>>, <<running>>, <<jumping>>, etc.")
    print("Type 'quit' to exit\n")
    
    generator = PromptGeneratorStandalone()
    
    while True:
        try:
            template = input("Enter template (or 'quit'): ").strip()
            if template.lower() == 'quit':
                break
                
            outfit_type = input(f"Enter outfit type [{OUTFIT_TYPE_NAMES[0]}]: ").strip()
            if not outfit_type:
                outfit_type = OUTFIT_TYPE_NAMES[0]
                
            location = input(f"Enter location [{LOCATION_TYPE_NAMES[0]}]: ").strip()
            if not location:
                location = LOCATION_TYPE_NAMES[0]
                
            seed_input = input("Enter seed (-1 for random): ").strip()
            seed = int(seed_input) if seed_input and seed_input != "-1" else -1
            
            barefoot_input = input("Force barefoot? (y/n) [n]: ").strip().lower()
            force_barefoot = barefoot_input == 'y'
            
            result = generator.generate_prompt(template, outfit_type, location, seed, force_barefoot)
            print(f"\nResult: {result}\n")
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    print("PromptGenerator Standalone Test Script")
    print("=====================================\n")
    
    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        interactive_test()
    else:
        # Run automated tests
        test_basic_functionality()
        test_all_outfit_types()
        test_all_locations()
        
        print("\n=== All Tests Complete ===")
        print("Run with 'python test_prompt_generator.py interactive' for interactive testing")