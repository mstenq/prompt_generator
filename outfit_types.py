"""
Outfit types definitions for the ComfyUI Outfit Generator.
This file contains the OutfitType enum and related constants.
"""

from enum import Enum

class OutfitType(Enum):
    BUSINESS_WEAR = "business wear"
    LINGERIE = "lingerie"
    BEACH_WEAR = "beach wear"
    GRUNGE = "grunge"
    PREPPY = "preppy"
    EVENING_FORMAL = "evening/formal wear"
    CASUAL_CHIC = "casual chic"
    ATHLEISURE = "athleisure"
    STREETWEAR = "streetwear"
    NORMCORE = "normcore"
    PUNK = "punk"
    CYBERPUNK = "cyberpunk"
    BOHEMIAN = "bohemian"
    COTTAGECORE = "cottagecore"
    LOLITA = "lolita"
    MILITARY = "military"
    COWBOY = "cowboy"
    ETHEREAL = "ethereal"
    CLUB_PARTY = "club/party wear"
    PIN_UP = "pin-up"
    AVANT_GARDE = "avant-garde"
    FESTIVAL = "festival wear"
    GOTHIC = "gothic"
    STEAMPUNK = "steampunk"
    RETRO = "retro"
    MINIMALIST = "minimalist"
    KAWAII = "kawaii"
    ROCKABILLY = "rockabilly"
    ROMANTIC = "romantic"

# Generate outfit type names for dropdown from enum values
OUTFIT_TYPE_NAMES = ["random"] + [outfit_type.value for outfit_type in OutfitType]