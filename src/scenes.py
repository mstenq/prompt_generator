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
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.MEDIEVAL],
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
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.MEDIEVAL],
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
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.ETHEREAL, OutfitType.MEDIEVAL, OutfitType.FANTASY],
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
        "types": [OutfitType.GOTHIC, OutfitType.LINGERIE, OutfitType.MEDIEVAL],
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
        "types": [OutfitType.VINTAGE, OutfitType.GOTHIC, OutfitType.CASUAL_CHIC, OutfitType.MEDIEVAL],
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
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.NORMCORE],
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

    # Front Yard Scenes
    "victorian house front yard with ornate trim, stained glass windows, and climbing ivy on the facade": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.VINTAGE, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "colonial mansion front yard with brick walkway, tall columns, and manicured boxwood hedges": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PREPPY, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "craftsman bungalow front yard with low-pitched roof, wide porch, and river rock landscaping": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "mid-century modern home front yard with flat roof, geometric lines, and drought-tolerant plants": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "contemporary glass house front yard with floor-to-ceiling windows, reflecting pool, and sculptural lawn": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "farmhouse front yard with wraparound porch, barn-red shutters, and wildflower borders": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.COWBOY],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "Tudor-style home front yard with half-timbered facade, steep gables, and clipped yew hedges": {
        "types": [OutfitType.PREPPY, OutfitType.VINTAGE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "Mediterranean villa front yard with terracotta roof tiles, stucco walls, and olive trees": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "Cape Cod cottage front yard with cedar shingles, window boxes, and a picket fence gate": {
        "types": [OutfitType.COTTAGECORE, OutfitType.PREPPY, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "art deco townhouse front yard with geometric ironwork, stepped facade, and manicured lawn": {
        "types": [OutfitType.VINTAGE, OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "ranch-style home front yard with low profile, attached garage, and wide green lawn": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "modern minimalist home front yard with concrete path, ornamental grasses, and clean lines": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.AVANT_GARDE],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "front yard rose garden with trellised climbers, gravel paths, and blooming hybrid tea roses": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "front yard with sculpted topiary hedges, symmetrical beds, and a central fountain": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PREPPY, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "front yard stone fountain surrounded by lavender beds and cobblestone walkway": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "front yard flagstone walkway lined with solar lights and ornamental shrubs": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "front yard Japanese maple garden with raked gravel, moss accents, and stepping stones": {
        "types": [OutfitType.MINIMALIST, OutfitType.ETHEREAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "desert xeriscape front yard with succulents, agave plants, and decomposed granite mulch": {
        "types": [OutfitType.BOHEMIAN, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "spring front yard with colorful tulip beds, budding trees, and fresh green lawn": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "autumn front yard with pumpkins on the steps, hay bales, and orange maple leaves": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "winter front yard with snow-dusted evergreens, frosted shrubs, and icicle-laden gutters": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "front yard wildflower meadow edge blending into a trimmed suburban lawn": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "suburban front yard wedding ceremony with white chairs, floral arch, and rose petals on the lawn": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "front yard graduation party with balloons on the mailbox, banner on the porch, and folding chairs": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "front yard birthday party with balloon arch on the driveway and colorful lawn decorations": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "staged front yard open house with for-sale sign, fresh mulch, and potted plants by the door": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "neighborhood block party spilling across front yards with tables, grills, and bunting flags": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "front yard with American flags on the porch and red-white-blue bunting for a holiday": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "Halloween-decorated front yard with jack-o-lanterns, spider webs, and fog machine on the porch": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "Christmas front yard with elaborate light display, inflatable snowman, and lit wreath on the door": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.KAWAII],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "front yard Easter egg hunt with pastel decorations, bunny cutouts, and baskets on the lawn": {
        "types": [OutfitType.KAWAII, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "front yard baby shower setup with pink and blue balloons, gift table, and garden chairs": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "southern home with wraparound porch, rocking chairs, and hanging ferns in the front yard": {
        "types": [OutfitType.COTTAGECORE, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "grand brick steps leading to a double-door entrance with potted topiaries on each side": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PREPPY, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "circular driveway front yard with a central island of flowers and a luxury sedan parked": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "wrought iron gate entrance with stone pillars and a long tree-lined driveway beyond": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "carriage house front yard with cobblestone court, lantern posts, and horse-stable doors": {
        "types": [OutfitType.VINTAGE, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "covered portico front yard with arched entry, hanging lantern, and clipped hedges": {
        "types": [OutfitType.ROMANTIC, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "estate entrance with tall stone pillars, iron gates, and a gravel approach through oaks": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PREPPY, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "second-story balcony overlooking the front yard with flower boxes and a curved driveway": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "charming front yard mailbox garden with climbing roses, bird bath, and painted mailbox": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "white picket fence front yard lane with cottage gates and hydrangea bushes": {
        "types": [OutfitType.COTTAGECORE, OutfitType.PREPPY, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "golden-hour suburban front yard with long shadows, warm light on the facade, and trimmed lawn": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "rainy front yard with umbrella on the porch, wet walkway, and glistening leaves": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "foggy morning front yard with mist over the lawn and dew on spider webs": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "sunset mansion front yard with long driveway, amber sky, and silhouetted trees": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "twilight front yard with paper lantern path, glowing porch light, and fireflies": {
        "types": [OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "spring blossom front yard with cherry trees in full bloom and petals on the walkway": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "summer front yard lemonade stand with checkered tablecloth and shade umbrella": {
        "types": [OutfitType.KAWAII, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },
    "fall front yard with leaf-strewn walkway, mums in pots, and a harvest wreath on the door": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FRONT_YARD],
    },

    # Back Yard Scenes
    "luxury back yard with infinity pool, lounge chairs, and palm trees at golden hour": {
        "types": [OutfitType.SWIMSUIT, OutfitType.BIKINI, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard lap pool with lane markers, teak decking, and glass pool fence": {
        "types": [OutfitType.SWIMSUIT, OutfitType.ATHLEISURE, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard pool with diving board, concrete deck, and colorful pool toys scattered nearby": {
        "types": [OutfitType.SWIMSUIT, OutfitType.BIKINI, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard with inflatable kiddie pool, sprinkler, and grassy play area": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard hot tub deck with cedar surround, string lights, and privacy fence": {
        "types": [OutfitType.SWIMSUIT, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard pool party with inflatable floats, tropical drinks, and music speakers": {
        "types": [OutfitType.BIKINI, OutfitType.SWIMSUIT, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard pool with natural rock waterfall feature and tropical landscaping": {
        "types": [OutfitType.SWIMSUIT, OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard natural stone pool with boulders, ferns, and a wooden bridge": {
        "types": [OutfitType.SWIMSUIT, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard pool at night with underwater lights, lit palm trees, and moonlit water": {
        "types": [OutfitType.SWIMSUIT, OutfitType.BIKINI, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard poolside cabana with white curtains, daybed, and shaded bar area": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard BBQ party with smoking grill, picnic tables, and checkered tablecloths": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard patio dining under string lights with long farm table and candle centerpieces": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard outdoor kitchen with stone counter, built-in grill, and herb planters": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard fire pit circle with Adirondack chairs, s'mores supplies, and starry sky": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard tiki bar with bamboo accents, thatched roof, and tropical drink setup": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard garden cocktail party with linen-draped tables, champagne, and twinkle lights": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard luau setup with tiki torches, leis on chairs, and a roasted pig table": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard kids birthday party with piñata, balloon arch, and colorful bunting": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard wine tasting patio with barrel tables, vineyard views, and grape vines overhead": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard outdoor movie night with projector screen, blankets, and popcorn station": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard vegetable garden with raised beds, trellised tomatoes, and compost bin": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard greenhouse filled with tropical plants, potting bench, and misted glass panels": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard koi pond with stepping stones, bamboo fence, and lily pads": {
        "types": [OutfitType.ETHEREAL, OutfitType.BOHEMIAN, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard butterfly garden with wildflowers, bird bath, and wooden bench": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard herb garden with labeled planters, stone path, and kitchen door nearby": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard zen rock garden with raked gravel, moss islands, and bamboo screening": {
        "types": [OutfitType.MINIMALIST, OutfitType.ETHEREAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard orchard with fruit trees, wooden ladder, and fallen apples on the grass": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard wildflower border along a cedar fence with bees and butterflies": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard white gazebo with climbing roses, lattice sides, and garden chairs inside": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard pergola draped with wisteria vines, hanging lanterns, and a dining set below": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard treehouse with rope ladder, wooden platform, and leafy canopy overhead": {
        "types": [OutfitType.KAWAII, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard swing set and slide on a rubber mulch play area with picket fence": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard hammock strung between two oak trees with dappled shade and a book nearby": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard chicken coop with wire run, nesting boxes, and free-ranging hens": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard shed workshop with open doors, tools on pegboard, and woodworking bench": {
        "types": [OutfitType.COTTAGECORE, OutfitType.GRUNGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard covered patio with ceiling fan, wicker furniture, and potted palms": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "estate back yard with manicured lawn, tiered fountain, and marble statuary": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard private tennis court with net, clay surface, and spectator bench": {
        "types": [OutfitType.ATHLEISURE, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard putting green with sand trap, flag pin, and clubhouse view": {
        "types": [OutfitType.ATHLEISURE, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard outdoor ballroom tent with chandeliers, dance floor, and draped fabric walls": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard estate rose garden with arbors, gravel paths, and heirloom varieties": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard marble terrace with urn planters, wrought iron furniture, and city views": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard sculpted topiary maze with hedgerows, gravel paths, and a central bench": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard vineyard rows at the property edge with grapevines and rolling hills beyond": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard wedding reception with long dining tables, string lights, and floral centerpieces": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard graduation cookout with banner on the fence, cooler of drinks, and folding chairs": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard anniversary dinner for two with candlelit table, rose petals, and fountain": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard poolside engagement party with champagne tower, floral arch, and sunset glow": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard summer festival tent with bunting, food stalls, and live music stage": {
        "types": [OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },
    "back yard outdoor yoga session on rolled mats with sunrise light and dewy grass": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.BACK_YARD],
    },


    # Restaurant Scenes
    "intimate french bistro with candlelit tables, exposed brick walls, and vintage wine racks": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "bustling tokyo ramen shop with steam rising from copper pots and red lantern glow": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "grand italian trattoria with checkered floors, hanging garlic braids, and open wood-fired oven": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "michelin-star tasting room with minimalist white plates and soft spotlighting on each course": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "1950s american diner with chrome stools, neon jukebox, and checkerboard tile floor": {
        "types": [OutfitType.RETRO, OutfitType.PIN_UP, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "dim sum parlor with bamboo steamers stacked high and round lazy susan tables": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "spanish tapas bar interior with dark wood beams, jamón legs hanging overhead, and tiled walls": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "korean bbq restaurant with built-in table grills, sizzling meat, and smoky ventilation hoods": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "art deco seafood restaurant with brass railings, porthole windows, and nautical chandeliers": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.RETRO, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "cozy scandinavian café-restaurant with blonde wood furniture, hygge candles, and wool throws": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "moroccan riad dining room with mosaic tile fountains, carved cedar screens, and brass lanterns": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "industrial loft restaurant with exposed steel beams, Edison bulbs, and communal farm tables": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "victorian tea room with lace curtains, porcelain teapots, and tiered pastry stands": {
        "types": [OutfitType.ROMANTIC, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "mexican cantina interior with colorful papel picado banners, terracotta pots, and mariachi stage": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "sushi omakase counter with cedar bar seating, chef's knife work, and seasonal fish display": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "indian curry house with saffron-colored walls, brass serving dishes, and spice market aromas": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "greek taverna with whitewashed walls, blue-painted shutters, and olive branch centerpieces": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "steakhouse dining room with dark leather booths, mahogany paneling, and dim amber lighting": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "plant-based fine dining with living green walls, sculptural plating, and ambient nature sounds": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "thai street-food inspired restaurant with neon signs, plastic stools, and wok flame theatrics": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "russian tea house with samovars steaming, ornate samovar tea sets, and fur-trimmed booth seating": {
        "types": [OutfitType.RETRO, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "peruvian cevicheria with lime-green walls, fishing net décor, and ceviche bar counter": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "ethiopian restaurant with woven basket tables, injera bread spreads, and hand-washing ritual basin": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "belgian brasserie with art nouveau stained glass, mussel pot service, and abbey beer taps": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "chinese hot pot restaurant with divided broth cauldrons, dipping sauce bar, and bubbling steam": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "provence countryside restaurant with lavender bundles, stone fireplace, and rustic linen tablecloths": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "underground wine cellar restaurant with arched stone vaults, candle clusters, and oak barrel tables": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "hawaiian poke bowl spot with surfboard wall art, tiki torches indoors, and tropical flower leis": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "lebanese mezze restaurant with mosaic floors, hookah corner, and mezze platter spreads": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "new orleans creole restaurant with wrought iron balcony views inside, jazz trio corner, and gumbo pots": {
        "types": [OutfitType.RETRO, OutfitType.ROMANTIC, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "swiss fondue chalet dining room with pine paneling, cowbell décor, and melted cheese cauldron": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "vietnamese pho shop with plastic table covers, herb garnish trays, and broth steam clouds": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "turkish kebab house with copper grill smoke, rotating spit meat, and ornate tile backsplash": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "portuguese seafood tavern with blue azulejo tiles, sardine grill, and fishing boat model décor": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "farm-to-table restaurant with open kitchen, herb garden window boxes, and mason jar cocktails": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "jazz-age supper club dining room with velvet curtains, champagne towers, and live piano": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PIN_UP, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "middle eastern shawarma shop with vertical rotisserie, flatbread press, and spice rack walls": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "cuban paladar with vintage 1950s car photos, rum cocktail bar, and ropa vieja platters": {
        "types": [OutfitType.RETRO, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.RESTAURANT],
    },
    "sun-dappled mediterranean restaurant patio with terracotta pots, grapevine trellis, and linen umbrellas": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "rooftop restaurant terrace overlooking city skyline with string lights and glass windscreens": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "french café sidewalk terrace with wicker bistro chairs, cobblestone street, and morning espresso crowd": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "tuscan vineyard restaurant patio with long harvest table, cypress trees, and golden hour light": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.RESTAURANT],
    },
    "miami art deco hotel restaurant poolside patio with palm fronds and pastel umbrella shades": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "japanese zen garden restaurant terrace with koi pond edge seating and maple tree canopy": {
        "types": [OutfitType.MINIMALIST, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.RESTAURANT],
    },
    "texas hill country bbq restaurant picnic patio with long wooden benches and smoker pit nearby": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.RESTAURANT],
    },
    "greek island cliffside taverna terrace with whitewashed railing and aegean sea sunset view": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.RESTAURANT],
    },
    "brooklyn brownstone backyard restaurant garden patio with string lights and herb planter dividers": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "location": [LocationType.OUTDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },
    "moroccan courtyard restaurant open-air patio with mosaic fountain centerpiece and lantern strings": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.RESTAURANT],
    },
    "california farm restaurant orchard patio with fruit tree shade and farmstand flower arrangements": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.RESTAURANT],
    },
    "parisian hidden courtyard restaurant patio with ivy-covered stone walls and iron café tables": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.RESTAURANT, LocationType.CITY],
    },

    # Bar Scenes
    "hidden speakeasy behind unmarked door with velvet banquettes, dim amber sconces, and jazz trio": {
        "types": [OutfitType.RETRO, OutfitType.EVENING_FORMAL, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "irish pub with dark mahogany bar, Guinness taps, and vintage rugby memorabilia on walls": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "craft cocktail lounge with marble bar top, copper shakers, and backlit bottle display wall": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "dive bar with neon beer signs, sticky wooden floor, and pool table under cigarette haze": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "rooftop cocktail bar interior with floor-to-ceiling windows and panoramic night city views": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "tiki bar with bamboo walls, thatched roof accents, flaming tiki torches, and rum punch bowls": {
        "types": [OutfitType.RETRO, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "wine bar with exposed brick, barrel-table seating, and chalkboard wine list by the glass": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "sports bar with wall of HD screens, team pennants, and crowded game-day atmosphere": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "whiskey library bar with floor-to-ceiling bottle shelves, leather armchairs, and cigar humidor": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.RETRO, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "punk rock bar with band stickers covering walls, jukebox blasting, and graffiti bathroom doors": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "hotel lobby bar with grand piano, crystal chandeliers, and white-gloved bartender service": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "mezcal bar with agave plant murals, clay copita glasses, and Oaxacan folk art shelves": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "german beer hall with long communal tables, stein racks overhead, and oompah band stage": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "jazz club bar with low stage, red velvet curtains, and smoky spotlight on saxophonist": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.RETRO, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "molecular mixology lab bar with dry ice cocktails, beakers, and laboratory glassware décor": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "country honky-tonk bar with line dancing floor, neon cowboy boot sign, and mechanical bull nearby": {
        "types": [OutfitType.COWBOY, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "absinthe bar with green fairy posters, ornate fountains, and Belle Époque absinthe spoons": {
        "types": [OutfitType.RETRO, OutfitType.GOTHIC, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "karaoke bar with private booth rooms, disco ball, and LED lyric screen on main stage": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "sake bar with tatami seating alcoves, cedar counter, and warm paper lantern glow": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "prohibition-era basement bar with brick archways, password entry, and flask-shaped lamps": {
        "types": [OutfitType.RETRO, OutfitType.PIN_UP, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "champagne bar with gold mirrored walls, coupe glass towers, and velvet rope VIP section": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "beach-themed tiki dive with fishing nets, pufferfish lamps, and hurricane glass cocktails": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "scotch whisky bar with tartan plaid upholstery, peat smoke aroma, and glencairn glass service": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.RETRO, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "latin salsa bar with dance floor tiles, live percussion band, and colorful papel picado": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "gastropub with craft beer taps, gourmet bar snacks menu, and reclaimed wood interior": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "blues bar with neon crossroads sign, worn barstools, and guitarist on corner stool": {
        "types": [OutfitType.GRUNGE, OutfitType.RETRO, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "hotel rooftop bar enclosure with retractable glass walls and heated outdoor lounge beyond": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "vodka tasting bar with frozen shot glasses, ice sculpture bar back, and Russian nesting doll décor": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "arcade bar with vintage pinball machines, craft beer on tap, and retro game cabinet row": {
        "types": [OutfitType.RETRO, OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "art gallery bar hybrid with rotating exhibition walls and curator-selected wine pairings": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "cowboy saloon bar with swinging doors, brass spittoons, and long polished pine bar top": {
        "types": [OutfitType.COWBOY, OutfitType.RETRO, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "gin botanical bar with hanging herb gardens, copper still display, and botanical illustration wallpaper": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "underground bunker bar with concrete walls, military surplus stools, and red emergency lighting": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "piano bar with sing-along sheet music, spotlight on grand piano, and cocktail waitress in sequins": {
        "types": [OutfitType.PIN_UP, OutfitType.RETRO, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "tequila cantina bar with agave field mural, salt-rim station, and mariachi jukebox": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "library bar with bookshelves behind bar, reading lamp pools, and literary cocktail menu": {
        "types": [OutfitType.PREPPY, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "neon-lit cyberpunk-themed bar with holographic menus, LED strip architecture, and synthwave DJ booth": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "bourbon street-style balcony bar overlooking parade route with wrought iron railings": {
        "types": [OutfitType.FESTIVAL, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "mountain lodge aprés-ski bar with stone fireplace, antler chandelier, and hot toddy steam": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "port wine lodge bar with river-view windows, oak cask aging room visible through glass": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "cocktail omakase bar with eight-seat counter, chef-bartender performance, and seasonal tasting flight": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "dive punk karaoke basement bar with duct-taped microphones and sticker-covered bathroom mirror": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "art deco cocktail bar with geometric gold leaf ceiling, martini glass chandeliers, and jazz age murals": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.RETRO, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "farm distillery bar with copper pot still visible, hay bale seating, and apple orchard view windows": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "high-end hotel sky bar with infinity edge glass floor and clouds visible below at dusk": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "rum pirate-themed bar with ship wheel décor, barrel-aged rum racks, and nautical rope rigging": {
        "types": [OutfitType.RETRO, OutfitType.GRUNGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "natural wine bar with minimal concrete interior, orange wine bottles, and sourdough bar snacks": {
        "types": [OutfitType.MINIMALIST, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },
    "blues and bourbon bar with vinyl record wall, worn leather Chesterfield, and low amber pendant lights": {
        "types": [OutfitType.RETRO, OutfitType.GRUNGE, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "hotel pool bar indoor cabana with tropical plants, bamboo screens, and frozen cocktail blender": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.BAR],
    },
    "underground jazz speakeasy with brick vault ceiling, candlelit tables, and upright bass corner": {
        "types": [OutfitType.RETRO, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.BAR, LocationType.CITY],
    },

    # Nightclub Scenes
    "neon-drenched main dance floor with laser grid overhead and pounding bass speakers": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "vip bottle service booth with velvet rope, champagne buckets, and LED bottle glorifier": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "underground techno bunker with concrete walls, strobe flashes, and fog machine haze": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "retro disco club with mirror ball, colorful dance floor tiles, and platform shoe crowd": {
        "types": [OutfitType.RETRO, OutfitType.CLUB_PARTY, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "latin reggaeton nightclub with salsa dance floor, live DJ booth, and tropical LED palms": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "gothic industrial nightclub with chain curtains, red spotlight pools, and darkwave DJ set": {
        "types": [OutfitType.GOTHIC, OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "rooftop enclosed nightclub with glass walls, city lights panorama, and rooftop pool edge": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "hip-hop club with graffiti mural walls, go-go dancer platforms, and gold chain décor": {
        "types": [OutfitType.STREETWEAR, OutfitType.CLUB_PARTY, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "edm festival-style mega club with massive LED wall, CO2 cannons, and crowd surge energy": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "1920s speakeasy nightclub with flapper dancers, art deco bar, and hidden dance floor": {
        "types": [OutfitType.PIN_UP, OutfitType.RETRO, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "k-pop themed nightclub with LED light sticks, holographic stage, and fan chant energy": {
        "types": [OutfitType.KAWAII, OutfitType.CLUB_PARTY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "warehouse rave nightclub with exposed steel trusses, UV paint splatter, and DJ riser": {
        "types": [OutfitType.CYBERPUNK, OutfitType.PUNK, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "cabaret nightclub with feathered showgirl stage, velvet curtains, and spotlight runway": {
        "types": [OutfitType.PIN_UP, OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "afrobeat nightclub with live drum circle, colorful Ankara fabric drapes, and dance circle": {
        "types": [OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "minimalist white-room nightclub with monochrome décor, ambient techno, and sculptural seating": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "country line-dance nightclub with hay bale décor, neon boot sign, and mechanical bull corner": {
        "types": [OutfitType.COWBOY, OutfitType.RETRO, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "drag show nightclub with runway stage, spotlight sequins, and audience cabaret tables": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CLUB_PARTY, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "japanese host club with plush booth seating, champagne towers, and ornate gold interiors": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.KAWAII, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "psychedelic trance nightclub with UV reactive art, liquid light projections, and incense haze": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CYBERPUNK, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "hipster indie dance club with vintage vinyl DJ booth, thrift-store décor, and disco lights": {
        "types": [OutfitType.RETRO, OutfitType.GRUNGE, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "beach club indoor section with sand floor, tiki bar, and tropical house music": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "fashion week afterparty nightclub with runway extension, photographer flashes, and model crowd": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "metal nightclub with band merch walls, mosh pit area, and aggressive strobe lighting": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "ballroom converted nightclub with crystal chandeliers, parquet dance floor, and orchestra pit DJ": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "cyberpunk-themed nightclub with holographic dancers, neon kanji signs, and rain-slick aesthetic": {
        "types": [OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "salsa nightclub with live band stage, hardwood dance floor, and spinning mirror ball": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "underground hip-hop battle club with graffiti cypher circle, boombox décor, and raw concrete": {
        "types": [OutfitType.STREETWEAR, OutfitType.PUNK, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "luxury yacht-themed nightclub with porthole windows, nautical rope, and champagne spray": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "rave cave nightclub with stalactite projections, cave-like rock walls, and subwoofer rumble": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "pin-up burlesque nightclub with velvet booths, feather fans on stage, and martini service": {
        "types": [OutfitType.PIN_UP, OutfitType.RETRO, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "korean club room with soju bottle towers, neon noraebang booths, and K-pop video walls": {
        "types": [OutfitType.KAWAII, OutfitType.CLUB_PARTY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "art installation nightclub with rotating sculptural pieces, gallery-white walls, and ambient beats": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "steampunk-themed nightclub with brass gears, clockwork projections, and industrial DJ platform": {
        "types": [OutfitType.STEAMPUNK, OutfitType.RETRO, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "pool party nightclub indoor section with swim-up bar, underwater LED lights, and DJ booth": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.BEACH_WEAR, OutfitType.BIKINI],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "reggae dancehall nightclub with sound system wall of speakers, red-gold-green lighting, and dub vibes": {
        "types": [OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "futuristic nightclub with LED floor panels, robot bartender, and chrome geometric architecture": {
        "types": [OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "vintage roller disco nightclub with skate floor, retro disco ball, and quad skate rental": {
        "types": [OutfitType.RETRO, OutfitType.PIN_UP, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "lgbtq+ pride nightclub with rainbow LED installation, inclusive dance floor, and drag host": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "bollywood nightclub with ornate gold pillars, colorful sari-draped décor, and bhangra DJ": {
        "types": [OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "after-hours warehouse nightclub with sunrise light through cracked windows and exhausted dancers": {
        "types": [OutfitType.GRUNGE, OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "champagne and caviar nightclub with ice sculpture bar, oyster station, and crystal décor": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "anime-themed nightclub with cosplay crowd, manga wall art, and J-pop remix DJ": {
        "types": [OutfitType.ANIME, OutfitType.KAWAII, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "desert oasis themed nightclub with sand dunes projection, palm tree silhouettes, and tribal beats": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "punk rock nightclub with stage diving area, band posters, and sticky beer-soaked floor": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "silent disco nightclub with glowing headphone zones, color-coded channels, and quiet dance floor": {
        "types": [OutfitType.MINIMALIST, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "velvet underground-style nightclub with black walls, single spotlight, and avant-garde performances": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "carnival-themed nightclub with ferris wheel projection, cotton candy bar, and funhouse mirrors": {
        "types": [OutfitType.FESTIVAL, OutfitType.RETRO, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "high-energy shuffle nightclub with LED shuffle circle, fast-tempo house, and sneaker crowd": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },
    "opera house converted nightclub with balcony boxes, grand stage DJ setup, and dramatic lighting": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB],
    },
    "neon Tokyo alley-inspired nightclub with narrow corridor dance floor and vending machine bar": {
        "types": [OutfitType.CYBERPUNK, OutfitType.KAWAII, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.NIGHTCLUB, LocationType.CITY],
    },

    # Gym Scenes
    "modern crossfit box with rubber flooring, pull-up rig, and chalk dust in the air": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "luxury hotel gym with floor-to-ceiling windows, Technogym equipment, and towel service station": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "old-school iron gym with rusty free weights, motivational posters, and no-frills mirrors": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "boutique spin studio with colored mood lighting, stadium seating bikes, and instructor podium": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "yoga studio with bamboo floors, meditation cushions, and soft natural morning light": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "24-hour neon-lit gym with fluorescent overhead lights and late-night solo lifters": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "boxing gym with heavy bags hanging in rows, speed bag platform, and worn canvas ring": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "climbing gym with colorful bouldering walls, crash pads, and chalk bag stations": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "university campus rec center with basketball court visible, student ID check-in, and busy cardio deck": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "pilates reformer studio with sleek machines, mirrored wall, and neutral-toned décor": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "warehouse-style gym with exposed ductwork, tire flip area, and battle rope stations": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "hotel rooftop gym enclosure with city skyline view and compact cable machine setup": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "mma training gym with octagon cage, Thai pads on wall, and fighter mural": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "women-only fitness studio with pink accent walls, group class mirrors, and smoothie bar corner": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "powerlifting gym with competition platforms, calibrated plates, and chalk bucket stations": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "aerial silks circus gym with high ceilings, silk fabric drops, and crash mat flooring": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "corporate office building gym with badge-access entry, locker rooms, and lunchtime crowd": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "retro 1980s gym with vintage Nautilus machines, orange carpet, and wall-mounted CRT TVs": {
        "types": [OutfitType.RETRO, OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "swimming pool-adjacent gym with lap pool windows, aquatic cardio machines, and humid air": {
        "types": [OutfitType.ATHLEISURE, OutfitType.SWIMSUIT, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "functional fitness studio with kettlebell racks, sled push track, and turf sprint lane": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "dance fitness studio with wall mirrors, hardwood floor, and Zumba class in session": {
        "types": [OutfitType.ATHLEISURE, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "physical therapy gym hybrid with rehab equipment, resistance bands, and clinical white walls": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "underground basement gym with low ceilings, fluorescent flicker, and gritty atmosphere": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "luxury spa gym with marble accents, eucalyptus steam room visible, and orchid arrangements": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "parkour training gym with foam pit, wall run obstacles, and urban obstacle course setup": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "cycling gym with virtual reality screens, immersive road routes, and fan cooling": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CYBERPUNK, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "hotel basement gym with compact equipment, mirrored walls, and single treadmill row": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "community center gym with basketball hoops lowered, folding bleachers, and family-friendly vibe": {
        "types": [OutfitType.ATHLEISURE, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "barre fitness studio with ballet barres, soft pink lighting, and tulle curtain accents": {
        "types": [OutfitType.ATHLEISURE, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "strongman training gym with atlas stones, log press, and farmer walk handles": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "hotel resort gym with tropical plant dividers, ocean-view windows, and open-air ventilation": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "kickboxing gym with muay thai ring, heavy bag forest, and Thai flag wall banner": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "meditation and movement studio with floor cushions, singing bowls, and dim amber lighting": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "apartment building fitness room with basic dumbbell rack, one elliptical, and laundry room adjacent": {
        "types": [OutfitType.ATHLEISURE, OutfitType.NORMCORE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "Olympic weightlifting gym with platform blocks, bumper plates, and national flag banners": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "hot yoga studio with heated room, infrared panels, and sweat-drenched mirrored walls": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "military-style boot camp gym with obstacle course elements, drill instructor whistle, and camo netting": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "hotel penthouse gym with private elevator access, panoramic views, and concierge towel service": {
        "types": [OutfitType.ATHLEISURE, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "gymnastics training center with balance beams, parallel bars, and foam pit landing zone": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "rowing club indoor tank with erg machines lined up, boat oar wall display, and river club banners": {
        "types": [OutfitType.ATHLEISURE, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "neon cyberpunk-themed boutique gym with LED strip equipment, holographic trainers, and dark walls": {
        "types": [OutfitType.CYBERPUNK, OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "senior fitness center with low-impact machines, handrail-equipped treadmills, and social seating area": {
        "types": [OutfitType.ATHLEISURE, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "hotel spa wellness gym with salt wall, infrared sauna adjacent, and herbal tea station": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "grappling academy gym with wrestling mats, gi racks, and academy patch wall": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "hotel conference center gym pop-up with portable equipment and convention attendee crowd": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "calisthenics park indoor facility with pull-up bars, dip stations, and rings setup": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "hotel ski lodge gym with wood paneling, ski rack by door, and après workout fireplace nearby": {
        "types": [OutfitType.ATHLEISURE, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "rehabilitation sports gym with anti-gravity treadmill, hydrotherapy pool view, and athlete posters": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.PREPPY],
        "location": [LocationType.INDOOR, LocationType.GYM],
    },
    "underground fight club aesthetic gym with bare bulb lighting, concrete floor, and no signage": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },
    "boutique HIIT studio with heart rate monitor screens, turf floor stations, and motivational neon sign": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.CLUB_PARTY],
        "location": [LocationType.INDOOR, LocationType.GYM, LocationType.CITY],
    },

    # Hotel Scenes
    "grand hotel lobby with marble floors, crystal chandelier, and concierge desk with bellhops": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "boutique hotel reception with curated art pieces, fresh flower arrangement, and designer furniture": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "luxury suite bedroom with king bed, silk sheets, city-view floor-to-ceiling windows": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "hotel presidential suite living room with panoramic views, grand piano, and butler service cart": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "art deco hotel corridor with geometric carpet, brass elevator doors, and sconce lighting": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.RETRO, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel spa relaxation lounge with heated loungers, cucumber water, and eucalyptus steam": {
        "types": [OutfitType.MINIMALIST, OutfitType.ROMANTIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "rooftop hotel restaurant interior with panoramic windows and white tablecloth fine dining": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "historic hotel library lounge with leather armchairs, globe bar cart, and afternoon tea service": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "modern minimalist hotel room with platform bed, neutral palette, and smart home controls": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "honeymoon suite with rose petal bed, champagne bucket, and balcony doors open to ocean breeze": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel business center with workstations, printer stations, and early-morning suited travelers": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "tropical resort hotel open-air lobby with thatched roof, ceiling fans, and welcome fruit punch": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "gothic revival hotel staircase with ornate banister, stained glass window, and red carpet runner": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel conference ballroom pre-event with round tables, stage setup, and AV crew testing lights": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "ski lodge hotel great room with stone fireplace, mounted antlers, and hot cocoa station": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel rooftop bar lounge interior with retractable skylight and craft cocktail menu": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "extended-stay hotel kitchenette suite with small dining table, mini fridge, and laptop workspace": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "palace hotel grand ballroom with gold leaf ceiling, crystal chandeliers, and waltz-ready floor": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.AVANT_GARDE],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel pool indoor atrium with glass ceiling, palm trees, and heated turquoise water": {
        "types": [OutfitType.SWIMSUIT, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "design hotel elevator lobby with statement sculpture, mood lighting, and gallery wall": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "hotel bridal suite preparation room with vanity mirrors, floral arch, and champagne toast table": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "airport hotel transit lounge room with blackout curtains, jet-lagged traveler, and room service tray": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "ryokan-style hotel room with tatami mats, futon bedding, and shoji screen doors": {
        "types": [OutfitType.MINIMALIST, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel cigar lounge with leather Chesterfield sofas, humidor cabinet, and whiskey decanter service": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "overwater bungalow hotel room with glass floor panel showing lagoon fish below": {
        "types": [OutfitType.ROMANTIC, OutfitType.BEACH_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel fitness center adjacent lounge with post-workout smoothie bar and massage chair": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "victorian bed and breakfast hotel parlor with lace doilies, antique clock, and guest book": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel mezzanine library with spiral staircase, rare book collection, and reading nook alcoves": {
        "types": [OutfitType.PREPPY, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "casino hotel gaming floor adjacent lounge with slot machine glow and cocktail waitress": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "eco-lodge hotel room with reclaimed wood furniture, solar panel view, and organic cotton linens": {
        "types": [OutfitType.BOHEMIAN, OutfitType.MINIMALIST, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel executive club floor lounge with complimentary breakfast buffet and city-view terrace door": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "moroccan riad hotel courtyard room opening to tiled fountain courtyard with orange trees": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel jazz lounge with small stage, cocktail tables, and upright bass in corner": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.RETRO, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "capsule hotel pod interior with compact sleeping berth, ambient blue lighting, and privacy curtain": {
        "types": [OutfitType.MINIMALIST, OutfitType.CYBERPUNK, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "hotel wedding venue preparation suite with dress rack, floral centerpieces, and nervous energy": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "converted monastery hotel cell room with stone walls, arched window, and simple wooden crucifix": {
        "types": [OutfitType.GOTHIC, OutfitType.MINIMALIST, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel afternoon tea salon with tiered sandwich stands, fine china, and harpist in corner": {
        "types": [OutfitType.ROMANTIC, OutfitType.PREPPY, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "penthouse hotel terrace room with private hot tub, fire pit, and skyline panorama through glass": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "hotel art gallery corridor with rotating exhibition pieces and gallery track lighting": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "historic train car converted hotel suite with brass fixtures, velvet seating, and window landscape": {
        "types": [OutfitType.RETRO, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel kids club activity room with colorful play structures visible through glass partition": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "wellness retreat hotel meditation room with floor cushions, singing bowl, and Himalayan salt lamp": {
        "types": [OutfitType.MINIMALIST, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel luggage storage room with brass luggage carts, tagged suitcases, and bellhop uniforms": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.RETRO, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "ice hotel interior room with carved ice furniture, fur blankets, and blue ambient lighting": {
        "types": [OutfitType.MINIMALIST, OutfitType.AVANT_GARDE, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel rooftop greenhouse lounge with tropical plants, glass walls, and afternoon tea service": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "boutique hotel bathroom suite with rainfall shower, marble vanity, and luxury amenity display": {
        "types": [OutfitType.MINIMALIST, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel New Year's Eve gala ballroom with countdown clock, confetti cannons, and formal crowd": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL, LocationType.CITY],
    },
    "desert luxury tent hotel interior with woven rugs, lantern light, and stargazing roof flap open": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "hotel film noir themed bar lounge with black and white photos, jazz piano, and smoky atmosphere": {
        "types": [OutfitType.RETRO, OutfitType.EVENING_FORMAL, OutfitType.PIN_UP],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },
    "floating houseboat hotel cabin with river views through porthole windows and gentle rocking motion": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.HOTEL],
    },

    # Park Scenes
    "sun-dappled meadow with wildflowers": {
        "types": [OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "cherry blossom-lined walking path": {
        "types": [OutfitType.FESTIVAL, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "moss-covered stone bridge over a creek": {
        "types": [OutfitType.COTTAGECORE, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "picnic blanket under a sprawling oak tree": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "rustic wooden park bench at golden hour": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "butterfly garden in full bloom": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "misty morning jogging trail through pines": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "autumn leaf-strewn woodland path": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "frozen pond with ice skaters nearby": {
        "types": [OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "community garden raised beds": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "willow tree shade by a quiet pond": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "dog park fenced play area": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "sculpture garden with modern art pieces": {
        "types": [OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "amphitheater stone steps at dusk": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "botanical greenhouse exterior walkway": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "fountain plaza with splashing water jets": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "tree-lined boulevard in spring bloom": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "hidden grove with fern-covered ground": {
        "types": [OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "bird sanctuary wooden observation deck": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "sunset hilltop overlooking the city": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "covered wooden gazebo in rain": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "wildflower prairie stretching to horizon": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "creek-side stepping stones": {
        "types": [OutfitType.COTTAGECORE, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "memorial rose garden in peak season": {
        "types": [OutfitType.FESTIVAL, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "playground swings at twilight": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "nature trail boardwalk through wetlands": {
        "types": [OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "rock garden with zen raked gravel": {
        "types": [OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "outdoor yoga lawn at sunrise": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "historic bandstand on village green": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "lily pad pond with dragonflies": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "shaded reading nook under maple trees": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "outdoor chess tables in dappled light": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "community orchard with ripe fruit trees": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "firefly-lit meadow at summer dusk": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "snow-covered pine forest clearing": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "herb garden with lavender rows": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "outdoor amphitheater empty seats": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "koi pond with arched red bridge": {
        "types": [OutfitType.FESTIVAL, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "wild blackberry bramble path": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "sunflower field edge near park fence": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "outdoor fitness station on gravel path": {
        "types": [OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "bee apiary fenced meadow corner": {
        "types": [OutfitType.COTTAGECORE, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "storybook trail with carved wooden signs": {
        "types": [OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "outdoor meditation circle of stones": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "rainbow flag festival grounds setup": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "outdoor library book exchange kiosk": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "treehouse lookout platform in woods": {
        "types": [OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "outdoor pottery market on grass lawn": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "moonlit park path with lantern posts": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },
    "spring tulip display in formal beds": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.PARK],
    },

    # Pool Scenes
    "infinity pool overlooking ocean cliffs": {
        "types": [OutfitType.SWIMSUIT, OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "rooftop pool with city skyline backdrop": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.BIKINI],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "resort lagoon pool with swim-up bar": {
        "types": [OutfitType.SWIMSUIT, OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "olympic-size lap pool lane markers": {
        "types": [OutfitType.BIKINI, OutfitType.ATHLEISURE, OutfitType.SWIMSUIT],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "tropical pool surrounded by palm trees": {
        "types": [OutfitType.BIKINI, OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "desert oasis pool with sandstone deck": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.SWIMSUIT, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "backyard pool with inflatable lounger": {
        "types": [OutfitType.SWIMSUIT, OutfitType.BEACH_WEAR, OutfitType.BIKINI],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "hotel courtyard pool with mosaic tiles": {
        "types": [OutfitType.SWIMSUIT, OutfitType.BIKINI, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "natural rock pool at waterfall base": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.SWIMSUIT],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "community pool diving board platform": {
        "types": [OutfitType.BIKINI, OutfitType.BEACH_WEAR, OutfitType.SWIMSUIT],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "indoor spa pool with steam rising": {
        "types": [OutfitType.BIKINI, OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "indoor hotel pool under glass dome": {
        "types": [OutfitType.ATHLEISURE, OutfitType.SWIMSUIT, OutfitType.BIKINI],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "indoor lap pool with lane dividers": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.SWIMSUIT, OutfitType.BIKINI],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "indoor wellness center pool with jets": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BIKINI, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "indoor aquatic center competition pool": {
        "types": [OutfitType.ATHLEISURE, OutfitType.SWIMSUIT, OutfitType.BEACH_WEAR],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "indoor resort pool with palm murals": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR, OutfitType.SWIMSUIT],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "indoor thermal pool with stone walls": {
        "types": [OutfitType.SWIMSUIT, OutfitType.ATHLEISURE, OutfitType.BIKINI],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "indoor gym pool with floor-to-ceiling windows": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR, OutfitType.BIKINI],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "poolside cabana with striped curtains": {
        "types": [OutfitType.BIKINI, OutfitType.SWIMSUIT, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "pool deck with sun loungers and umbrellas": {
        "types": [OutfitType.BIKINI, OutfitType.SWIMSUIT, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "heated outdoor pool in winter steam": {
        "types": [OutfitType.SWIMSUIT, OutfitType.BIKINI, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "kids splash pool with water slides": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BIKINI, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "pool grotto with hidden cave entrance": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BIKINI, OutfitType.SWIMSUIT],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "sunset pool party with floating lights": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BIKINI, OutfitType.SWIMSUIT],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "morning lap swim empty pool lanes": {
        "types": [OutfitType.BIKINI, OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "pool volleyball net over shallow end": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR, OutfitType.BIKINI],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "lazy river pool with inner tubes": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BIKINI, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "poolside bar with tropical cocktails": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BIKINI, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "cliffside pool with glass edge": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.BIKINI],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "villa pool surrounded by olive trees": {
        "types": [OutfitType.BIKINI, OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "beach club pool steps to sand": {
        "types": [OutfitType.BIKINI, OutfitType.ATHLEISURE, OutfitType.SWIMSUIT],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "pool with underwater bench seating": {
        "types": [OutfitType.SWIMSUIT, OutfitType.ATHLEISURE, OutfitType.BIKINI],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "night pool lit with blue led strips": {
        "types": [OutfitType.ATHLEISURE, OutfitType.SWIMSUIT, OutfitType.BIKINI],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "poolside fire pit and lounge chairs": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BIKINI, OutfitType.SWIMSUIT],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "indoor infinity pool with city view": {
        "types": [OutfitType.SWIMSUIT, OutfitType.BIKINI, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "indoor pool with retractable roof open": {
        "types": [OutfitType.BIKINI, OutfitType.SWIMSUIT, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "indoor pool sauna adjacent glass wall": {
        "types": [OutfitType.SWIMSUIT, OutfitType.BIKINI, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "indoor pool with underwater windows": {
        "types": [OutfitType.BIKINI, OutfitType.ATHLEISURE, OutfitType.SWIMSUIT],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "indoor pool at luxury spa retreat": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BIKINI, OutfitType.SWIMSUIT],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "pool deck yoga session at dawn": {
        "types": [OutfitType.BIKINI, OutfitType.SWIMSUIT, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "poolside brunch table with fruit platter": {
        "types": [OutfitType.SWIMSUIT, OutfitType.ATHLEISURE, OutfitType.BIKINI],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "empty pool during maintenance drain": {
        "types": [OutfitType.ATHLEISURE, OutfitType.SWIMSUIT, OutfitType.BIKINI],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "pool with floating breakfast tray": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.SWIMSUIT, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "water polo goals at deep end": {
        "types": [OutfitType.ATHLEISURE, OutfitType.SWIMSUIT, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "pool with bubble jet massage corner": {
        "types": [OutfitType.SWIMSUIT, OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "saltwater pool with ocean breeze": {
        "types": [OutfitType.SWIMSUIT, OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "pool surrounded by tropical garden": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR, OutfitType.SWIMSUIT],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "pool with swim-up tanning ledge": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.SWIMSUIT],
        "location": [LocationType.OUTDOOR, LocationType.POOL],
    },
    "indoor pool with arched brick ceiling": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BIKINI, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },
    "indoor pool with mood lighting strips": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BIKINI, OutfitType.BEACH_WEAR],
        "location": [LocationType.INDOOR, LocationType.POOL],
    },

    # Subway Scenes
    "crowded rush hour subway platform": {
        "types": [OutfitType.STREETWEAR, OutfitType.CYBERPUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "empty late-night subway car interior": {
        "types": [OutfitType.CYBERPUNK, OutfitType.NORMCORE, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "graffiti-covered subway tunnel wall": {
        "types": [OutfitType.GRUNGE, OutfitType.NORMCORE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway turnstile entrance with fluorescent lights": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway escalator descending into depths": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway map wall with route lines": {
        "types": [OutfitType.GRUNGE, OutfitType.CYBERPUNK, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway bench waiting area with ads": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway train doors opening at station": {
        "types": [OutfitType.NORMCORE, OutfitType.CYBERPUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway stairwell with tiled walls": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway token booth vintage counter": {
        "types": [OutfitType.NORMCORE, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway platform edge yellow safety line": {
        "types": [OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway car pole grip standing room": {
        "types": [OutfitType.CYBERPUNK, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway station archway brick ceiling": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway transfer corridor connecting lines": {
        "types": [OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway platform digital countdown board": {
        "types": [OutfitType.NORMCORE, OutfitType.CYBERPUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway tunnel lights stretching to vanishing point": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway station newsstand kiosk": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway emergency exit stairwell": {
        "types": [OutfitType.NORMCORE, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway car window reflection at night": {
        "types": [OutfitType.NORMCORE, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway platform musician busking corner": {
        "types": [OutfitType.STREETWEAR, OutfitType.CYBERPUNK, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway station mosaic tile artwork": {
        "types": [OutfitType.GRUNGE, OutfitType.CYBERPUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway ventilation grate steam rising": {
        "types": [OutfitType.GRUNGE, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway platform rain dripping from ceiling": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway car seats with worn fabric": {
        "types": [OutfitType.NORMCORE, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway station clock above tracks": {
        "types": [OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway platform gap warning signs": {
        "types": [OutfitType.NORMCORE, OutfitType.CYBERPUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway underground shopping arcade entrance": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway station pillar with peeling paint": {
        "types": [OutfitType.CYBERPUNK, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway car handrail chrome reflections": {
        "types": [OutfitType.NORMCORE, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway platform crowd surge at doors": {
        "types": [OutfitType.STREETWEAR, OutfitType.CYBERPUNK, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway station neon line name sign": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway tunnel curve with approaching headlights": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway station wheelchair ramp access": {
        "types": [OutfitType.GRUNGE, OutfitType.CYBERPUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway platform vending machine corner": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway car overhead strap handles": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway station lost and found window": {
        "types": [OutfitType.STREETWEAR, OutfitType.CYBERPUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway platform maintenance workers zone": {
        "types": [OutfitType.GRUNGE, OutfitType.CYBERPUNK, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway station security camera dome": {
        "types": [OutfitType.CYBERPUNK, OutfitType.NORMCORE, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway car floor mosaic pattern": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway platform wind from passing train": {
        "types": [OutfitType.NORMCORE, OutfitType.CYBERPUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway station historic tile lettering": {
        "types": [OutfitType.NORMCORE, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway tunnel emergency phone box": {
        "types": [OutfitType.GRUNGE, OutfitType.NORMCORE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway platform bench with homeless sleeper": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway car digital route display": {
        "types": [OutfitType.NORMCORE, OutfitType.CYBERPUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway station fare card tap gate": {
        "types": [OutfitType.CYBERPUNK, OutfitType.NORMCORE, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway platform puddle reflecting lights": {
        "types": [OutfitType.GRUNGE, OutfitType.NORMCORE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway car corner seat by window": {
        "types": [OutfitType.GRUNGE, OutfitType.CYBERPUNK, OutfitType.NORMCORE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway station construction barricade zone": {
        "types": [OutfitType.NORMCORE, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway tunnel signal light changing": {
        "types": [OutfitType.STREETWEAR, OutfitType.CYBERPUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },
    "subway platform last train announcement board": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.SUBWAY, LocationType.CITY],
    },

    # Airport Scenes
    "departure gate lounge with runway view": {
        "types": [OutfitType.MINIMALIST, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "international terminal check-in counters": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport security screening queue": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "duty-free shopping corridor": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport baggage claim carousel": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport arrival hall with welcome signs": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport moving walkway between terminals": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport business class lounge fireplace": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.AIRPORT],
    },
    "airport customs inspection area": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport jet bridge boarding corridor": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT],
    },
    "airport food court with global cuisine": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport observation deck overlooking tarmac": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT],
    },
    "airport passport control queue lines": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport gate seating rows with charging ports": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport information desk with flight boards": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport VIP lounge with leather chairs": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT],
    },
    "airport terminal glass wall runway sunset": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport luggage trolley parking area": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport currency exchange kiosk": {
        "types": [OutfitType.MINIMALIST, OutfitType.ATHLEISURE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport prayer room quiet corner": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.AIRPORT],
    },
    "airport kids play zone near gate": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport smoking lounge sealed room": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.ATHLEISURE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT],
    },
    "airport lost luggage office counter": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport gate agent boarding podium": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport terminal skylight atrium": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport tram between concourses": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport first class check-in desk": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport gate area with delayed flight screen": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport terminal art installation hall": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport restroom hallway with signage": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT],
    },
    "airport gate window plane pushback view": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport terminal floor directional arrows": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport lounge shower facility": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT],
    },
    "airport terminal newsstand rack": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport gate priority boarding lane": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport terminal empty red-eye hours": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport baggage drop self-service kiosk": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport terminal rain on glass facade": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport lounge buffet spread table": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT],
    },
    "airport terminal connecting flight desk": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport gate area family with strollers": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport terminal construction renovation zone": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport lounge quiet work pod": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.AIRPORT],
    },
    "airport terminal holiday decoration display": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.ATHLEISURE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport gate last call boarding announcement": {
        "types": [OutfitType.MINIMALIST, OutfitType.ATHLEISURE, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport terminal floor seating pods": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport customs declaration form desk": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airport terminal night empty corridors": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },
    "airway bridge window deplaning view": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.AIRPORT],
    },
    "airport terminal sunrise through windows": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.AIRPORT, LocationType.CITY],
    },

    # Train Station Scenes
    "grand Victorian train station hall": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "outdoor platform with overhead wires": {
        "types": [OutfitType.VINTAGE, OutfitType.RETRO, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station clock tower facade": {
        "types": [OutfitType.VINTAGE, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "indoor waiting room with wooden benches": {
        "types": [OutfitType.MINIMALIST, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "platform edge with arriving locomotive": {
        "types": [OutfitType.MINIMALIST, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station ticket office window": {
        "types": [OutfitType.MINIMALIST, OutfitType.VINTAGE, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "covered platform shelter in rain": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station departure board flip display": {
        "types": [OutfitType.VINTAGE, OutfitType.MINIMALIST, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "outdoor platform bench at dusk": {
        "types": [OutfitType.VINTAGE, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station arched glass roof atrium": {
        "types": [OutfitType.VINTAGE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "platform flower vendor cart": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station lost property office": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "outdoor platform snow on tracks": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station first class lounge": {
        "types": [OutfitType.VINTAGE, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "platform gap between train and edge": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station historic tile floor": {
        "types": [OutfitType.MINIMALIST, OutfitType.RETRO, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "outdoor platform autumn leaves on rails": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station news kiosk on concourse": {
        "types": [OutfitType.RETRO, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "platform underpass tunnel connecting tracks": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "outdoor platform sunset golden light": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station luggage cart parking": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "platform with steam-era locomotive": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station cafe counter on concourse": {
        "types": [OutfitType.RETRO, OutfitType.MINIMALIST, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "outdoor platform wind and coat tails": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station information booth": {
        "types": [OutfitType.VINTAGE, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "platform with overhead departure sign": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station grand staircase to platforms": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "outdoor platform fog rolling in": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station bookshop on concourse": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "platform with freight cars in background": {
        "types": [OutfitType.VINTAGE, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station restroom corridor": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "outdoor platform pigeons on bench": {
        "types": [OutfitType.RETRO, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station heritage plaque on wall": {
        "types": [OutfitType.MINIMALIST, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "platform with high-speed train blur": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station waiting room fireplace": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "outdoor platform wildflowers trackside": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station elevator to underground platforms": {
        "types": [OutfitType.VINTAGE, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "platform with vintage luggage stacked": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station art deco lighting fixtures": {
        "types": [OutfitType.RETRO, OutfitType.VINTAGE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "outdoor platform night platform lamps": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.VINTAGE],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station left luggage lockers": {
        "types": [OutfitType.VINTAGE, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "platform with conductor whistle moment": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.VINTAGE, OutfitType.RETRO],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station mezzanine overlooking tracks": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "outdoor platform spring blossom trees": {
        "types": [OutfitType.MINIMALIST, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station bar with stained glass": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "platform with bicycle storage racks": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station quiet early morning concourse": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.RETRO],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "outdoor platform rain on canopy": {
        "types": [OutfitType.RETRO, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },
    "train station historic departure bell": {
        "types": [OutfitType.RETRO, OutfitType.MINIMALIST, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.TRAIN_STATION],
    },
    "outdoor platform last train departure": {
        "types": [OutfitType.VINTAGE, OutfitType.RETRO, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.TRAIN_STATION],
    },

    # Rooftop Scenes
    "downtown rooftop at golden hour with champagne flutes": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rain-slicked city rooftop after a summer storm": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "neon-lit rooftop lounge overlooking midnight skyline": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "minimalist rooftop terrace at dawn with soft fog": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop cocktail party under string lights at dusk": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "windy rooftop helipad at blue hour with city glow": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "snow-dusted penthouse rooftop in winter twilight": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop yoga deck at sunrise above glass towers": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "exclusive rooftop gala under a starlit canopy": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "abandoned rooftop with graffiti and overcast sky": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop pool party at high noon with heat haze": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "quiet rooftop garden escape amid urban sprawl": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop jazz terrace on a humid summer night": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "sleek rooftop bar with chrome railings at sunset": {
        "types": [OutfitType.MINIMALIST, OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop film screening under projector light rain": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "foggy rooftop observation deck at first light": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop champagne brunch on a crisp autumn morning": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "electric rooftop dance floor during a lightning storm": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "penthouse rooftop with infinity edge at twilight": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop farmers market setup in early spring drizzle": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "art deco rooftop terrace during a blood orange sunset": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop speakeasy hidden behind a steel door at night": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop picnic blanket spread under cotton candy clouds": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "industrial rooftop with exposed ducts in harsh noon sun": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop wedding reception under paper lanterns at dusk": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop meditation space with incense at pre-dawn mist": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "city rooftop during a sudden hailstorm and dark clouds": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop vinyl listening lounge on a breezy fall evening": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "glass-walled rooftop atrium open to starry night sky": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop fashion shoot set with wind machines at dawn": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop hot tub steam rising into freezing winter air": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop herb garden with bees on a sunny april afternoon": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop silent disco with colored headphones at midnight": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop overlooking fireworks on new year's eve": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "deserted rooftop parking level at 4am city stillness": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop wine tasting with vineyard crates at golden dusk": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop greenhouse nook dripping with condensation": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop boxing ring under floodlights on a rainy night": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop telescope platform during a lunar eclipse": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop sushi bar with cherry blossom petals drifting": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop skate ramp covered in morning dew and mist": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop charity auction under crystal chandeliers outdoors": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop apiary with beehives on a hazy summer afternoon": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop cinema rooftop with velvet seats at blue hour": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop graffiti mural wall during a paint festival": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop reflecting pool mirroring storm clouds overhead": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop tango floor with candles flickering in wind": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop sunrise coffee ritual above sleeping metropolis": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop laser light show cutting through dense fog": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },
    "rooftop zen rock garden after a gentle spring shower": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.ROOFTOP, LocationType.CITY],
    },

    # Forest Scenes
    "misty ancient forest path at dawn with spiderwebs": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "sun-dappled birch grove in late afternoon light": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "dark pine forest clearing under a full moon": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "enchanted fern canyon after a spring rainfall": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "autumn maple forest with falling crimson leaves": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "moss-covered stone ruins deep in an old growth forest": {
        "types": [OutfitType.GOTHIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "bohemian forest campfire circle at twilight": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "ethereal fog bank drifting through redwood trunks": {
        "types": [OutfitType.ETHEREAL, OutfitType.GOTHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "witch hazel grove during a witching hour drizzle": {
        "types": [OutfitType.GOTHIC, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "wildflower meadow edge bordering a dark oak forest": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "frozen forest stream with icicle-laden branches": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "sunrise light piercing through a dense cedar canopy": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "gothic cathedral of towering hemlock trees at noon": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "bohemian tapestry hung between two forest birches": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "thunderstorm rolling through a valley of spruce": {
        "types": [OutfitType.GOTHIC, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "cottagecore mushroom foraging trail in morning mist": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "bioluminescent forest floor on a humid summer night": {
        "types": [OutfitType.ETHEREAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "abandoned forest chapel overtaken by ivy and vines": {
        "types": [OutfitType.GOTHIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "willow swamp forest with hanging moss at golden hour": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "snow-laden evergreen forest in soft winter silence": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ETHEREAL, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "forest waterfall grotto with rainbow mist at midday": {
        "types": [OutfitType.ETHEREAL, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "gothic ravens circling above a deadwood forest": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "bohemian drum circle deep in a bamboo thicket": {
        "types": [OutfitType.BOHEMIAN, OutfitType.GOTHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "cottagecore picnic blanket under a canopy of leaves": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "ethereal sunbeams through morning fog in an ash forest": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "forest boardwalk through a carnivorous plant bog": {
        "types": [OutfitType.GOTHIC, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "wild blackberry bramble thicket at high summer noon": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "moonlit forest pool reflecting starlight perfectly": {
        "types": [OutfitType.ETHEREAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "cottagecore treehouse village connected by rope bridges": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ETHEREAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "gothic iron gate at the entrance to a forbidden forest": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "bohemian forest festival grounds after the rain": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "ethereal firefly swarm in a humid june evening grove": {
        "types": [OutfitType.ETHEREAL, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "forest hollow with a ring of wild mushrooms at dusk": {
        "types": [OutfitType.GOTHIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "cottagecore herb drying racks among forest pines": {
        "types": [OutfitType.COTTAGECORE, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "gothic cemetery border deep within a yew forest": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "bohemian silk canopy strung between forest maples": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "forest river ford with stepping stones at sunrise": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ETHEREAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "ethereal aurora visible through a break in forest canopy": {
        "types": [OutfitType.ETHEREAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "gothic stone circle hidden in a foggy oak woodland": {
        "types": [OutfitType.GOTHIC, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "cottagecore fairy door carved into an ancient tree trunk": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ETHEREAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "forest fire scar regrowth with vibrant green shoots": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "ethereal frost crystals on every branch at dawn": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "gothic hollow tree trunk altar covered in candle wax": {
        "types": [OutfitType.GOTHIC, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "bohemian forest hot spring surrounded by ferns": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "cottagecore wild bee apiary at the forest edge": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "forest canopy walkway swaying in a windy autumn storm": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "ethereal morning dew on spider silk between trees": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "gothic twisted root archway over a forest trail": {
        "types": [OutfitType.GOTHIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "bohemian forest tea ceremony on a mossy log platform": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },
    "cottagecore lantern-lit forest path during first snowfall": {
        "types": [OutfitType.COTTAGECORE, OutfitType.GOTHIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.FOREST],
    },

    # Mountain Scenes
    "alpine summit at sunrise with cloud sea below": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "rocky mountain trail switchback in afternoon heat": {
        "types": [OutfitType.ATHLEISURE, OutfitType.COTTAGECORE, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "snow-capped peak base camp at blue hour": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain meadow wildflowers at golden hour": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "steep cliff overlook during a dramatic thunderstorm": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain cabin porch with valley view at dusk": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "glacier lake reflection on a windless morning": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "military observation post on a foggy ridge": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain boulder field under harsh midday sun": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "alpine ski lodge deck in fresh powder snowfall": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain pass road at dawn with frost on guardrails": {
        "types": [OutfitType.MILITARY, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "cottagecore mountain herb garden on a terraced slope": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "rocky scree slope during a dust storm": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain waterfall plunge pool in summer shade": {
        "types": [OutfitType.ATHLEISURE, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "high altitude plateau with prayer flags fluttering": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain ridge line hike at sunset with long shadows": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "abandoned mountain bunker entrance overgrown with grass": {
        "types": [OutfitType.MILITARY, OutfitType.COTTAGECORE, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain goat trail along a sheer cliff face": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "cottagecore mountain tea house on a misty morning": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "volcanic mountain crater rim at midday haze": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain river gorge with rapids after spring melt": {
        "types": [OutfitType.ATHLEISURE, OutfitType.COTTAGECORE, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "casual chic mountain overlook cafe at golden hour": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "military training ground on a barren mountain plateau": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain wildflower slope in breezy late spring": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "ice cave entrance at the foot of a glacier": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain cable car station above the cloud line": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "cottagecore mountain barn with hay bales at dawn": {
        "types": [OutfitType.COTTAGECORE, OutfitType.MILITARY, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "rocky mountain col between two storm fronts": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain hot spring pool steaming in winter air": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "alpine lake dock at twilight with mirror stillness": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain rescue helipad on a windswept peak": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "cottagecore mountain orchard in autumn harvest light": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "sheer granite face during a rock climbing session": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain monastery terrace overlooking misty valleys": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "military radar station on a remote snowy summit": {
        "types": [OutfitType.MILITARY, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain wildfire lookout tower at sunset": {
        "types": [OutfitType.MILITARY, OutfitType.COTTAGECORE, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "cottagecore mountain stream crossing with stepping stones": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "alpine tundra plateau under midnight starlight": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain switchback road during a blizzard": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "casual chic mountain vineyard terrace at harvest": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain saddle pass with wild horses grazing": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ATHLEISURE, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "rocky pinnacle summit during a lightning storm": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain railway trestle bridge in morning fog": {
        "types": [OutfitType.MILITARY, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "cottagecore mountain cheese cave entrance at cool dusk": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "high mountain desert plateau with sparse juniper": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain avalanche path through fresh spring snow": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MILITARY, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "casual chic mountain spa deck with panoramic views": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "military mountain bunker complex carved into rock": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "mountain wild thyme slope buzzing with bees at noon": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },
    "alpine star observatory dome on a crystal clear night": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MILITARY, OutfitType.ATHLEISURE],
        "location": [LocationType.OUTDOOR, LocationType.MOUNTAIN],
    },

    # Desert Scenes
    "sun-baked sand dunes at high noon with heat shimmer": {
        "types": [OutfitType.COWBOY, OutfitType.BOHEMIAN, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert canyon slot with red rock walls at dawn": {
        "types": [OutfitType.COWBOY, OutfitType.GRUNGE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "abandoned desert gas station at twilight": {
        "types": [OutfitType.GRUNGE, OutfitType.COWBOY, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "bohemian desert festival camp under a star canopy": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COWBOY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "military desert training ground in dusty wind": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.COWBOY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert oasis palm grove at golden hour": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COWBOY, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "cracked desert salt flat reflecting storm clouds": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "cowboy desert corral at sunrise with dust clouds": {
        "types": [OutfitType.COWBOY, OutfitType.MILITARY, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert ghost town main street in harsh afternoon sun": {
        "types": [OutfitType.GRUNGE, OutfitType.COWBOY, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "bohemian desert yoga circle at sunrise": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COWBOY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "military desert outpost watchtower during sandstorm": {
        "types": [OutfitType.MILITARY, OutfitType.COWBOY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert wildflower superbloom after rare spring rain": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COWBOY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "grunge desert junkyard with rusted cars at dusk": {
        "types": [OutfitType.GRUNGE, OutfitType.COWBOY, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert mesa overlook during a blood red sunset": {
        "types": [OutfitType.COWBOY, OutfitType.BOHEMIAN, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "military desert airstrip at dawn with heat haze": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.COWBOY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "bohemian desert art installation among cacti": {
        "types": [OutfitType.BOHEMIAN, OutfitType.GRUNGE, OutfitType.COWBOY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert riverbed dry wash after flash flood remnants": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "cowboy desert campfire under a milky way sky": {
        "types": [OutfitType.COWBOY, OutfitType.BOHEMIAN, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert volcanic black rock field at midday": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.COWBOY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "bohemian desert textile market in morning shade": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COWBOY, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "grunge desert mine shaft entrance at blue hour": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.COWBOY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert saguaro cactus forest during monsoon lightning": {
        "types": [OutfitType.COWBOY, OutfitType.GRUNGE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "military desert convoy rest stop at noon": {
        "types": [OutfitType.MILITARY, OutfitType.COWBOY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert wind farm turbines on a dusty ridge": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "cowboy desert horse trail through juniper scrub": {
        "types": [OutfitType.COWBOY, OutfitType.MILITARY, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "bohemian desert drum circle at full moon rise": {
        "types": [OutfitType.BOHEMIAN, OutfitType.GRUNGE, OutfitType.COWBOY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert petrified wood field under overcast sky": {
        "types": [OutfitType.GRUNGE, OutfitType.BOHEMIAN, OutfitType.COWBOY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "military desert bunker entrance half buried in sand": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.COWBOY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert hot spring pool steaming at winter dawn": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COWBOY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "cowboy desert saloon porch during a dust devil": {
        "types": [OutfitType.COWBOY, OutfitType.GRUNGE, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "grunge desert radio tower on a lonely hilltop": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert Joshua tree grove at magic hour": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COWBOY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "military desert obstacle course in scorching heat": {
        "types": [OutfitType.MILITARY, OutfitType.COWBOY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert caravan rest stop with woven tents": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COWBOY, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "cowboy desert branding pen at early morning": {
        "types": [OutfitType.COWBOY, OutfitType.MILITARY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "grunge desert highway overpass at midnight": {
        "types": [OutfitType.GRUNGE, OutfitType.COWBOY, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert sandstone arch at sunrise with long shadows": {
        "types": [OutfitType.COWBOY, OutfitType.BOHEMIAN, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "bohemian desert crystal healing circle at dusk": {
        "types": [OutfitType.BOHEMIAN, OutfitType.GRUNGE, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "military desert missile silo hatch in flat terrain": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.COWBOY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert playa lake bed after rain with mirror reflections": {
        "types": [OutfitType.BOHEMIAN, OutfitType.GRUNGE, OutfitType.COWBOY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "cowboy desert windmill pump at golden afternoon": {
        "types": [OutfitType.COWBOY, OutfitType.BOHEMIAN, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "grunge desert scrap metal sculpture garden": {
        "types": [OutfitType.GRUNGE, OutfitType.BOHEMIAN, OutfitType.COWBOY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert nomad camp with camel silhouettes at sunset": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COWBOY, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "military desert radar dome on a rocky outcrop": {
        "types": [OutfitType.MILITARY, OutfitType.COWBOY, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert badlands erosion formations at harsh noon": {
        "types": [OutfitType.GRUNGE, OutfitType.COWBOY, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "cowboy desert rodeo arena under floodlights at night": {
        "types": [OutfitType.COWBOY, OutfitType.GRUNGE, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "bohemian desert silk canopy lounge in afternoon shade": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COWBOY, OutfitType.GRUNGE],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert meteor crater rim during a cold dawn": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "grunge desert abandoned motel pool at twilight": {
        "types": [OutfitType.GRUNGE, OutfitType.BOHEMIAN, OutfitType.COWBOY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },
    "desert cliff dwelling ruins at last light": {
        "types": [OutfitType.COWBOY, OutfitType.BOHEMIAN, OutfitType.MILITARY],
        "location": [LocationType.OUTDOOR, LocationType.DESERT],
    },

    # Garden Scenes
    "english rose garden in full bloom at golden hour": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "japanese zen garden with raked gravel at dawn": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "bohemian wildflower garden with macrame hammocks": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "gothic walled garden with iron gates at twilight": {
        "types": [OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "cottagecore vegetable patch after a spring shower": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "ethereal moonlit garden with white night-blooming flowers": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "romantic garden gazebo draped in wisteria at sunset": {
        "types": [OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "bohemian herb garden with wind chimes at midday": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "cottagecore butterfly garden in summer haze": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "ethereal morning mist in a formal parterre garden": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "romantic garden fountain courtyard during light rain": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "bohemian succulent garden on terracotta steps": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ROMANTIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "cottagecore lavender field border garden at dusk": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "ethereal garden arbor tunnel of blooming jasmine": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "romantic secret garden hidden behind ivy walls": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "bohemian garden tea party setup under cherry blossoms": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ROMANTIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "cottagecore kitchen garden with heirloom tomatoes": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "ethereal garden pond with lily pads at sunrise": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "romantic garden maze center at blue hour": {
        "types": [OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "bohemian mandala flower bed garden in autumn light": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "cottagecore bee garden buzzing at warm afternoon": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "ethereal frost-kissed garden on a cold november morning": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "romantic garden swing beneath an old oak tree": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "bohemian garden fire pit circle at starry night": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "cottagecore potting shed garden corner in spring drizzle": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "ethereal garden with hanging lanterns at twilight": {
        "types": [OutfitType.ETHEREAL, OutfitType.BOHEMIAN, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "romantic topiary garden after a summer storm": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "bohemian xeriscape garden with desert blooms": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "cottagecore herb spiral garden at morning dew": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "ethereal garden sundial casting long shadows at noon": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "romantic garden bridge over a koi stream": {
        "types": [OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "bohemian garden mosaic path through wild grasses": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "cottagecore orchard garden with fallen apple blossoms": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "ethereal garden greenhouse exterior dripping with rain": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "romantic garden pergola covered in climbing roses": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "bohemian garden sculpture park at golden hour": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "cottagecore fairy garden with miniature houses": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "ethereal garden with fireflies on a humid july evening": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "romantic sunken garden terrace at sunset": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "bohemian community garden plot in afternoon sun": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.GARDEN],
    },
    "victorian glass conservatory filled with tropical ferns": {
        "types": [OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.GARDEN],
    },
    "indoor orchid conservatory during a rainy afternoon": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.GARDEN],
    },
    "cottagecore conservatory potting bench in winter warmth": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.GARDEN],
    },
    "ethereal conservatory with stained glass roof at dawn": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.GARDEN],
    },
    "romantic conservatory dinner table among blooming camellias": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.GARDEN],
    },
    "bohemian conservatory lounge with hanging plants": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.GARDEN],
    },
    "indoor palm house conservatory in humid tropical heat": {
        "types": [OutfitType.ETHEREAL, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.GARDEN],
    },
    "cottagecore conservatory seed starting shelves in spring": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.GARDEN],
    },
    "romantic moonlit conservatory with candlelit pathways": {
        "types": [OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.GARDEN],
    },
    "bohemian conservatory art studio surrounded by vines": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.GARDEN],
    },

    # Studio Scenes
    "white cyclorama photography studio with softbox lighting": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "minimalist concrete studio with floor-to-ceiling windows": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "fashion shoot loft with exposed brick and track lights": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "high-key studio with seamless paper backdrop": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "industrial photo studio with metal truss rigging": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "boutique portrait studio with velvet curtains": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "daylight studio with north-facing skylights": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "black box studio with dramatic spotlight": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "editorial studio with geometric prop blocks": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "runway rehearsal space with mirrored wall": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "makeup chair area in backstage studio": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "styling rack corner of a commercial studio": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "green screen studio with chroma key floor": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "vintage film studio with wooden floorboards": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "open-plan creative studio with easels and mannequins": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "sound-dampened studio with acoustic panels": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "gallery-white studio with floating staircase": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "converted warehouse studio with polished concrete": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "sunlit atelier studio with linen drapes": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "moody charcoal studio with single key light": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "pop-up studio inside a renovated factory": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "boutique studio with parquet flooring": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "studio mezzanine overlooking shooting floor": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "infinity cove studio with curved white walls": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "rental studio with rolling wardrobe racks": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "art direction studio cluttered with fabric swatches": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "studio corner with ring light and tripod setup": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "loft studio with exposed ductwork and pendant lamps": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "boutique studio with arched windows and plaster walls": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "studio set with minimalist cube platforms": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "photography studio dressing room with mirrors": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "studio with paper roll backdrops in muted tones": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "creative studio with projection mapping wall": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "studio lounge with mid-century furniture props": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "open studio with polished marble floor": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "studio alcove with sheer diffusion panels": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "fashion studio with garment steamer and irons": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "studio with hanging plants and natural textures": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "compact studio with fold-away backdrop stand": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "studio with checkerboard floor for editorial shoots": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "day-for-night studio with controlled blackout blinds": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "studio with sculptural plinths and pedestals": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "boutique studio with herringbone wood floor": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "studio set dressed with monochrome furniture": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "studio with rolling ladder and prop shelves": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "creative studio with mood boards pinned to walls": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "studio with frosted glass partition and soft glow": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "high-ceiling studio with cable rigging overhead": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "studio corner with vintage camera collection display": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },
    "intimate portrait studio with tufted bench seating": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.STUDIO],
    },

    # Warehouse Scenes
    "abandoned warehouse with broken skylights and dust motes": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "converted warehouse loft with exposed steel beams": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "empty warehouse floor with graffiti-covered walls": {
        "types": [OutfitType.PUNK, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse loading dock with roll-up doors open": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "dim warehouse aisle between towering pallet racks": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse mezzanine overlooking concrete floor": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "spray-painted warehouse with stencil murals": {
        "types": [OutfitType.PUNK, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse corner with stacked shipping containers": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "industrial warehouse with chain-link partitions": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with flickering fluorescent tube lights": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "rain-leaking warehouse with puddles on concrete": {
        "types": [OutfitType.PUNK, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse storage bay with rusted metal shelving": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "open warehouse with forklift and pallet jacks": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse catwalk above factory floor": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "derelict warehouse with shattered windows": {
        "types": [OutfitType.PUNK, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse studio space with cinder block walls": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with corrugated metal walls and oil stains": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "converted warehouse event space with string lights": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse back room with locked chain doors": {
        "types": [OutfitType.PUNK, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with exposed rebar and unfinished columns": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "sprawling warehouse with numbered bay doors": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse corner piled with wooden crates": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with overhead crane and hook chains": {
        "types": [OutfitType.PUNK, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "underground warehouse basement with low ceiling": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with peeling paint and water damage": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse loading ramp with yellow safety stripes": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with tagged roller shutters": {
        "types": [OutfitType.PUNK, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "open warehouse with sawdust and workshop debris": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse corridor with flickering emergency exit sign": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with stacked tires and auto parts": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse loft with rope swings and rigging": {
        "types": [OutfitType.PUNK, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with broken tile floor and rebar showing": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse corner with makeshift skate ramp": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with metal staircase and grated landings": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse bay with morning light through dust": {
        "types": [OutfitType.PUNK, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with hanging industrial lamps": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with pallet fort and stacked boxes": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with exposed brick and iron columns": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse storage with shrink-wrapped pallets": {
        "types": [OutfitType.PUNK, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with oil drum fire pit setup": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with tagged concrete pillars": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse mezzanine with chain-link railing": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with collapsed ceiling tiles": {
        "types": [OutfitType.PUNK, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse corner with welding sparks and tools": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with rain dripping through roof holes": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with numbered storage lockers": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with conveyor belt remnants": {
        "types": [OutfitType.PUNK, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with broken neon sign on wall": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with stacked lumber and sawhorses": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },
    "warehouse with graffiti tunnel connecting bays": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.WAREHOUSE],
    },

    # Church Scenes
    "gothic cathedral nave with stained glass windows": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "stone chapel with candlelit altar": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "abandoned church with ivy creeping through broken windows": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "small country chapel with wooden pews": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "cathedral choir loft with carved wooden railings": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church crypt with vaulted stone ceilings": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "ornate basilica with gilded iconostasis": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "rainy church courtyard with mossy headstones": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church sacristy with embroidered vestments on hooks": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "cathedral transept with rose window light": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "ruined church with collapsed roof beams": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "chapel confessional booth in dim candlelight": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church bell tower with rope and iron bell": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "stone church with arched cloister walkway": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "cathedral side chapel with marble statues": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "village church with whitewashed walls and wildflowers": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church organ loft with towering pipes": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "gothic church with flying buttresses visible outside": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "chapel with flickering votive candles along walls": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "cathedral apse with frescoed ceiling": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church cemetery gate with wrought iron arch": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "stone chapel with leaded glass windows": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church nave with long aisle of wooden pews": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "cathedral baptistery with marble font": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "abandoned chapel overtaken by wild roses": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church vestry with antique mirrors and lace": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "cathedral with incense smoke drifting through light": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "small stone church on a windswept hill": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church crypt with stone sarcophagi": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "gothic chapel with pointed arch doorways": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "cathedral with checkerboard marble floor": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church porch with carved wooden doors": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "chapel altar draped in white linen cloth": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "cathedral with towering ribbed vault ceiling": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "country church with wildflower meadow outside": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church with weathered stone gargoyles overhead": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "cathedral side aisle with dim amber light": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "stone chapel with iron candelabras": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church with hymn books left open on pews": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "cathedral with carved wooden pulpit": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "ruined abbey church with grass growing inside": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "chapel with stained glass casting colored light": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church with stone baptismal pool": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "cathedral triforium gallery overlooking nave": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "small chapel with hand-painted icons": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church with wrought iron chandelier": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "gothic cathedral with lancet windows": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "chapel with velvet kneelers and prie-dieu": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "church with moss-covered stone steps": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },
    "cathedral ambulatory with side chapels": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.CHURCH],
    },

    # Carnival Scenes
    "abandoned carnival midway with rusted ferris wheel": {
        "types": [OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival entrance gate with faded ticket booth": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "neon-lit carnival at night with spinning rides": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival game stalls with stuffed prize walls": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "empty carnival lot with overturned popcorn cart": {
        "types": [OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival carousel with peeling paint horses": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "foggy carnival grounds at dawn": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival funhouse mirror maze entrance": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival bumper car arena with scuffed floor": {
        "types": [OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival food court with cotton candy machines": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "derelict carnival with collapsed tent canvas": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival ring toss alley with blinking lights": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival haunted house facade with painted monsters": {
        "types": [OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival parking lot with striped tents": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival tilt-a-whirl with chipped paint": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival boardwalk with game barkers signs": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival swing ride silhouetted at sunset": {
        "types": [OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival tunnel of love boat channel": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival prize counter with shelves of plush toys": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival shooting gallery with paper targets": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival scrambler ride with centrifugal lights": {
        "types": [OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival ticket wicket with torn banners": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival dunk tank with painted bullseye": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival mirror tent with distorted reflections": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival whack-a-mole booth with worn mallets": {
        "types": [OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival roller coaster track overhead": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival kissing booth with heart-shaped sign": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival ring of fire motorcycle cage": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival balloon dart game wall": {
        "types": [OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival pirate ship ride at full swing": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival fortune teller tent with beaded curtain": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival candy floss stand with pink clouds": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival strength tester hammer game": {
        "types": [OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival log flume splash zone": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival octopus ride with waving arms": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival ticket stub littered pathway": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival ghost train tunnel entrance": {
        "types": [OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival teacup ride with floral patterns": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival ringmaster stage with red curtains": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival bumper boats on murky water": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival zip line tower with safety harnesses": {
        "types": [OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival paintball gallery with splattered targets": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival sideshow banner alley": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival swing boat ride at peak arc": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival ring fire performer platform": {
        "types": [OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival balloon arch entrance tunnel": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival milk bottle toss lane": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival scrambler queue rail with chains": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival after-hours lot with single security light": {
        "types": [OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },
    "carnival ferris wheel gondolas frozen at apex": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.OUTDOOR, LocationType.CARNIVAL],
    },

    # Farm Scenes
    "red barn with open hayloft doors at golden hour": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "wheat field with rolling hills and fence line": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farmhouse porch with rocking chairs and mason jars": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "rustic chicken coop with scattered feed": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "horse stable aisle with wooden stall doors": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm orchard with ladder leaning on apple tree": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "windmill on open prairie with wild grasses": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm tractor parked beside silo at sunrise": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "vegetable garden rows with drip irrigation": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm pond with wooden dock and cattails": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "sheep pasture with split-rail fence": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm milking parlor with stainless tanks": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "cornfield path with towering stalks on both sides": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm equipment shed with rusted tools": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "hay bale stack beside weathered fence post": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm gate with hand-painted welcome sign": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "sunflower field stretching to the horizon": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm chicken yard with wire mesh fencing": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "rustic farmhouse kitchen garden with herbs": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm gravel driveway lined with maple trees": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "pig pen with muddy wallow and trough": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm grain silo with ladder and catwalk": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "wildflower meadow bordering farm pasture": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm apple orchard in autumn leaf fall": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "dairy farm with black and white cows grazing": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm compost pile beside wooden pallets": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "goat pen with climbing platforms and bells": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm windbreak of evergreen trees": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "irrigation canal running through crop rows": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm scarecrow in tattered plaid shirt": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "beehive boxes at edge of clover field": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm wagon with wooden wheels in tall grass": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "chicken run with roosting bars and nesting boxes": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm creek crossing with stone stepping path": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "tobacco drying barn with hanging leaves": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm pumpkin patch in October mist": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "horse paddock with white rail fence": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm tool shed with open door and pitchfork": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "lavender rows on hillside farm plot": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm stone wall bordering sheep meadow": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "rustic farm stand with hand-lettered prices": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm blackberry bramble along fence line": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "cattle pen with metal chute and gate": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm oat field rippling in summer breeze": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "duck pond beside farm barn with reeds": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm herb drying rack in open-air shed": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "peach orchard with wooden picking crates": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm dirt road with tire tracks and dust": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "goose pond at farm edge with cattail fringe": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },
    "farm greenhouse with steamed glass panels": {
        "types": [OutfitType.COWBOY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.FARM],
    },

    # Boat Scenes
    "sun-drenched yacht bow at midday": {
        "types": [OutfitType.PREPPY, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "polished teak deck during golden hour": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "sailboat cockpit with billowing white sails": {
        "types": [OutfitType.PREPPY, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "luxury motor yacht stern lounge at sunset": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "wooden fishing skiff on calm morning water": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "catamaran netting stretched over turquoise sea": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "classic schooner helm with brass instruments": {
        "types": [OutfitType.PREPPY, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "speedboat wake cutting through glassy lake": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "yacht flybridge with champagne bucket at dusk": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "dinghy tied to a mooring buoy at dawn": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "houseboat rooftop deck with potted palms": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "sailboat mast against cloudless summer sky": {
        "types": [OutfitType.PREPPY, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "yacht swim platform with folded diving ladder": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "canal barge deck passing under stone bridge": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "pontoon boat party deck with string lights": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "rowboat drifting through lily-covered pond": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "yacht salon doorway opening to open sea": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "kayak pulled alongside a anchored sailboat": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "wooden sailboat cabin hatch with sea breeze": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "yacht bow rail with distant island horizon": {
        "types": [OutfitType.PREPPY, OutfitType.BEACH_WEAR, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "fishing trawler deck with coiled rope piles": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "sunset cruise deck with jazz quartet corner": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "sailboat tiller with wind-filled mainsail": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "yacht jacuzzi tub on upper deck at twilight": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "narrow canal boat bow with flower boxes": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "motor yacht aft deck with linen-draped table": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "sailboat boom shadow across teak planks": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "party yacht dance floor under starlit sky": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "wooden dory beached beside a dock ladder": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "yacht sun pad with stacked nautical cushions": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "sailboat winch and cleat close-up on deck": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "harbor tour boat upper open-air seating": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "yacht boarding gangway over marina water": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "sloop anchored in a sheltered cove": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "yacht bar counter facing endless ocean": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "sailboat jib unfurling in fresh sea wind": {
        "types": [OutfitType.PREPPY, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "houseboat front porch with rocking chairs": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "yacht helipad edge overlooking blue water": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "fishing boat stern with tackle box open": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "sailboat companionway steps to open deck": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "yacht tender davits with folded life jackets": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "river cruise boat observation deck at noon": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "sailboat pulpit rail with dolphin wake below": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "yacht aft sunshade with wicker lounge set": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "wooden sailboat moored at weathered pier": {
        "types": [OutfitType.PREPPY, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "catamaran trampoline net over splashing waves": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "yacht formal dinner setup on aft deck": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "sailboat masthead view from spreader level": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "houseboat rooftop garden with river sunset": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },
    "yacht swim ladder dangling in crystal water": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BOAT],
    },

    # Garage Scenes
    "oil-stained concrete garage with open bay door": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "cluttered home garage with pegboard tools": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "muscle car garage with chrome engine exposed": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "dim garage lit by single hanging work lamp": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "band practice garage with stacked amplifiers": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "motorcycle garage with leather jacket on peg": {
        "types": [OutfitType.STREETWEAR, OutfitType.PUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "military surplus gear stacked in garage corner": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "graffiti-tagged garage wall behind parked van": {
        "types": [OutfitType.PUNK, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "vintage pickup truck garage with hay bales": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage workbench covered in wrenches and bolts": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "converted garage art studio with spray cans": {
        "types": [OutfitType.PUNK, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "snow-covered garage interior with idling truck": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage loft with ladder and stored surfboards": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "neon sign glow in a late-night garage": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage gym setup with punching bag hanging": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "rusted classic car on jack stands in garage": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage packed with moving boxes and tarps": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "custom chopper build mid-frame in garage": {
        "types": [OutfitType.PUNK, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage floor with tire marks and chalk outlines": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "suburban two-car garage with basketball hoop": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage freezer and camping gear stacked high": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "lowrider garage with hydraulic lift platform": {
        "types": [OutfitType.STREETWEAR, OutfitType.PUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage with chain-link storage cages and bikes": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "industrial garage bay with rolling steel door": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage poker table between parked motorcycles": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "dusty garage attic stairs with cobweb corners": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage stereo blasting beside polished rims": {
        "types": [OutfitType.STREETWEAR, OutfitType.PUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "mechanic garage with hydraulic floor jack": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage mini stage with drum kit and cables": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "overhead garage door half open at dawn": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage shelf lined with paint cans and solvents": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "detailing bay garage with foam cannon setup": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage corner shrine of band posters and stickers": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "military jeep restoration project in garage": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage with fluorescent tubes and concrete stains": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "skateboard ramp folded against garage wall": {
        "types": [OutfitType.STREETWEAR, OutfitType.PUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage kegerator beside tool chest drawers": {
        "types": [OutfitType.PUNK, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "abandoned garage with shattered window panes": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage epoxy floor reflecting overhead lights": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "tactical gear drying on garage clothesline": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage turntable setup between speaker stacks": {
        "types": [OutfitType.PUNK, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "classic hot rod garage with checkered floor": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage welding station with spark-scarred table": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage mini fridge covered in band stickers": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage with snow chains and winter tires stacked": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "low-ceiling garage packed with vintage crates": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage dartboard beside parked dirt bike": {
        "types": [OutfitType.STREETWEAR, OutfitType.PUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage air compressor hissing beside workbench": {
        "types": [OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage loft bed above parked project car": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },
    "garage with open trunk and road trip gear": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.MILITARY],
        "location": [LocationType.INDOOR, LocationType.GARAGE],
    },

    # Basement Scenes
    "unfinished basement with exposed joists and pipes": {
        "types": [OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "cyberpunk basement server room with cable racks": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "gothic basement chapel with candlelit altar": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "punk basement venue with sticker-covered walls": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "floodlit basement laundry room with humming machines": {
        "types": [OutfitType.GRUNGE, OutfitType.CYBERPUNK, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement recording booth with foam panel walls": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "damp basement stone walls with iron support beams": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement gaming den with rgb monitors glowing": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement wine cellar with arched brick ceiling": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "graffiti basement tunnel with flickering bulbs": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement workshop with soldering iron and parts bins": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "creepy basement furnace room with rusted pipes": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement punk show mosh pit under low ceiling": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement fallout shelter stocked with canned goods": {
        "types": [OutfitType.GRUNGE, OutfitType.CYBERPUNK, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "neon-lit basement arcade with vintage cabinets": {
        "types": [OutfitType.CYBERPUNK, OutfitType.PUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement storage maze of labeled cardboard boxes": {
        "types": [OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement occult library with dusty grimoires": {
        "types": [OutfitType.GOTHIC, OutfitType.CYBERPUNK, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement skate ramp with chipped concrete floor": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement boiler room with steam hissing valves": {
        "types": [OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement hacker lab with multiple terminal screens": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement speakeasy bar with brick vault door": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement concrete stairs with peeling paint": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement tattoo parlor with blacklight posters": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement grow room with purple grow lights": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement horror movie set with plastic sheeting": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement drum circle corner with rug and candles": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement electronics graveyard with gutted monitors": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement pool table under bare bulb light": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement crypt-like hallway with stone floor": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement synth studio with analog modular racks": {
        "types": [OutfitType.CYBERPUNK, OutfitType.PUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement flooded corner with standing water": {
        "types": [OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement zine printing press with ink rollers": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement velvet lounge with red low lighting": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement circuit board workbench under magnifier lamp": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement rehearsal space with duct-taped cables": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement crawl space entrance with hanging cobwebs": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement vr rig room with motion capture sensors": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement taxidermy workshop with specimen jars": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement punk zine distro with Xerox machine": {
        "types": [OutfitType.PUNK, OutfitType.CYBERPUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement cold storage room with frosted breath": {
        "types": [OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement candlelit séance circle on concrete floor": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement retro computer museum with beige towers": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement punk merch table with screen-print frames": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement utility sink area with mop and buckets": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement gothic mirror hall with cracked glass": {
        "types": [OutfitType.GOTHIC, OutfitType.CYBERPUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement dj booth with vinyl crates stacked high": {
        "types": [OutfitType.CYBERPUNK, OutfitType.PUNK, OutfitType.GRUNGE],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement storm shelter with metal door and bench": {
        "types": [OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement punk practice space with broken cymbal": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement fiber optic cable hub with blinking nodes": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GRUNGE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },
    "basement root cellar with earthen walls and crates": {
        "types": [OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.PUNK],
        "location": [LocationType.INDOOR, LocationType.BASEMENT],
    },

    # Attic Scenes
    "sunlit attic with sloped ceiling and dormer window": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "dusty attic trunk room with lace doilies": {
        "types": [OutfitType.VINTAGE, OutfitType.COTTAGECORE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "gothic attic nursery with antique rocking horse": {
        "types": [OutfitType.GOTHIC, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "ethereal attic loft with gauze curtains drifting": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "cottagecore attic sewing nook with fabric bolts": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic rafters draped with dried lavender bundles": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "vintage attic dress form beside oval mirror": {
        "types": [OutfitType.VINTAGE, OutfitType.GOTHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic gothic window with rain streaked glass": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic artist garret with easel and skylight": {
        "types": [OutfitType.ETHEREAL, OutfitType.VINTAGE, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic cedar chest overflowing with old letters": {
        "types": [OutfitType.VINTAGE, OutfitType.COTTAGECORE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic fairy light canopy over low beam ceiling": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic taxidermy moth collection in glass cases": {
        "types": [OutfitType.GOTHIC, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic herb drying rack with twine and jars": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic gramophone corner with stacked 78 records": {
        "types": [OutfitType.VINTAGE, OutfitType.GOTHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic moonlit alcove with feather pillow nest": {
        "types": [OutfitType.ETHEREAL, OutfitType.GOTHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic quilt frame with half-finished patchwork": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic gothic portrait gallery leaning on rafters": {
        "types": [OutfitType.GOTHIC, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic telescope pointed through round skylight": {
        "types": [OutfitType.ETHEREAL, OutfitType.VINTAGE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic wicker basket storage with quilted blankets": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic typewriter desk with yellowed manuscript pages": {
        "types": [OutfitType.VINTAGE, OutfitType.GOTHIC, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic candlelit reading nook under angled roof": {
        "types": [OutfitType.GOTHIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic dried flower wreath workshop with scissors": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic vintage hat box collection on wooden floor": {
        "types": [OutfitType.VINTAGE, OutfitType.COTTAGECORE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic cobweb corner with porcelain doll shelf": {
        "types": [OutfitType.GOTHIC, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic sunbeam shaft through dusty air particles": {
        "types": [OutfitType.ETHEREAL, OutfitType.VINTAGE, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic pottery wheel corner with clay splatters": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic steamer trunk labeled with travel stickers": {
        "types": [OutfitType.VINTAGE, OutfitType.ETHEREAL, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic gothic chandelier without power hanging askew": {
        "types": [OutfitType.GOTHIC, OutfitType.VINTAGE, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic dreamcatcher wall with feather mobiles": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic spinning wheel beside basket of raw wool": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic antique vanity with tarnished silver brush set": {
        "types": [OutfitType.VINTAGE, OutfitType.GOTHIC, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic tarot reading table with velvet cloth": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic pressed flower journal desk by window": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic brass bed frame with lace canopy": {
        "types": [OutfitType.VINTAGE, OutfitType.ETHEREAL, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic gothic stained glass fragment on sill": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic mason jar candle-making station with wax": {
        "types": [OutfitType.COTTAGECORE, OutfitType.GOTHIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic vintage camera collection on shelf run": {
        "types": [OutfitType.VINTAGE, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic wind chime corner with open gable vent": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic gothic writing desk with inkwell and quill": {
        "types": [OutfitType.GOTHIC, OutfitType.VINTAGE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic embroidery hoop wall with floral patterns": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic music box shelf with ballerina figurines": {
        "types": [OutfitType.VINTAGE, OutfitType.GOTHIC, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic gossamer fabric draped over exposed beams": {
        "types": [OutfitType.ETHEREAL, OutfitType.GOTHIC, OutfitType.COTTAGECORE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic apothecary shelf with labeled glass bottles": {
        "types": [OutfitType.COTTAGECORE, OutfitType.GOTHIC, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic vintage suitcase tower tied with ribbon": {
        "types": [OutfitType.VINTAGE, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic gothic lace curtain filtering afternoon light": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic watercolor paint set beside open sketchbook": {
        "types": [OutfitType.ETHEREAL, OutfitType.COTTAGECORE, OutfitType.VINTAGE],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic rocking chair with hand-knit throw blanket": {
        "types": [OutfitType.COTTAGECORE, OutfitType.VINTAGE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic gothic birdcage empty beside potted fern": {
        "types": [OutfitType.GOTHIC, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic star chart pinned above narrow writing desk": {
        "types": [OutfitType.ETHEREAL, OutfitType.VINTAGE, OutfitType.GOTHIC],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },
    "attic heirloom quilt draped over wooden ladder": {
        "types": [OutfitType.VINTAGE, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.ATTIC],
    },

    # Balcony Scenes
    "flower-filled balcony overlooking quiet garden": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "minimalist glass balcony with sleek metal railing": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "urban high-rise balcony with skyline at dusk": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "romantic balcony bistro set with candle lanterns": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "casual chic balcony with morning coffee tray": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "parisian wrought-iron balcony with geranium boxes": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "penthouse balcony infinity edge above city lights": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "balcony hammock strung between potted olive trees": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "snow-dusted balcony with steaming mug on rail": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "balcony herb garden with terracotta pots lined up": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "rooftop-adjacent balcony with string light canopy": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "minimalist concrete balcony with single lounge chair": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "balcony champagne toast setup at golden hour": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "coastal balcony with ocean breeze and linen curtains": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "urban apartment balcony crowded with potted succulents": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "balcony yoga mat corner facing sunrise horizon": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "gothic iron balcony overlooking cobblestone street": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "balcony picnic blanket with cheese board spread": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "modern city balcony with floor-to-ceiling glass door": {
        "types": [OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "balcony telescope aimed at night sky above skyline": {
        "types": [OutfitType.ROMANTIC, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "rainy balcony with droplets on glass balustrade": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "balcony formal railing with velvet throw on bench": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "narrow european balcony with laundry lines fluttering": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "balcony fire pit table with city glow beyond": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "balcony reading chair with stacked novels and throw": {
        "types": [OutfitType.MINIMALIST, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "luxury hotel balcony with marble rail and sea view": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "balcony sunset silhouette against warm orange sky": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "urban loft balcony with exposed brick wall edge": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "balcony wind chimes and bamboo screen privacy": {
        "types": [OutfitType.MINIMALIST, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "balcony formal dinner table for two under stars": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "tree-lined balcony overlooking park canopy below": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "midtown balcony with neon signs reflected on glass": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "balcony citrus tree in pot beside wicker loveseat": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "minimalist japanese balcony with stone lantern": {
        "types": [OutfitType.MINIMALIST, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "balcony jazz evening with small speaker and wine": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "wraparound balcony with panoramic mountain view": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "balcony fairy lights draped over railing at night": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "downtown balcony overlooking busy intersection below": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "balcony easel setup painting the view beyond rail": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "balcony brunch spread with fresh pastries and juice": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "skyscraper balcony helipad view at blue hour": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "balcony climbing ivy wall with wooden bench": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "balcony cocktail hour with crystal tumblers lined up": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "suburban balcony with backyard fence view below": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "balcony wind-swept sheer curtains at twilight": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "urban balcony herb drying rack with city haze beyond": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "balcony telescope and star map on small side table": {
        "types": [OutfitType.MINIMALIST, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "corner balcony with L-shaped seating and lanterns": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    "balcony sunrise meditation with incense smoke drifting": {
        "types": [OutfitType.MINIMALIST, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY],
    },
    "historic townhouse balcony above lantern-lit street": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "location": [LocationType.OUTDOOR, LocationType.BALCONY, LocationType.CITY],
    },
    # Sauna scenes
    "finnish cedar sauna with hot stones and tiered wooden benches": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.LINGERIE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "infrared sauna cabin with glowing red heat panels": {
        "types": [OutfitType.ATHLEISURE, OutfitType.LINGERIE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "traditional russian banya with birch whisk bundles on hooks": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.LINGERIE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "hotel sauna with marble tiles and folded white towels": {
        "types": [OutfitType.LINGERIE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.SAUNA, LocationType.HOTEL],
    },
    "dry sauna with eucalyptus oil dispenser on cedar wall": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "steam sauna with misty haze and dim amber lighting": {
        "types": [OutfitType.LINGERIE, OutfitType.BEACH_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "barrel-shaped wooden sauna interior with curved benches": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.COTTAGECORE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "lakeside lodge sauna with knotty pine walls and stone heater": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "luxury spa sauna with heated stone floor and orchid vase": {
        "types": [OutfitType.LINGERIE, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA, LocationType.SPA],
    },
    "co-ed sauna with tiered cedar seating and water bucket": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "private sauna suite with personal ladle and cold shower": {
        "types": [OutfitType.LINGERIE, OutfitType.BEACH_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA, LocationType.SPA],
    },
    "gym sauna with tiled floor and metal towel hooks": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA, LocationType.GYM],
    },
    "scandinavian minimalist sauna with clean lines and pale wood": {
        "types": [OutfitType.MINIMALIST, OutfitType.ATHLEISURE, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "sauna with panoramic window overlooking snowy forest": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.COTTAGECORE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "aromatherapy sauna with lavender steam and soft glow": {
        "types": [OutfitType.ETHEREAL, OutfitType.LINGERIE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA, LocationType.SPA],
    },
    "salt wall sauna with pink himalayan brick panels": {
        "types": [OutfitType.MINIMALIST, OutfitType.LINGERIE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.SAUNA, LocationType.SPA],
    },
    "japanese onsen-style sauna room with bamboo accents": {
        "types": [OutfitType.MINIMALIST, OutfitType.BEACH_WEAR, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "boutique spa sauna with led bench lighting and candles": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA, LocationType.SPA],
    },
    "sauna cooling room with cold plunge tub adjacent": {
        "types": [OutfitType.BIKINI, OutfitType.SWIMSUIT, OutfitType.BEACH_WEAR],
        "location": [LocationType.INDOOR, LocationType.SAUNA, LocationType.SPA],
    },
    "rooftop spa sauna with city skyline through frosted glass": {
        "types": [OutfitType.LINGERIE, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA, LocationType.SPA],
    },
    "rustic log cabin sauna with chinking walls and iron stove": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BEACH_WEAR, OutfitType.COWBOY],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "modern black-tile sauna with led strip bench lighting": {
        "types": [OutfitType.MINIMALIST, OutfitType.LINGERIE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "wellness center sauna with relaxation music speakers": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.BEACH_WEAR],
        "location": [LocationType.INDOOR, LocationType.SAUNA],
    },
    "couples sauna with dual bench levels and dim lanterns": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.BEACH_WEAR],
        "location": [LocationType.INDOOR, LocationType.SAUNA, LocationType.SPA],
    },
    "hammam-style steam sauna with mosaic tile floor": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ETHEREAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SAUNA, LocationType.SPA],
    },
    # Spa scenes
    "luxury spa relaxation lounge with herbal tea station": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa treatment room with massage table and flickering candles": {
        "types": [OutfitType.LINGERIE, OutfitType.ETHEREAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa hydrotherapy pool with jets and mosaic tile walls": {
        "types": [OutfitType.BIKINI, OutfitType.SWIMSUIT, OutfitType.BEACH_WEAR],
        "location": [LocationType.INDOOR, LocationType.SPA, LocationType.POOL],
    },
    "spa mud bath room with warm clay basins and stone walls": {
        "types": [OutfitType.LINGERIE, OutfitType.BEACH_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa aromatherapy bar with essential oil diffusers and herbs": {
        "types": [OutfitType.ETHEREAL, OutfitType.BOHEMIAN, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa zen garden room with raked sand and bamboo screens": {
        "types": [OutfitType.MINIMALIST, OutfitType.ETHEREAL, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa facial treatment room with steamer and vanity mirrors": {
        "types": [OutfitType.LINGERIE, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa nail salon station with plush pedicure chairs": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.LINGERIE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa herbal steam room with mint and eucalyptus vapor": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.LINGERIE, OutfitType.ATHLEISURE],
        "location": [LocationType.INDOOR, LocationType.SPA, LocationType.SAUNA],
    },
    "spa meditation room with floor cushions and incense smoke": {
        "types": [OutfitType.ETHEREAL, OutfitType.BOHEMIAN, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa reception lobby with orchids and trickling water feature": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa locker room with wood lockers and folded robes": {
        "types": [OutfitType.ATHLEISURE, OutfitType.LINGERIE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa couples suite with dual soaking tubs and rose petals": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa reflexology foot bath station with smooth river stones": {
        "types": [OutfitType.LINGERIE, OutfitType.BEACH_WEAR, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa thermal bath with mineral water pools and arched ceilings": {
        "types": [OutfitType.BIKINI, OutfitType.SWIMSUIT, OutfitType.BEACH_WEAR],
        "location": [LocationType.INDOOR, LocationType.SPA, LocationType.POOL],
    },
    "spa yoga retreat studio with bamboo floors and soft light": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BOHEMIAN, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa salt grotto with ambient blue lighting and stalactites": {
        "types": [OutfitType.ETHEREAL, OutfitType.LINGERIE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa float therapy pod room with dim purple glow": {
        "types": [OutfitType.LINGERIE, OutfitType.MINIMALIST, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa champagne lounge with cucumber water pitchers and loungers": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa atrium with living green wall and natural skylight": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BOHEMIAN],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa reflexology lounge with reclining chairs and dim lamps": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa thai massage pavilion with silk drapes and floor mats": {
        "types": [OutfitType.LINGERIE, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa salt scrub station with sea salt jars and warm towels": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.LINGERIE, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa relaxation pod with zero-gravity chairs and headphones": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "spa solarium lounge with heated loungers and glass ceiling": {
        "types": [OutfitType.BIKINI, OutfitType.BEACH_WEAR, OutfitType.LINGERIE],
        "location": [LocationType.INDOOR, LocationType.SPA],
    },
    "hotel spa wellness corridor with eucalyptus scent and robes": {
        "types": [OutfitType.LINGERIE, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "location": [LocationType.INDOOR, LocationType.SPA, LocationType.HOTEL],
    },
}
