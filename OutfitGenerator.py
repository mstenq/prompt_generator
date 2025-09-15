import random
from .outfit_types import OutfitType, OUTFIT_TYPE_NAMES
from .female.tops import FEMALE_TOPS
from .female.bottoms import FEMALE_BOTTOMS
from .female.accessories import FEMALE_ACCESSORIES
from .female.shoes import FEMALE_SHOES
from .male.tops import MALE_TOPS
from .male.bottoms import MALE_BOTTOMS
from .male.accessories import MALE_ACCESSORIES
from .male.shoes import MALE_SHOES

class OutfitGenerator:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "outfit_type": (OUTFIT_TYPE_NAMES, {}),
            },
            "optional": {
                "seed": ("INT", {"default": -1, "min": -1, "max": 2147483647}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("femaleOutfit1", "femaleOutfit2", "maleOutfit1", "maleOutfit2")

    FUNCTION = "generate_scene"

    CATEGORY = "examples"

    def _generate_single_outfit(self, outfit_type_enum, sex="female"):
        """Generate a single outfit description for the given outfit type and sex"""
        # Use either male or female clothing items based on sex parameter
        if sex == "female":
            TOPS = FEMALE_TOPS
            BOTTOMS = FEMALE_BOTTOMS
            ACCESSORIES = FEMALE_ACCESSORIES
            SHOES = FEMALE_SHOES
        else:  # male
            TOPS = MALE_TOPS
            BOTTOMS = MALE_BOTTOMS
            ACCESSORIES = MALE_ACCESSORIES
            SHOES = MALE_SHOES

        # Filter clothing items that match the selected outfit type
        compatible_tops = [name for name, data in TOPS.items() if outfit_type_enum in data["types"]]
        compatible_bottoms = [name for name, data in BOTTOMS.items() if outfit_type_enum in data["types"]]
        compatible_accessories = [name for name, data in ACCESSORIES.items() if outfit_type_enum in data["types"]]
        compatible_shoes = [name for name, data in SHOES.items() if outfit_type_enum in data["types"]]
        
        # Fallback to all items if no matches found (shouldn't happen with proper data)
        if not compatible_tops:
            compatible_tops = list(TOPS.keys())
        if not compatible_bottoms:
            compatible_bottoms = list(BOTTOMS.keys())
        if not compatible_accessories:
            compatible_accessories = list(ACCESSORIES.keys())
        if not compatible_shoes:
            compatible_shoes = list(SHOES.keys())
        
        # Select random items
        selected_top = random.choice(compatible_tops)
        selected_bottom = random.choice(compatible_bottoms)
        selected_accessory = random.choice(compatible_accessories)
        selected_shoes = random.choice(compatible_shoes)
        
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

        # Create outfit description
        outfit_description = f"{top_color} {selected_top}, {bottom_color} {selected_bottom}, {selected_shoes}, {selected_accessory}"
        return outfit_description

    def generate_scene(self, outfit_type, seed=-1):
        """Generate two random female and two random male outfit descriptions based on the selected type"""
        
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

        # Generate two different female outfits using the same outfit type
        female_outfit1 = self._generate_single_outfit(outfit_type_enum, "female")
        female_outfit2 = self._generate_single_outfit(outfit_type_enum, "female")
        
        # Generate two different male outfits using the same outfit type
        male_outfit1 = self._generate_single_outfit(outfit_type_enum, "male")
        male_outfit2 = self._generate_single_outfit(outfit_type_enum, "male")
        
        return (female_outfit1, female_outfit2, male_outfit1, male_outfit2)

NODE_CLASS_MAPPINGS = {
    "outfit-generator": OutfitGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "outfit-generator": "Outfit Generator"
}