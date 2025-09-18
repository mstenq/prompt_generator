"""
Clothing data definitions for the ComfyUI Outfit Generator.
This file contains clothing items tagged with their compatible outfit types and color palettes.
"""

from .enums import OutfitType, LocationType
from .colors import *

SCENES = {
    "living room": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "rooftop bar at sunset": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR],
    },
    "underground subway station": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "high-rise corporate office": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.PREPPY],
        "location": [LocationType.INDOOR],
    },
    "cozy coffee shop corner": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR],
    },
    "neon-lit city alleyway": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.PUNK],
        "location": [LocationType.OUTDOOR],
    },
    "tropical beach at sunrise": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "deserted carnival grounds": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR],
    },
    "mountain hiking trail": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR],
    },
    "vintage record store": {
        "types": [OutfitType.RETRO, OutfitType.GRUNGE, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR],
    },
    "crowded street market": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR],
    },
    "dark forest clearing": {
        "types": [OutfitType.GOTHIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "art museum gallery": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR],
    },
    "small-town diner booth": {
        "types": [OutfitType.RETRO, OutfitType.ROCKABILLY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR],
    },
    "abandoned factory floor": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR],
    },
    "upscale hotel lobby": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "skate park at dusk": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR],
    },
    "rain-soaked city street": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR],
    },
    "luxury yacht deck": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR],
    },
    "old library reading room": {
        "types": [OutfitType.PREPPY, OutfitType.COTTAGECORE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "desert road with tumbleweeds": {
        "types": [OutfitType.COWBOY, OutfitType.GRUNGE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR],
    },
    "fire escape stairwell": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR],
    },
    "festival main stage crowd": {
        "types": [OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR],
    },
    "hidden speakeasy": {
        "types": [OutfitType.RETRO, OutfitType.EVENING_FORMAL, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR],
    },
    "stone castle courtyard": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "flower-filled meadow": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR],
    },
    "train station platform": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "parisian balcony view": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR],
    },
    "futuristic cyber-city skyline": {
        "types": [OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR],
    },
    "old wooden barn interior": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR],
    },
    "lantern-lit garden at night": {
        "types": [OutfitType.ROMANTIC, OutfitType.GOTHIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "motorcycle garage workshop": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR],
    },
    "snowy mountain lodge": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR],
    },
    "ivy-covered college campus": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR],
    },
    "downtown fashion district": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR],
    },
    "jungle waterfall pool": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR],
    },
    "rainforest canopy bridge": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BOHEMIAN, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR],
    },
    "suburban backyard bbq": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR],
    },
    "candlelit ballroom": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR],
    },
    "desert oasis camp": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR],
    },
    "cliffside overlook": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "secret underground bunker": {
        "types": [OutfitType.MILITARY, OutfitType.CYBERPUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR],
    },
    "bustling airport terminal": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR],
    },
    "roller skating rink": {
        "types": [OutfitType.RETRO, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR],
    },
    "vibrant chinatown street": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR],
    },
    "dilapidated church ruins": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "cozy cabin fireplace": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR],
    },
    "shimmering ice cave": {
        "types": [OutfitType.ETHEREAL, OutfitType.GOTHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "classic 1950s diner": {
        "types": [OutfitType.RETRO, OutfitType.ROCKABILLY, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR],
    },
    "retro arcade": {
        "types": [OutfitType.RETRO, OutfitType.KAWAII, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR],
    },
    "empty movie theater": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR],
    },
    "rooftop greenhouse garden": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "farmer's market stall": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR],
    },
    "dusty wild west saloon": {
        "types": [OutfitType.COWBOY, OutfitType.RETRO, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR],
    },
    "urban graffiti wall": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.OUTDOOR],
    },
    "mediterranean vineyard": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR],
    },
    "gothic cathedral interior": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR],
    },
    "remote desert gas station": {
        "types": [OutfitType.GRUNGE, OutfitType.COWBOY, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "underground rave": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR],
    },
    "antique bookshop": {
        "types": [OutfitType.COTTAGECORE, OutfitType.PREPPY, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR],
    },
    "tranquil japanese garden": {
        "types": [OutfitType.MINIMALIST, OutfitType.ETHEREAL, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR],
    },
    "modern art installation room": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR],
    },
    "carnival ferris wheel seat": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR],
    },
    "ski resort après-ski lounge": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.INDOOR],
    },
    "rainy bus stop bench": {
        "types": [OutfitType.GRUNGE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR],
    },
    "boardwalk by the ocean": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR],
    },
    "overgrown abandoned greenhouse": {
        "types": [OutfitType.COTTAGECORE, OutfitType.GRUNGE, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "polished marble courthouse steps": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR],
    },
    "shimmering desert dunes": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR],
    },
    "futuristic hover-train terminal": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MINIMALIST, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR],
    },
    "small-town fairgrounds": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR],
    },
    "candlelit wine cellar": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR],
    },
    "rooftop infinity pool": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR],
    },
    "tropical jungle ruins": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ATHLEISURE, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR],
    },
    "grungy dive bar": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.ROCKABILLY],
        "location": [LocationType.INDOOR],
    },
    "stone-paved european street": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR],
    },
    "old clock tower interior": {
        "types": [OutfitType.STEAMPUNK, OutfitType.GOTHIC, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR],
    },
    "dark velvet opera house": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.GOTHIC, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR],
    },
    "moonlit pier": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "city park fountain": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR],
    },
    "luxurious fashion runway": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "underground catacombs": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.MILITARY],
        "location": [LocationType.INDOOR],
    },
    "enchanted forest glade": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR],
    },
    "crashed spaceship wreckage": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MILITARY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR],
    },
    "classic drive-in theater": {
        "types": [OutfitType.RETRO, OutfitType.ROCKABILLY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR],
    },
    "wide-open sunflower field": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR],
    },
    "sleek glass skyscraper lobby": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR],
    },
    "remote mountain monastery": {
        "types": [OutfitType.MINIMALIST, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR],
    },
    "train dining car": {
        "types": [OutfitType.RETRO, OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "1920s jazz club": {
        "types": [OutfitType.RETRO, OutfitType.EVENING_FORMAL, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR],
    },
    "industrial shipping docks": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR],
    },
    "rooftop helipad": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR],
    },
    "vibrant moroccan bazaar": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR],
    },
    "haunted victorian mansion": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.LOLITA],
        "location": [LocationType.INDOOR],
    },
    "foggy cemetery": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "glittering las vegas strip": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.PIN_UP],
        "location": [LocationType.OUTDOOR],
    },
    "floating sky island": {
        "types": [OutfitType.ETHEREAL, OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK],
        "location": [LocationType.OUTDOOR],
    },
    "hidden speakeasy jazz bar": {
        "types": [OutfitType.RETRO, OutfitType.EVENING_FORMAL, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR],
    },
    "subway graffiti tunnel": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR],
    },
    "secluded cliffside lighthouse": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "golden autumn forest path": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR],
    },
    # Home Interior Scenes
    "living room with a big sofa": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR],
    },
    "kitchen with breakfast table": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "bedroom with messy sheets": {
        "types": [OutfitType.LINGERIE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bathroom vanity mirror": {
        "types": [OutfitType.LINGERIE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR],
    },
    "walk-in closet full of clothes": {
        "types": [OutfitType.LINGERIE, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "laundry room with clothesline": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR],
    },
    "home office desk setup": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "attic filled with boxes": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.GRUNGE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "basement storage area": {
        "types": [OutfitType.GRUNGE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "garage with tools and bikes": {
        "types": [OutfitType.GRUNGE, OutfitType.ATHLEISURE, OutfitType.MILITARY],
        "location": [LocationType.INDOOR],
    },
    "dining room with chandelier": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.INDOOR],
    },
    "hallway with framed photos": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.PREPPY],
        "location": [LocationType.INDOOR],
    },
    "cozy fireplace living room": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR],
    },
    "pantry or food cupboard": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR],
    },
    "child's playroom": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "apartment balcony with plants": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR],
    },
    "studio apartment loft": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR],
    },
    "stairwell in a home": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "sunroom with glass windows": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "kitchen island counter": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    # Outdoor Mundane/Urban
    "city sidewalk with streetlights": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR],
    },
    "residential driveway": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR],
    },
    "backyard garden with fence": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR],
    },
    "front porch with rocking chair": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR],
    },
    "neighborhood cul-de-sac": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR],
    },
    "community park playground": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR],
    },
    "suburban street at dusk": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR],
    },
    "school hallway with lockers": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR],
    },
    "high school classroom": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.KAWAII],
        "location": [LocationType.INDOOR],
    },
    "empty basketball court": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR],
    },
    "tennis court": {
        "types": [OutfitType.ATHLEISURE, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR],
    },
    "baseball field dugout": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR],
    },
    "small-town post office": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "grocery store aisle": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR],
    },
    "shopping mall food court": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.KAWAII],
        "location": [LocationType.INDOOR],
    },
    "gas station pump": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.GRUNGE, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR],
    },
    "car wash tunnel": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "parking garage rooftop": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR],
    },
    "alleyway with dumpsters": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR],
    },
    "bus stop shelter": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.GRUNGE, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR],
    },
    # Work/Professional Spaces
    "corporate boardroom": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.PREPPY],
        "location": [LocationType.INDOOR],
    },
    "open-plan tech office": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "hospital waiting room": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR],
    },
    "doctor's examination room": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR],
    },
    "dentist's chair": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR],
    },
    "school science lab": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "university lecture hall": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR],
    },
    "library study table": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR],
    },
    "police station bullpen": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MILITARY, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "courtroom witness stand": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.PREPPY],
        "location": [LocationType.INDOOR],
    },
    "military barracks": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "airport check-in counter": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR],
    },
    "restaurant kitchen line": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR],
    },
    "café counter with pastries": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "hotel room bedspread": {
        "types": [OutfitType.LINGERIE, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR],
    },
    "hair salon chair with mirror": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR],
    },
    "nail salon booth": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "construction site scaffolding": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR],
    },
    "factory assembly line": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "recording studio booth": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR],
    },
    # Travel & Transportation
    "train station concourse": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.RETRO],
        "location": [LocationType.INDOOR],
    },
    "subway train interior": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR],
    },
    "bus interior at night": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.GRUNGE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "taxi cab backseat": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR],
    },
    "ride-share car": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR],
    },
    "airplane economy cabin": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "airplane first-class seat": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "airport baggage claim": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR],
    },
    "ferry deck": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR],
    },
    "cruise ship dining hall": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.INDOOR],
    },
    "motorcycle on highway overlook": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR],
    },
    "bicycle path through park": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR],
    },
    "skateboard ramp": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR],
    },
    "highway rest stop": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR],
    },
    "scenic overlook parking lot": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR],
    },
    "cable car on mountain": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "hot air balloon basket": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR],
    },
    "horse-drawn carriage": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "roller coaster cart": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR],
    },
    "carnival bumper cars": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR],
    },
    # Leisure & Entertainment
    "movie theater lobby": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY, OutfitType.RETRO],
        "location": [LocationType.INDOOR],
    },
    "popcorn stand": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.RETRO],
        "location": [LocationType.INDOOR],
    },
    "bowling alley lane": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR],
    },
    "arcade machine corner": {
        "types": [OutfitType.RETRO, OutfitType.KAWAII, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR],
    },
    "casino roulette table": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR],
    },
    "nightclub dance floor": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR],
    },
    "karaoke stage": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.KAWAII, OutfitType.RETRO],
        "location": [LocationType.INDOOR],
    },
    "live music concert pit": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "theater backstage dressing room": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR],
    },
    "opera house balcony seats": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR],
    },
    "indoor swimming pool": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "outdoor public pool": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PIN_UP],
        "location": [LocationType.OUTDOOR],
    },
    "waterpark lazy river": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.KAWAII, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR],
    },
    "spa sauna room": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.LINGERIE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "yoga studio": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR],
    },
    "gym weight room": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR],
    },
    "boxing ring": {
        "types": [OutfitType.ATHLEISURE, OutfitType.GRUNGE, OutfitType.MILITARY],
        "location": [LocationType.INDOOR],
    },
    "ice skating rink": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.KAWAII],
        "location": [LocationType.INDOOR],
    },
    "indoor climbing wall": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR],
    },
    "mini golf course": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR],
    },
    # Nature & Outdoors
    "rocky beach tide pools": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "grassy park hill": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR],
    },
    "flower garden path": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR],
    },
    "autumn leaf pile": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR],
    },
    "pine forest trail": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ATHLEISURE, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR],
    },
    "rainy woodland bridge": {
        "types": [OutfitType.COTTAGECORE, OutfitType.GOTHIC, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR],
    },
    "snowy open field": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "desert canyon floor": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COWBOY, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "volcano rim overlook": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.AVANT_GARDE],
        "location": [LocationType.OUTDOOR],
    },
    "waterfall base pool": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "bamboo forest path": {
        "types": [OutfitType.MINIMALIST, OutfitType.ETHEREAL, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR],
    },
    "vineyard hillside": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR],
    },
    "orchard with ripe fruit": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR],
    },
    "farm cornfield rows": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR],
    },
    "barn hayloft": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR],
    },
    "rural dirt road": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR],
    },
    "windmill field": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "prairie wildflowers": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR],
    },
    "clifftop overlooking ocean": {
        "types": [OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR],
    },
    "frozen lake surface": {
        "types": [OutfitType.ETHEREAL, OutfitType.GOTHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR],
    },
    # Unique / Quirky Settings
    "abandoned amusement park": {
        "types": [OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.PUNK],
        "location": [LocationType.OUTDOOR],
    },
    "wax museum hallway": {
        "types": [OutfitType.GOTHIC, OutfitType.AVANT_GARDE, OutfitType.RETRO],
        "location": [LocationType.INDOOR],
    },
    "aquarium glass tunnel": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR],
    },
    "zoo enclosure walkway": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "planetarium dome": {
        "types": [OutfitType.ETHEREAL, OutfitType.CYBERPUNK, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "observatory telescope platform": {
        "types": [OutfitType.ETHEREAL, OutfitType.STEAMPUNK, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "science fair exhibition hall": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.KAWAII],
        "location": [LocationType.INDOOR],
    },
    "escape room chamber": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR],
    },
    "haunted house attraction": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR],
    },
    "fortune teller's tent": {
        "types": [OutfitType.BOHEMIAN, OutfitType.GOTHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "tarot reading table": {
        "types": [OutfitType.BOHEMIAN, OutfitType.GOTHIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "carnival ring toss booth": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR],
    },
    "puppet theater stage": {
        "types": [OutfitType.KAWAII, OutfitType.AVANT_GARDE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR],
    },
    "retro photo booth": {
        "types": [OutfitType.RETRO, OutfitType.PIN_UP, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "indoor trampoline park": {
        "types": [OutfitType.ATHLEISURE, OutfitType.KAWAII, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR],
    },
    "laser tag arena": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CYBERPUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR],
    },
    "indoor jungle gym": {
        "types": [OutfitType.ATHLEISURE, OutfitType.KAWAII, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR],
    },
    "toy store aisle": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.INDOOR],
    },
    "ice cream parlor": {
        "types": [OutfitType.KAWAII, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR],
    },
    "candy shop interior": {
        "types": [OutfitType.KAWAII, OutfitType.LOLITA, OutfitType.RETRO],
        "location": [LocationType.INDOOR],
    },
    # Historic / Cultural Settings
    "medieval castle dining hall": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR],
    },
    "stone dungeon cell": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.MILITARY],
        "location": [LocationType.INDOOR],
    },
    "ancient roman ruins": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.AVANT_GARDE],
        "location": [LocationType.OUTDOOR],
    },
    "egyptian desert pyramid base": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.AVANT_GARDE],
        "location": [LocationType.OUTDOOR],
    },
    "greek amphitheater steps": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR],
    },
    "old european village street": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR],
    },
    "renaissance courtyard": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "victorian parlor room": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.LOLITA],
        "location": [LocationType.INDOOR],
    },
    "1920s speakeasy bar": {
        "types": [OutfitType.RETRO, OutfitType.EVENING_FORMAL, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR],
    },
    "1950s drive-in diner": {
        "types": [OutfitType.RETRO, OutfitType.ROCKABILLY, OutfitType.PIN_UP],
        "location": [LocationType.OUTDOOR],
    },
    "1970s roller disco": {
        "types": [OutfitType.RETRO, OutfitType.CLUB_PARTY, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR],
    },
    "1980s neon arcade": {
        "types": [OutfitType.RETRO, OutfitType.CYBERPUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR],
    },
    "1990s internet café": {
        "types": [OutfitType.RETRO, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR],
    },
    "old west main street": {
        "types": [OutfitType.COWBOY, OutfitType.RETRO, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR],
    },
    "saloon poker table": {
        "types": [OutfitType.COWBOY, OutfitType.RETRO, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR],
    },
    "train robbery scene": {
        "types": [OutfitType.COWBOY, OutfitType.MILITARY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR],
    },
    "pirate ship deck": {
        "types": [OutfitType.ROMANTIC, OutfitType.GRUNGE, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR],
    },
    "shipwrecked island shore": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.GRUNGE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR],
    },
    "samurai dojo": {
        "types": [OutfitType.MILITARY, OutfitType.MINIMALIST, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR],
    },
    "shinto shrine gates": {
        "types": [OutfitType.ETHEREAL, OutfitType.MINIMALIST, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR],
    },
    # Futuristic / Fantasy
    "cyberpunk neon rooftop": {
        "types": [OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR],
    },
    "floating holographic mall": {
        "types": [OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "space station observation deck": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MINIMALIST, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "starship control bridge": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MILITARY, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "teleportation chamber": {
        "types": [OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR],
    },
    "futuristic vr arcade": {
        "types": [OutfitType.CYBERPUNK, OutfitType.KAWAII, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR],
    },
    "android repair shop": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STEAMPUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR],
    },
    "robot factory": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MILITARY, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "hoverboard park": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR],
    },
    "neon-drenched undercity": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.OUTDOOR],
    },
    "elven forest village": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR],
    },
    "dwarven forge": {
        "types": [OutfitType.STEAMPUNK, OutfitType.MILITARY, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR],
    },
    "fairy glen": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR],
    },
    "crystal cave interior": {
        "types": [OutfitType.ETHEREAL, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR],
    },
    "dragon's lair cave": {
        "types": [OutfitType.GOTHIC, OutfitType.MILITARY, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR],
    },
    "magical academy classroom": {
        "types": [OutfitType.PREPPY, OutfitType.GOTHIC, OutfitType.KAWAII],
        "location": [LocationType.INDOOR],
    },
    "wizard's tower library": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR],
    },
    "haunted enchanted swamp": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "gothic vampire castle": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR],
    },
    "werewolf forest den": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR],
    },
    # Everyday Social Settings
    "family dinner table": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR],
    },
    "coffee shop study nook": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.PREPPY],
        "location": [LocationType.INDOOR],
    },
    "book club circle": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR],
    },
    "board game night living room": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "house party basement": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR],
    },
    "frat house keg party": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.PREPPY, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR],
    },
    "dorm room bunk bed": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "college cafeteria": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR],
    },
    "bbq picnic table": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR],
    },
    "tailgate parking lot": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR],
    },
    "sports stadium bleachers": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR],
    },
    "farmer's market stand": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR],
    },
    "food truck festival": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR],
    },
    "open-air flea market": {
        "types": [OutfitType.BOHEMIAN, OutfitType.GRUNGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR],
    },
    "thrift shop racks": {
        "types": [OutfitType.GRUNGE, OutfitType.RETRO, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR],
    },
    "record shop browsing": {
        "types": [OutfitType.GRUNGE, OutfitType.RETRO, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR],
    },
    "tattoo parlor": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR],
    },
    "pier carnival stand": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR],
    },
    "antique store": {
        "types": [OutfitType.COTTAGECORE, OutfitType.RETRO, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR],
    },
    "photography studio": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR],
    },
    # Weather & Atmosphere
    "thunderstorm street corner": {
        "types": [OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR],
    },
    "snowstorm sidewalk": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR],
    },
    "heavy fog pier": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR],
    },
    "heatwave desert roadside": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR],
    },
    "rainy day café window": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR],
    },
    "breezy rooftop": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR],
    },
    "windy field with kites": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR],
    },
    "golden hour meadow": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "midnight graveyard": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "sunrise beach walk": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ETHEREAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    # Domestic Oddities
    "bathroom bubble bath": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR],
    },
    "kitchen baking session": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.KAWAII],
        "location": [LocationType.INDOOR],
    },
    "messy teenager's bedroom": {
        "types": [OutfitType.GRUNGE, OutfitType.KAWAII, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "hall closet full of coats": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.PREPPY],
        "location": [LocationType.INDOOR],
    },
    "laundry basket pile": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.LINGERIE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "garage band rehearsal": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR],
    },
    "home gym treadmill": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "backyard hammock": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR],
    },
    "porch swing at night": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR],
    },
    "attic skylight window": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ETHEREAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR],
    },
    # Travel/Exotic
    "moroccan tea house": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR],
    },
    "tokyo street crossing": {
        "types": [OutfitType.KAWAII, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "location": [LocationType.OUTDOOR],
    },
    "london red phone booth": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR],
    },
    "italian piazza": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR],
    },
    "french vineyard cellar": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR],
    },
    "santorini cliffside": {
        "types": [OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "dubai desert camp": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR],
    },
    "indian spice market": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR],
    },
    "himalayan monastery": {
        "types": [OutfitType.ETHEREAL, OutfitType.MINIMALIST, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR],
    },
    "amazon rainforest canopy": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR],
    },
    # Extra Dramatic Scenes
    "police interrogation room": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.GRUNGE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR],
    },
    "crime scene with tape": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MILITARY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR],
    },
    "hospital emergency ward": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR],
    },
    "war-torn battlefield ruins": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR],
    },
    "protest rally in streets": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.OUTDOOR],
    },
    "burning building rooftop": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR],
    },
    "flooded street corner": {
        "types": [OutfitType.GRUNGE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR],
    },
    "train derailment site": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR],
    },
    "deserted highway": {
        "types": [OutfitType.GRUNGE, OutfitType.COWBOY, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR],
    },
    "collapsing bridge": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR],
    },
    # Surreal / Abstract
    "infinite white void": {
        "types": [OutfitType.MINIMALIST, OutfitType.ETHEREAL, OutfitType.AVANT_GARDE],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "checkerboard floor dimension": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "floating staircases": {
        "types": [OutfitType.ETHEREAL, OutfitType.AVANT_GARDE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "upside-down living room": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.KAWAII, OutfitType.CYBERPUNK],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "endless library stacks": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "glitching cyber-space": {
        "types": [OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "dreamy cloudscape": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "giant oversized furniture room": {
        "types": [OutfitType.KAWAII, OutfitType.AVANT_GARDE, OutfitType.LOLITA],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "mirror maze": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    "shattered glass world": {
        "types": [OutfitType.GOTHIC, OutfitType.AVANT_GARDE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.INDOOR],
    },
    # Famous Beach Locations
    "Waikiki Beach, Hawaii": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "Bondi Beach, Australia": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "Copacabana Beach, Brazil": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "Venice Beach, California": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "South Beach, Miami": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.RETRO, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "Brighton Beach, UK": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "Bora Bora Lagoon": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR],
    },
    "Maya Bay, Thailand": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "Anse Source d'Argent, Seychelles": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR],
    },
    "Navagio (Shipwreck) Beach, Greece": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    # Beach Time of Day/Weather Scenes
    "sunrise beach with fishermen's boats": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR],
    },
    "sunset bonfire beach party": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "midnight full moon reflecting on the ocean": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "stormy beach with crashing waves": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.GRUNGE, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "foggy morning beach walk": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.MINIMALIST, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "tide pools at low tide with starfish": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "bioluminescent glowing waves at night": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ETHEREAL, OutfitType.CYBERPUNK],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "windy beach with flying kites": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "deserted winter beach with icy waves": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.MINIMALIST, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "overcast gray-sky beach with gulls": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.GRUNGE, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    # Beach Activities
    "beach volleyball game in progress": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "surf competition with flags and judges": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "beach yoga sunrise session": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "children building sandcastles": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "lifeguard tower with binoculars": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "beachside food trucks and vendors": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "fishing pier with people casting lines": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "jet skis racing offshore": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "kite surfing launch zone": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    # Unique Beach Types
    "black sand volcanic beach": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.GOTHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "pink sand beach (Bahamas)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "white chalk cliff beach": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.MINIMALIST, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "mangrove beach with tangled roots": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "rocky tide pool coast with crabs": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.GRUNGE, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "desert beach with sand dunes rolling into water": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "glacier-fed beach with icebergs": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.MINIMALIST, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "hidden cove accessible only by boat": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "cliffside beach with stairway down": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "tropical jungle beach with palm canopy": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    # Beach Events and Culture
    "beach festival stage setup": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "beachside wedding arch and chairs": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "Hawaiian luau with tiki torches": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "Mediterranean café tables on the sand": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "beach carnival with Ferris wheel nearby": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "Caribbean steel drum music performance": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "fisherman's village drying nets on shore": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "surf shack rental hut": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "family picnic under umbrellas": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "sunset couples' stroll with lanterns": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.BEACH],
    },
    "minimalist bedroom with white sheets and no clutter": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "messy teenager's bedroom with posters and clothes on floor": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.NORMCORE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "cozy bedroom with fairy lights and books stacked on the nightstand": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "master bedroom with king bed and big windows": {
        "types": [ OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "small studio apartment bedroom nook with a futon": {
        "types": [OutfitType.MINIMALIST, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "attic bedroom with slanted ceilings and skylight": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "shared dorm room with bunk beds": {
        "types": [OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "guest bedroom with folded towels on the bed": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.PREPPY, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with a large vanity and makeup scattered around": {
        "types": [  OutfitType.ROMANTIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with sliding glass doors leading to a balcony": {
        "types": [ OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bohemian-style bedroom with tapestries and plants": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "gothic bedroom with black canopy bed and candles": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "futuristic bedroom with neon accent lighting": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "romantic bedroom with rose petals on the bed": {
        "types": [OutfitType.ROMANTIC,   OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "shabby chic bedroom with distressed furniture": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "industrial loft bedroom with exposed brick walls": {
        "types": [OutfitType.STREETWEAR, OutfitType.MINIMALIST, OutfitType.GRUNGE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "coastal beach-themed bedroom with seashell decor": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "cottagecore bedroom with quilts and floral curtains": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.ROMANTIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "kawaii pastel bedroom with plush toys and frills": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "rocker's bedroom with guitars and amps against the wall": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "hotel suite bedroom with crisp sheets and city view": {
        "types": [ OutfitType.BUSINESS_WEAR,  OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with canopy bed draped in silk curtains": {
        "types": [ OutfitType.ROMANTIC,  OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with fireplace at the foot of the bed": {
        "types": [ OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "royal palace bedroom with ornate gold headboard": {
        "types": [  OutfitType.VINTAGE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "penthouse bedroom with floor-to-ceiling windows": {
        "types": [ OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with fur rugs and velvet furniture": {
        "types": [  OutfitType.GOTHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with chandelier above the bed": {
        "types": [  OutfitType.VINTAGE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "high-rise bedroom overlooking skyline at night": {
        "types": [ OutfitType.MINIMALIST, OutfitType.CYBERPUNK, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with aquarium wall beside the bed": {
        "types": [ OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "tropical villa bedroom with open-air walls": {
        "types": [ OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with open suitcase and clothes spilling out": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom mid-pillow fight": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with laptop glowing on the bed at night": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with sketchbooks and art supplies everywhere": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with laundry piles sorted on the floor": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with candles lit for a cozy reading session": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with gaming setup glowing in RGB lights": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with TV and movie night snacks on bed": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with crib and baby toys scattered": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "bedroom with workout gear and yoga mat rolled out": {
        "types": [OutfitType.ATHLEISURE, OutfitType.NORMCORE, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "traditional Japanese tatami room with futon bedding": {
        "types": [OutfitType.MINIMALIST,  OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "Middle Eastern bedroom with low cushions and lanterns": {
        "types": [OutfitType.BOHEMIAN,   OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "Victorian bedroom with lace drapes and antique furniture": {
        "types": [OutfitType.VINTAGE, OutfitType.GOTHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "1970s retro bedroom with shag carpet and lava lamp": {
        "types": [OutfitType.RETRO, OutfitType.BOHEMIAN, OutfitType.VINTAGE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "1980s neon bedroom with cassette player and arcade posters": {
        "types": [OutfitType.RETRO, OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "futon on the floor in a minimalist modern Asian room": {
        "types": [OutfitType.MINIMALIST,  OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "tribal-inspired bedroom with woven textiles and masks": {
        "types": [OutfitType.BOHEMIAN,  OutfitType.ETHEREAL, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "medieval stone chamber with simple straw bedding": {
        "types": [OutfitType.GOTHIC,  OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "Arctic cabin bedroom with furs and wooden bed": {
        "types": [OutfitType.MILITARY, OutfitType.COTTAGECORE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
    "Moroccan riad bedroom with mosaic tiles and ornate lanterns": {
        "types": [OutfitType.BOHEMIAN,   OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BEDROOM],
    },
}
