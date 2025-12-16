"""
Outfit types definitions for the ComfyUI Outfit Generator.
This file contains the OutfitType enum and related constants.
"""

from enum import Enum

class OutfitType(Enum):
    ATHLEISURE = "athleisure"
    AVANT_GARDE = "avant-garde"
    BEACH_WEAR = "beach wear" 
    BOHEMIAN = "bohemian"
    BUSINESS_WEAR = "business wear"
    CASUAL_CHIC = "casual chic"
    CLUB_PARTY = "club/party wear"
    COTTAGECORE = "cottagecore"
    COWBOY = "cowboy"
    CYBERPUNK = "cyberpunk"
    ETHEREAL = "ethereal"
    EVENING_FORMAL = "evening/formal wear"
    FANTASY = "fantasy"
    FESTIVAL = "festival wear"
    GOTHIC = "gothic"
    GRUNGE = "grunge"
    KAWAII = "kawaii"
    LINGERIE = "lingerie"
    LOLITA = "lolita"
    MILITARY = "military"
    MINIMALIST = "minimalist"
    NORMCORE = "normcore"
    PIN_UP = "pin-up"
    PREPPY = "preppy"
    PUNK = "punk"
    RETRO = "retro"
    ROCKABILLY = "rockabilly"
    ROMANTIC = "romantic"
    STEAMPUNK = "steampunk"
    STREETWEAR = "streetwear"
    VINTAGE = "vintage"

class LocationType(Enum):
    BATHROOM = "bathroom"
    BEACH = "beach"
    BEDROOM = "bedroom"
    CITY = "city"
    INDOOR = "indoors"
    KITCHEN = "kitchen"
    LIVING_ROOM = "living room"
    MALL = "mall"
    OFFICE = "office"
    OUTDOOR = "outdoors"
    STORE = "store"

# Generate outfit type names for dropdown from enum values
OUTFIT_TYPE_NAMES = ["random"] + [outfit_type.value for outfit_type in OutfitType]

# Generate location type names for dropdown from enum values
LOCATION_TYPE_NAMES = ["anything"] + [location_type.value for location_type in LocationType]