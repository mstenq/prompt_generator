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
        "location": [LocationType.INDOOR, LocationType.STORE],
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
        "location": [LocationType.INDOOR, LocationType.STORE],
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
        "location": [LocationType.INDOOR, LocationType.STORE],
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
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "shopping mall food court": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.KAWAII],
        "location": [LocationType.INDOOR, LocationType.STORE],
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
        "location": [LocationType.INDOOR, LocationType.STORE],
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
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "ice cream parlor": {
        "types": [OutfitType.KAWAII, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "candy shop interior": {
        "types": [OutfitType.KAWAII, OutfitType.LOLITA, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.STORE],
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
        "location": [LocationType.INDOOR, LocationType.STORE],
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
        "location": [LocationType.INDOOR, LocationType.STORE],
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
        "location": [LocationType.INDOOR, LocationType.STORE],
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
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "record shop browsing": {
        "types": [OutfitType.GRUNGE, OutfitType.RETRO, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
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
        "location": [LocationType.INDOOR, LocationType.STORE],
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
        "location": [LocationType.INDOOR, LocationType.STORE],
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
    "beach house bathroom with light <<color:blues,whites,pastels,earth_tones,jewel_tones>> walls and seashell decor": {
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
    "coastal living room with wicker furniture and light <<color:blues,whites,pastels,earth_tones,jewel_tones>> accents": {
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
    "kitchen with light <<color:blues,whites,pastels,jewel_tones>> cabinets and gold accents": {
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
    "sunlit atrium with towering palm trees and glass ceilings spilling golden light across marble floors": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "neon-soaked arcade corridor filled with retro games, glowing buttons, and colorful reflections on polished tile": {
        "types": [OutfitType.STREETWEAR, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "high-end fashion wing with glossy black floors and mannequins posed beneath spotlit designer displays": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "1980s-style food court with pastel seating, stainless steel counters, and big glowing menu boards": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "rooftop garden above a mall, featuring wooden walkways, string lights, and a panoramic sunset skyline": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "empty mall at night, lit only by emergency lights and glowing storefronts behind metal gates": {
        "types": [OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "bustling holiday mall with oversized ornaments hanging from the ceiling and shimmering tinsel draped everywhere": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "serene Japanese mall courtyard with koi ponds, paper lanterns, and wooden bridges connecting shops": {
        "types": [OutfitType.MINIMALIST, OutfitType.ETHEREAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "glass-enclosed elevator shaft rising through multiple mall levels, reflecting shoppers as it ascends": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "luxury jewelry store with mirrored walls, velvet counters, and sparkling gemstone spotlights": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL, LocationType.STORE],
    },
    "futuristic mall hallway with holographic signs and transparent digital kiosks floating midair": {
        "types": [OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "Parisian-inspired shopping avenue inside a mall, complete with cobblestone floors and faux balconies": {
        "types": [OutfitType.ROMANTIC, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "vintage carousel in the center atrium surrounded by warm lights and painted wooden horses": {
        "types": [OutfitType.VINTAGE, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "rainforest-themed mall zone with artificial waterfalls, mist, and vines wrapping around pillars": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "tech mall section filled with glowing <<color:blues,reds,greens,jewel_tones>> LED strips and sleek glass demo tables": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "bustling toy store bursting with plush animals, colorful boxes, and life-sized character statues": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.MALL, LocationType.STORE],
    },
    "children's play area shaped like a miniature city with soft foam buildings and rainbow slides": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "mall ice-skating rink with skaters blurring under cool white overhead lights": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "bookshop café with warm amber lighting, wooden shelves, and cozy windowside seating": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.MALL, LocationType.STORE],
    },
    "candy store overflowing with rainbow bins of sweets, oversized lollipops, and glossy jars": {
        "types": [OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL, LocationType.STORE],
    },
    "mall courtyard featuring an oversized kinetic sculpture with spinning metal rings": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "quiet morning mall scene before opening, with janitors polishing spotless floors": {
        "types": [OutfitType.NORMCORE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "mall wing under renovation, filled with scaffolding, tarps, and construction lighting": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "designer shoe boutique with illuminated glass shelves stacked with elegant displays": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL, LocationType.STORE],
    },
    "mall with an indoor canal where small gondolas glide beneath arched bridges": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "discount outlet wing decorated with bold sale banners and chaotic color palettes": {
        "types": [OutfitType.NORMCORE, OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "completely mirrored hallway creating infinite reflections in every direction": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "mall entrance at dusk with glowing signage and crowds streaming through rotating doors": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "rustic-themed market area with wooden stalls, hanging copper lights, and artisan goods": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "comic-book store with wall-to-wall posters, action figures, and brightly colored decor": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.KAWAII],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "minimalist boutique with stark white walls, geometric shelving, and soft ambient lighting": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.MALL, LocationType.STORE],
    },
    "bustling escalator bank moving multiple streams of people across three levels": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "perfume shop with shimmering glass bottles arranged in gradient hues": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "grand mall staircase made of marble, flanked by sculpted railings and floral arrangements": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "pop-up art gallery inside the mall displaying bold abstract canvases and modern sculptures": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "mall aquarium tunnel with fish swimming overhead in <<color:blues>> ambient light": {
        "types": [OutfitType.ETHEREAL, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "LEGO store filled with towering brick sculptures and display walls of colorful pieces": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "nail salon with neon signage, pastel furniture, and rows of shimmering nail polish": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "indoor mini-theme park with bright rides and flashing lights": {
        "types": [OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC, OutfitType.KAWAII],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "mall Starbucks with cozy seating, wood textures, and bustling lines of customers": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "central fountain with synchronized jets and colorful programmable lights": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "jewelry kiosk under a shining chandelier in the middle of a busy walkway": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "dimly lit massage chair lounge filled with soft blue lighting and relaxed customers": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "fancy chocolate boutique displaying artisanal truffles in glass cases": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.MALL, LocationType.STORE],
    },
    "plant-filled eco-mall area with living walls and large skylights that brighten the greenery": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "bustling supermarket entrance with overflowing produce displays and warm lighting": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "indoor skate shop with graffiti mural walls and racks of boards": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "sunglasses boutique with mirrored surfaces and dramatic reflections": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.MALL, LocationType.STORE],
    },
    "phone and gadget kiosk surrounded by glowing LED cases": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL, LocationType.STORE],
    },
    "mall with a massive LED waterfall display cascading digital water animations": {
        "types": [OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "modern mall exterior at night with glowing architectural lines and glass facades": {
        "types": [OutfitType.CYBERPUNK, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "abandoned mall wing with dusty floors, dim natural light, and shuttered stores": {
        "types": [OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "donut shop with pastel interiors and trays of brightly colored pastries": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "mall food court filled with globe-shaped hanging lamps and diverse cuisine counters": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "high-fashion cosmetic store drenched in glossy lighting and sleek black fixtures": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "mall pet store with playful puppies, colorful tanks, and bright signage": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "mall corridor decorated with Chinese New Year lanterns and red banners": {
        "types": [OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "toy-themed Christmas pop-up with oversized presents and a giant Santa chair": {
        "types": [OutfitType.FESTIVAL, OutfitType.KAWAII, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "fountain courtyard surrounded by balcony walkways and overhead string lights": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "sports shop with bold graphics, neon edge lights, and towering wall displays of shoes": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "organic food pop-up market with wicker baskets and earthy tones": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "minimalist tech zone with a floor made of white glass and floating product displays": {
        "types": [OutfitType.MINIMALIST, OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "vintage camera shop filled with wooden shelves and retro signage": {
        "types": [OutfitType.VINTAGE, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "tea shop with soft lighting, bamboo decor, and glowing jars of loose leaves": {
        "types": [OutfitType.MINIMALIST, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "bustling perfume sampling booth with clouds of mist and glittering bottles": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "colorful balloon vendor kiosk set up in the middle of a busy walkway": {
        "types": [OutfitType.FESTIVAL, OutfitType.KAWAII, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "high-end watch boutique with spotlit rotating displays and dark velvet walls": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL, LocationType.STORE],
    },
    "shoe store with a dramatic tunnel entrance lined with LED strips": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.MALL, LocationType.STORE],
    },
    "mall corridor decorated for autumn with hanging leaves and warm harvest colors": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "mall rooftop lounge with modern furniture and illuminated planters": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "candy-themed photo booth surrounded by pastel backdrops and fun props": {
        "types": [OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "bustling weekend craft fair setup with handmade goods and string-light booths": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "VR gaming zone glowing with cyberpunk purples and blues": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "gourmet popcorn stand with shiny metal warmers and colorful flavor signage": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.KAWAII],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "mall aquarium exhibit featuring jellyfish tanks glowing in ultraviolet light": {
        "types": [OutfitType.ETHEREAL, OutfitType.CYBERPUNK, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "luxury handbag store with soft leather textures and marble countertops": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "European café hallway lined with outdoor-style seating and wrought-iron rails": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "kid-friendly robot show stage with animatronic characters performing": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "mall monorail track suspended above the shoppers below": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "crystal chandelier corridor with dozens of hanging lights and reflective flooring": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "holiday pop-up ice village with fake snow and cozy wooden huts": {
        "types": [OutfitType.FESTIVAL, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "tropical smoothie bar with bamboo counters and colorful fruit displays": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "kinetic LED art tunnel where lights ripple as people walk through": {
        "types": [OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "denim store filled with stacks of jeans and industrial metal fixtures": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "busy checkout line scene with beeping scanners and conveyor belts of items": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "luxury watch repair booth with tiny tools and magnifying lamps": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "towering multi-story bookstore with spiral staircases and warm amber lighting": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "spa supply shop with stone textures, diffusers emitting mist, and soft mood lighting": {
        "types": [OutfitType.ETHEREAL, OutfitType.MINIMALIST, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "comic con event setup in the mall with costumes, banners, and photo ops": {
        "types": [OutfitType.KAWAII, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "bubble-tea shop decorated with glowing pink lights and whimsical art": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "sneaker customization booth with bright paints and drying shelves": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "mall garden atrium filled with tall bamboo and stepping-stone paths": {
        "types": [OutfitType.MINIMALIST, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "street-food themed mall food hall with colorful stalls and overhead signage": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "sunglass kiosk surrounded by mirrored pyramids reflecting passerby": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "luxury home décor store lit with golden pendants and glass sculptures": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "mall security office windowed above the main walkway with monitors glowing inside": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "children's science exhibit with glowing plasma globes and interactive displays": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "massive indoor Christmas tree reaching multiple stories high with sparkling lights": {
        "types": [OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "art supply store bursting with colorful brushes, paints, and canvas stacks": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "sleek modern mall restroom with futuristic mirrors and soft, indirect lighting": {
        "types": [OutfitType.MINIMALIST, OutfitType.CYBERPUNK, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.MALL],
    },
    "cluttered startup loft office with exposed brick walls, mismatched desks, and cables snaking across the floor": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "minimalist Scandinavian-style workspace with pale wood desks and soft natural light pouring through tall windows": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "dimly lit corporate cubicle farm with gray partitions stretching into the distance like a maze": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE, OutfitType.MINIMALIST],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "retro 1980s office with beige computers, boxy monitors, and fluorescent lights humming overhead": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "modern tech office with glass-walled meeting rooms and neon accent lighting glowing behind monitors": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "cramped accountant's office filled with filing cabinets, paper stacks, and a single desk lamp": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE, OutfitType.PREPPY],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "sleek corner executive office overlooking a skyline at sunset, decorated with polished stone surfaces": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "creative agency studio with mood boards pinned everywhere and colorful sticky notes covering the walls": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "abandoned office floor with overturned chairs and dust floating through broken window light": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.PUNK],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "tiny home-office nook with plants crowding the desk and a laptop glowing warmly": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "high-energy sales bullpen with whiteboards covered in numbers and headsets scattered across desks": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "medical administrative office with neatly labeled folders and sterile white countertops": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "vintage newspaper office with typewriters, stacks of copy paper, and overhead fans spinning slowly": {
        "types": [OutfitType.VINTAGE, OutfitType.RETRO, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "nighttime open-plan office illuminated only by computer screens and a few desk lamps": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "law firm library office with dark wood shelves stacked floor to ceiling with leather-bound books": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.PREPPY],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "mid-century office featuring teak furniture, rotary phones, and amber desk lamps": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.MINIMALIST],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "research lab office lined with microscopes, charts, and whiteboards filled with equations": {
        "types": [OutfitType.NORMCORE, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "design studio with oversized monitors, color swatches, and artistic clutter everywhere": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "government office with metal desks, drop ceilings, and green-shaded banker lamps": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE, OutfitType.VINTAGE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "small insurance office with pastel walls, framed motivational posters, and a crowded reception desk": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "shared coworking space filled with mismatched chairs, succulents, and buzzing conversation areas": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BOHEMIAN],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "basement IT office with server racks humming and cables hanging overhead like vines": {
        "types": [OutfitType.CYBERPUNK, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "construction-site trailer office with blueprint rolls spread across a worn folding table": {
        "types": [OutfitType.MILITARY, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "polished finance office with chrome furniture, monochrome décor, and floor-to-ceiling windows": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "cramped translator's office with multiple keyboards, language dictionaries, and sticky notes everywhere": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "security office with multiple CCTV monitors casting blue light across the room": {
        "types": [OutfitType.CYBERPUNK, OutfitType.NORMCORE, OutfitType.MILITARY],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "travel agency office with maps pinned to the walls and brochures covering every surface": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "dusty archivist's office with old boxes, brittle documents, and a single flickering light": {
        "types": [OutfitType.VINTAGE, OutfitType.GOTHIC, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "trendy startup office with bean bags, LED strips, and whiteboards filled with sketches": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "quiet HR office with neutral colors, organized binders, and a small meeting table": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.PREPPY],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "gaming company office with character figurines lining shelves and RGB-lit workstations": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "nonprofit organization office with handmade posters and a clutter of donated supplies": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "luxury real estate office with marble floors and glossy architectural models on display": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "cramped newsroom office with monitors showing live feeds and frantic scribbled notes everywhere": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "dusty old professor's office stuffed with books, journals, and framed diplomas": {
        "types": [OutfitType.VINTAGE, OutfitType.PREPPY, OutfitType.BOHEMIAN],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "robotics workshop office with half-built prototypes and shelves full of mechanical parts": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STEAMPUNK, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "warm, earth-toned psychologist's office with soft lighting, plush chairs, and a calming atmosphere": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.MINIMALIST],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "tax-preparation office filled with calculators, towering paper files, and fluorescent lights": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE, OutfitType.PREPPY],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "industrial warehouse office with metal desks and a large window overlooking the factory floor": {
        "types": [OutfitType.MILITARY, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "realtor's office with bright lighting, home-listing boards, and neatly staged décor": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "logistics operations office with large digital maps and whiteboards full of route lines": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE, OutfitType.MILITARY],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "animation studio office with hand-drawn sketches taped everywhere and a colorful creative vibe": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC, OutfitType.KAWAII],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "political campaign office with yard signs, stacks of flyers, and ringing phones": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "biotech office with sterile surfaces, sample fridges, and glowing lab instruments": {
        "types": [OutfitType.MINIMALIST, OutfitType.CYBERPUNK, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "call center with rows of identical workstations and soft partitions dividing each space": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "tiny private detective's office with Venetian blinds, an old desk fan, and dim tungsten lighting": {
        "types": [OutfitType.VINTAGE, OutfitType.RETRO, OutfitType.GOTHIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "space agency mission-control office with massive screens and rows of consoles": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "print shop office with ink samples, paper reams, and a faint smell of toner": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.VINTAGE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "public school administrative office with children's artwork pinned behind worn desks": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.PREPPY],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "travel writer's home office filled with postcards, maps, and warm ambient lighting": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "software engineer's cluttered workspace with mechanical keyboards and hardware parts": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "minimalist CEO office with a single desk, few objects, and a panoramic city view": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "customs checkpoint office with surveillance screens and shelves holding seized items": {
        "types": [OutfitType.MILITARY, OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "rural small-town office with wood-paneled walls and a hand-painted sign out front": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "café-style coworking corner with exposed beams, plants, and bar-height work tables": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "marketing office with color palettes, product samples, and photography lights": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "legal aid office stacked with case files and poster reminders of rights and services": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "therapist's office with cozy rugs, framed nature art, and soft diffused lighting": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "sports team front-office with memorabilia, jerseys, and large whiteboards with game plans": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "data center control office with temperature monitors and blinking server indicators": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MINIMALIST, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "construction company's office with hard hats hanging on hooks and concrete samples on display": {
        "types": [OutfitType.MILITARY, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "antique shop's tiny office in the back, filled with old ledgers and dusty trinkets": {
        "types": [OutfitType.VINTAGE, OutfitType.GOTHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "mining company field office with rugged furniture, maps of excavation sites, and dirty boots by the door": {
        "types": [OutfitType.MILITARY, OutfitType.NORMCORE, OutfitType.GRUNGE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "small-town newspaper editor's office with yellowed articles pinned on a corkboard": {
        "types": [OutfitType.VINTAGE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "real-estate development office with 3D-printed building models and elegant architectural drawings": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.AVANT_GARDE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "marine research office with nautical charts, seashell samples, and blue-toned lighting": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "bustling startup accelerator shared office filled with pitch decks and laptops": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.STREETWEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "bank manager's office with polished wood furniture and stacks of signed forms": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.PREPPY],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "fashion design office with mannequins, fabric samples, and sewing tools scattered around": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "emergency-response coordination office with wall-sized maps and red marker tracking lines": {
        "types": [OutfitType.MILITARY, OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "university admissions office with promotional posters and stacks of brochures": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "small digital-nomad desk at a beachside coworking hut with ocean light pouring in": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "fire-station administrative office with gear lockers and radios crackling in the background": {
        "types": [OutfitType.MILITARY, OutfitType.NORMCORE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "minimalist architect's office with scale rulers, drafting tables, and monochrome sketches": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.AVANT_GARDE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "artist's office corner with messy paint tubes, canvases, and scribbled ideas": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.BOHEMIAN, OutfitType.GRUNGE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "veterinarian's office desk filled with pet photos, medical charts, and small animal models": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "retro 1970s office with avocado-green chairs, shag carpet, and wood-grain paneling": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.BOHEMIAN],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "cramped dorm-room study desk with textbooks piled high and fairy lights overhead": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.COTTAGECORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "biomedical research office with glowing sample refrigerators and transparent glass partitions": {
        "types": [OutfitType.MINIMALIST, OutfitType.CYBERPUNK, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "rural clinic office with simple furnishings, paper charts, and sunlight streaming through blinds": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "minimalist coding den with dual monitors, a clean desk, and a single potted plant": {
        "types": [OutfitType.MINIMALIST, OutfitType.CYBERPUNK, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "video-production office with camera gear, softboxes, and editing rigs glowing at night": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CASUAL_CHIC, OutfitType.AVANT_GARDE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "construction permit office with blueprints pinned everywhere and dated metal desks": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE, OutfitType.VINTAGE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "toy company office with bright colors, prototype models, and playful displays": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.AVANT_GARDE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "logistics dispatch office with ringing phones, route trackers, and messy clipboards": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "medical billing office with color-coded folders and cramped cubicles": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE, OutfitType.MINIMALIST],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "forest ranger's office with maps, binoculars, and wildlife posters": {
        "types": [OutfitType.MILITARY, OutfitType.COTTAGECORE, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "commuter train station manager's office overlooking the tracks through a dusty window": {
        "types": [OutfitType.VINTAGE, OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "corporate boardroom with a massive glossy table and soft recessed lighting": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "influencer's home office with LED accents, ring lights, and decorative shelves": {
        "types": [OutfitType.CYBERPUNK, OutfitType.KAWAII, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "mechanic shop office with greasy paperwork, worn furniture, and tools hanging behind the desk": {
        "types": [OutfitType.GRUNGE, OutfitType.NORMCORE, OutfitType.MILITARY],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "minimal concrete-walled design office with industrial lamps and sleek metal furniture": {
        "types": [OutfitType.MINIMALIST, OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "marine shipping office with radio equipment and a window facing docked cargo ships": {
        "types": [OutfitType.MILITARY, OutfitType.NORMCORE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "film studio production office with scheduling charts, scripts, and scattered coffee cups": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.AVANT_GARDE, OutfitType.BOHEMIAN],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "government records office with dusty shelves, old binders, and a vintage stamp machine": {
        "types": [OutfitType.VINTAGE, OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "plush investment firm office with deep carpets, modern art, and quiet ambient lighting": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "snowed-in mountain lodge office with wood beams, heavy blankets, and a small glowing computer screen": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "airport operations office with runway diagrams, radio chatter, and bright safety vests hung on hooks": {
        "types": [OutfitType.MILITARY, OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "tech repair office filled with half-assembled devices, screwdrivers, and magnifying lamps": {
        "types": [OutfitType.CYBERPUNK, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "quiet, sunlit suburban office with patterned carpet, leafy plants, and softly humming AC": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.PREPPY],
        "location": [LocationType.OFFICE, LocationType.INDOOR],
    },
    "Target superstore with a wide, brightly lit interior, glossy white floors, red aisle markers hanging from the ceiling, and long symmetrical rows of shelves stretching into the distance": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Target store in an older urban building with beige tile floors, lower ceilings, slightly dim lighting, and red signage that looks faded and worn": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.NORMCORE, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Walmart Supercenter featuring vast open space, polished concrete floors, exposed ceiling beams, fluorescent lighting, and massive blue signs floating above endless aisles": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Walmart Neighborhood Market with a smaller footprint, narrow aisles, soft white lighting, green accent walls, and compact refrigerated sections lining the perimeter": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Kmart store interior with dusty tiled floors, flickering fluorescent lights, empty metal racks, and sun-faded red signage peeling from the walls": {
        "types": [OutfitType.GRUNGE, OutfitType.NORMCORE, OutfitType.VINTAGE, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Blockbuster Video store with deep blue carpet, yellow-and-blue signage, waist-high shelves filled with VHS cases, and glowing movie poster lightboxes": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Blockbuster Video store packed with DVD cases on tall shelves, flat-screen TVs looping movie trailers, and bright retail lighting reflecting off plastic covers": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "GameStop store inside a mall with dark gray carpet, black shelving units crammed with game cases, neon-lit screens, and walls covered in character posters": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.KAWAII],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "GameStop storefront in a strip mall with bright white lighting, narrow aisles, slat walls holding controllers and headsets, and a crowded checkout counter": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Best Buy electronics store with wide aisles, blue-and-yellow signage, polished floors, and glowing demo screens covering entire walls": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Circuit City store with a red-and-white color scheme, boxy shelving, rows of CRT televisions, and thick carpet worn down in high-traffic areas": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "RadioShack shop with a tight interior, pegboard walls covered in wires and adapters, glass display cases, and handwritten sale signs": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Toys R Us store filled with bright primary colors, oversized mascot signage, towering toy aisles, and shiny floors reflecting neon shelf labels": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "KB Toys mall storefront packed floor-to-ceiling with toys, cluttered shelves, narrow walkways, and bright chaotic lighting": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.NORMCORE, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Hollister clothing store with a dark, cave-like interior, wooden floors, faux beach shack walls, dim lighting, and a soft blue glow": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.PREPPY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Abercrombie & Fitch store with extremely dark lighting, heavy wood fixtures, large black-and-white photos, and a moody, shadow-filled atmosphere": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "American Eagle Outfitters store with warm lighting, light wood floors, denim tables neatly folded, and soft neutral wall colors": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Foot Locker store featuring glossy tile floors, a black-and-white color scheme, sneaker walls lit by spotlights, and a striped checkout counter": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Champs Sports store with bright overhead lights, metallic racks, bold brand logos, and shoe displays arranged like a showroom": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Finish Line sneaker store with clean white walls, minimalist shelving, bright lighting, and shoes displayed on illuminated wall pegs": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Hot Topic store with black walls, low lighting, band posters covering every surface, metal racks packed with graphic tees, and glowing neon accents": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Spencer Gifts store with narrow aisles, novelty items covering every wall, harsh fluorescent lighting, and chaotic visual clutter": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Barnes & Noble bookstore with warm wood shelves, carpeted floors, reading tables, soft yellow lighting, and tall bookcases forming quiet corridors": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Borders bookstore with dated carpet, large windows, wooden shelving, and a café area filled with round tables and muted colors": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.VINTAGE, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Books-A-Million store with bright lighting, wide aisles, bargain book tables near the entrance, and beige-and-brown interior tones": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.NORMCORE, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Apple Store inside a mall with an all-white interior, glass walls, pale wood tables, bright even lighting, and a minimalist open layout": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Apple Store flagship location with a massive glass façade, stone floors, towering ceilings, indoor trees, and wide open floor space": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Microsoft Store with blue accent lighting, glossy floors, large interactive screens, and sleek metallic display tables": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Staples office supply store with red signage, tall shelving units, beige tile floors, and long aisles of neatly organized products": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Office Depot store featuring bright fluorescent lighting, wide open aisles, and shelves filled with paper, binders, and electronics": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "OfficeMax store with slightly dimmer lighting, gray carpet tiles, and large red-and-black hanging signs marking departments": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Costco warehouse store with enormous open space, concrete floors, towering pallet shelves, bright industrial lighting, and bulk items stacked high": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Sam's Club warehouse with wide aisles, blue signage, exposed ceilings, and massive stacks of bulk merchandise": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "IKEA showroom with staged furniture rooms, warm lighting, maze-like pathways, and colorful directional arrows on the floor": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.NORMCORE, OutfitType.SCANDINAVIAN],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "TJ Maxx store with bright lights, tightly packed racks, mismatched fixtures, and a cluttered treasure-hunt atmosphere": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Marshalls store with long clothing racks, neutral walls, bright overhead lighting, and uneven spacing that creates visual busyness": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Ross Dress for Less store with harsh fluorescent lighting, chaotic clothing racks, discount signage, and beige tile floors": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Forever 21 store with bright white lighting, fast-fashion racks tightly arranged, glossy floors, and bold promotional signs": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.KAWAII, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Urban Outfitters store with an industrial aesthetic, concrete floors, exposed brick, creative displays, and warm accent lighting": {
        "types": [OutfitType.BOHEMIAN, OutfitType.VINTAGE, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Zumiez store with a skate shop vibe, wood floors, sticker-covered counters, dark walls, and racks of streetwear": {
        "types": [OutfitType.STREETWEAR, OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "PacSun store with light wood accents, beach-inspired visuals, neutral lighting, and neatly arranged clothing tables": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.STREETWEAR, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Old Navy store with bright lighting, colorful folded clothing tables, blue signage, and wide open aisles": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Gap store with clean white walls, soft lighting, minimalist tables, and neatly folded stacks of neutral-colored clothing": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.PREPPY, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Banana Republic store with warm lighting, dark wood fixtures, upscale displays, and muted earth-tone colors": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "JCPenney department store with large open floors, carpeted sections, dated signage, and wide clothing departments": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Sears store in decline with dim lighting, empty racks, yellow clearance signs, and worn, stained carpet": {
        "types": [OutfitType.GRUNGE, OutfitType.NORMCORE, OutfitType.VINTAGE, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Kohl's store with beige tile floors, bright overhead lights, orderly racks, and bold red sale signage": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.PREPPY, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Macy's department store with high ceilings, carpeted floors, ornate lighting fixtures, and large brand-specific sections": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Nordstrom store with soft lighting, plush carpet, minimalist displays, and wide calm shopping areas": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Nordstrom Rack store with brighter lighting, tightly packed racks, and a fast-paced discount-store feel": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "CVS Pharmacy with narrow aisles, white tile floors, bright fluorescent lights, and red signage throughout": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Walgreens store with a clean layout, wide aisles, bright lighting, and neatly organized shelves": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Rite Aid store with slightly dim lighting, beige tile floors, and dated shelving units": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.GRUNGE, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "7-Eleven convenience store with bright fluorescent lights, glossy tile floors, colorful packaging, and drink coolers lining the walls": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Circle K convenience store with bold red signage, tightly packed shelves, and harsh overhead lighting": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Game Crazy video game store with a small cramped interior, glass cases, neon signage, and stacked game boxes": {
        "types": [OutfitType.STREETWEAR, OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "EB Games store with purple accents, carpeted floors, and tightly packed shelves filled with games": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.KAWAII],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "FYE music store with bright lighting, CD racks, band posters, and listening stations with headphones": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Suncoast Motion Picture Company store with glossy movie posters, DVD racks, merchandise displays, and bright mall lighting": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Tower Records store with tall shelves of vinyl and CDs, handwritten signs, bright lighting, and dense visual texture": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.GRUNGE, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Virgin Megastore with a modern retail layout, red accents, open floor plan, and glowing media displays": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.MINIMALIST, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Claire's store with a pink-and-purple color scheme, mirrored displays, bright lighting, and accessory racks everywhere": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Justice kids clothing store with extremely colorful interiors, glittery signage, bright lights, and playful decor": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Build-A-Bear Workshop with bright cheerful lighting, pastel colors, bins of stuffed animals, and interactive stations": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Petco store with bright lights, polished floors, fish tanks lining the walls, and wide aisles of pet supplies": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "PetSmart store with neutral colors, high ceilings, animal enclosures, and clear department signage": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.ATHLEISURE, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Bed Bath & Beyond store with tightly packed shelves reaching high, blue-and-white signage, and a cluttered retail density": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "World Market store with warm lighting, eclectic decor, wooden shelves, and a global bazaar atmosphere": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Pier 1 Imports store with dim cozy lighting, densely packed decor items, and narrow winding aisles": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Home Depot store with tall warehouse shelving, orange signage, concrete floors, and industrial lighting": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Lowe's store with blue signage, high ceilings, wide concrete aisles, and neatly organized hardware sections": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Menards store with bright warehouse lighting, green signage, and expansive concrete floors": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Ace Hardware store with a smaller cozy interior, narrow aisles, and shelves packed tightly with tools": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Bass Pro Shops store with a lodge-style interior, wood beams, taxidermy animals, and dim atmospheric lighting": {
        "types": [OutfitType.COWBOY, OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Cabela's store with outdoor-themed decor, rock displays, water features, and dramatic lighting": {
        "types": [OutfitType.COWBOY, OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "REI store with clean modern design, wood accents, climbing walls, and soft natural lighting": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Dick's Sporting Goods store with bright lights, tall racks of equipment, and turf flooring in select areas": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Sports Authority store with a large open layout, red signage, and wide aisles that feel empty": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Party City store with fluorescent lighting, aisles bursting with colorful decorations, balloons, and costumes": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.KAWAII, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Dollar Tree store with bright lights, tightly packed shelves, green signage, and uniform price labels": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Dollar General store with narrow aisles, yellow-and-black signage, and cluttered shelves": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Five Below store with bright playful lighting, colorful signage, and low shelves filled with novelty items": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.KAWAII, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Big Lots store with warehouse-style lighting, mixed product categories, and wide aisles": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.GRUNGE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Michaels craft store with bright lighting, tall shelving of supplies, and colorful product packaging": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.NORMCORE, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Joann Fabrics store with long aisles of fabric bolts, soft lighting, and patterned textiles everywhere": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Hobby Lobby store with warm lighting, faux-wood floors, and carefully staged decor displays": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Lids store with walls covered in hats, bright spotlights, and mirrored displays": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Footaction store with a dark interior, bold lighting accents, and sneaker displays lining the walls": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Journeys shoe store with black walls, wood floors, bright spotlights, and tightly packed shoe displays": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Sunglass Hut store with a small glossy interior, mirrored walls, bright lighting, and floating display shelves": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.PREPPY, OutfitType.BEACH_WEAR],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Victoria's Secret store with soft pink lighting, glossy floors, dramatic signage, and fabric displays": {
        "types": [OutfitType.LINGERIE, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Bath & Body Works store with bright white lighting, glowing shelves, and colorful bottles arranged symmetrically": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.NORMCORE, OutfitType.KAWAII],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Lush cosmetics store with dark walls, warm lighting, black tile floors, and vibrant handmade products stacked high": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Sephora store with a black-and-white color scheme, bright makeup lighting, mirrored displays, and clean modern lines": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Ulta Beauty store with wide aisles, bright overhead lights, colorful brand displays, and organized shelving": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.NORMCORE, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Local retro video game store with cluttered shelves, neon signs, mismatched fixtures, and stacked cartridges": {
        "types": [OutfitType.RETRO, OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Independent video rental store with faded carpet, handwritten labels, plastic DVD cases, and buzzing fluorescent lights": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.GRUNGE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Mall phone accessory kiosk with bright LED lights, glass cases packed with colorful phone cases, and reflective surfaces": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.KAWAII],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
    "Vintage thrift store with uneven lighting, mismatched racks, handwritten price tags, and worn wooden floors": {
        "types": [OutfitType.VINTAGE, OutfitType.GRUNGE, OutfitType.BOHEMIAN, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.STORE],
    },
    "Dead mall anchor store with a huge empty retail space, dim lighting, dusty floors, abandoned fixtures, and an echoing atmosphere": {
        "types": [OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.STREETWEAR, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.STORE, LocationType.MALL],
    },
}
