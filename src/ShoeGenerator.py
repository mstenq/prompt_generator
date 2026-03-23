import random
from .enums import OutfitType, OUTFIT_TYPE_NAMES
from .female.shoes import FEMALE_SHOES
from .male.shoes import MALE_SHOES
from .utils import clean_generated_text


class ShoeGenerator:
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
                "force_barefoot": ("BOOLEAN", {"default": False}),
                "seed": ("INT", {"default": -1, "min": -1, "max": 2147483647}),
            },
        }

    RETURN_TYPES = ("PROMPT_VAR",)
    RETURN_NAMES = ("shoe",)

    FUNCTION = "generate_shoe_node"

    CATEGORY = "prompt_generator"
    OUTPUT_NODE = True
       
    def generate_shoe_node(self, outfit_type, sex, seed=-1, force_barefoot=False):
        """Node function to generate shoe with optional seed for randomness"""
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
                
        shoe_description = self.generate_shoe(outfit_type_enum, sex, force_barefoot)
        return {
            "ui": {"text": (shoe_description,)},
            "result": (shoe_description,)
        }
    
    @staticmethod
    def generate_shoe(outfit_type_enum, sex="female", force_barefoot=False):
        """Generate a single outfit description for the given outfit type and sex"""
        # Use either male or female clothing items based on sex parameter
        if sex == "female":
            SHOES = FEMALE_SHOES
        else:  # male
            SHOES = MALE_SHOES

        # Filter clothing items that match the selected outfit type
        compatible_shoes = [name for name, data in SHOES.items() if outfit_type_enum in data["types"]]
        
        # Fallback to all items if no matches found (shouldn't happen with proper data)
        if not compatible_shoes:
            compatible_shoes = list(SHOES.keys())
              
        # Force barefoot if requested, otherwise use existing logic
        if force_barefoot:
            selected_shoes = "barefoot"
        elif outfit_type_enum == OutfitType.BEACH_WEAR and random.random() < 0.4:
            selected_shoes = "barefoot"
        elif outfit_type_enum == OutfitType.LINGERIE and random.random() < 0.4:
            selected_shoes = "barefoot"
        else:
            selected_shoes = random.choice(compatible_shoes)
        
        shoe_color = random.choice(SHOES[selected_shoes]["colors"])
        
        # Create outfit description
        if selected_shoes == "barefoot":
            # Only add toenail polish for female characters
            if sex == "female":
                shoe_part = f"{selected_shoes} with toenails painted with {shoe_color}"
            else:
                shoe_part = f"{selected_shoes}"
        else:
            shoe_part = f"{shoe_color} {selected_shoes}"
        
        shoe_description = f"{shoe_part}"
        
        # Clean up the generated text
        shoe_description = clean_generated_text(shoe_description)
        
        return shoe_description