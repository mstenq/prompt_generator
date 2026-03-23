import random
from .enums import OutfitType, OUTFIT_TYPE_NAMES
from .female.tops import FEMALE_TOPS
from .male.tops import MALE_TOPS
from .utils import clean_generated_text


class TopGenerator:
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
                "seed": ("INT", {"default": -1, "min": -1, "max": 2147483647}),
            },
        }

    RETURN_TYPES = ("PROMPT_VAR",)
    RETURN_NAMES = ("top",)

    FUNCTION = "generate_top_node"

    CATEGORY = "prompt_generator"
    OUTPUT_NODE = True
       
    def generate_top_node(self, outfit_type, sex, seed=-1):
        """Node function to generate top with optional seed for randomness"""
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
                
        outfit_description = self.generate_top(outfit_type_enum, sex)
        return {
            "ui": {"text": (outfit_description,)},
            "result": (outfit_description,)
        }
    
    @staticmethod
    def generate_top(outfit_type_enum, sex="female"):
        """Generate a single outfit description for the given outfit type and sex"""
        # Use either male or female clothing items based on sex parameter
        if sex == "female":
            TOPS = FEMALE_TOPS

        else:  # male
            TOPS = MALE_TOPS

        # Filter clothing items that match the selected outfit type
        compatible_tops = [name for name, data in TOPS.items() if outfit_type_enum in data["types"]]
        
        # Fallback to all items if no matches found (shouldn't happen with proper data)
        if not compatible_tops:
            compatible_tops = list(TOPS.keys())
        
        # Select random items
        selected_top = random.choice(compatible_tops)       
        top_color = random.choice(TOPS[selected_top]["colors"])

        
        outfit_description = f"{top_color} {selected_top}"
        
        # Clean up the generated text
        outfit_description = clean_generated_text(outfit_description)
        
        return outfit_description