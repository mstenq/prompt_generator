from .CharacterGenerator import FemaleCharacterGenerator, SimpleFemaleCharacterGenerator, MaleCharacterGenerator, SimpleMaleCharacterGenerator
from .PromptGenerator import PromptGenerator
from .OutfitGenerator import OutfitGenerator
from .SceneGenerator import SceneGenerator
from .TopGenerator import TopGenerator
from .BottomsGenerator import BottomsGenerator

NODE_CLASS_MAPPINGS = {
    "prompt-generator": PromptGenerator,
    "outfit-generator": OutfitGenerator,
    "scene-generator": SceneGenerator,
    "female-generator": FemaleCharacterGenerator,
    "simple-female-generator": SimpleFemaleCharacterGenerator,
    "male-generator": MaleCharacterGenerator,
    "simple-male-generator": SimpleMaleCharacterGenerator,
    "bottoms-generator": BottomsGenerator,
    "top-generator": TopGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "prompt-generator": "Prompt Generator",
    "outfit-generator": "Outfit Generator",
    "scene-generator": "Scene Generator",
    "female-generator": "Female Generator",
    "simple-female-generator": "Simple Female Generator",
    "male-generator": "Male Generator",
    "simple-male-generator": "Simple Male Generator",
    "bottoms-generator": "Bottoms Generator",
    "top-generator": "Top Generator"
}