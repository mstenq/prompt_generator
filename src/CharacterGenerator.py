
import random
from .female.character import (
    NATIONALITY as FEMALE_NATIONALITY,
    BODY_TYPE as FEMALE_BODY_TYPE,
    BREAST_SIZES as FEMALE_BREAST_SIZES,
    HAIR_STYLES as FEMALE_HAIR_STYLES,
    HAIR_COLORS as FEMALE_HAIR_COLORS,
    EYE_COLORS as FEMALE_EYE_COLORS,
    EYE_SHAPES as FEMALE_EYE_SHAPES,
    SKIN_TONES as FEMALE_SKIN_TONES,
    FACIAL_FEATURES as FEMALE_FACIAL_FEATURES,
    LIP_SHAPES as FEMALE_LIP_SHAPES,
    NOSE_SHAPES as FEMALE_NOSE_SHAPES,
    MAKEUP_STYLES as FEMALE_MAKEUP_STYLES,
    AGE_GROUPS as FEMALE_AGE_GROUPS,
    PERSONALITY_VIBES as FEMALE_PERSONALITY_VIBES,
    FACIAL_EXPRESSIONS as FEMALE_FACIAL_EXPRESSIONS
)
from .male.character import (
    NATIONALITY as MALE_NATIONALITY,
    BODY_STYLE as MALE_BODY_STYLE,
    BREAST_SIZES as MALE_BREAST_SIZES,
    HAIR_STYLES as MALE_HAIR_STYLES,
    HAIR_COLORS as MALE_HAIR_COLORS,
    EYE_COLORS as MALE_EYE_COLORS,
    EYE_SHAPES as MALE_EYE_SHAPES,
    SKIN_TONES as MALE_SKIN_TONES,
    FACIAL_FEATURES as MALE_FACIAL_FEATURES,
    LIP_SHAPES as MALE_LIP_SHAPES,
    NOSE_SHAPES as MALE_NOSE_SHAPES,
    MAKEUP_STYLES as MALE_MAKEUP_STYLES,
    AGE_GROUPS as MALE_AGE_GROUPS,
    PERSONALITY_VIBES as MALE_PERSONALITY_VIBES,
    FACIAL_EXPRESSIONS as MALE_FACIAL_EXPRESSIONS
)

class FemaleCharacterGenerator:
    def __init__(self):
     pass

    @classmethod
    def INPUT_TYPES(s):
        # Extract options from weighted lists (hair styles, hair colors, eye colors)
        hair_style_options = ["Random"] + [item[0] for item in FEMALE_HAIR_STYLES]
        hair_color_options = ["Random"] + [item[0] for item in FEMALE_HAIR_COLORS]
        eye_color_options = ["Random"] + [item[0] for item in FEMALE_EYE_COLORS]
        
        return {            
            "optional": {
                "nationality": (["Random"] + FEMALE_NATIONALITY, {"default": "Random"}),
                "body_type": (["Random"] + FEMALE_BODY_TYPE, {"default": "Random"}),
                "breast_size": (["Random"] + FEMALE_BREAST_SIZES, {"default": "Random"}),
                "hair_style": (hair_style_options, {"default": "Random"}),
                "hair_color": (hair_color_options, {"default": "Random"}),
                "eye_color": (eye_color_options, {"default": "Random"}),
                "eye_shape": (["Random"] + FEMALE_EYE_SHAPES, {"default": "Random"}),
                "skin_tone": (["Random"] + FEMALE_SKIN_TONES, {"default": "Random"}),
                "facial_feature": (["Random"] + FEMALE_FACIAL_FEATURES, {"default": "Random"}),
                "lip_shape": (["Random"] + FEMALE_LIP_SHAPES, {"default": "Random"}),
                "nose_shape": (["Random"] + FEMALE_NOSE_SHAPES, {"default": "Random"}),
                "makeup_style": (["Random"] + FEMALE_MAKEUP_STYLES, {"default": "Random"}),
                "age_group": (["Random"] + FEMALE_AGE_GROUPS, {"default": "Random"}),
                "personality_vibe": (["Random"] + FEMALE_PERSONALITY_VIBES, {"default": "Random"}),
                "facial_expression": (["Random"] + FEMALE_FACIAL_EXPRESSIONS, {"default": "Random"}),
                "seed": ("INT", {"default": -1, "min": -1, "max": 2147483647}),
            },
        }

    RETURN_TYPES = ("PROMPT_VAR",)
    RETURN_NAMES = ("woman",)

    FUNCTION = "generate_female_character_node"

    CATEGORY = "prompt_generator"
    OUTPUT_NODE = True  
    
    def generate_female_character_node(self, nationality="Random", body_type="Random", breast_size="Random", 
                                      hair_style="Random", hair_color="Random", eye_color="Random", 
                                      eye_shape="Random", skin_tone="Random", facial_feature="Random",
                                      lip_shape="Random", nose_shape="Random", makeup_style="Random",
                                      age_group="Random", personality_vibe="Random", facial_expression="Random",
                                      seed=-1):
        """Node function to generate female character with optional preset selections"""
        if seed != -1:
            random.seed(seed)
        
        # Build presets dict with only non-Random values
        presets = {}
        if nationality != "Random": presets["nationality"] = nationality
        if body_type != "Random": presets["body_type"] = body_type
        if breast_size != "Random": presets["breast_size"] = breast_size
        if hair_style != "Random": presets["hair_style"] = hair_style
        if hair_color != "Random": presets["hair_color"] = hair_color
        if eye_color != "Random": presets["eye_color"] = eye_color
        if eye_shape != "Random": presets["eye_shape"] = eye_shape
        if skin_tone != "Random": presets["skin_tone"] = skin_tone
        if facial_feature != "Random": presets["facial_feature"] = facial_feature
        if lip_shape != "Random": presets["lip_shape"] = lip_shape
        if nose_shape != "Random": presets["nose_shape"] = nose_shape
        if makeup_style != "Random": presets["makeup_style"] = makeup_style
        if age_group != "Random": presets["age_group"] = age_group
        if personality_vibe != "Random": presets["personality_vibe"] = personality_vibe
        if facial_expression != "Random": presets["facial_expression"] = facial_expression

        character_description = CharacterGenerator.generate_character("female", presets)
        return {
            "ui": {"text": (character_description,)},
            "result": (character_description,)
        }

class SimpleFemaleCharacterGenerator:
    def __init__(self):
     pass

    @classmethod
    def INPUT_TYPES(s):
        # Extract options from weighted lists (hair styles, hair colors, eye colors)
        hair_style_options = ["Random"] + [item[0] for item in FEMALE_HAIR_STYLES]
        hair_color_options = ["Random"] + [item[0] for item in FEMALE_HAIR_COLORS]
        
        return {            
            "optional": {
                "body_type": (["Random"] + FEMALE_BODY_TYPE, {"default": "Random"}),
                "breast_size": (["Random"] + FEMALE_BREAST_SIZES, {"default": "Random"}),
                "hair_style": (hair_style_options, {"default": "Random"}),
                "hair_color": (hair_color_options, {"default": "Random"}),
                "skin_tone": (["Random"] + FEMALE_SKIN_TONES, {"default": "Random"}),
                "makeup_style": (["Random"] + FEMALE_MAKEUP_STYLES, {"default": "Random"}),
                "age_group": (["Random"] + FEMALE_AGE_GROUPS, {"default": "Random"}),
                "seed": ("INT", {"default": -1, "min": -1, "max": 2147483647}),
            },
        }

    RETURN_TYPES = ("PROMPT_VAR",)
    RETURN_NAMES = ("woman",)

    FUNCTION = "generate_simple_female_character_node"

    CATEGORY = "prompt_generator"
    OUTPUT_NODE = True  
    
    def generate_simple_female_character_node(self, 
                                      body_type="Random", 
                                      breast_size="Random", 
                                      hair_style="Random", 
                                      hair_color="Random",  
                                      skin_tone="Random", 
                                      makeup_style="Random",
                                      age_group="Random",
                                      seed=-1):
        """Node function to generate simple female character with optional preset selections"""
        if seed != -1:
            random.seed(seed)
        
        # Build presets dict with only non-Random values
        presets = {}
        if body_type != "Random": presets["body_type"] = body_type
        if breast_size != "Random": presets["breast_size"] = breast_size
        if hair_style != "Random": presets["hair_style"] = hair_style
        if hair_color != "Random": presets["hair_color"] = hair_color
        if skin_tone != "Random": presets["skin_tone"] = skin_tone
        if makeup_style != "Random": presets["makeup_style"] = makeup_style
        if age_group != "Random": presets["age_group"] = age_group

        character_description = CharacterGenerator.generate_simple_character("female", presets)
        return {
            "ui": {"text": (character_description,)},
            "result": (character_description,)
        }

class CharacterGenerator:
           
    @staticmethod
    def generate_character(sex="female", presets=None):
        """Generate a single character description string for the given sex with optional presets
        
        Args:
            sex: "female" or "male"
            presets: Optional dict with preset values for any attributes (e.g., {"hair_color": "blonde", "age_group": "early 20s"})
        """
        if presets is None:
            presets = {}
        
        # Use either male or female character attributes based on sex parameter
        if sex == "female":
            NATIONALITY = FEMALE_NATIONALITY
            BODY_TYPE = FEMALE_BODY_TYPE
            BREAST_SIZES = FEMALE_BREAST_SIZES
            HAIR_STYLES = FEMALE_HAIR_STYLES
            HAIR_COLORS = FEMALE_HAIR_COLORS
            EYE_COLORS = FEMALE_EYE_COLORS
            EYE_SHAPES = FEMALE_EYE_SHAPES
            SKIN_TONES = FEMALE_SKIN_TONES
            FACIAL_FEATURES = FEMALE_FACIAL_FEATURES
            LIP_SHAPES = FEMALE_LIP_SHAPES
            NOSE_SHAPES = FEMALE_NOSE_SHAPES
            MAKEUP_STYLES = FEMALE_MAKEUP_STYLES
            AGE_GROUPS = FEMALE_AGE_GROUPS
            PERSONALITY_VIBES = FEMALE_PERSONALITY_VIBES
            FACIAL_EXPRESSIONS = FEMALE_FACIAL_EXPRESSIONS
            gender_pronoun = "her"
        else:  # male
            NATIONALITY = MALE_NATIONALITY
            BODY_TYPE = MALE_BODY_STYLE  # Note: male uses BODY_STYLE instead of BODY_TYPE
            BREAST_SIZES = MALE_BREAST_SIZES  # Will be empty for males
            HAIR_STYLES = MALE_HAIR_STYLES
            HAIR_COLORS = MALE_HAIR_COLORS
            EYE_COLORS = MALE_EYE_COLORS
            EYE_SHAPES = MALE_EYE_SHAPES
            SKIN_TONES = MALE_SKIN_TONES
            FACIAL_FEATURES = MALE_FACIAL_FEATURES
            LIP_SHAPES = MALE_LIP_SHAPES
            NOSE_SHAPES = MALE_NOSE_SHAPES
            MAKEUP_STYLES = MALE_MAKEUP_STYLES  # Will be empty for males
            AGE_GROUPS = MALE_AGE_GROUPS
            PERSONALITY_VIBES = MALE_PERSONALITY_VIBES
            FACIAL_EXPRESSIONS = MALE_FACIAL_EXPRESSIONS
            gender_pronoun = "his"
        
        # Generate character attributes (same logic for both sexes)
        # Use preset values if provided, otherwise random selection
        nationality = presets.get("nationality", random.choice(NATIONALITY))
        body_type = presets.get("body_type", random.choice(BODY_TYPE))
        
        if sex == "female":
            breast_size_value = presets.get("breast_size", random.choice(BREAST_SIZES))
            breast_size = "with " + breast_size_value
        else:
            breast_size = ""
        
        # Handle weighted selection for hair styles and colors (works for both male and female)
        if "hair_style" in presets:
            hair_style = presets["hair_style"]
        else:
            hair_style = random.choices([item[0] for item in HAIR_STYLES], 
                                        weights=[item[1] for item in HAIR_STYLES], 
                                        k=1)[0]
        
        if "hair_color" in presets:
            hair_color = presets["hair_color"]
        else:
            hair_color = random.choices([item[0] for item in HAIR_COLORS], 
                                        weights=[item[1] for item in HAIR_COLORS], 
                                        k=1)[0]

        # Handle weighted selection for eye colors
        if "eye_color" in presets:
            eye_color = presets["eye_color"]
        else:
            eye_color = random.choices([item[0] for item in EYE_COLORS], 
                                       weights=[item[1] for item in EYE_COLORS], 
                                       k=1)[0]
        
        eye_shape = presets.get("eye_shape", random.choice(EYE_SHAPES))
        skin_tone = presets.get("skin_tone", random.choice(SKIN_TONES))
        facial_features = presets.get("facial_feature", random.choice(FACIAL_FEATURES))
        lip_shape = presets.get("lip_shape", random.choice(LIP_SHAPES))
        nose_shape = presets.get("nose_shape", random.choice(NOSE_SHAPES))
        makeup_style = presets.get("makeup_style", random.choice(MAKEUP_STYLES))
        age_group = presets.get("age_group", random.choice(AGE_GROUPS))
        personality_vibe = presets.get("personality_vibe", random.choice(PERSONALITY_VIBES))
        facial_expression = presets.get("facial_expression", random.choice(FACIAL_EXPRESSIONS))
        
        # Create descriptive string
        character_description = f"{nationality} in {gender_pronoun} {age_group}, {hair_color} {hair_style}, {eye_color} {eye_shape}, {skin_tone}, {body_type} {breast_size}, {lip_shape}, {nose_shape}, {facial_features}, {makeup_style}, {personality_vibe} personality, {facial_expression}"
        return character_description
    
    @staticmethod
    def generate_simple_character(sex="female", presets=None):
        """Generate a simplified character description string with only basic attributes
        
        Args:
            sex: "female" or "male"
            presets: Optional dict with preset values for any attributes (e.g., {"hair_color": "blonde", "age_group": "early 20s"})
        """
        if presets is None:
            presets = {}
        
        # Use either male or female character attributes based on sex parameter
        if sex == "female":
            BODY_TYPE = FEMALE_BODY_TYPE
            BREAST_SIZES = FEMALE_BREAST_SIZES
            HAIR_STYLES = FEMALE_HAIR_STYLES
            HAIR_COLORS = FEMALE_HAIR_COLORS
            SKIN_TONES = FEMALE_SKIN_TONES
            MAKEUP_STYLES = FEMALE_MAKEUP_STYLES
            AGE_GROUPS = FEMALE_AGE_GROUPS
        else:  # male
            BODY_TYPE = MALE_BODY_STYLE  # Note: male uses BODY_STYLE instead of BODY_TYPE
            BREAST_SIZES = MALE_BREAST_SIZES  # Will be empty for males
            HAIR_STYLES = MALE_HAIR_STYLES
            HAIR_COLORS = MALE_HAIR_COLORS
            SKIN_TONES = MALE_SKIN_TONES
            MAKEUP_STYLES = MALE_MAKEUP_STYLES  # Will be empty for males
            AGE_GROUPS = MALE_AGE_GROUPS
        
        # Generate only the simplified character attributes
        # Use preset values if provided, otherwise random selection
        body_type = presets.get("body_type", random.choice(BODY_TYPE))
        
        if sex == "female":
            breast_size_value = presets.get("breast_size", random.choice(BREAST_SIZES))
            breast_size = "with " + breast_size_value
        else:
            breast_size = ""
        
        # Handle weighted selection for hair styles and colors (works for both male and female)
        if "hair_style" in presets:
            hair_style = presets["hair_style"]
        else:
            hair_style = random.choices([item[0] for item in HAIR_STYLES], 
                                        weights=[item[1] for item in HAIR_STYLES], 
                                        k=1)[0]
        
        if "hair_color" in presets:
            hair_color = presets["hair_color"]
        else:
            hair_color = random.choices([item[0] for item in HAIR_COLORS], 
                                        weights=[item[1] for item in HAIR_COLORS], 
                                        k=1)[0]

        skin_tone = presets.get("skin_tone", random.choice(SKIN_TONES))
        makeup_style = presets.get("makeup_style", random.choice(MAKEUP_STYLES))
        age_group = presets.get("age_group", random.choice(AGE_GROUPS))
        
        # Create simplified descriptive string
        character_description = f"{age_group}, {hair_color} {hair_style}, {skin_tone}, {body_type} {breast_size}, {makeup_style}"
        return character_description