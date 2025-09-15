"""
Clothing data definitions for the ComfyUI Outfit Generator.
This file contains clothing items tagged with their compatible outfit types and color palettes.
"""

from ..outfit_types import OutfitType
from ..colors import *

# Bottoms with their compatible outfit types and color palettes
FEMALE_BOTTOMS = {
    "jeans": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.GRUNGE, OutfitType.COWBOY, OutfitType.STREETWEAR],
        "colors": ["denim", "black denim", "white denim", "distressed", "ripped", "high-waisted"]
    },
    "dress pants": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + BLUES + BROWNS + ["pinstripe", "tailored"]
    },
    "pencil skirt": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PIN_UP, OutfitType.RETRO],
        "colors": BLACKS + GRAYS + REDS + ["leather", "high-waisted"]
    },
    "midi skirt": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.RETRO, OutfitType.MINIMALIST],
        "colors": PASTELS + EARTH_TONES + PATTERNS + ["A-line", "pleated"]
    },
    "maxi skirt": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.BEACH_WEAR],
        "colors": EARTH_TONES + JEWEL_TONES + ["flowing", "tiered", "floral print"]
    },
    "mini skirt": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.KAWAII],
        "colors": BLACKS + METALLICS + NEONS + ["leather", "plaid", "sequined"]
    },
    "leggings": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.GOTHIC],
        "colors": BLACKS + GRAYS + NEONS + ["metallic", "mesh panels", "high-waisted"]
    },
    "cargo pants": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.CYBERPUNK, OutfitType.GRUNGE],
        "colors": GREENS + BLACKS + GRAYS + ["camouflage", "utility pockets"]
    },
    "leather pants": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.CLUB_PARTY],
        "colors": BLACKS + BROWNS + ["studded", "tight-fitting"]
    },
    "chinos": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "colors": BROWNS + BLUES + GREENS + ["khaki", "tailored"]
    },
    "joggers": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": BLACKS + GRAYS + NEONS + ["tapered", "drawstring"]
    },
    "board shorts": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLUES + NEONS + ["tropical print", "quick-dry"]
    },
    "bell-bottoms": {
        "types": [OutfitType.BOHEMIAN, OutfitType.RETRO, OutfitType.FESTIVAL],
        "colors": ["denim", "corduroy"] + EARTH_TONES + ["flared"]
    },
    "high-waisted shorts": {
        "types": [OutfitType.PIN_UP, OutfitType.RETRO, OutfitType.FESTIVAL, OutfitType.KAWAII],
        "colors": PASTELS + REDS + ["denim", "polka dots", "gingham"]
    },
    "bondage pants": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "colors": BLACKS + ["chains", "straps", "zippers"]
    },
    "tutu skirt": {
        "types": [OutfitType.LOLITA, OutfitType.KAWAII, OutfitType.ETHEREAL],
        "colors": PASTELS + WHITES + ["tulle", "layered", "puffy"]
    },
    
    # TROUSERS & PANTS
    "straight-leg trousers": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + BLUES + BROWNS + ["tailored", "pressed"]
    },
    "wide-leg trousers": {
        "types": [OutfitType.BOHEMIAN, OutfitType.RETRO, OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "colors": BLACKS + EARTH_TONES + JEWEL_TONES + ["flowing", "dramatic"]
    },
    "bootcut pants": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.COWBOY],
        "colors": BLACKS + BROWNS + BLUES + ["denim", "flared hem"]
    },
    "flared pants": {
        "types": [OutfitType.BOHEMIAN, OutfitType.RETRO, OutfitType.FESTIVAL],
        "colors": EARTH_TONES + ["corduroy", "wide flare", "bell-bottom style"]
    },
    "skinny pants": {
        "types": [OutfitType.STREETWEAR, OutfitType.PUNK, OutfitType.CASUAL_CHIC, OutfitType.GOTHIC],
        "colors": BLACKS + GRAYS + ["tight-fitting", "stretchy"]
    },
    "cigarette pants": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.RETRO],
        "colors": BLACKS + GRAYS + BLUES + ["slim-fit", "ankle-length"]
    },
    "cropped trousers": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.PREPPY],
        "colors": PASTELS + EARTH_TONES + ["ankle-length", "tapered"]
    },
    "ankle pants": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + BLUES + ["fitted", "cropped"]
    },
    "capris": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": PASTELS + WHITES + ["mid-calf", "stretchy"]
    },
    "gaucho pants": {
        "types": [OutfitType.BOHEMIAN, OutfitType.RETRO, OutfitType.FESTIVAL],
        "colors": EARTH_TONES + ["wide-leg", "cropped", "flowing"]
    },
    "palazzo pants": {
        "types": [OutfitType.BOHEMIAN, OutfitType.BEACH_WEAR, OutfitType.EVENING_FORMAL],
        "colors": EARTH_TONES + JEWEL_TONES + ["wide-leg", "flowing", "dramatic"]
    },
    "pegged trousers": {
        "types": [OutfitType.RETRO, OutfitType.ROCKABILLY, OutfitType.AVANT_GARDE],
        "colors": BLACKS + GRAYS + ["tapered", "high-waisted"]
    },
    "paperbag waist trousers": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.ROMANTIC],
        "colors": EARTH_TONES + PASTELS + ["high-waisted", "belted", "gathered"]
    },
    "pleated trousers": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.RETRO, OutfitType.PREPPY],
        "colors": GRAYS + BLUES + BROWNS + ["pressed", "formal"]
    },
    "tailored slacks": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + BLUES + BROWNS + ["fitted", "pressed"]
    },
    "chino pants": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "colors": BROWNS + BLUES + GREENS + ["khaki", "cotton", "tailored"]
    },
    "corduroy pants": {
        "types": [OutfitType.RETRO, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + EARTH_TONES + ["textured", "ribbed"]
    },
    "linen trousers": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "colors": WHITES + EARTH_TONES + PASTELS + ["breathable", "relaxed"]
    },
    "high-waisted trousers": {
        "types": [OutfitType.RETRO, OutfitType.PIN_UP, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + GRAYS + REDS + ["fitted", "vintage-style"]
    },
    "low-rise trousers": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.CLUB_PARTY],
        "colors": BLACKS + GRAYS + ["hip-hugger", "fitted"]
    },
    
    # CARGO & UTILITY PANTS
    "cargo pants classic": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "colors": GREENS + BLACKS + GRAYS + ["camouflage", "utility pockets", "baggy"]
    },
    "cargo pants slim-fit": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.CYBERPUNK],
        "colors": BLACKS + GRAYS + ["fitted", "multiple pockets"]
    },
    "utility pants with straps": {
        "types": [OutfitType.CYBERPUNK, OutfitType.PUNK, OutfitType.AVANT_GARDE],
        "colors": BLACKS + ["straps", "buckles", "tactical"]
    },
    "carpenter pants": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": BROWNS + BLUES + ["tool loops", "utility pockets"]
    },
    "painter's pants": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": WHITES + ["paint-splattered", "utility pockets"]
    },
    "military fatigues": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "colors": GREENS + ["camouflage", "combat-style", "tactical"]
    },
    "parachute pants": {
        "types": [OutfitType.STREETWEAR, OutfitType.CLUB_PARTY, OutfitType.RETRO],
        "colors": NEONS + METALLICS + ["baggy", "reflective", "windbreaker material"]
    },
    
    # ATHLETIC & CASUAL PANTS
    "track pants": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": BLACKS + GRAYS + NEONS + ["side stripes", "elastic waist"]
    },
    "tearaway track pants": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.CLUB_PARTY],
        "colors": NEONS + BLACKS + ["snap buttons", "removable"]
    },
    "sweatpants classic": {
        "types": [OutfitType.ATHLEISURE, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "colors": GRAYS + BLACKS + ["fleece", "drawstring", "relaxed"]
    },
    "oversized sweatpants": {
        "types": [OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "colors": GRAYS + BLACKS + PASTELS + ["baggy", "oversized fit"]
    },
    "slim-fit sweatpants": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "colors": BLACKS + GRAYS + ["tapered", "fitted"]
    },
    "yoga pants": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + GRAYS + PASTELS + ["stretchy", "high-waisted", "fitted"]
    },
    "leggings cotton": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "colors": BLACKS + GRAYS + PASTELS + ["soft", "comfortable"]
    },
    "leggings spandex": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CLUB_PARTY, OutfitType.GOTHIC],
        "colors": BLACKS + NEONS + METALLICS + ["shiny", "stretchy", "tight"]
    },
    "mesh panel leggings": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CLUB_PARTY, OutfitType.GOTHIC],
        "colors": BLACKS + GRAYS + ["mesh inserts", "athletic"]
    },
    "leather leggings": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + BROWNS + ["tight", "edgy"]
    },
    
    # SPECIALTY MATERIALS
    "faux leather pants": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY, OutfitType.STREETWEAR],
        "colors": BLACKS + BROWNS + ["vegan leather", "edgy"]
    },
    "vinyl pants": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.PUNK, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["shiny", "reflective"]
    },
    "latex pants": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.GOTHIC],
        "colors": BLACKS + REDS + ["glossy", "second-skin"]
    },
    "metallic trousers": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "colors": METALLICS + ["shimmery", "reflective"]
    },
    "satin pants": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CLUB_PARTY],
        "colors": JEWEL_TONES + METALLICS + ["lustrous", "flowing"]
    },
    "silk pajama-style pants": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.BOHEMIAN],
        "colors": PASTELS + JEWEL_TONES + ["flowing", "luxurious"]
    },
    "sequin pants": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "colors": METALLICS + ["sparkly", "glamorous"]
    },
    "glitter leggings": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.KAWAII],
        "colors": METALLICS + NEONS + ["sparkly", "party-ready"]
    },
    
    # JEANS VARIATIONS
    "ripped jeans": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "colors": ["denim", "black denim", "distressed", "torn"]
    },
    "distressed jeans": {
        "types": [OutfitType.GRUNGE, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "colors": ["light denim", "faded", "worn", "vintage wash"]
    },
    "skinny jeans": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.PUNK],
        "colors": ["denim", "black denim", "white denim", "colored denim"]
    },
    "slim-straight jeans": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "colors": ["dark denim", "indigo", "black denim"]
    },
    "wide-leg jeans": {
        "types": [OutfitType.RETRO, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "colors": ["denim", "vintage wash", "wide cut"]
    },
    "flare jeans": {
        "types": [OutfitType.RETRO, OutfitType.BOHEMIAN, OutfitType.FESTIVAL],
        "colors": ["denim", "boot cut", "flared hem"]
    },
    "bootcut jeans": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COWBOY, OutfitType.RETRO],
        "colors": ["dark denim", "medium wash", "boot cut"]
    },
    "cropped jeans": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "colors": ["denim", "ankle-length", "frayed hem"]
    },
    "low-rise jeans": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.CLUB_PARTY],
        "colors": ["denim", "hip-hugger", "low-waisted"]
    },
    "high-waisted jeans": {
        "types": [OutfitType.RETRO, OutfitType.PIN_UP, OutfitType.CASUAL_CHIC],
        "colors": ["denim", "vintage wash", "high-rise"]
    },
    "mom jeans": {
        "types": [OutfitType.RETRO, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "colors": ["light wash", "relaxed fit", "vintage style"]
    },
    "dad jeans": {
        "types": [OutfitType.NORMCORE, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "colors": ["light wash", "relaxed fit", "vintage style"]
    },
    "boyfriend jeans": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.GRUNGE],
        "colors": ["light wash", "relaxed fit", "rolled cuffs"]
    },
    "girlfriend jeans": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.STREETWEAR],
        "colors": ["medium wash", "fitted", "tapered"]
    },
    "carpenter jeans": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": ["denim", "utility pockets", "tool loops"]
    },
    "cargo jeans": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.MILITARY],
        "colors": ["denim", "cargo pockets", "utility style"]
    },
    "patchwork jeans": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.AVANT_GARDE],
        "colors": ["mixed denim", "patchwork", "artistic"]
    },
    "acid-wash jeans": {
        "types": [OutfitType.RETRO, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "colors": ["acid wash", "vintage", "bleached"]
    },
    "stonewashed jeans": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.NORMCORE],
        "colors": ["stonewashed", "soft", "vintage wash"]
    },
    "embroidered jeans": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.ROMANTIC],
        "colors": ["denim", "floral embroidery", "decorative"]
    },
    "bedazzled jeans": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.KAWAII, OutfitType.FESTIVAL],
        "colors": ["denim", "rhinestones", "sparkly"]
    },
    "lace-up side jeans": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.CLUB_PARTY],
        "colors": ["black denim", "lace-up details", "edgy"]
    },
    "painted jeans": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.FESTIVAL, OutfitType.STREETWEAR],
        "colors": ["denim", "hand-painted", "artistic"]
    },
    
    # SHORTS
    "denim shorts cutoffs": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.BEACH_WEAR],
        "colors": ["denim", "frayed hem", "distressed"]
    },
    "distressed denim shorts": {
        "types": [OutfitType.GRUNGE, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "colors": ["light denim", "ripped", "distressed"]
    },
    "low-rise shorts": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY, OutfitType.STREETWEAR],
        "colors": PASTELS + ["hip-hugger", "low-waisted"]
    },
    "paperbag waist shorts": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.RETRO],
        "colors": EARTH_TONES + PASTELS + ["high-waisted", "belted"]
    },
    "pleated shorts": {
        "types": [OutfitType.PREPPY, OutfitType.RETRO, OutfitType.BUSINESS_WEAR],
        "colors": PASTELS + BLUES + ["tailored", "pressed"]
    },
    "tailored shorts": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + GRAYS + BLUES + ["fitted", "professional"]
    },
    "city shorts": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + EARTH_TONES + ["tailored", "knee-length"]
    },
    "chino shorts": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR],
        "colors": BROWNS + BLUES + PASTELS + ["cotton", "classic cut"]
    },
    "corduroy shorts": {
        "types": [OutfitType.RETRO, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + EARTH_TONES + ["textured", "vintage"]
    },
    "bike shorts": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + GRAYS + NEONS + ["fitted", "stretchy"]
    },
    "running shorts": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR],
        "colors": NEONS + BLACKS + ["lightweight", "moisture-wicking"]
    },
    "gym shorts": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + GRAYS + NEONS + ["athletic", "stretchy"]
    },
    "sweat shorts": {
        "types": [OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "colors": GRAYS + BLACKS + ["fleece", "relaxed"]
    },
    "mesh shorts": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "colors": NEONS + BLACKS + ["breathable", "athletic"]
    },
    "compression shorts": {
        "types": [OutfitType.ATHLEISURE],
        "colors": BLACKS + GRAYS + ["tight", "performance"]
    },
    "cargo shorts": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MILITARY, OutfitType.STREETWEAR],
        "colors": GREENS + BROWNS + ["utility pockets", "practical"]
    },
    "utility shorts with zippers": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.PUNK],
        "colors": BLACKS + ["multiple zippers", "tactical"]
    },
    "belted shorts": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.RETRO],
        "colors": EARTH_TONES + PASTELS + ["high-waisted", "belted"]
    },
    "skater shorts": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "colors": BLACKS + GRAYS + ["relaxed fit", "skateboard-inspired"]
    },
    "bermuda shorts": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR],
        "colors": PASTELS + BLUES + ["knee-length", "tailored"]
    },
    "capri-length shorts": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": PASTELS + WHITES + ["mid-calf", "fitted"]
    },
    "hot pants": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.RETRO],
        "colors": METALLICS + NEONS + ["very short", "tight"]
    },
    "micro shorts": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": NEONS + METALLICS + ["ultra-short", "revealing"]
    },
    "leather shorts": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + BROWNS + ["edgy", "fitted"]
    },
    "faux leather shorts": {
        "types": [OutfitType.PUNK, OutfitType.STREETWEAR, OutfitType.CLUB_PARTY],
        "colors": BLACKS + BROWNS + ["vegan leather", "edgy"]
    },
    "satin shorts": {
        "types": [OutfitType.ROMANTIC, OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL],
        "colors": PASTELS + JEWEL_TONES + ["lustrous", "smooth"]
    },
    "silk pajama shorts": {
        "types": [OutfitType.ROMANTIC, OutfitType.LINGERIE, OutfitType.BOHEMIAN],
        "colors": PASTELS + JEWEL_TONES + ["luxurious", "flowing"]
    },
    "lace-trimmed lingerie shorts": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC],
        "colors": PASTELS + WHITES + ["lace trim", "delicate"]
    },
    "sequin shorts": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.EVENING_FORMAL],
        "colors": METALLICS + ["sparkly", "glamorous"]
    },
    "metallic shorts": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.AVANT_GARDE],
        "colors": METALLICS + ["shiny", "reflective"]
    },
    "holographic shorts": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.CYBERPUNK],
        "colors": ["holographic", "iridescent", "rainbow"]
    },
    "festival fringe shorts": {
        "types": [OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.AVANT_GARDE],
        "colors": EARTH_TONES + ["fringe trim", "boho"]
    },
    "crochet shorts": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.BEACH_WEAR],
        "colors": WHITES + EARTH_TONES + ["handmade", "textured"]
    },
    "printed boho shorts": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.BEACH_WEAR],
        "colors": EARTH_TONES + ["paisley", "floral", "tribal print"]
    },
    "scallop-hem shorts": {
        "types": [OutfitType.PREPPY, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "colors": PASTELS + WHITES + ["scalloped edge", "feminine"]
    },
    
    # SKIRTS EXPANDED
    "micro mini skirt": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.AVANT_GARDE],
        "colors": METALLICS + NEONS + ["ultra-short", "daring"]
    },
    "pleated mini skirt": {
        "types": [OutfitType.KAWAII, OutfitType.PREPPY, OutfitType.LOLITA],
        "colors": PASTELS + BLUES + ["pleated", "school-style"]
    },
    "knife-pleat skirt": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "colors": GRAYS + BLUES + ["sharp pleats", "tailored"]
    },
    "box-pleat skirt": {
        "types": [OutfitType.PREPPY, OutfitType.BUSINESS_WEAR, OutfitType.RETRO],
        "colors": BLUES + GRAYS + ["structured pleats", "classic"]
    },
    "circle skirt": {
        "types": [OutfitType.RETRO, OutfitType.PIN_UP, OutfitType.ROCKABILLY],
        "colors": REDS + PASTELS + ["full circle", "vintage"]
    },
    "a-line skirt": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.RETRO],
        "colors": BLACKS + GRAYS + PASTELS + ["fitted waist", "flared"]
    },
    "high-waisted pencil skirt": {
        "types": [OutfitType.PIN_UP, OutfitType.BUSINESS_WEAR, OutfitType.RETRO],
        "colors": BLACKS + REDS + ["fitted", "vintage-style"]
    },
    "low-rise mini skirt": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "colors": BLACKS + METALLICS + ["hip-hugger", "low-waisted"]
    },
    "wrap skirt": {
        "types": [OutfitType.BOHEMIAN, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": EARTH_TONES + PATTERNS + ["wrap-around", "adjustable"]
    },
    "sarong skirt": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.FESTIVAL],
        "colors": EARTH_TONES + ["wrap-style", "flowing"]
    },
    "skater skirt": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.STREETWEAR],
        "colors": PASTELS + BLACKS + ["flared", "fit-and-flare"]
    },
    "tulip skirt": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "colors": PASTELS + JEWEL_TONES + ["tulip-shaped", "draped"]
    },
    "bubble skirt": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "colors": PASTELS + JEWEL_TONES + ["bubble hem", "structured"]
    },
    "mermaid skirt": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.AVANT_GARDE],
        "colors": JEWEL_TONES + METALLICS + ["fitted", "flared hem"]
    },
    "trumpet skirt": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.RETRO],
        "colors": JEWEL_TONES + METALLICS + ["fitted", "trumpet flare"]
    },
    "godet skirt": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.RETRO],
        "colors": JEWEL_TONES + ["triangular inserts", "flowing"]
    },
    "bias-cut satin skirt": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "colors": JEWEL_TONES + METALLICS + ["bias-cut", "flowing"]
    },
    "panel skirt": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + GRAYS + ["geometric panels", "structured"]
    },
    "paneled leather skirt": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "colors": BLACKS + BROWNS + ["leather panels", "edgy"]
    },
    "cargo skirt": {
        "types": [OutfitType.STREETWEAR, OutfitType.MILITARY, OutfitType.GRUNGE],
        "colors": GREENS + BLACKS + ["utility pockets", "functional"]
    },
    "denim skirt mini": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "colors": ["denim", "distressed", "frayed hem"]
    },
    "denim skirt midi": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.NORMCORE],
        "colors": ["denim", "button-front", "A-line"]
    },
    "denim skirt maxi": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "colors": ["denim", "long", "flowing"]
    },
    "patchwork denim skirt": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.AVANT_GARDE],
        "colors": ["mixed denim", "patchwork", "artistic"]
    },
    "ruffled skirt": {
        "types": [OutfitType.ROMANTIC, OutfitType.LOLITA, OutfitType.KAWAII],
        "colors": PASTELS + WHITES + ["ruffles", "feminine"]
    },
    "tiered maxi skirt": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.ROMANTIC],
        "colors": EARTH_TONES + PASTELS + ["layered tiers", "flowing"]
    },
    "prairie skirt": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.RETRO],
        "colors": EARTH_TONES + PASTELS + ["vintage", "modest"]
    },
    "peasant skirt": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.COTTAGECORE],
        "colors": EARTH_TONES + ["flowing", "ethnic-inspired"]
    },
    "gypsy skirt": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.ETHEREAL],
        "colors": EARTH_TONES + JEWEL_TONES + ["flowing", "layered"]
    },
    "bohemian embroidered skirt": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.ROMANTIC],
        "colors": EARTH_TONES + ["embroidered", "ethnic details"]
    },
    "crochet skirt": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.BEACH_WEAR],
        "colors": WHITES + EARTH_TONES + ["handmade", "textured"]
    },
    "lace skirt": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.LOLITA],
        "colors": WHITES + PASTELS + BLACKS + ["delicate", "feminine"]
    },
    "sheer overlay skirt": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.ETHEREAL],
        "colors": PASTELS + WHITES + ["transparent", "layered"]
    },
    "tulle skirt short": {
        "types": [OutfitType.ROMANTIC, OutfitType.KAWAII, OutfitType.LOLITA],
        "colors": PASTELS + WHITES + ["tulle", "puffy"]
    },
    "tulle skirt ballerina": {
        "types": [OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.EVENING_FORMAL],
        "colors": PASTELS + WHITES + ["long tulle", "ballerina-style"]
    },
    "organza skirt": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": PASTELS + JEWEL_TONES + ["sheer", "structured"]
    },
    "sequin mini skirt": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.FESTIVAL],
        "colors": METALLICS + ["sparkly", "glamorous"]
    },
    "metallic foil skirt": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK],
        "colors": METALLICS + ["reflective", "futuristic"]
    },
    "holographic skirt": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.CYBERPUNK],
        "colors": ["holographic", "iridescent", "rainbow"]
    },
    "vinyl skirt": {
        "types": [OutfitType.PUNK, OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["shiny", "edgy"]
    },
    "leather pencil skirt": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + BROWNS + ["fitted", "edgy"]
    },
    "studded leather mini skirt": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + ["studded", "edgy", "rebellious"]
    },
    "gothic layered skirt": {
        "types": [OutfitType.GOTHIC, OutfitType.LOLITA, OutfitType.STEAMPUNK],
        "colors": BLACKS + PURPLES + ["layered", "dramatic"]
    },
    "corset-belt skirt": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.ROMANTIC],
        "colors": BLACKS + REDS + ["corset waist", "fitted"]
    },
    "bustle skirt steampunk": {
        "types": [OutfitType.STEAMPUNK, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "colors": BROWNS + BLACKS + ["bustle", "Victorian-inspired"]
    },
    "asymmetrical hem skirt": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + GRAYS + ["uneven hem", "modern"]
    },
    "high-low skirt": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.AVANT_GARDE],
        "colors": JEWEL_TONES + PASTELS + ["high-low hem", "dramatic"]
    },
    "draped skirt": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.AVANT_GARDE],
        "colors": JEWEL_TONES + EARTH_TONES + ["draped", "flowing"]
    },
    "harem skirt": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.ETHEREAL],
        "colors": EARTH_TONES + JEWEL_TONES + ["draped", "loose"]
    },
    "bubble hem skirt": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.ROMANTIC, OutfitType.KAWAII],
        "colors": PASTELS + JEWEL_TONES + ["bubble hem", "structured"]
    },
    "apron skirt overlay": {
        "types": [OutfitType.COTTAGECORE, OutfitType.LOLITA, OutfitType.KAWAII],
        "colors": PASTELS + WHITES + ["apron-style", "layered"]
    },
    "kilt": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.RETRO],
        "colors": ["tartan", "plaid", "traditional"]
    },
    "school uniform pleated skirt": {
        "types": [OutfitType.KAWAII, OutfitType.LOLITA, OutfitType.PREPPY],
        "colors": BLUES + GRAYS + ["pleated", "uniform-style"]
    },
    "tennis skirt": {
        "types": [OutfitType.ATHLEISURE, OutfitType.PREPPY, OutfitType.KAWAII],
        "colors": WHITES + PASTELS + ["pleated", "athletic"]
    },
    "cheerleading skirt": {
        "types": [OutfitType.ATHLEISURE, OutfitType.KAWAII, OutfitType.PREPPY],
        "colors": NEONS + WHITES + ["pleated", "sporty"]
    },
    
    # ROMPERS & JUMPSUITS
    "romper": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": PASTELS + PATTERNS + ["one-piece", "shorts combo"]
    },
    "playsuit": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CLUB_PARTY],
        "colors": JEWEL_TONES + PASTELS + ["dressy", "one-piece"]
    },
    "overall shorts denim": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.GRUNGE, OutfitType.NORMCORE],
        "colors": ["denim", "overalls", "casual"]
    },
    "overall pants denim": {
        "types": [OutfitType.GRUNGE, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "colors": ["denim", "overalls", "vintage"]
    },
    "corduroy overalls": {
        "types": [OutfitType.COTTAGECORE, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + EARTH_TONES + ["corduroy", "textured"]
    },
    "utility overalls": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "colors": GREENS + BLACKS + ["utility pockets", "functional"]
    },
    "cargo overalls": {
        "types": [OutfitType.STREETWEAR, OutfitType.MILITARY, OutfitType.GRUNGE],
        "colors": GREENS + BLACKS + ["cargo pockets", "utilitarian"]
    },
    "jumpsuit slim fit": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + ["fitted", "tailored"]
    },
    "jumpsuit wide-leg": {
        "types": [OutfitType.BOHEMIAN, OutfitType.EVENING_FORMAL, OutfitType.RETRO],
        "colors": EARTH_TONES + JEWEL_TONES + ["wide-leg", "flowing"]
    },
    "boilersuit": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.STREETWEAR],
        "colors": BLUES + GREENS + ["utilitarian", "work-inspired"]
    },
    "catsuit spandex": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["tight", "second-skin"]
    },
    "leather catsuit": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.CLUB_PARTY],
        "colors": BLACKS + BROWNS + ["leather", "form-fitting"]
    },
    "sheer mesh catsuit": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.GOTHIC],
        "colors": BLACKS + ["sheer", "mesh", "revealing"]
    },
    "festival unitard": {
        "types": [OutfitType.FESTIVAL, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": NEONS + METALLICS + ["fitted", "performance"]
    },
    "two-piece matching pants": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + JEWEL_TONES + ["coordinated", "matching set"]
    },
    "two-piece matching skirt": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "colors": PASTELS + JEWEL_TONES + ["coordinated", "matching set"]
    },
    "suspender skirt": {
        "types": [OutfitType.LOLITA, OutfitType.KAWAII, OutfitType.RETRO],
        "colors": PASTELS + BLACKS + ["suspender straps", "vintage"]
    },
    "suspender shorts": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.KAWAII],
        "colors": PASTELS + ["suspender straps", "vintage"]
    },
    "suspender trousers": {
        "types": [OutfitType.RETRO, OutfitType.STEAMPUNK, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + GRAYS + BROWNS + ["suspenders", "vintage"]
    },
    
    # AVANT-GARDE & SPECIALTY
    "cage skirt": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["cage structure", "architectural"]
    },
    "hoop skirt": {
        "types": [OutfitType.STEAMPUNK, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "colors": BLACKS + WHITES + ["structured", "Victorian-inspired"]
    },
    "bustle skirt": {
        "types": [OutfitType.STEAMPUNK, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "colors": BROWNS + BLACKS + ["bustle", "period-inspired"]
    },
    "petticoat skirt": {
        "types": [OutfitType.LOLITA, OutfitType.STEAMPUNK, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + ["layered", "structured"]
    },
    "steampunk layered skirt": {
        "types": [OutfitType.STEAMPUNK, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "colors": BROWNS + BLACKS + ["layered", "mechanical details"]
    },
    "feathered skirt": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE, OutfitType.CLUB_PARTY],
        "colors": BLACKS + JEWEL_TONES + ["feather trim", "dramatic"]
    },
    "fringe skirt": {
        "types": [OutfitType.FESTIVAL, OutfitType.CLUB_PARTY, OutfitType.BOHEMIAN],
        "colors": EARTH_TONES + METALLICS + ["fringe", "movement"]
    },
    "glow-in-the-dark skirt": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.CYBERPUNK],
        "colors": NEONS + ["glow-in-the-dark", "party"]
    },
    "led skirt": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": NEONS + ["LED lights", "futuristic"]
    },
    "transparent vinyl skirt": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK],
        "colors": ["transparent", "vinyl", "futuristic"]
    },
    "chainmail skirt": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.AVANT_GARDE],
        "colors": METALLICS + ["chainmail", "armor-inspired"]
    },
    "armor-inspired pleated skirt": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["armor details", "structured"]
    },
    "quilted skirt": {
        "types": [OutfitType.COTTAGECORE, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "colors": EARTH_TONES + PASTELS + ["quilted", "textured"]
    },
    "patchwork fabric skirt": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.COTTAGECORE],
        "colors": EARTH_TONES + ["patchwork", "handmade"]
    },
    "ripped deconstructed skirt": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.AVANT_GARDE],
        "colors": BLACKS + GRAYS + ["distressed", "deconstructed"]
    },
    "sculptural skirt": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + WHITES + METALLICS + ["architectural", "artistic"]
    }
}

