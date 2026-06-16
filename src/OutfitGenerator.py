import random
from .enums import OutfitType, OUTFIT_TYPE_NAMES, FOOTWEAR_MODE_NAMES
from .female.tops import FEMALE_TOPS
from .female.bottoms import FEMALE_BOTTOMS
from .female.accessories import FEMALE_ACCESSORIES
from .male.tops import MALE_TOPS
from .male.bottoms import MALE_BOTTOMS
from .male.accessories import MALE_ACCESSORIES
from .ShoeGenerator import ShoeGenerator
from .utils import clean_generated_text


class OutfitGenerator:
    def __init__(self):
     pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "outfit_type": (OUTFIT_TYPE_NAMES, {}),
                "sex": (["female", "male"], {"default": "female"}),
            },
            "optional": {
                "footwear_mode": (FOOTWEAR_MODE_NAMES, {"default": "shoes"}),
                "seed": ("INT", {"default": -1, "min": -1, "max": 2147483647}),
            },
        }

    RETURN_TYPES = ("PROMPT_VAR",)
    RETURN_NAMES = ("outfit",)

    FUNCTION = "generate_outfit_node"

    CATEGORY = "prompt_generator"
    OUTPUT_NODE = True
       
    def generate_outfit_node(self, outfit_type, sex, seed=-1, footwear_mode="shoes"):
        """Node function to generate outfit with optional seed for randomness"""
        if seed != -1:
            random.seed(seed)
            
        outfit_type_enum = None        

        if outfit_type == "random":
            # Random outfit type
            outfit_type_enum = random.choice(list(OutfitType))
        else:
            # Specific outfit type requested - find the matching enum
            for ot in OutfitType:
                if ot.value == outfit_type:
                    outfit_type_enum = ot
                    break
            if outfit_type_enum is None:
                outfit_type_enum = OutfitType.CASUAL_CHIC  # Default fallback
                
        outfit_description = self.generate_outfit(outfit_type_enum, sex, footwear_mode)
        return {
            "ui": {"text": (outfit_description,)},
            "result": (outfit_description,)
        }
    
    @staticmethod
    def generate_outfit(outfit_type_enum, sex="female", footwear_mode="shoes"):
        """Generate a single outfit description for the given outfit type and sex"""
        # Use either male or female clothing items based on sex parameter
        if sex == "female":
            TOPS = FEMALE_TOPS
            BOTTOMS = FEMALE_BOTTOMS
            ACCESSORIES = FEMALE_ACCESSORIES
        else:  # male
            TOPS = MALE_TOPS
            BOTTOMS = MALE_BOTTOMS
            ACCESSORIES = MALE_ACCESSORIES

        # Filter clothing items that match the selected outfit type
        compatible_tops = [name for name, data in TOPS.items() if outfit_type_enum in data["types"]]
        compatible_bottoms = [name for name, data in BOTTOMS.items() if outfit_type_enum in data["types"]]
        compatible_accessories = [name for name, data in ACCESSORIES.items() if outfit_type_enum in data["types"]]
        
        # Fallback to all items if no matches found (shouldn't happen with proper data)
        if not compatible_tops:
            compatible_tops = list(TOPS.keys())
        if not compatible_bottoms:
            compatible_bottoms = list(BOTTOMS.keys())
        if not compatible_accessories:
            compatible_accessories = list(ACCESSORIES.keys())
        
        # Select random items
        selected_top = random.choice(compatible_tops)
        selected_bottom = random.choice(compatible_bottoms)
        # Only select accessory 30% of the time, otherwise use empty string
        selected_accessory = random.choice(compatible_accessories) if random.random() < 0.3 else ""
        
        # Check for full-body items and handle accordingly
        if TOPS[selected_top].get("fullBody", False):
            # If top is full-body, empty the bottom
            selected_bottom = ""
            bottom_color = ""
            top_color = random.choice(TOPS[selected_top]["colors"])
        elif BOTTOMS[selected_bottom].get("fullBody", False):
            # If bottom is full-body, empty the top
            selected_top = ""
            top_color = ""
            bottom_color = random.choice(BOTTOMS[selected_bottom]["colors"])
        else:
            # Normal outfit with separate top and bottom
            top_color = random.choice(TOPS[selected_top]["colors"])
            bottom_color = random.choice(BOTTOMS[selected_bottom]["colors"])
            
            # Ensure top and bottom colors are different (if possible)
            attempts = 0
            while bottom_color == top_color and attempts < 10:
                bottom_color = random.choice(BOTTOMS[selected_bottom]["colors"])
                attempts += 1

        shoe_part = ShoeGenerator.generate_shoe(outfit_type_enum, sex, footwear_mode)
        
        outfit_description = f"{top_color} {selected_top}, {bottom_color} {selected_bottom}, {shoe_part}, {selected_accessory}"
        
        # Clean up the generated text
        outfit_description = clean_generated_text(outfit_description)
        
        return outfit_description
