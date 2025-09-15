"""
Clothing data definitions for the ComfyUI Outfit Generator.
This file contains clothing items tagged with their compatible outfit types and color palettes.
"""

from ..outfit_types import OutfitType
from ..colors import *

# Bottoms with their compatible outfit types and color palettes
MALE_BOTTOMS = {
    # Formal/Business Pants
    "dress pants": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + BLUES + BROWNS + ["pinstripe", "tailored", "wool"]
    },
    "suit trousers": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + GRAYS + BLUES + BROWNS + ["matching set", "pressed", "wool blend"]
    },
    "tuxedo pants": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": BLACKS + ["midnight blue", "satin stripe", "formal"]
    },
    "pleated pants": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.RETRO],
        "colors": GRAYS + BROWNS + BLUES + ["high-waisted", "classic fit", "wool"]
    },
    "flat-front pants": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + GRAYS + BLUES + BROWNS + ["slim fit", "modern cut"]
    },
    "wool trousers": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "colors": GRAYS + BROWNS + BLUES + ["flannel", "worsted wool", "classic"]
    },
    
    # Casual Pants
    "jeans": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.GRUNGE, OutfitType.COWBOY, OutfitType.STREETWEAR],
        "colors": ["denim", "black denim", "white denim", "distressed", "ripped", "high-waisted", "vintage wash"]
    },
    "skinny jeans": {
        "types": [OutfitType.STREETWEAR, OutfitType.PUNK, OutfitType.ROCKABILLY],
        "colors": ["black denim", "dark wash", "ripped", "tight fit"]
    },
    "straight leg jeans": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.MINIMALIST],
        "colors": ["classic denim", "dark wash", "medium wash", "vintage"]
    },
    "bootcut jeans": {
        "types": [OutfitType.COWBOY, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": ["dark denim", "medium wash", "slightly flared"]
    },
    "wide leg jeans": {
        "types": [OutfitType.STREETWEAR, OutfitType.RETRO, OutfitType.AVANT_GARDE],
        "colors": ["baggy fit", "90s style", "loose denim"]
    },
    "ripped jeans": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "colors": ["distressed", "heavily ripped", "punk style"]
    },
    "chinos": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "colors": BROWNS + GREENS + BLUES + GRAYS + ["khaki", "cotton twill", "slim fit"]
    },
    "khakis": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "colors": BROWNS + ["tan", "beige", "classic khaki", "cotton"]
    },
    "corduroy pants": {
        "types": [OutfitType.PREPPY, OutfitType.RETRO, OutfitType.COTTAGECORE],
        "colors": BROWNS + GREENS + BLUES + ["ribbed texture", "vintage style"]
    },
    "cargo pants": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": GREENS + BROWNS + BLACKS + ["utility pockets", "tactical", "baggy"]
    },
    "joggers": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": GRAYS + BLACKS + BLUES + ["fleece", "sweatpant style", "tapered"]
    },
    "sweatpants": {
        "types": [OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "colors": GRAYS + BLACKS + BLUES + ["fleece", "loose fit", "comfort"]
    },
    "track pants": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.RETRO],
        "colors": BLACKS + BLUES + REDS + ["side stripe", "athletic", "vintage"]
    },
    
    # Shorts
    "dress shorts": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR],
        "colors": BLUES + BROWNS + GREENS + ["tailored", "above knee", "cotton"]
    },
    "chino shorts": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR],
        "colors": BROWNS + GREENS + BLUES + WHITES + ["khaki", "cotton twill"]
    },
    "denim shorts": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.GRUNGE],
        "colors": ["denim", "distressed", "cut-off", "vintage wash"]
    },
    "cargo shorts": {
        "types": [OutfitType.MILITARY, OutfitType.NORMCORE, OutfitType.BEACH_WEAR],
        "colors": GREENS + BROWNS + BLACKS + ["utility pockets", "relaxed fit"]
    },
    "athletic shorts": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR],
        "colors": BLACKS + BLUES + REDS + NEONS + ["moisture-wicking", "lightweight"]
    },
    "board shorts": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLUES + GREENS + ["tropical prints", "quick-dry", "surf style"]
    },
    "swim trunks": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLUES + GREENS + REDS + ["solid colors", "tropical prints", "mesh lining"]
    },
    "running shorts": {
        "types": [OutfitType.ATHLEISURE],
        "colors": BLACKS + BLUES + NEONS + ["lightweight", "split hem", "performance"]
    },
    "basketball shorts": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "colors": BLACKS + BLUES + REDS + ["mesh", "baggy", "team colors"]
    },
    
    # Alternative/Subculture
    "leather pants": {
        "types": [OutfitType.PUNK, OutfitType.ROCKABILLY, OutfitType.GOTHIC],
        "colors": BLACKS + BROWNS + ["tight fit", "motorcycle style", "patent leather"]
    },
    "vinyl pants": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "colors": BLACKS + ["shiny", "tight fit", "fetish style"]
    },
    "bondage pants": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC],
        "colors": BLACKS + ["straps", "D-rings", "chains", "punk style"]
    },
    "ripped leather pants": {
        "types": [OutfitType.PUNK, OutfitType.ROCKABILLY],
        "colors": BLACKS + ["distressed", "torn", "edgy"]
    },
    "mesh pants": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + ["see-through", "layering piece", "industrial"]
    },
    
    # Specialty/Themed
    "western jeans": {
        "types": [OutfitType.COWBOY, OutfitType.ROCKABILLY],
        "colors": ["classic denim", "bootcut", "vintage wash", "rodeo style"]
    },
    "wrangler jeans": {
        "types": [OutfitType.COWBOY, OutfitType.NORMCORE],
        "colors": ["authentic denim", "working cowboy", "classic fit"]
    },
    "military fatigues": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR],
        "colors": GREENS + ["camouflage", "BDU style", "tactical"]
    },
    "camouflage pants": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "colors": GREENS + BROWNS + ["woodland camo", "digital camo", "urban camo"]
    },
    "paratrooper pants": {
        "types": [OutfitType.MILITARY, OutfitType.PUNK, OutfitType.STREETWEAR],
        "colors": GREENS + BLACKS + ["cargo pockets", "utility", "combat style"]
    },
    
    # Formal Variations
    "morning dress trousers": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": GRAYS + ["striped", "formal", "traditional"]
    },
    "white tie trousers": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": BLACKS + ["satin stripe", "formal", "tailcoat companion"]
    },
    "dinner suit trousers": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": BLACKS + ["midnight blue", "silk stripe", "formal"]
    },
    
    # Tech/Modern
    "tech pants": {
        "types": [OutfitType.MINIMALIST, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "colors": BLACKS + GRAYS + ["technical fabric", "water-resistant", "minimal"]
    },
    "compression leggings": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CYBERPUNK],
        "colors": BLACKS + GRAYS + ["performance fabric", "fitted", "athletic"]
    },
    "performance pants": {
        "types": [OutfitType.ATHLEISURE],
        "colors": BLACKS + GRAYS + BLUES + ["moisture-wicking", "stretch", "athletic"]
    },
    
    # Vintage/Retro
    "high-waisted jeans": {
        "types": [OutfitType.RETRO, OutfitType.STREETWEAR, OutfitType.ROCKABILLY],
        "colors": ["vintage denim", "90s style", "mom jeans"]
    },
    "bell-bottom jeans": {
        "types": [OutfitType.RETRO, OutfitType.BOHEMIAN],
        "colors": ["flared", "70s style", "vintage wash"]
    },
    "vintage chinos": {
        "types": [OutfitType.RETRO, OutfitType.PREPPY],
        "colors": BROWNS + GREENS + ["classic cut", "vintage style"]
    },
    "sailor pants": {
        "types": [OutfitType.RETRO, OutfitType.MINIMALIST],
        "colors": WHITES + BLUES + ["wide leg", "nautical", "button front"]
    },
    
    # Unique/Statement
    "drop-crotch pants": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.STREETWEAR],
        "colors": BLACKS + GRAYS + ["low crotch", "baggy", "modern"]
    },
    "harem pants": {
        "types": [OutfitType.BOHEMIAN, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "colors": EARTH_TONES + JEWEL_TONES + ["flowing", "loose fit", "ethnic"]
    },
    "asymmetric pants": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK],
        "colors": BLACKS + WHITES + ["uneven hem", "architectural", "modern"]
    },
    "layered pants": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.GOTHIC],
        "colors": BLACKS + ["multiple layers", "deconstructed", "complex"]
    },
    "convertible pants": {
        "types": [OutfitType.MINIMALIST, OutfitType.CYBERPUNK],
        "colors": BLACKS + GRAYS + ["zip-off legs", "functional", "technical"]
    },
    
    # Seasonal
    "thermal underwear": {
        "types": [OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "colors": GRAYS + WHITES + BLACKS + ["base layer", "long johns", "thermal"]
    },
    "fleece pants": {
        "types": [OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "colors": GRAYS + BLACKS + BLUES + ["warm", "soft", "casual"]
    },
    "snow pants": {
        "types": [OutfitType.ATHLEISURE],
        "colors": BLACKS + BLUES + GRAYS + ["waterproof", "insulated", "ski wear"]
    },
    
    # Workwear
    "work pants": {
        "types": [OutfitType.NORMCORE, OutfitType.MILITARY],
        "colors": BROWNS + BLUES + BLACKS + ["durable", "heavy-duty", "utility"]
    },
    "carpenter pants": {
        "types": [OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "colors": BROWNS + BLUES + ["tool pockets", "hammer loop", "workwear"]
    },
    "coverall pants": {
        "types": [OutfitType.NORMCORE, OutfitType.MINIMALIST],
        "colors": BLUES + GREENS + BLACKS + ["work wear", "industrial", "utility"]
    },
    
    # Lounge/Comfort
    "pajama pants": {
        "types": [OutfitType.NORMCORE],
        "colors": BLUES + GRAYS + ["soft", "comfortable", "loungewear"]
    },
    "lounge pants": {
        "types": [OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "colors": GRAYS + BLACKS + BLUES + ["comfortable", "relaxed fit", "casual"]
    },
    "sleep shorts": {
        "types": [OutfitType.NORMCORE],
        "colors": BLUES + GRAYS + ["comfortable", "lightweight", "loungewear"]
    }
}

