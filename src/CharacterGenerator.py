
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

class CharacterGenerator:
    
    @staticmethod
    def generate_character(sex="female"):
        """Generate a single character description string for the given sex"""
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
        nationality = random.choice(NATIONALITY)
        body_type = random.choice(BODY_TYPE)
        breast_size = "with " + random.choice(BREAST_SIZES) if sex == "female" else ""
        
        # Handle weighted selection for hair styles and colors (works for both male and female)
        hair_style = random.choices([item[0] for item in HAIR_STYLES], 
                                    weights=[item[1] for item in HAIR_STYLES], 
                                    k=1)[0]
        hair_color = random.choices([item[0] for item in HAIR_COLORS], 
                                    weights=[item[1] for item in HAIR_COLORS], 
                                    k=1)[0]

        # Handle weighted selection for eye colors
        eye_color = random.choices([item[0] for item in EYE_COLORS], 
                                   weights=[item[1] for item in EYE_COLORS], 
                                   k=1)[0]
        
        eye_shape = random.choice(EYE_SHAPES)
        skin_tone = random.choice(SKIN_TONES)
        facial_features = random.choice(FACIAL_FEATURES)
        lip_shape = random.choice(LIP_SHAPES)
        nose_shape = random.choice(NOSE_SHAPES)
        makeup_style = random.choice(MAKEUP_STYLES)
        age_group = random.choice(AGE_GROUPS)
        personality_vibe = random.choice(PERSONALITY_VIBES)
        facial_expression = random.choice(FACIAL_EXPRESSIONS)
        
        # Create descriptive string
        character_description = f"{nationality} in {gender_pronoun} {age_group}, {hair_color} {hair_style}, {eye_color} {eye_shape}, {skin_tone}, {body_type} {breast_size}, {lip_shape}, {nose_shape}, {facial_features}, {makeup_style}, {personality_vibe} personality, {facial_expression}"
        return character_description
    
    @staticmethod
    def generate_simple_character(sex="female"):
        """Generate a simplified character description string with only basic attributes"""
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
        body_type = random.choice(BODY_TYPE)
        breast_size = "with " + random.choice(BREAST_SIZES) if sex == "female" else ""
        
        # Handle weighted selection for hair styles and colors (works for both male and female)
        hair_style = random.choices([item[0] for item in HAIR_STYLES], 
                                    weights=[item[1] for item in HAIR_STYLES], 
                                    k=1)[0]
        hair_color = random.choices([item[0] for item in HAIR_COLORS], 
                                    weights=[item[1] for item in HAIR_COLORS], 
                                    k=1)[0]

        skin_tone = random.choice(SKIN_TONES)
        makeup_style = random.choice(MAKEUP_STYLES)
        age_group = random.choice(AGE_GROUPS)
        
        # Create simplified descriptive string
        character_description = f"{age_group}, {hair_color} {hair_style}, {skin_tone}, {body_type} {breast_size}, {makeup_style}"
        return character_description