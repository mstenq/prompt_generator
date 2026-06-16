import random
from .enums import OutfitType, OUTFIT_TYPE_NAMES, FOOTWEAR_MODE_NAMES
from .female.shoes import FEMALE_SHOES
from .male.shoes import MALE_SHOES
from .ColorGenerator import ColorGenerator
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
                "footwear_mode": (FOOTWEAR_MODE_NAMES, {"default": "shoes"}),
                "seed": ("INT", {"default": -1, "min": -1, "max": 2147483647}),
            },
        }

    RETURN_TYPES = ("PROMPT_VAR",)
    RETURN_NAMES = ("shoe",)

    FUNCTION = "generate_shoe_node"

    CATEGORY = "prompt_generator"
    OUTPUT_NODE = True
       
    def generate_shoe_node(self, outfit_type, sex, seed=-1, footwear_mode="shoes"):
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
                
        shoe_description = self.generate_shoe(outfit_type_enum, sex, footwear_mode)
        return {
            "ui": {"text": (shoe_description,)},
            "result": (shoe_description,)
        }
    
    @staticmethod
    def generate_shoe(outfit_type_enum, sex="female", footwear_mode="shoes"):
        """Generate a single footwear description for the given outfit type and sex"""
        if footwear_mode == "omit":
            return ""

        if footwear_mode == "barefoot - natural toenails":
            return clean_generated_text("barefoot")

        if footwear_mode == "barefoot - painted toenails":
            if sex == "female":
                nail_color = random.choice(FEMALE_SHOES["barefoot"]["colors"])
                return clean_generated_text(f"barefoot with toenails painted with {nail_color}")
            return clean_generated_text("barefoot")

        if footwear_mode == "socks - white":
            return clean_generated_text("white socks")

        if footwear_mode == "socks - black":
            return clean_generated_text("black socks")

        if footwear_mode == "socks - any color":
            sock_color = ColorGenerator.generate_color()
            return clean_generated_text(f"{sock_color} socks")

        # Use either male or female clothing items based on sex parameter
        if sex == "female":
            SHOES = FEMALE_SHOES
        else:  # male
            SHOES = MALE_SHOES

        # Filter clothing items that match the selected outfit type
        compatible_shoes = [
            name for name, data in SHOES.items()
            if outfit_type_enum in data["types"] and name != "barefoot"
        ]
        
        # Fallback to all items if no matches found (shouldn't happen with proper data)
        if not compatible_shoes:
            compatible_shoes = [name for name in SHOES.keys() if name != "barefoot"]
              
        selected_shoes = random.choice(compatible_shoes)
        shoe_color = random.choice(SHOES[selected_shoes]["colors"])
        shoe_description = clean_generated_text(f"{shoe_color} {selected_shoes}")
        
        return shoe_description
