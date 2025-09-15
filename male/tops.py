"""
Clothing data definitions for the ComfyUI Outfit Generator.
This file contains clothing items tagged with their compatible outfit types and color palettes.
"""

from ..outfit_types import OutfitType
from ..colors import *


# Tops with their compatible outfit types and color palettes
MALE_TOPS = {
    # Formal/Business
    "blazer": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + BLUES + BROWNS + ["pinstripe", "herringbone", "tweed"]
    },
    "dress shirt": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.EVENING_FORMAL],
        "colors": WHITES + BLUES + ["pinstripe", "checked", "French cuffs"]
    },
    "button-down shirt": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "colors": WHITES + BLUES + PASTELS + ["classic cotton", "crisp", "Oxford"]
    },
    "tuxedo shirt": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": WHITES + ["wing collar", "pleated front", "bow tie ready"]
    },
    "waistcoat": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.STEAMPUNK],
        "colors": BLACKS + GRAYS + BROWNS + ["brocade", "silk", "velvet"]
    },
    "tuxedo": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": BLACKS + ["midnight blue", "classic", "shawl lapel"],
        "fullBody": True
    },
    "three-piece suit": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + GRAYS + BLUES + BROWNS + ["pinstripe", "wool"],
        "fullBody": True
    },
    "morning coat": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": GRAYS + BLACKS + ["traditional", "tailcoat style"]
    },
    
    # Casual Shirts
    "polo shirt": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "colors": WHITES + BLUES + GREENS + REDS + ["classic fit", "pique cotton"]
    },
    "t-shirt": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "colors": WHITES + BLACKS + GRAYS + BLUES + REDS + ["cotton", "basic"]
    },
    "graphic t-shirt": {
        "types": [OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.GRUNGE],
        "colors": BLACKS + WHITES + GRAYS + ["vintage print", "band tee", "logo"]
    },
    "henley shirt": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.MINIMALIST],
        "colors": WHITES + GRAYS + BLUES + GREENS + ["ribbed", "long sleeve"]
    },
    "crew neck sweater": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "colors": BLUES + GRAYS + BROWNS + GREENS + ["wool", "cashmere", "cable knit"]
    },
    "v-neck sweater": {
        "types": [OutfitType.PREPPY, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLUES + GRAYS + BROWNS + GREENS + ["merino wool", "lightweight"]
    },
    "cardigan": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "colors": GRAYS + BLUES + BROWNS + GREENS + ["button-up", "wool blend"]
    },
    "turtleneck": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.AVANT_GARDE],
        "colors": BLACKS + GRAYS + WHITES + BLUES + ["fitted", "wool", "cashmere"]
    },
    "flannel shirt": {
        "types": [OutfitType.GRUNGE, OutfitType.NORMCORE, OutfitType.COTTAGECORE],
        "colors": REDS + BLUES + GREENS + BROWNS + ["plaid", "checkered", "brushed cotton"]
    },
    "denim shirt": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "colors": BLUES + ["chambray", "classic denim", "faded", "dark wash"]
    },
    "linen shirt": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.MINIMALIST],
        "colors": WHITES + BLUES + EARTH_TONES + ["breathable", "relaxed fit"]
    },
    
    # Athletic/Casual
    "tank top": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": WHITES + BLACKS + GRAYS + BLUES + ["ribbed", "muscle tee"]
    },
    "athletic tank": {
        "types": [OutfitType.ATHLEISURE],
        "colors": BLACKS + GRAYS + BLUES + NEONS + ["moisture-wicking", "performance"]
    },
    "compression shirt": {
        "types": [OutfitType.ATHLEISURE],
        "colors": BLACKS + GRAYS + BLUES + ["fitted", "performance fabric"]
    },
    "mesh tank": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "colors": BLACKS + WHITES + NEONS + ["breathable", "athletic"]
    },
    "performance t-shirt": {
        "types": [OutfitType.ATHLEISURE],
        "colors": GRAYS + BLUES + BLACKS + NEONS + ["moisture-wicking", "quick-dry"]
    },
    "workout hoodie": {
        "types": [OutfitType.ATHLEISURE],
        "colors": GRAYS + BLACKS + BLUES + ["zip-up", "performance fabric"]
    },
    
    # Outerwear
    "hoodie": {
        "types": [OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "colors": GRAYS + BLACKS + BLUES + REDS + ["pullover", "zip-up", "fleece"]
    },
    "sweatshirt": {
        "types": [OutfitType.NORMCORE, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "colors": GRAYS + BLACKS + BLUES + ["crew neck", "vintage", "oversized"]
    },
    "bomber jacket": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.MILITARY],
        "colors": BLACKS + GREENS + BLUES + ["satin", "MA-1 style", "leather"]
    },
    "leather jacket": {
        "types": [OutfitType.PUNK, OutfitType.ROCKABILLY, OutfitType.STREETWEAR],
        "colors": BLACKS + BROWNS + ["motorcycle style", "bomber", "vintage"]
    },
    "denim jacket": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.GRUNGE],
        "colors": BLUES + ["classic", "distressed", "vintage wash", "dark denim"]
    },
    "peacoat": {
        "types": [OutfitType.PREPPY, OutfitType.MILITARY, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + BLUES + GRAYS + ["double-breasted", "wool", "navy style"]
    },
    "trench coat": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "colors": BROWNS + BLACKS + GRAYS + ["classic", "belted", "khaki"]
    },
    "parka": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": GREENS + BLACKS + BROWNS + ["hooded", "fur trim", "utility"]
    },
    "windbreaker": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": BLACKS + BLUES + NEONS + ["lightweight", "packable", "colorblock"]
    },
    "track jacket": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.RETRO],
        "colors": BLACKS + BLUES + REDS + ["striped", "vintage", "zip-up"]
    },
    
    # Alternative/Subculture
    "band t-shirt": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "colors": BLACKS + GRAYS + ["vintage", "distressed", "tour merch"]
    },
    "mesh shirt": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + ["see-through", "industrial", "layering"]
    },
    "fishnet top": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + ["open weave", "layering piece"]
    },
    "studded vest": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.ROCKABILLY],
        "colors": BLACKS + ["metal studs", "leather", "denim"]
    },
    "harness": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "colors": BLACKS + ["leather", "straps", "buckles"]
    },
    "corset": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.AVANT_GARDE],
        "colors": BLACKS + REDS + PURPLES + ["lace-up", "brocade", "leather"]
    },
    
    # Specialty/Themed
    "western shirt": {
        "types": [OutfitType.COWBOY, OutfitType.ROCKABILLY],
        "colors": BLUES + REDS + BROWNS + ["pearl snaps", "embroidered", "denim"]
    },
    "hawaiian shirt": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.RETRO, OutfitType.FESTIVAL],
        "colors": ["tropical print", "floral", "bright colors", "vintage"]
    },
    "utility vest": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "colors": GREENS + BLACKS + BROWNS + ["multiple pockets", "tactical"]
    },
    "cargo vest": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "colors": GREENS + BLACKS + BROWNS + ["utility pockets", "tactical"]
    },
    "muscle shirt": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR, OutfitType.NORMCORE],
        "colors": WHITES + GRAYS + BLACKS + ["fitted", "sleeveless"]
    },
    "rugby shirt": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": BLUES + GREENS + REDS + ["striped", "collar", "heavyweight"]
    },
    "letterman jacket": {
        "types": [OutfitType.PREPPY, OutfitType.RETRO, OutfitType.STREETWEAR],
        "colors": BLUES + REDS + GREENS + ["varsity", "patches", "wool sleeves"]
    },
    "varsity jacket": {
        "types": [OutfitType.PREPPY, OutfitType.RETRO, OutfitType.STREETWEAR],
        "colors": BLUES + REDS + GREENS + ["team colors", "patches", "satin"]
    },
    
    # Tech/Modern
    "smart casual shirt": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "colors": WHITES + GRAYS + BLUES + ["wrinkle-free", "stretch fabric"]
    },
    "tech hoodie": {
        "types": [OutfitType.STREETWEAR, OutfitType.CYBERPUNK, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + ["technical fabric", "minimal design"]
    },
    "moisture-wicking polo": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "colors": WHITES + BLUES + GRAYS + ["performance fabric", "quick-dry"]
    },
    
    # Vintage/Retro
    "bowling shirt": {
        "types": [OutfitType.RETRO, OutfitType.ROCKABILLY, OutfitType.CASUAL_CHIC],
        "colors": ["two-tone", "vintage patterns", "camp collar"]
    },
    "camp collar shirt": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR],
        "colors": WHITES + BLUES + ["tropical prints", "relaxed fit"]
    },
    "vintage band tee": {
        "types": [OutfitType.GRUNGE, OutfitType.RETRO, OutfitType.STREETWEAR],
        "colors": ["faded black", "vintage wash", "distressed"]
    },
    "ringer tee": {
        "types": [OutfitType.RETRO, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "colors": WHITES + ["contrasting trim", "vintage style"]
    },
    
    # Formal Variations
    "morning dress": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": GRAYS + BLACKS + ["traditional", "cutaway coat"],
        "fullBody": True
    },
    "dinner jacket": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": BLACKS + ["midnight blue", "shawl lapel", "silk facings"]
    },
    "smoking jacket": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + PURPLES + ["velvet", "quilted", "luxury"]
    },
    
    # Seasonal
    "thermal shirt": {
        "types": [OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "colors": GRAYS + WHITES + BLACKS + ["ribbed", "long sleeve", "base layer"]
    },
    "long sleeve tee": {
        "types": [OutfitType.NORMCORE, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "colors": WHITES + BLACKS + GRAYS + BLUES + ["cotton", "basic"]
    },
    "sleeveless hoodie": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "colors": GRAYS + BLACKS + ["cut-off", "urban style"]
    },
    
    # Unique/Statement
    "asymmetric top": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK],
        "colors": BLACKS + WHITES + ["architectural", "modern cut"]
    },
    "geometric print shirt": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST],
        "colors": BLACKS + WHITES + ["abstract patterns", "modern"]
    },
    "color-block sweater": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": ["contrasting panels", "modern", "geometric"]
    },
    "oversized blazer": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + ["relaxed fit", "modern cut"]
    },
    "cropped sweater": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.STREETWEAR],
        "colors": BLACKS + GRAYS + PASTELS + ["short length", "modern"]
    },
    "sheer shirt": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CLUB_PARTY, OutfitType.GOTHIC],
        "colors": BLACKS + WHITES + ["transparent", "layering piece"]
    },
    "metallic shirt": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE],
        "colors": METALLICS + ["shiny", "futuristic", "party wear"]
    },
    "chain mail top": {
        "types": [OutfitType.CYBERPUNK, OutfitType.PUNK, OutfitType.AVANT_GARDE],
        "colors": METALLICS + ["metal links", "industrial", "armor-inspired"]
    },
    
    # Full Body Options
    "jumpsuit": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "colors": BLACKS + GRAYS + BLUES + GREENS + ["one-piece", "utilitarian"],
        "fullBody": True
    },
    "coveralls": {
        "types": [OutfitType.NORMCORE, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "colors": BLUES + GREENS + BLACKS + ["work wear", "utility"],
        "fullBody": True
    },
    "boilersuit": {
        "types": [OutfitType.MINIMALIST, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "colors": BLACKS + GRAYS + BLUES + ["industrial", "one-piece"],
        "fullBody": True
    },
    "flight suit": {
        "types": [OutfitType.MILITARY, OutfitType.CYBERPUNK, OutfitType.STREETWEAR],
        "colors": GREENS + BLACKS + ["tactical", "pilot style"],
        "fullBody": True
    }
}
