import random
from .enums import OutfitType, OUTFIT_TYPE_NAMES, FOOTWEAR_MODE_NAMES
from .female.tops import FEMALE_TOPS
from .female.bottoms import FEMALE_BOTTOMS
from .female.accessories import FEMALE_ACCESSORIES
from .male.tops import MALE_TOPS
from .male.bottoms import MALE_BOTTOMS
from .male.accessories import MALE_ACCESSORIES
from .ShoeGenerator import ShoeGenerator
from .utils import clean_generated_text, filter_items


def resolve_outfit_type(outfit_type: str) -> OutfitType:
    if outfit_type == "random":
        return random.choice(list(OutfitType))

    for ot in OutfitType:
        if ot.value == outfit_type:
            return ot

    return OutfitType.CASUAL_CHIC


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

        outfit_type_enum = resolve_outfit_type(outfit_type)
        outfit_description = self.generate_outfit(outfit_type_enum, sex, footwear_mode)
        return {
            "ui": {"text": (outfit_description,)},
            "result": (outfit_description,)
        }
    
    @staticmethod
    def generate_outfit(outfit_type_enum, sex="female", footwear_mode="shoes"):
        """Generate a single outfit description for the given outfit type and sex"""
        return OutfitGenerator.generate_outfit_with_search(
            outfit_type_enum, sex, footwear_mode
        )

    @staticmethod
    def generate_outfit_with_search(
        outfit_type_enum,
        sex="female",
        footwear_mode="shoes",
        top_search="",
        bottom_search="",
        shoe_search="",
        accessory_search="",
    ):
        """Generate outfit with optional per-category search filters."""
        if sex == "female":
            TOPS = FEMALE_TOPS
            BOTTOMS = FEMALE_BOTTOMS
            ACCESSORIES = FEMALE_ACCESSORIES
        else:
            TOPS = MALE_TOPS
            BOTTOMS = MALE_BOTTOMS
            ACCESSORIES = MALE_ACCESSORIES

        compatible_tops = filter_items(TOPS, outfit_type_enum, top_search)
        compatible_bottoms = filter_items(BOTTOMS, outfit_type_enum, bottom_search)
        compatible_accessories = filter_items(
            ACCESSORIES, outfit_type_enum, accessory_search
        )

        selected_top = random.choice(compatible_tops)
        selected_bottom = random.choice(compatible_bottoms)
        selected_accessory = (
            random.choice(compatible_accessories) if random.random() < 0.3 else ""
        )

        if TOPS[selected_top].get("fullBody", False):
            selected_bottom = ""
            bottom_color = ""
            top_color = random.choice(TOPS[selected_top]["colors"])
        elif BOTTOMS[selected_bottom].get("fullBody", False):
            selected_top = ""
            top_color = ""
            bottom_color = random.choice(BOTTOMS[selected_bottom]["colors"])
        else:
            top_color = random.choice(TOPS[selected_top]["colors"])
            bottom_color = random.choice(BOTTOMS[selected_bottom]["colors"])

            attempts = 0
            while bottom_color == top_color and attempts < 10:
                bottom_color = random.choice(BOTTOMS[selected_bottom]["colors"])
                attempts += 1

        shoe_part = ShoeGenerator.generate_shoe(
            outfit_type_enum, sex, footwear_mode, shoe_search=shoe_search
        )

        outfit_description = (
            f"{top_color} {selected_top}, {bottom_color} {selected_bottom}, "
            f"{shoe_part}, {selected_accessory}"
        )

        return clean_generated_text(outfit_description)


def _gendered_outfit_input_types():
    return {
        "required": {
            "outfit_type": (OUTFIT_TYPE_NAMES, {}),
        },
        "optional": {
            "footwear_mode": (FOOTWEAR_MODE_NAMES, {"default": "shoes"}),
            "seed": ("INT", {"default": -1, "min": -1, "max": 2147483647}),
            "top_search": ("STRING", {"default": ""}),
            "bottom_search": ("STRING", {"default": ""}),
            "shoe_search": ("STRING", {"default": ""}),
            "accessory_search": ("STRING", {"default": ""}),
        },
    }


class _GenderedOutfitGeneratorBase:
    RETURN_TYPES = ("PROMPT_VAR",)
    RETURN_NAMES = ("outfit",)
    FUNCTION = "generate_outfit_node"
    CATEGORY = "prompt_generator"
    OUTPUT_NODE = True
    SEX = "female"

    @classmethod
    def INPUT_TYPES(cls):
        return _gendered_outfit_input_types()

    def generate_outfit_node(
        self,
        outfit_type,
        seed=-1,
        footwear_mode="shoes",
        top_search="",
        bottom_search="",
        shoe_search="",
        accessory_search="",
    ):
        if seed != -1:
            random.seed(seed)

        outfit_type_enum = resolve_outfit_type(outfit_type)
        outfit_description = OutfitGenerator.generate_outfit_with_search(
            outfit_type_enum,
            self.SEX,
            footwear_mode,
            top_search=top_search,
            bottom_search=bottom_search,
            shoe_search=shoe_search,
            accessory_search=accessory_search,
        )
        return {
            "ui": {"text": (outfit_description,)},
            "result": (outfit_description,),
        }


class FemaleOutfitGenerator(_GenderedOutfitGeneratorBase):
    SEX = "female"


class MaleOutfitGenerator(_GenderedOutfitGeneratorBase):
    SEX = "male"
