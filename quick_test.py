#!/usr/bin/env python3
"""
Quick test script for PromptGenerator - just basic functionality
Run this from the outfit_generator directory with: python quick_test.py
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


class QuickPromptTest:
    def __init__(self):
        # Create instances of all generators
        self.outfit_generator = OutfitGenerator()
        self.scene_generator = SceneGenerator()
        self.character_generator = CharacterGenerator()
        self.pose_generator = PoseGenerator()

    def test_female_outfit(self):
        print("=== Female Outfit Test ===")
        template = "A photo of <<woman>> wearing <<femaleOutfit>>"
        result = self.process_template(template, "casual chic", "indoors")
        print(f"Template: {template}")
        print(f"Result: {result}")
        print()

    def test_male_outfit(self):
        print("=== Male Outfit Test ===")
        template = "A photo of <<man>> wearing <<maleOutfit>>"
        result = self.process_template(template, "business wear", "outdoors")
        print(f"Template: {template}")
        print(f"Result: {result}")
        print()

    def test_with_pose_and_scene(self):
        print("=== Pose and Scene Test ===")
        template = "<<woman>> <<standing>> wearing <<femaleOutfit>> in <<scene>>"
        result = self.process_template(template, "punk", "outdoors")
        print(f"Template: {template}")
        print(f"Result: {result}")
        print()

    def process_template(self, template, outfit_type, location):
        # Convert outfit type to enum
        if outfit_type == "random":
            outfit_type_enum = random.choice(list(OutfitType))
        else:
            outfit_type_enum = None
            for ot in OutfitType:
                if ot.value == outfit_type:
                    outfit_type_enum = ot
                    break
            if outfit_type_enum is None:
                outfit_type_enum = OutfitType.CASUAL_CHIC

        result = template
        
        # Replace characters
        while "<<woman>>" in result:
            character = self.character_generator.generate_character("female")
            result = result.replace("<<woman>>", character, 1)
        
        while "<<man>>" in result:
            character = self.character_generator.generate_character("male")
            result = result.replace("<<man>>", character, 1)
        
        # Replace poses
        while "<<standing>>" in result:
            pose = self.pose_generator.generate_standing_pose()
            result = result.replace("<<standing>>", pose, 1)
        
        # Replace outfits
        while "<<femaleOutfit>>" in result:
            outfit = self.outfit_generator.generate_outfit(outfit_type_enum, "female")
            result = result.replace("<<femaleOutfit>>", outfit, 1)
        
        while "<<maleOutfit>>" in result:
            outfit = self.outfit_generator.generate_outfit(outfit_type_enum, "male")
            result = result.replace("<<maleOutfit>>", outfit, 1)
        
        # Replace scenes
        while "<<scene>>" in result:
            scene = self.scene_generator.generate_scene(outfit_type_enum, location)
            result = result.replace("<<scene>>", scene, 1)
        
        return result


if __name__ == "__main__":
    print("Quick PromptGenerator Test")
    print("==========================\n")
    
    tester = QuickPromptTest()
    
    try:
        tester.test_female_outfit()
        tester.test_male_outfit()
        tester.test_with_pose_and_scene()
        print("✅ All tests passed!")
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()