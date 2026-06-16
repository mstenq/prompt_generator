"""
Outfit types definitions for the ComfyUI Outfit Generator.
This file contains the OutfitType enum and related constants.
"""

from enum import Enum

class OutfitType(Enum):
    ANIME = "anime"
    ATHLEISURE = "athleisure"
    AVANT_GARDE = "avant-garde"
    BEACH_WEAR = "beach wear"
    BIKINI = "bikini" 
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
    SWIMSUIT = "swimsuit"
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
    FRONT_YARD = "front yard"
    BACK_YARD = "back yard"
    RESTAURANT = "restaurant"
    BAR = "bar"
    NIGHTCLUB = "nightclub"
    GYM = "gym"
    HOTEL = "hotel"
    PARK = "park"
    POOL = "pool"
    SUBWAY = "subway"
    AIRPORT = "airport"
    TRAIN_STATION = "train station"
    ROOFTOP = "rooftop"
    FOREST = "forest"
    MOUNTAIN = "mountain"
    DESERT = "desert"
    GARDEN = "garden"
    STUDIO = "studio"
    WAREHOUSE = "warehouse"
    CHURCH = "church"
    CARNIVAL = "carnival"
    FARM = "farm"
    BOAT = "boat"
    GARAGE = "garage"
    BASEMENT = "basement"
    ATTIC = "attic"
    BALCONY = "balcony"

# Generate outfit type names for dropdown from enum values
OUTFIT_TYPE_NAMES = ["random"] + [outfit_type.value for outfit_type in OutfitType]

# Generate location type names for dropdown from enum values
LOCATION_TYPE_NAMES = ["anything"] + [location_type.value for location_type in LocationType]

FOOTWEAR_MODE_NAMES = [
    "omit",
    "barefoot - natural toenails",
    "barefoot - painted toenails",
    "socks - white",
    "socks - black",
    "socks - any color",
    "shoes",
]