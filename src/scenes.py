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
        "location": [LocationType.OUTDOOR,  LocationType.CITY],
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
        "location": [LocationType.OUTDOOR,  LocationType.CITY],
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
        "location": [LocationType.OUTDOOR,  LocationType.CITY],
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
        "location": [LocationType.OUTDOOR,  LocationType.CITY],
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
        "location": [LocationType.OUTDOOR,  LocationType.CITY],
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
        "location": [LocationType.OUTDOOR,  LocationType.CITY],
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
    
    # New York City
    "Times Square at night with billboards glowing": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Central Park in autumn with falling leaves": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Empire State Building observation deck": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Brooklyn Bridge pedestrian walkway": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Statue of Liberty ferry view": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Fifth Avenue luxury shopping district": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Wall Street financial district": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Grand Central Terminal main concourse": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Yankee Stadium during a game": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Coney Island boardwalk and Ferris wheel": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Los Angeles
    "Hollywood Walk of Fame stars": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Griffith Observatory overlooking city lights": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Venice Beach boardwalk with skaters": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Santa Monica Pier roller coaster": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Rodeo Drive high-end shopping strip": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Sunset Boulevard neon signs": {
        "types": [OutfitType.STREETWEAR, OutfitType.RETRO, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "LACMA Urban Light installation": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Dodgers Stadium during a game": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Malibu beach mansions": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Downtown LA Arts District with murals": {
        "types": [OutfitType.STREETWEAR, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Chicago
    "Millennium Park with Cloud Gate (\"The Bean\")": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Navy Pier Ferris wheel": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Willis (Sears) Tower Skydeck glass floor": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Chicago Riverwalk with skyscraper reflections": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Wrigley Field during a Cubs game": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Magnificent Mile shopping district": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Chicago Theatre marquee lit at night": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Lake Michigan shoreline at sunrise": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Elevated \"L\" train tracks": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Deep-dish pizzeria interior": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    
    # San Francisco
    "Golden Gate Bridge in fog": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Alcatraz Island prison yard": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Lombard Street winding road": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Fisherman's Wharf with sea lions": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Painted Ladies Victorian houses": {
        "types": [OutfitType.VINTAGE, OutfitType.PREPPY, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Chinatown lantern-lined street": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Mission District mural alleyways": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.AVANT_GARDE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Union Square shopping plaza": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Castro District rainbow crosswalk": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Haight-Ashbury vintage shops": {
        "types": [OutfitType.VINTAGE, OutfitType.BOHEMIAN, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Las Vegas
    "Las Vegas Strip with neon lights": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Bellagio fountains at night": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Luxor pyramid with spotlight": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Fremont Street canopy light show": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.STREETWEAR, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Caesar's Palace casino floor": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    "Venetian canals with gondolas": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    "Neon Boneyard sign graveyard": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.AVANT_GARDE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Desert outskirts with city skyline view": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Miami
    "South Beach pastel lifeguard stands": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Ocean Drive Art Deco hotels": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Wynwood Walls graffiti art": {
        "types": [OutfitType.STREETWEAR, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Little Havana street music scene": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Biscayne Bay waterfront view": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # London
    "Big Ben and Houses of Parliament": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Tower Bridge spanning the Thames": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Buckingham Palace gates": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Piccadilly Circus billboards": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Camden Market stalls": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Covent Garden performers": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "London Eye ferris wheel": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Notting Hill pastel houses": {
        "types": [OutfitType.PREPPY, OutfitType.ROMANTIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Soho nightlife street": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "West End theatre district": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Paris
    "Eiffel Tower at twilight": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Louvre glass pyramid courtyard": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Montmartre street artists": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.AVANT_GARDE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Arc de Triomphe roundabout": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Seine River boat cruise": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Notre-Dame cathedral square": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Champs-Élysées shopping avenue": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Latin Quarter café terraces": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Versailles Hall of Mirrors": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    "Moulin Rouge cabaret exterior": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PIN_UP, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Tokyo
    "Shibuya Crossing with neon screens": {
        "types": [OutfitType.STREETWEAR, OutfitType.CYBERPUNK, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Shinjuku skyscraper skyline": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CYBERPUNK],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Harajuku Takeshita Street fashion hub": {
        "types": [OutfitType.KAWAII, OutfitType.AVANT_GARDE, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Akihabara anime shops": {
        "types": [OutfitType.KAWAII, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Tsukiji fish market": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Tokyo Tower at night": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.CYBERPUNK],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Meiji Shrine forest path": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Asakusa Senso-ji temple gate": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Odaiba waterfront with Rainbow Bridge": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.CYBERPUNK, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Capsule hotel interior": {
        "types": [OutfitType.MINIMALIST, OutfitType.CYBERPUNK, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    
    # Hong Kong
    "Victoria Peak cityscape view": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Tsim Sha Tsui promenade at night": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Star Ferry crossing the harbor": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Mong Kok night market": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.CYBERPUNK],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Temple Street fortune teller stalls": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Tian Tan Buddha on Lantau Island": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Shanghai
    "The Bund colonial waterfront": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Oriental Pearl Tower glowing at night": {
        "types": [OutfitType.CYBERPUNK, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Yu Garden traditional pavilions": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Nanjing Road shopping street": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Maglev train station": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    "French Concession leafy lanes": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Dubai
    "Burj Khalifa observation deck": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Palm Jumeirah island beach": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Dubai Mall fountain show": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Gold Souk traditional market": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Desert dunes outside city": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Rome
    "Colosseum arena floor": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Trevi Fountain at night": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "St. Peter's Basilica interior": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    "Spanish Steps with crowds": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Piazza Navona fountains": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Roman Forum ruins": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Moscow
    "Red Square with St. Basil's Cathedral": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Kremlin walls at sunset": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "GUM shopping arcade": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    "Moscow Metro ornate station": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    "Bolshoi Theatre interior": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    
    # Sydney, Australia
    "Sydney Opera House": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Harbour Bridge climb": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Rio de Janeiro, Brazil
    "Christ the Redeemer statue": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Copacabana Beach promenade": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Madrid, Spain
    "Plaza Mayor": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Barcelona, Spain
    "Sagrada Família basilica": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "La Rambla street performers": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Berlin, Germany
    "Berlin Brandenburg Gate": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "East Side Gallery Berlin Wall murals": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.AVANT_GARDE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Alexanderplatz TV Tower": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.CYBERPUNK],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Prague, Czech Republic
    "Prague Charles Bridge sunrise": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Old Town Square with Astronomical Clock": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Vienna, Austria
    "Vienna Schönbrunn Palace gardens": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Budapest, Hungary
    "Budapest Parliament Building on the Danube": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Istanbul, Turkey
    "Istanbul Hagia Sophia interior": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    "Blue Mosque courtyard": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Grand Bazaar bustling aisles": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    
    # Marrakech, Morocco
    "Marrakech Jemaa el-Fnaa night market": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Cape Town, South Africa
    "Cape Town Table Mountain view": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Seoul, South Korea
    "Gyeongbokgung Palace courtyard": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Myeongdong street food stalls": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Gangnam nightlife district": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.CYBERPUNK],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "N Seoul Tower with love locks": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Dongdaemun Design Plaza futuristic architecture": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Bukchon Hanok Village traditional houses": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Beijing, China
    "Forbidden City palace gates": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Tiananmen Square at sunrise": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Temple of Heaven circular altar": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ETHEREAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Summer Palace lakeside pavilions": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Great Wall Mutianyu section": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Bangkok, Thailand
    "Grand Palace golden spires": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Wat Arun temple by the river": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ETHEREAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Floating market boats with fruit": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Khao San Road backpacker nightlife": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Chatuchak weekend market stalls": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Singapore
    "Marina Bay Sands rooftop infinity pool": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Gardens by the Bay Supertree Grove at night": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.CYBERPUNK, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Clarke Quay riverside nightlife": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Chinatown food hawker center": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Sentosa Island beach": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Delhi, India
    "India Gate monument": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Red Fort courtyard": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Chandni Chowk spice bazaar": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Lotus Temple lotus-shaped design": {
        "types": [OutfitType.MINIMALIST, OutfitType.ETHEREAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Jama Masjid mosque steps": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Mumbai, India
    "Gateway of India arch": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Marine Drive seafront at night": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Chhatrapati Shivaji train station": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Dharavi neighborhood alleys": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Bollywood film studio set": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    
    # Cairo, Egypt
    "Giza Pyramids with camels nearby": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Sphinx at sunset": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Khan el-Khalili bazaar": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Nile River dinner cruise": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Egyptian Museum artifacts": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    
    # Athens, Greece
    "Acropolis Parthenon hilltop view": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Plaka old town cobblestone streets": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Monastiraki flea market": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Olympic Stadium ruins": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Mount Lycabettus viewpoint": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Additional Istanbul scenes
    "Bosphorus ferry ride": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Topkapi Palace courtyard": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Spice Bazaar stalls": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    "Galata Tower rooftop view": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Istiklal Avenue shopping street": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Mexico City, Mexico
    "Zócalo central square": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Frida Kahlo's Blue House": {
        "types": [OutfitType.BOHEMIAN, OutfitType.AVANT_GARDE, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Xochimilco colorful canal boats": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Chapultepec Castle on the hill": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Teotihuacan Pyramids (outside city)": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Additional Rio de Janeiro, Brazil scenes
    "Ipanema Beach promenade": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Maracanã Stadium during a match": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Selarón Steps mosaic staircase": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.AVANT_GARDE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Sugarloaf Mountain cable car": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Sambadrome Carnival parade": {
        "types": [OutfitType.FESTIVAL, OutfitType.AVANT_GARDE, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Buenos Aires, Argentina
    "La Boca colorful houses and tango dancers": {
        "types": [OutfitType.ROMANTIC, OutfitType.VINTAGE, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Plaza de Mayo with Casa Rosada": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Recoleta Cemetery mausoleums": {
        "types": [OutfitType.GOTHIC, OutfitType.VINTAGE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Palermo café-lined streets": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Teatro Colón opera house": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    
    # Additional Cape Town, South Africa scenes
    "V&A Waterfront with Table Mountain backdrop": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Robben Island ferry dock": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Bo-Kaap pastel houses": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Clifton Beach shoreline": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Lion's Head hiking summit": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Additional Sydney, Australia scenes
    "Circular Quay ferry terminal": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Bondi Icebergs pool by the ocean": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Darling Harbour skyline": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Taronga Zoo with city views": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Royal Botanic Gardens": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Melbourne, Australia
    "Federation Square modern architecture": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Hosier Lane graffiti alley": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.AVANT_GARDE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Melbourne Cricket Ground (MCG)": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Queen Victoria Market food stalls": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "St. Kilda Pier with penguins": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Toronto, Canada
    "CN Tower glass floor": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Distillery District cobblestone streets": {
        "types": [OutfitType.VINTAGE, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Kensington Market bohemian shops": {
        "types": [OutfitType.BOHEMIAN, OutfitType.GRUNGE, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Nathan Phillips Square ice rink": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Toronto Islands ferry dock": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Vancouver, Canada
    "Stanley Park seawall": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Capilano Suspension Bridge": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Granville Island market": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Gastown steam clock": {
        "types": [OutfitType.VINTAGE, OutfitType.CASUAL_CHIC, OutfitType.STEAMPUNK],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Grouse Mountain ski slopes": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Montreal, Canada
    "Old Montreal cobblestones": {
        "types": [OutfitType.VINTAGE, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Notre-Dame Basilica interior": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    "Mount Royal overlook": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Jean-Talon Market stalls": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Underground City shopping tunnels": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    
    # San Juan, Puerto Rico
    "El Morro fortress walls": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MILITARY, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Old San Juan colorful streets": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Condado Beach shoreline": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Calle del Cristo shopping street": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Salsa dance club": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    
    # Havana, Cuba
    "Malecón seaside promenade": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Old Havana pastel streets": {
        "types": [OutfitType.VINTAGE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Classic cars lined up in square": {
        "types": [OutfitType.VINTAGE, OutfitType.RETRO, OutfitType.ROCKABILLY],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Revolution Square with Che mural": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MILITARY, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Tropicana cabaret": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PIN_UP, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    
    # Reykjavik, Iceland
    "Reykjavik Hallgrímskirkja church": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Blue Lagoon geothermal spa": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.MINIMALIST, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Edinburgh, Scotland
    "Edinburgh Castle hilltop": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.VINTAGE, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Royal Mile cobblestones": {
        "types": [OutfitType.VINTAGE, OutfitType.CASUAL_CHIC, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Dublin, Ireland
    "Dublin Temple Bar nightlife": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC, OutfitType.PUNK],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Guinness Storehouse brewery": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    
    # Brussels, Belgium
    "Brussels Grand Place square": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.VINTAGE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Atomium futuristic monument": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Amsterdam, Netherlands
    "Amsterdam canals with bicycles": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Red Light District neon streets": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.PUNK, OutfitType.AVANT_GARDE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Anne Frank House exterior": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Copenhagen, Denmark
    "Copenhagen Nyhavn harbor": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    "Tivoli Gardens amusement park": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Stockholm, Sweden
    "Stockholm Gamla Stan old town": {
        "types": [OutfitType.VINTAGE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Helsinki, Finland
    "Helsinki Senate Square": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Oslo, Norway
    "Oslo Opera House rooftop": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Saint Petersburg, Russia
    "Saint Petersburg Hermitage Museum": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CITY],
    },
    "Winter Palace square": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.VINTAGE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Tallinn, Estonia
    "Tallinn medieval old town": {
        "types": [OutfitType.VINTAGE, OutfitType.GOTHIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.CITY],
    },
    
    # Bathroom Scenes
    "bathroom with subway tiles and modern shower that is bright and clean": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "small bathroom with pedestal sink and hexagon floor tiles": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "minimalist bathroom with floating vanity and frameless glass shower": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "farmhouse bathroom with shiplap walls and a clawfoot tub": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "industrial bathroom with exposed brick and matte black fixtures": {
        "types": [OutfitType.GRUNGE, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "luxury bathroom with marble floors and freestanding soaking tub": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "hotel-style bathroom with double vanity and walk-in shower": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "cozy bathroom with warm wood accents and stone tiles": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "powder room with wallpaper and pedestal sink": {
        "types": [OutfitType.VINTAGE, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "white bathroom with skylight and walk-in rain shower": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "compact apartment bathroom with corner shower and wall-mounted sink": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "spa-inspired bathroom with bamboo details and soaking tub": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "contemporary bathroom with large mirrors and recessed lighting": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "retro bathroom with pastel tiles and chrome fixtures": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "transitional bathroom with shaker cabinets and quartz counters": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "rustic bathroom with log walls and stone flooring": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "guest bathroom with shower-tub combo and neutral palette": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "chic bathroom with herringbone tile floor and gold accents": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "black-and-white bathroom with checkerboard floor tiles": {
        "types": [OutfitType.RETRO, OutfitType.MINIMALIST, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "nautical bathroom with beadboard walls and rope accents": {
        "types": [OutfitType.PREPPY, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "ensuite bathroom with frosted glass partition and modern vanity": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "open-concept bathroom with wet room shower design": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "elegant bathroom with chandelier above the bathtub": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "functional family bathroom with double sinks and built-in storage": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "scandinavian bathroom with light wood and matte white finishes": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "budget-friendly bathroom with vinyl floors and fiberglass shower": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "modern bathroom with concrete floors and sleek lines": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "beach house bathroom with light blue walls and seashell decor": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "classic bathroom with hex tile floor and wainscoting": {
        "types": [OutfitType.VINTAGE, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "high-rise condo bathroom with floor-to-ceiling glass shower": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "tiny bathroom with pocket door and corner vanity": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "zen bathroom with pebble flooring and wooden soaking tub": {
        "types": [OutfitType.MINIMALIST, OutfitType.ATHLEISURE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "accessible bathroom with grab bars and roll-in shower": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "business restroom with stainless steel stalls and tile floors": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "half-bath with floating sink and accent mirror": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with stone countertop and under-mount sink": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with patterned encaustic floor tiles": {
        "types": [OutfitType.BOHEMIAN, OutfitType.VINTAGE, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with frosted glass shower doors and white tile walls": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "guest powder room with vessel sink and wall sconces": {
        "types": [OutfitType.ROMANTIC, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with skylight over freestanding tub": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with heated floors and towel warmer": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with natural stone tiles and rainfall shower": {
        "types": [OutfitType.COTTAGECORE, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with soft gray palette and shaker-style cabinets": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with wood-look porcelain floor tiles": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with wide vanity and large frameless mirror": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with pocket shower and sliding glass door": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with rustic barn door entrance": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with matte black faucets and fixtures": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with cream marble counters and gold-trimmed mirror": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with recessed shelving and built-in niches": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with slate flooring and vessel sink": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with brick accent wall and vintage lighting": {
        "types": [OutfitType.VINTAGE, OutfitType.GRUNGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with white shiplap and farmhouse sink": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with wall-mounted toilet and clean lines": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with linen closet and built-in shelves": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with freestanding oval tub and chandelier": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with double showerheads and bench seating": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with large format tiles and minimal grout lines": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with frosted window and natural light": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with travertine tile floors and counters": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with bamboo flooring and organic accents": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ATHLEISURE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with oversized mirror and vanity lighting": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with compact layout and efficient storage": {
        "types": [OutfitType.MINIMALIST, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with polished chrome fixtures and bright finishes": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with patterned wallpaper and traditional sink": {
        "types": [OutfitType.VINTAGE, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with natural wood vanity and quartz top": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with frameless corner shower enclosure": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with chevron tile backsplash": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with granite counters and stainless faucets": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with textured stone walls and recessed lights": {
        "types": [OutfitType.COTTAGECORE, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with walk-through shower and glass partition": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with terrazzo flooring and sleek cabinets": {
        "types": [OutfitType.RETRO, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with beadboard wainscoting and round mirror": {
        "types": [OutfitType.COTTAGECORE, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with light oak cabinetry and soft white tones": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with floor-to-ceiling marble walls": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with space-saving wall-hung vanity": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with separate shower and bathtub": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with bold accent wall and minimal decor": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with skylight tube and neutral palette": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with shower curtain and simple tub": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with open shelving and woven baskets": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with floating toilet and hidden tank": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with round soaking tub and wood beams": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with stone sink basin and rustic vanity": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with vertical subway tiles and matte fixtures": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with LED backlit mirror and glossy finishes": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with natural stone mosaic shower floor": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with mid-century vanity and round mirror": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with high ceilings and tall window": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with towel ladder and spa-like vibe": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with antique vanity and vintage mirror": {
        "types": [OutfitType.VINTAGE, OutfitType.ROMANTIC, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with large soaking tub set into a tile surround": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with glass block shower wall": {
        "types": [OutfitType.RETRO, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with compact stacked washer and dryer": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with dark cabinets and white countertops": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with geometric floor tiles and modern sink": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with neutral stone backsplash and chrome fixtures": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with wall-to-wall mirror and minimal vanity": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with contrasting dark floor and bright walls": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    "bathroom with walk-in shower, bench, and handheld sprayer": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.BATHROOM],
    },
    
    # Living Room Scenes
    "living room with sectional sofa and wall-mounted TV": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with hardwood floors and stone fireplace": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "modern living room with floor-to-ceiling windows and clean lines": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "cozy living room with overstuffed sofa and area rug": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "farmhouse living room with shiplap walls and rustic beams": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "industrial loft-style living room with exposed brick and ductwork": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "luxury living room with marble floors and chandelier": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "minimalist living room with low-profile furniture and white walls": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "contemporary living room with neutral palette and large artwork": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "retro living room with mid-century sofa and geometric rug": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "open-concept living room with kitchen island view": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "family living room with large sectional and toy storage": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "scandinavian living room with light wood and neutral tones": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "apartment living room with compact sofa and small coffee table": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "traditional living room with crown molding and classic sofa set": {
        "types": [OutfitType.PREPPY, OutfitType.BUSINESS_WEAR, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with built-in bookshelves and reading nook": {
        "types": [OutfitType.PREPPY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with bay window and cushioned seating": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with dark leather sofas and wood coffee table": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.GRUNGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "bright living room with skylights and indoor plants": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with vaulted ceilings and exposed beams": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with double French doors and outdoor access": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with stone accent wall and modern fireplace": {
        "types": [OutfitType.MINIMALIST, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with oversized sectional and floor lamp": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with patterned wallpaper and bold accent chairs": {
        "types": [OutfitType.BOHEMIAN, OutfitType.VINTAGE, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with sliding glass doors to patio": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "coastal living room with wicker furniture and light blue accents": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with built-in media center and recessed lighting": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "small living room with loveseat and wall-mounted shelves": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with oversized area rug and layered textures": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with gallery wall of family photos": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with neutral sectional and colorful throw pillows": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with wood-burning stove and rustic decor": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with herringbone wood floors and clean lines": {
        "types": [OutfitType.MINIMALIST, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with chaise lounge and accent chair": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with round coffee table and soft lighting": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with corner sectional and modern shelving": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with wall-to-wall carpet and soft colors": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with glass coffee table and modern decor": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with rustic barn door and stone fireplace": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with exposed ceiling beams and leather furniture": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BUSINESS_WEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with soft gray tones and scandinavian accents": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with modern abstract rug and minimalist sofa": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with fireplace surrounded by built-in cabinetry": {
        "types": [OutfitType.PREPPY, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with tufted sofa and vintage chandelier": {
        "types": [OutfitType.VINTAGE, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with open shelving and modern TV setup": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with tall ceilings and oversized windows": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with large sectional and ottoman coffee table": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with parquet flooring and traditional furniture": {
        "types": [OutfitType.VINTAGE, OutfitType.PREPPY, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with colorful rug and eclectic wall art": {
        "types": [OutfitType.BOHEMIAN, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with wall-mounted fireplace and sleek sofa": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with arched doorway and warm tones": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with indoor plants and woven furniture": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with window seat and soft cushions": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with curved sofa and sculptural coffee table": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with brick fireplace and wood mantel": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with track lighting and neutral furniture": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with floor-to-ceiling curtains and soft textures": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with modern sectional and accent wall": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with stone floor tiles and warm lighting": {
        "types": [OutfitType.COTTAGECORE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with minimalist TV stand and open layout": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with wall-mounted shelves and industrial accents": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with light-colored sectional and airy decor": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with rustic wood floors and plaid throws": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with metallic accents and glass furniture": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with large bay window and light filtering drapes": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with oversized fireplace and built-in seating": {
        "types": [OutfitType.COTTAGECORE, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with neutral palette and accent rug": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with home theater setup and surround sound": {
        "types": [OutfitType.NORMCORE, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with sectional and round dining table nearby": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with wall sconces and elegant sofa set": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with floating shelves and gallery artwork": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with vaulted ceiling and stone fireplace": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with cozy sectional and layered blankets": {
        "types": [OutfitType.COTTAGECORE, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with rustic wood coffee table and farmhouse accents": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with minimal sofa and sleek black details": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with built-in bar and entertainment area": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with patterned accent rug and bold pillows": {
        "types": [OutfitType.BOHEMIAN, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with fireplace and TV mounted above": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with modular seating and flexible layout": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with geometric shelving and modern accents": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with cream-colored furniture and subtle decor": {
        "types": [OutfitType.MINIMALIST, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with two accent chairs and side table": {
        "types": [OutfitType.PREPPY, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with exposed brick wall and neutral furniture": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with wooden ceiling beams and large chandelier": {
        "types": [OutfitType.COTTAGECORE, OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with modern low coffee table and sectional": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with bohemian decor and colorful textiles": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with neutral tones and oversized sectional": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with large mirror and bright lighting": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with vintage furniture and patterned wallpaper": {
        "types": [OutfitType.VINTAGE, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with corner fireplace and cozy layout": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with indoor-outdoor connection via sliding doors": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with recessed ceiling lighting and bold rug": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with wood-paneled walls and retro vibes": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with neutral leather sectional and stone accents": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with fireplace bench seating and open shelving": {
        "types": [OutfitType.COTTAGECORE, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with black-framed windows and modern finishes": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with tall plants and natural wood furniture": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with floating entertainment console and minimal TV wall": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with neutral sectional and accent color scheme": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    "living room with fireplace, built-in shelving, and cozy atmosphere": {
        "types": [OutfitType.COTTAGECORE, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.LIVING_ROOM],
    },
    
    # Kitchen Scenes
    "kitchen with white shaker cabinets and subway tile backsplash": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with marble countertops and stainless steel appliances": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "modern kitchen with flat-panel cabinets and quartz island": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "farmhouse kitchen with apron-front sink and open shelving": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.COWBOY],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "industrial kitchen with exposed brick and metal accents": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "contemporary kitchen with large waterfall island and pendant lights": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "cozy kitchen with wood cabinets and patterned backsplash": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "galley kitchen with sleek white cabinetry and under-cabinet lighting": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "luxury kitchen with double island and chandelier lighting": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "small apartment kitchen with compact layout and bar seating": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "rustic kitchen with reclaimed wood beams and stone counters": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "transitional kitchen with shaker doors and modern hardware": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "black-and-white kitchen with checkerboard floor tiles": {
        "types": [OutfitType.RETRO, OutfitType.MINIMALIST, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "open-concept kitchen with breakfast bar and pendant lights": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "scandinavian kitchen with light oak cabinets and white finishes": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "traditional kitchen with raised-panel cabinetry and granite counters": {
        "types": [OutfitType.PREPPY, OutfitType.BUSINESS_WEAR, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "minimalist kitchen with handleless cabinets and built-in appliances": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with herringbone wood floor and quartz counters": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with navy cabinets and brass hardware": {
        "types": [OutfitType.PREPPY, OutfitType.BUSINESS_WEAR, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with butcher block counters and farmhouse sink": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.COWBOY],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with stainless steel countertops and industrial shelves": {
        "types": [OutfitType.GRUNGE, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with terracotta tile flooring and rustic cabinets": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.COWBOY],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with glass-front upper cabinets and display lighting": {
        "types": [OutfitType.PREPPY, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with matte black cabinets and wood accents": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with tiled backsplash in bold geometric pattern": {
        "types": [OutfitType.BOHEMIAN, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with peninsula layout and bar stools": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with skylight and bright open space": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with gray cabinetry and marble backsplash": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with compact island and hanging pot rack": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with two-tone cabinets and contrasting island": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with concrete countertops and open shelving": {
        "types": [OutfitType.GRUNGE, OutfitType.MINIMALIST, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with wide farmhouse table in center": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with built-in banquette seating and storage": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with floor-to-ceiling cabinetry and integrated appliances": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with corner sink and efficient layout": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with light blue cabinets and gold accents": {
        "types": [OutfitType.ROMANTIC, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with stone floor tiles and rustic wood cabinetry": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with stainless steel island and commercial appliances": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with high ceilings and exposed wood beams": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with patterned cement tiles and neutral cabinets": {
        "types": [OutfitType.BOHEMIAN, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with wine rack built into the island": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with copper range hood and farmhouse details": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with large pantry and sliding barn door": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with frosted glass cabinet doors and sleek finishes": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with oversized farmhouse sink and gooseneck faucet": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.COWBOY],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with glossy cabinets and modern LED lighting": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with wide island and waterfall countertop": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with travertine flooring and neutral tones": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with stacked double ovens and large fridge": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with curved island and bar seating": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with French doors opening to patio": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with wide galley layout and skylight": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with oak cabinets and granite counters": {
        "types": [OutfitType.PREPPY, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with polished concrete floors and clean design": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with reclaimed wood island and rustic stools": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with black granite counters and white cabinets": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with stainless steel backsplash and modern look": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with open shelving and ceramic dishes": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with island cooktop and overhead vent hood": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with patterned backsplash and matching rug": {
        "types": [OutfitType.BOHEMIAN, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with deep drawers and soft-close cabinetry": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with pendant lighting above large island": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with wide windows and garden views": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with sliding ladder for tall cabinets": {
        "types": [OutfitType.PREPPY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with dual-tone backsplash and neutral counters": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with integrated lighting under floating shelves": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with retro appliances and pastel cabinets": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with polished wood counters and white cabinets": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with wrap-around bar counter and stools": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with high-gloss cabinets and minimal decor": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with stone backsplash and rustic accents": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with tiled floor and compact breakfast nook": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with hidden pantry behind cabinet doors": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with brick accent wall and open shelving": {
        "types": [OutfitType.GRUNGE, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with dark espresso cabinetry and stainless appliances": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with wide island and farmhouse stools": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.COWBOY],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with natural wood tones and bright white walls": {
        "types": [OutfitType.COTTAGECORE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with butcher block island and hanging copper pans": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with stainless steel appliances and subway tiles": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with waterfall quartz counters and light wood": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with vaulted ceiling and skylights": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with French country details and rustic beams": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with mosaic backsplash and warm tones": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with all-white design and contrasting dark floors": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with integrated breakfast bar seating": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with open concept into dining and living areas": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with glossy backsplash tiles and wood accents": {
        "types": [OutfitType.MINIMALIST, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with ceiling-mounted pot rack and rustic vibe": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with large farmhouse table in center": {
        "types": [OutfitType.COTTAGECORE, OutfitType.COWBOY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with stacked stone backsplash and neutral palette": {
        "types": [OutfitType.COTTAGECORE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with built-in coffee station and wine fridge": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with round island and curved seating": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with colorful backsplash and modern finishes": {
        "types": [OutfitType.BOHEMIAN, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with bamboo cabinetry and eco-friendly materials": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with floor-to-ceiling windows and sleek design": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with wide pantry and organized shelving": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with marble slab backsplash and integrated lighting": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with terrazzo counters and bold cabinetry": {
        "types": [OutfitType.RETRO, OutfitType.AVANT_GARDE, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with oversized fridge and chef-style appliances": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
    "kitchen with glass-front island and illuminated shelving": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.KITCHEN],
    },
}
