from .CharacterGenerator import FemaleCharacterGenerator, SimpleFemaleCharacterGenerator
from .PromptGenerator import PromptGenerator
from .OutfitGenerator import OutfitGenerator
from .SceneGenerator import SceneGenerator

NODE_CLASS_MAPPINGS = {
    "prompt-generator": PromptGenerator,
    "outfit-generator": OutfitGenerator,
    "scene-generator": SceneGenerator,
    "female-generator": FemaleCharacterGenerator,
    "simple-female-generator": SimpleFemaleCharacterGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "prompt-generator": "Prompt Generator",
    "outfit-generator": "Outfit Generator",
    "scene-generator": "Scene Generator",
    "female-generator": "Female Generator",
    "simple-female-generator": "Simple Female Generator"
}