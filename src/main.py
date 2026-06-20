from .CharacterGenerator import FemaleCharacterGenerator, SimpleFemaleCharacterGenerator, MaleCharacterGenerator, SimpleMaleCharacterGenerator
from .PromptGenerator import PromptGenerator
from .OutfitGenerator import OutfitGenerator, FemaleOutfitGenerator, MaleOutfitGenerator
from .SceneGenerator import SceneGenerator
from .TopGenerator import TopGenerator
from .BottomsGenerator import BottomsGenerator
from .ShoeGenerator import ShoeGenerator

NODE_CLASS_MAPPINGS = {
    "prompt-generator": PromptGenerator,
    "outfit-generator": OutfitGenerator,
    "female-outfit-generator": FemaleOutfitGenerator,
    "male-outfit-generator": MaleOutfitGenerator,
    "scene-generator": SceneGenerator,
    "female-generator": FemaleCharacterGenerator,
    "simple-female-generator": SimpleFemaleCharacterGenerator,
    "male-generator": MaleCharacterGenerator,
    "simple-male-generator": SimpleMaleCharacterGenerator,
    "bottoms-generator": BottomsGenerator,
    "top-generator": TopGenerator,
    "shoe-generator": ShoeGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "prompt-generator": "Prompt Generator",
    "outfit-generator": "Outfit Generator",
    "female-outfit-generator": "Female Outfit Generator",
    "male-outfit-generator": "Male Outfit Generator",
    "scene-generator": "Scene Generator",
    "female-generator": "Female Generator",
    "simple-female-generator": "Simple Female Generator",
    "male-generator": "Male Generator",
    "simple-male-generator": "Simple Male Generator",
    "bottoms-generator": "Bottoms Generator",
    "top-generator": "Top Generator",
    "shoe-generator": "Shoe Generator"
}