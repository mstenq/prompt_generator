"""
Clothing data definitions for the ComfyUI Outfit Generator.
This file contains clothing items tagged with their compatible outfit types and color palettes.
"""

from ..outfit_types import OutfitType
from ..colors import *


# Tops with their compatible outfit types and color palettes
FEMALE_TOPS = {
    "blazer": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + BLUES + BROWNS + ["pinstripe"]
    },
    "dress shirt": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.EVENING_FORMAL],
        "colors": WHITES + BLUES + ["pinstripe", "checked"]
    },
    "button-down shirt": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "colors": WHITES + BLUES + PASTELS + ["classic cotton", "crisp"]
    },
    "silk button-down": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "colors": WHITES + BLACKS + PASTELS + JEWEL_TONES + ["silk", "lustrous"]
    },
    "oversized button-down": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "colors": WHITES + PASTELS + PATTERNS + ["oversized", "relaxed"]
    },
    "sleeveless button-down": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BEACH_WEAR],
        "colors": WHITES + PASTELS + BLUES + ["sleeveless", "vest style"]
    },
    "tie-front shirt": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": WHITES + PASTELS + PATTERNS + ["tie detail", "cropped"]
    },
    "double-breasted blouse": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.RETRO],
        "colors": WHITES + BLACKS + GRAYS + ["military inspired", "structured"]
    },
    "epaulette blouse": {
        "types": [OutfitType.MILITARY, OutfitType.STEAMPUNK, OutfitType.BUSINESS_WEAR],
        "colors": WHITES + BLACKS + GREENS + ["shoulder details", "structured"]
    },
    "blouse": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.RETRO],
        "colors": WHITES + PASTELS + PATTERNS + ["floral print", "silk"]
    },
    "camisole": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "colors": WHITES + BLACKS + PASTELS + ["basic", "layering"]
    },
    "silk camisole": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.LINGERIE],
        "colors": WHITES + BLACKS + PASTELS + JEWEL_TONES + ["silk", "luxurious"]
    },
    "lace camisole": {
        "types": [OutfitType.ROMANTIC, OutfitType.LINGERIE, OutfitType.COTTAGECORE],
        "colors": WHITES + BLACKS + PASTELS + ["delicate", "feminine"]
    },
    "velvet camisole": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.GOTHIC, OutfitType.RETRO],
        "colors": BLACKS + JEWEL_TONES + REDS + ["velvet", "luxurious"]
    },
    "off-shoulder blouse": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "colors": WHITES + PASTELS + EARTH_TONES + ["romantic", "flowing"]
    },
    "bell-sleeve blouse": {
        "types": [OutfitType.BOHEMIAN, OutfitType.RETRO, OutfitType.FESTIVAL],
        "colors": WHITES + PASTELS + EARTH_TONES + PATTERNS + ["flared sleeves"]
    },
    "bishop-sleeve blouse": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.RETRO],
        "colors": WHITES + PASTELS + ["puffy sleeves", "gathered"]
    },
    "puff-sleeve blouse": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.KAWAII],
        "colors": WHITES + PASTELS + ["puffy sleeves", "vintage"]
    },
    "poet blouse": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "colors": WHITES + PASTELS + EARTH_TONES + ["flowing", "billowy"]
    },
    "victorian blouse": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.LOLITA],
        "colors": WHITES + BLACKS + ["high neck", "lace details", "vintage"]
    },
    "ruffled blouse": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.LOLITA],
        "colors": WHITES + PASTELS + ["ruffles", "feminine"]
    },
    "peter pan collar blouse": {
        "types": [OutfitType.PREPPY, OutfitType.KAWAII, OutfitType.COTTAGECORE],
        "colors": WHITES + PASTELS + ["peter pan collar", "cute"]
    },
    "sailor collar blouse": {
        "types": [OutfitType.KAWAII, OutfitType.RETRO, OutfitType.PREPPY],
        "colors": WHITES + BLUES + ["sailor collar", "nautical"]
    },
    "mandarin collar blouse": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.AVANT_GARDE],
        "colors": WHITES + BLACKS + PASTELS + ["mandarin collar", "structured"]
    },
    "peplum top": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": BLACKS + WHITES + PASTELS + JEWEL_TONES + ["peplum hem", "fitted"]
    },
    "tunic top": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "colors": WHITES + EARTH_TONES + PASTELS + PATTERNS + ["loose fit", "flowing"]
    },
    "empire waist blouse": {
        "types": [OutfitType.ROMANTIC, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "colors": WHITES + PASTELS + PATTERNS + ["high waistline", "flowing"]
    },
    "baby doll top": {
        "types": [OutfitType.KAWAII, OutfitType.ROMANTIC, OutfitType.FESTIVAL],
        "colors": PASTELS + WHITES + ["loose fit", "childlike"]
    },
    "bardot top": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + PATTERNS + ["off-shoulder", "elastic neckline"]
    },
    "high-low blouse": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.AVANT_GARDE, OutfitType.MINIMALIST],
        "colors": WHITES + BLACKS + PASTELS + ["asymmetrical hem"]
    },
    "layered ruffle top": {
        "types": [OutfitType.ROMANTIC, OutfitType.FESTIVAL, OutfitType.COTTAGECORE],
        "colors": WHITES + PASTELS + PATTERNS + ["multiple ruffles", "textured"]
    },
    "sheer chiffon blouse": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.ETHEREAL],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["transparent", "flowing"]
    },
    "organza blouse": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.AVANT_GARDE],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["crisp", "structured"]
    },
    "satin wrap blouse": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "colors": BLACKS + WHITES + JEWEL_TONES + METALLICS + ["wrap style", "lustrous"]
    },
    "sequin blouse": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.FESTIVAL],
        "colors": METALLICS + BLACKS + JEWEL_TONES + ["sequined", "sparkly"]
    },
    "transparent vinyl top": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": ["clear", "transparent", "futuristic"]
    },
    "t-shirt": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "colors": BLACKS + WHITES + GRAYS + NEONS + ["graphic print"]
    },
    "crew neck t-shirt": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR, OutfitType.PREPPY],
        "colors": BLACKS + WHITES + GRAYS + PASTELS + ["classic fit"]
    },
    "v-neck t-shirt": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.MINIMALIST],
        "colors": BLACKS + WHITES + GRAYS + PASTELS + ["fitted", "relaxed"]
    },
    "oversized t-shirt": {
        "types": [OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.GRUNGE, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + GRAYS + NEONS + ["oversized", "boxy"]
    },
    "cropped t-shirt": {
        "types": [OutfitType.STREETWEAR, OutfitType.FESTIVAL, OutfitType.ATHLEISURE, OutfitType.GRUNGE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + ["fitted", "relaxed"]
    },
    "baby tee": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": PASTELS + WHITES + PINKS + ["fitted", "small fit"]
    },
    "ringer tee": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "colors": WHITES + PASTELS + ["contrasting trim", "vintage style"]
    },
    "baseball tee": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.RETRO],
        "colors": WHITES + GRAYS + BLUES + REDS + ["raglan sleeves"]
    },
    "graphic band tee": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + ["vintage", "distressed", "band logo"]
    },
    "distressed t-shirt": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR],
        "colors": BLACKS + WHITES + GRAYS + ["ripped", "holes", "frayed"]
    },
    "tie-dye tee": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.RETRO],
        "colors": ["tie-dye", "rainbow", "psychedelic"] + NEONS
    },
    "tank top": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR, OutfitType.GRUNGE, OutfitType.MILITARY, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + ["mesh", "ribbed"]
    },
    "cotton tank top": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR],
        "colors": WHITES + BLACKS + PASTELS + ["basic", "fitted"]
    },
    "ribbed tank top": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ATHLEISURE],
        "colors": WHITES + BLACKS + GRAYS + PASTELS + ["ribbed texture"]
    },
    "racerback tank": {
        "types": [OutfitType.ATHLEISURE, OutfitType.FESTIVAL, OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + ["athletic", "fitted"]
    },
    "sequin tank top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.EVENING_FORMAL],
        "colors": METALLICS + BLACKS + JEWEL_TONES + ["sequined", "sparkly"]
    },
    "studded tank top": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.GOTHIC],
        "colors": BLACKS + ["studded", "metal details"]
    },
    "hoodie": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.NORMCORE, OutfitType.GRUNGE],
        "colors": BLACKS + GRAYS + NEONS + ["oversized", "cropped"]
    },
    "cropped hoodie": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.FESTIVAL],
        "colors": BLACKS + GRAYS + NEONS + PASTELS + ["cropped", "fitted"]
    },
    "oversized hoodie": {
        "types": [OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "colors": BLACKS + GRAYS + PASTELS + ["oversized", "relaxed"]
    },
    "zip-up hoodie": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "colors": BLACKS + GRAYS + NEONS + ["zip closure", "athletic"]
    },
    "kawaii hoodie": {
        "types": [OutfitType.KAWAII, OutfitType.STREETWEAR],
        "colors": PASTELS + WHITES + PINKS + ["cute ears", "character design"]
    },
    "sweatshirt": {
        "types": [OutfitType.ATHLEISURE, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "colors": GRAYS + BLACKS + PASTELS + ["crewneck", "comfortable"]
    },
    "cropped sweatshirt": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + GRAYS + NEONS + PASTELS + ["cropped", "casual"]
    },
    "graphic sweatshirt": {
        "types": [OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + GRAYS + WHITES + ["graphic print", "logo"]
    },
    "sweater": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.NORMCORE],
        "colors": BROWNS + GREENS + BLUES + PASTELS + ["cable knit", "cashmere"]
    },
    "crewneck sweater": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "colors": BROWNS + GREENS + BLUES + PASTELS + GRAYS + ["classic fit"]
    },
    "v-neck sweater": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + GREENS + BLUES + GRAYS + ["layering", "classic"]
    },
    "cropped sweater": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.KAWAII],
        "colors": PASTELS + WHITES + BROWNS + ["cropped", "fitted"]
    },
    "turtleneck sweater": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + WHITES + GRAYS + BROWNS + ["high neck", "classic"]
    },
    "mock neck sweater": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "colors": BLACKS + WHITES + GRAYS + PASTELS + ["mock neck", "modern"]
    },
    "fisherman sweater": {
        "types": [OutfitType.COTTAGECORE, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "colors": WHITES + GRAYS + BLUES + ["chunky knit", "cable knit"]
    },
    "off-shoulder sweater": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "colors": PASTELS + WHITES + GRAYS + ["off-shoulder", "romantic"]
    },
    "puffy sweater": {
        "types": [OutfitType.KAWAII, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "colors": PASTELS + WHITES + PINKS + ["oversized", "fluffy"]
    },
    "argyle sweater": {
        "types": [OutfitType.PREPPY, OutfitType.RETRO, OutfitType.BUSINESS_WEAR],
        "colors": BLUES + GREENS + BROWNS + GRAYS + ["diamond pattern", "classic"]
    },
    "cardigan": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.COTTAGECORE, OutfitType.KAWAII],
        "colors": PASTELS + BROWNS + GRAYS + ["button-up", "oversized"]
    },
    "cropped cardigan": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.KAWAII, OutfitType.MINIMALIST],
        "colors": PASTELS + WHITES + GRAYS + ["cropped", "fitted"]
    },
    "oversized cardigan": {
        "types": [OutfitType.COTTAGECORE, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + GRAYS + PASTELS + EARTH_TONES + ["oversized", "cozy"]
    },
    "wrap cardigan": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.MINIMALIST],
        "colors": PASTELS + EARTH_TONES + GRAYS + ["wrap style", "flowing"]
    },
    "crochet cardigan": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.FESTIVAL],
        "colors": WHITES + EARTH_TONES + PASTELS + ["handmade", "openwork"]
    },
    "shrug": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.KAWAII],
        "colors": PASTELS + WHITES + METALLICS + ["short sleeves", "cropped"]
    },
    "bolero": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.RETRO],
        "colors": BLACKS + WHITES + JEWEL_TONES + METALLICS + ["cropped jacket", "formal"]
    },
    "sweater vest": {
        "types": [OutfitType.PREPPY, OutfitType.BUSINESS_WEAR, OutfitType.RETRO],
        "colors": BROWNS + GRAYS + BLUES + GREENS + ["sleeveless", "layering"]
    },
    "cropped vest": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + GRAYS + ["cropped", "structured"]
    },
    "denim vest": {
        "types": [OutfitType.GRUNGE, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "colors": ["denim", "distressed denim", "black denim"]
    },
    "leather vest": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.GOTHIC],
        "colors": BLACKS + BROWNS + ["leather", "studded"]
    },
    "military vest": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "colors": GREENS + BLACKS + GRAYS + ["utility pockets", "structured"]
    },
    "utility vest": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "colors": BLACKS + GREENS + GRAYS + ["multiple pockets", "functional"]
    },
    "cable knit vest": {
        "types": [OutfitType.PREPPY, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + GRAYS + BLUES + ["cable knit", "classic"]
    },
    "polo shirt": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "colors": WHITES + BLUES + GREENS + PINKS + ["striped collar"]
    },
    "rugby shirt": {
        "types": [OutfitType.PREPPY, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "colors": WHITES + BLUES + GREENS + REDS + ["horizontal stripes", "thick stripes"]
    },
    "henley shirt": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.MINIMALIST],
        "colors": WHITES + GRAYS + BLUES + EARTH_TONES + ["button placket", "collarless"]
    },
    "long-sleeve fitted top": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + GRAYS + PASTELS + ["fitted", "stretchy"]
    },
    "long-sleeve oversized top": {
        "types": [OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.ATHLEISURE],
        "colors": BLACKS + GRAYS + PASTELS + NEONS + ["oversized", "relaxed"]
    },
    "flannel shirt": {
        "types": [OutfitType.GRUNGE, OutfitType.COWBOY, OutfitType.NORMCORE, OutfitType.COTTAGECORE],
        "colors": ["plaid", "checked"] + REDS + GREENS + BLUES
    },
    "cropped flannel": {
        "types": [OutfitType.GRUNGE, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "colors": ["plaid", "checked"] + REDS + GREENS + BLUES + ["cropped"]
    },
    "western snap shirt": {
        "types": [OutfitType.COWBOY, OutfitType.ROCKABILLY, OutfitType.FESTIVAL],
        "colors": BLUES + REDS + BROWNS + WHITES + ["snap buttons", "western style"]
    },
    "fringe top": {
        "types": [OutfitType.COWBOY, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "colors": BROWNS + EARTH_TONES + WHITES + ["fringe details", "western"]
    },
    "sports bra": {
        "types": [OutfitType.ATHLEISURE, OutfitType.FESTIVAL, OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + ["athletic", "supportive"]
    },
    "athletic crop tank": {
        "types": [OutfitType.ATHLEISURE, OutfitType.FESTIVAL, OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + ["moisture-wicking", "athletic"]
    },
    "compression top": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CYBERPUNK],
        "colors": BLACKS + GRAYS + NEONS + ["tight-fitting", "athletic"]
    },
    "track jacket": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.RETRO],
        "colors": BLACKS + WHITES + NEONS + BLUES + ["zip-up", "sporty"]
    },
    "half-zip pullover": {
        "types": [OutfitType.ATHLEISURE, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "colors": GRAYS + BLACKS + BLUES + PASTELS + ["athletic", "layering"]
    },
    "windbreaker top": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.MILITARY],
        "colors": BLACKS + NEONS + GRAYS + ["lightweight", "sporty"]
    },
    "logo sports jersey": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC],
        "colors": WHITES + BLUES + REDS + BLACKS + ["team colors", "sporty"]
    },
    "baseball jersey": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.RETRO],
        "colors": WHITES + GRAYS + BLUES + REDS + ["baseball style", "raglan"]
    },
    "cheerleader crop top": {
        "types": [OutfitType.KAWAII, OutfitType.ATHLEISURE, OutfitType.FESTIVAL],
        "colors": WHITES + BLUES + REDS + PINKS + ["sporty", "cropped"]
    },
    "triangle bikini top": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["triangle cups", "tie strings"]
    },
    "halter bikini top": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["halter neck", "supportive"]
    },
    "bandeau bikini top": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["strapless", "bandeau"]
    },
    "surf rash guard": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + BLUES + ["UV protection", "long sleeve"]
    },
    "crochet halter top": {
        "types": [OutfitType.BOHEMIAN, OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": WHITES + EARTH_TONES + PASTELS + ["handmade", "boho"]
    },
    "apron top": {
        "types": [OutfitType.COTTAGECORE, OutfitType.KAWAII, OutfitType.RETRO],
        "colors": WHITES + PASTELS + PATTERNS + ["apron style", "vintage"]
    },
    "smocked peasant top": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + EARTH_TONES + ["smocked", "gathered"]
    },
    "gingham blouse": {
        "types": [OutfitType.COTTAGECORE, OutfitType.RETRO, OutfitType.KAWAII],
        "colors": ["gingham check"] + PASTELS + WHITES + ["checkered pattern"]
    },
    "embroidered peasant blouse": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.FESTIVAL],
        "colors": WHITES + EARTH_TONES + PASTELS + ["embroidered", "folk style"]
    },
    "lolita blouse": {
        "types": [OutfitType.LOLITA, OutfitType.KAWAII],
        "colors": WHITES + PASTELS + ["bow details", "frilly", "japanese fashion"]
    },
    "sailor fuku blouse": {
        "types": [OutfitType.KAWAII, OutfitType.LOLITA],
        "colors": WHITES + BLUES + ["sailor collar", "school uniform style"]
    },
    "cartoon print tee": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "colors": WHITES + PASTELS + NEONS + ["cartoon characters", "cute graphics"]
    },
    "rockabilly blouse": {
        "types": [OutfitType.ROCKABILLY, OutfitType.PIN_UP, OutfitType.RETRO],
        "colors": REDS + BLACKS + WHITES + ["polka dots", "tied front", "vintage"]
    },
    "polka dot halter": {
        "types": [OutfitType.PIN_UP, OutfitType.ROCKABILLY, OutfitType.RETRO],
        "colors": ["polka dots"] + REDS + BLACKS + WHITES + ["halter neck"]
    },
    "retro bowling shirt": {
        "types": [OutfitType.RETRO, OutfitType.ROCKABILLY, OutfitType.CASUAL_CHIC],
        "colors": WHITES + PASTELS + ["retro stripes", "vintage"]
    },
    "70s disco halter": {
        "types": [OutfitType.RETRO, OutfitType.CLUB_PARTY, OutfitType.FESTIVAL],
        "colors": METALLICS + JEWEL_TONES + ["sequined", "disco era"]
    },
    "80s power blouse": {
        "types": [OutfitType.RETRO, OutfitType.BUSINESS_WEAR, OutfitType.AVANT_GARDE],
        "colors": BLACKS + WHITES + JEWEL_TONES + ["shoulder pads", "structured"]
    },
    "90s spaghetti strap top": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "colors": BLACKS + WHITES + PASTELS + ["thin straps", "minimal"]
    },
    "y2k butterfly top": {
        "types": [OutfitType.RETRO, OutfitType.CLUB_PARTY, OutfitType.KAWAII],
        "colors": METALLICS + NEONS + PASTELS + ["butterfly print", "shimmery"]
    },
    "striped breton top": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": ["navy stripes", "red stripes"] + WHITES + ["horizontal stripes"]
    },
    "acid-wash denim shirt": {
        "types": [OutfitType.GRUNGE, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "colors": ["acid wash", "bleached denim", "distressed"]
    },
    "denim bustier": {
        "types": [OutfitType.GRUNGE, OutfitType.FESTIVAL, OutfitType.RETRO],
        "colors": ["denim", "distressed denim", "black denim"]
    },
    "structured sculptural top": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + WHITES + METALLICS + ["architectural", "geometric"]
    },
    "exaggerated shoulder top": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.RETRO, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + WHITES + JEWEL_TONES + ["dramatic shoulders", "sculptural"]
    },
    "origami fold top": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "colors": WHITES + BLACKS + GRAYS + ["geometric folds", "architectural"]
    },
    "glow in the dark top": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY, OutfitType.FESTIVAL],
        "colors": NEONS + ["glow-in-the-dark", "phosphorescent"]
    },
    "faux fur crop top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.AVANT_GARDE],
        "colors": WHITES + BLACKS + PASTELS + ["fluffy", "textured"]
    },
    "mesh rhinestone top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["sheer", "sparkly", "rhinestones"]
    },
    "patchwork top": {
        "types": [OutfitType.BOHEMIAN, OutfitType.GRUNGE, OutfitType.FESTIVAL],
        "colors": ["multicolor", "mixed fabrics", "eclectic"]
    },
    "leopard print tank": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.GRUNGE, OutfitType.PIN_UP],
        "colors": ["leopard print", "animal print"] + BROWNS + BLACKS
    },
    "snake print bodysuit": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "colors": ["snake print", "python print"] + GREENS + BROWNS + BLACKS
    },
    "school blazer vest": {
        "types": [OutfitType.KAWAII, OutfitType.PREPPY, OutfitType.LOLITA],
        "colors": BLUES + GRAYS + BLACKS + ["school uniform", "structured"]
    },
    "fishnet top": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + ["fishnet", "see-through", "layering"]
    },
    "lace long sleeve top": {
        "types": [OutfitType.ROMANTIC, OutfitType.GOTHIC, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + WHITES + PASTELS + ["delicate", "sheer"]
    },
    "military uniform blouse": {
        "types": [OutfitType.MILITARY, OutfitType.STEAMPUNK, OutfitType.AVANT_GARDE],
        "colors": GREENS + BLACKS + GRAYS + ["structured", "formal"]
    },
    "steampunk corset blouse": {
        "types": [OutfitType.STEAMPUNK, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "colors": BROWNS + BLACKS + METALLICS + ["brass details", "vintage"]
    },
    "victorian ruffle shirt": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.LOLITA],
        "colors": WHITES + BLACKS + ["elaborate ruffles", "high neck"]
    },
    "band t-shirt": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + ["vintage", "distressed", "graphic print"]
    },
    "crop top": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.FESTIVAL, OutfitType.CLUB_PARTY, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + ["mesh", "metallic"]
    },
    "fitted crop top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.ATHLEISURE, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + PASTELS + ["tight-fitting", "stretchy"]
    },
    "tube top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + PASTELS + ["strapless", "bandeau"]
    },
    "bandeau top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + PASTELS + ["strapless", "bandeau"]
    },
    "metallic crop top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK, OutfitType.FESTIVAL],
        "colors": METALLICS + ["silver", "gold", "holographic"]
    },
    "vinyl crop top": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY, OutfitType.PUNK],
        "colors": BLACKS + METALLICS + ["vinyl", "PVC", "shiny"]
    },
    "holographic top": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY, OutfitType.FESTIVAL],
        "colors": ["holographic", "iridescent", "rainbow"]
    },
    "neon spandex top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK, OutfitType.FESTIVAL],
        "colors": NEONS + ["spandex", "stretchy", "bright"]
    },
    "tie-front crop top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "colors": WHITES + PASTELS + PATTERNS + ["tie detail", "adjustable"]
    },
    "crochet crop top": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.BEACH_WEAR],
        "colors": WHITES + EARTH_TONES + PASTELS + ["handmade", "openwork"]
    },
    "lace crop top": {
        "types": [OutfitType.ROMANTIC, OutfitType.FESTIVAL, OutfitType.LINGERIE],
        "colors": WHITES + BLACKS + PASTELS + ["delicate", "sheer"]
    },
    "leather crop top": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + BROWNS + ["leather", "edgy"]
    },
    "feathered crop top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + PASTELS + ["feathers", "textured"]
    },
    "graphic crop hoodie": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.FESTIVAL],
        "colors": BLACKS + GRAYS + NEONS + ["graphic print", "hood"]
    },
    "halter top": {
        "types": [OutfitType.PIN_UP, OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY, OutfitType.FESTIVAL],
        "colors": REDS + PINKS + BLACKS + WHITES + ["polka dots"]
    },
    "wrap top": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN],
        "colors": PASTELS + EARTH_TONES + PATTERNS + ["tie detail", "adjustable"]
    },
    "one-shoulder top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "colors": BLACKS + WHITES + JEWEL_TONES + METALLICS + ["asymmetrical"]
    },
    "off-shoulder top": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "colors": WHITES + PASTELS + EARTH_TONES + ["flowing", "romantic"]
    },
    "cold-shoulder top": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.FESTIVAL],
        "colors": WHITES + PASTELS + PATTERNS + ["cutout shoulders"]
    },
    "strapless top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + JEWEL_TONES + ["sweetheart neckline", "bandeau"]
    },
    "choker neckline top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "colors": BLACKS + REDS + METALLICS + ["high neck", "choker detail"]
    },
    "cutout top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + ["strategic cutouts", "revealing"]
    },
    "cage detail top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.GOTHIC, OutfitType.FESTIVAL],
        "colors": BLACKS + METALLICS + ["strappy", "cage straps"]
    },
    "chain strap top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.PUNK, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["chain details", "edgy"]
    },
    "scarf top": {
        "types": [OutfitType.BOHEMIAN, OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": PATTERNS + PASTELS + JEWEL_TONES + ["wrapped", "tied"]
    },
    "corset": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.COTTAGECORE, OutfitType.LINGERIE, OutfitType.LOLITA],
        "colors": BLACKS + REDS + BROWNS + ["lace", "leather", "brocade"]
    },
    "leather jacket": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.ROCKABILLY],
        "colors": BLACKS + BROWNS + ["studded", "distressed"]
    },
    "bomber jacket": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.MILITARY],
        "colors": BLACKS + GREENS + NEONS + ["satin", "metallic"]
    },
    "kimono": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.KAWAII],
        "colors": PASTELS + JEWEL_TONES + ["floral print", "silk", "embroidered"]
    },
    "bodysuit": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.ATHLEISURE, OutfitType.LINGERIE, OutfitType.AVANT_GARDE],
        "colors": BLACKS + METALLICS + NEONS + ["sequined", "mesh"]
    },
    "sleeveless bodysuit": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.MINIMALIST, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + ["fitted", "stretchy"]
    },
    "long-sleeve bodysuit": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.MINIMALIST, OutfitType.GOTHIC],
        "colors": BLACKS + WHITES + GRAYS + ["fitted", "coverage"]
    },
    "mesh bodysuit": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK, OutfitType.FESTIVAL],
        "colors": BLACKS + NEONS + METALLICS + ["see-through", "layering"]
    },
    "bralette top": {
        "types": [OutfitType.FESTIVAL, OutfitType.BEACH_WEAR, OutfitType.LINGERIE],
        "colors": BLACKS + WHITES + PASTELS + ["wireless", "comfortable"]
    },
    "bustier top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.PIN_UP],
        "colors": BLACKS + REDS + METALLICS + ["structured", "fitted"]
    },
    "corset top": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + BROWNS + ["laced", "structured"]
    },
    "harness top": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "colors": BLACKS + ["leather", "straps", "buckles"]
    },
    "harness corset": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.CYBERPUNK],
        "colors": BLACKS + ["leather", "metal details", "straps"]
    },
    "chainmail top": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "colors": METALLICS + BLACKS + ["chain links", "metallic"]
    },
    "sequin bralette": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.EVENING_FORMAL],
        "colors": METALLICS + JEWEL_TONES + ["sequined", "sparkly"]
    },
    "glitter mesh top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.CYBERPUNK],
        "colors": METALLICS + NEONS + ["glittery", "mesh", "sparkly"]
    },
    "spiked bra top": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["spikes", "edgy", "metal studs"]
    },
    "mesh top": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK, OutfitType.PUNK, OutfitType.FESTIVAL],
        "colors": BLACKS + NEONS + METALLICS + ["see-through", "layered"]
    },
    "peasant top": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.FESTIVAL],
        "colors": WHITES + EARTH_TONES + ["embroidered", "flowing", "off-shoulder"]
    },
    
    # Full-body dresses
    "evening gown": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": BLACKS + GRAYS + BLUES + JEWEL_TONES + ["silk", "satin", "chiffon"],
        "fullBody": True
    },
    "cocktail dress": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY],
        "colors": BLACKS + JEWEL_TONES + METALLICS + ["silk", "sequined"],
        "fullBody": True
    },
    "prom dress": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": PASTELS + JEWEL_TONES + METALLICS + ["tulle", "satin", "sequined"],
        "fullBody": True
    },
    "little black dress": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + ["classic", "timeless"],
        "fullBody": True
    },
    "ball gown": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": JEWEL_TONES + PASTELS + METALLICS + ["tulle", "satin", "ornate"],
        "fullBody": True
    },
    "A-line dress": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.PREPPY],
        "colors": WHITES + PASTELS + BLUES + PATTERNS + ["classic", "flattering"],
        "fullBody": True
    },
    "empire waist dress": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "colors": PASTELS + WHITES + PATTERNS + ["flowing", "feminine"],
        "fullBody": True
    },
    "slip dress": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.CLUB_PARTY],
        "colors": BLACKS + JEWEL_TONES + METALLICS + ["satin", "silk", "bias-cut"],
        "fullBody": True
    },
    "sheath dress": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + BLUES + JEWEL_TONES + ["tailored", "sleek"],
        "fullBody": True
    },
    "shift dress": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.RETRO],
        "colors": PASTELS + PATTERNS + WHITES + ["mod", "geometric"],
        "fullBody": True
    },
    "shirt dress": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.BUSINESS_WEAR],
        "colors": WHITES + BLUES + PATTERNS + ["cotton", "crisp", "button-front"],
        "fullBody": True
    },
    "sweater dress": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.MINIMALIST],
        "colors": GRAYS + BROWNS + PASTELS + ["knit", "cozy", "wool"],
        "fullBody": True
    },
    "wrap dress": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.ROMANTIC],
        "colors": PATTERNS + JEWEL_TONES + PASTELS + ["flattering", "tied"],
        "fullBody": True
    },
    "sundress": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": PASTELS + PATTERNS + WHITES + YELLOWS + ["cotton", "breezy", "light"],
        "fullBody": True
    },
    "maxi dress": {
        "types": [OutfitType.BOHEMIAN, OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "colors": PATTERNS + EARTH_TONES + JEWEL_TONES + ["flowing", "floor-length"],
        "fullBody": True
    },
    "midi dress": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.ROMANTIC],
        "colors": PASTELS + PATTERNS + JEWEL_TONES + ["mid-length", "versatile"],
        "fullBody": True
    },
    "mini dress": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": PASTELS + JEWEL_TONES + PATTERNS + NEONS + ["short", "playful"],
        "fullBody": True
    },
    "peplum dress": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "colors": JEWEL_TONES + PASTELS + BLACKS + ["fitted", "flared waist"],
        "fullBody": True
    },
    "mermaid dress": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": JEWEL_TONES + METALLICS + BLACKS + ["fitted", "dramatic", "fishtail"],
        "fullBody": True
    },
    "trumpet dress": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": JEWEL_TONES + METALLICS + WHITES + ["fitted", "flared", "elegant"],
        "fullBody": True
    },
    "bias-cut dress": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST, OutfitType.VINTAGE],
        "colors": JEWEL_TONES + BLACKS + ["silk", "flowing", "draped"],
        "fullBody": True
    },
    "halter dress": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.BEACH_WEAR, OutfitType.RETRO],
        "colors": JEWEL_TONES + PASTELS + PATTERNS + ["tied neck", "backless"],
        "fullBody": True
    },
    "strapless dress": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY],
        "colors": JEWEL_TONES + PASTELS + BLACKS + ["strapless", "elegant"],
        "fullBody": True
    },
    "one-shoulder dress": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY],
        "colors": JEWEL_TONES + BLACKS + METALLICS + ["asymmetrical", "dramatic"],
        "fullBody": True
    },
    "off-the-shoulder dress": {
        "types": [OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "colors": PASTELS + WHITES + PATTERNS + ["feminine", "romantic"],
        "fullBody": True
    },
    "babydoll dress": {
        "types": [OutfitType.KAWAII, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC],
        "colors": PASTELS + WHITES + PATTERNS + ["sweet", "youthful", "empire waist"],
        "fullBody": True
    },
    "tiered ruffle dress": {
        "types": [OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.FESTIVAL],
        "colors": PASTELS + WHITES + PATTERNS + ["ruffled", "layered", "textured"],
        "fullBody": True
    },
    "tulle ballerina dress": {
        "types": [OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.KAWAII],
        "colors": PASTELS + WHITES + ["tulle", "dreamy", "fairy-like"],
        "fullBody": True
    },
    "high-low hem dress": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "colors": JEWEL_TONES + PASTELS + PATTERNS + ["asymmetrical", "modern"],
        "fullBody": True
    },
    "asymmetrical draped dress": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + JEWEL_TONES + ["draped", "sculptural", "artistic"],
        "fullBody": True
    },
    "bodycon dress": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + JEWEL_TONES + NEONS + ["fitted", "stretchy", "curve-hugging"],
        "fullBody": True
    },
    "cut-out dress": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": BLACKS + JEWEL_TONES + NEONS + ["edgy", "revealing", "architectural"],
        "fullBody": True
    },
    "bandage dress": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + JEWEL_TONES + NEONS + ["bodycon", "structured", "bandage"],
        "fullBody": True
    },
    "sequin party dress": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL],
        "colors": METALLICS + JEWEL_TONES + ["sequined", "sparkly", "glamorous"],
        "fullBody": True
    },
    "metallic foil dress": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK],
        "colors": METALLICS + ["holographic", "futuristic", "reflective"],
        "fullBody": True
    },
    "feathered evening dress": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "colors": BLACKS + JEWEL_TONES + WHITES + ["feathered", "luxurious", "textured"],
        "fullBody": True
    },
    "lace overlay dress": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.VINTAGE],
        "colors": WHITES + PASTELS + BLACKS + ["lace", "delicate", "romantic"],
        "fullBody": True
    },
    "crochet dress": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.BEACH_WEAR],
        "colors": WHITES + EARTH_TONES + PASTELS + ["crochet", "handmade", "boho"],
        "fullBody": True
    },
    "boho peasant maxi dress": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.COTTAGECORE],
        "colors": EARTH_TONES + PATTERNS + ["flowing", "embroidered", "free-spirited"],
        "fullBody": True
    },
    "prairie dress": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": PASTELS + PATTERNS + WHITES + ["modest", "high-necked", "vintage-inspired"],
        "fullBody": True
    },
    "cottagecore apron dress": {
        "types": [OutfitType.COTTAGECORE],
        "colors": PASTELS + PATTERNS + WHITES + ["apron-style", "rustic", "charming"],
        "fullBody": True
    },
    "lolita dress": {
        "types": [OutfitType.LOLITA, OutfitType.KAWAII],
        "colors": PASTELS + WHITES + BLACKS + ["sweet", "gothic", "classic", "elaborate"],
        "fullBody": True
    },
    "kawaii puff-sleeve dress": {
        "types": [OutfitType.KAWAII, OutfitType.LOLITA],
        "colors": PASTELS + WHITES + ["cute", "puffy sleeves", "sweet"],
        "fullBody": True
    },
    "gothic Victorian mourning dress": {
        "types": [OutfitType.GOTHIC, OutfitType.VINTAGE],
        "colors": BLACKS + PURPLES + ["Victorian", "ornate", "dramatic"],
        "fullBody": True
    },
    "steampunk bustle dress": {
        "types": [OutfitType.STEAMPUNK, OutfitType.VINTAGE],
        "colors": BROWNS + BLACKS + METALLICS + ["Victorian", "mechanical", "corseted"],
        "fullBody": True
    },
    "pin-up swing dress": {
        "types": [OutfitType.PIN_UP, OutfitType.RETRO, OutfitType.ROCKABILLY],
        "colors": PATTERNS + REDS + BLUES + ["1950s", "flared", "vintage"],
        "fullBody": True
    },
    "rockabilly halter dress": {
        "types": [OutfitType.ROCKABILLY, OutfitType.PIN_UP, OutfitType.RETRO],
        "colors": PATTERNS + REDS + BLACKS + ["1950s", "halter", "retro"],
        "fullBody": True
    },
    "retro polka dot dress": {
        "types": [OutfitType.RETRO, OutfitType.PIN_UP, OutfitType.ROCKABILLY],
        "colors": ["polka dots", "vintage patterns"] + REDS + BLUES,
        "fullBody": True
    },
    "disco halter sequin dress": {
        "types": [OutfitType.RETRO, OutfitType.CLUB_PARTY],
        "colors": METALLICS + JEWEL_TONES + ["sequined", "1970s", "disco"],
        "fullBody": True
    },
    "power-shoulder mini dress": {
        "types": [OutfitType.RETRO, OutfitType.BUSINESS_WEAR],
        "colors": JEWEL_TONES + BLACKS + ["1980s", "structured", "bold"],
        "fullBody": True
    },
    "Y2K butterfly dress": {
        "types": [OutfitType.RETRO, OutfitType.CLUB_PARTY, OutfitType.KAWAII],
        "colors": METALLICS + NEONS + PASTELS + ["iridescent", "2000s", "futuristic"],
        "fullBody": True
    },
    
    # Jumpsuits and one-piece outfits
    "classic jumpsuit": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + BLUES + JEWEL_TONES + ["tailored", "sleek"],
        "fullBody": True
    },
    "boilersuit": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": BLUES + GREENS + GRAYS + ["utility", "workwear", "functional"],
        "fullBody": True
    },
    "coveralls": {
        "types": [OutfitType.MILITARY, OutfitType.NORMCORE],
        "colors": BLUES + GREENS + GRAYS + ["workwear", "durable", "practical"],
        "fullBody": True
    },
    "catsuit": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE],
        "colors": BLACKS + METALLICS + ["spandex", "latex", "skin-tight", "shiny"],
        "fullBody": True
    },
    "romper": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": PASTELS + PATTERNS + WHITES + ["shorts combo", "playful", "summer"],
        "fullBody": True
    },
    "playsuit": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": JEWEL_TONES + PASTELS + PATTERNS + ["dressy", "elegant romper"],
        "fullBody": True
    },
    "overalls": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.NORMCORE],
        "colors": ["denim", "blue denim", "black denim", "vintage", "classic"],
        "fullBody": True
    },
    "overall shorts": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.KAWAII],
        "colors": ["denim", "pastel denim", "white denim", "cute", "summer"],
        "fullBody": True
    },
    "corduroy overalls": {
        "types": [OutfitType.COTTAGECORE, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + EARTH_TONES + ["corduroy", "textured", "vintage"],
        "fullBody": True
    },
    "utility jumpsuit": {
        "types": [OutfitType.MILITARY, OutfitType.CYBERPUNK, OutfitType.STREETWEAR],
        "colors": GREENS + BLACKS + GRAYS + ["pockets", "functional", "tactical"],
        "fullBody": True
    },
    "military flight suit": {
        "types": [OutfitType.MILITARY, OutfitType.CYBERPUNK],
        "colors": GREENS + GRAYS + ["olive", "military", "aviator", "tactical"],
        "fullBody": True
    },
    "parachute jumpsuit": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "colors": GREENS + BLACKS + GRAYS + ["parachute fabric", "baggy", "tactical"],
        "fullBody": True
    },
    "techwear jumpsuit": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.AVANT_GARDE],
        "colors": BLACKS + GRAYS + METALLICS + ["futuristic", "technical", "modular"],
        "fullBody": True
    },
    "festival unitard": {
        "types": [OutfitType.FESTIVAL, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": NEONS + METALLICS + PATTERNS + ["holographic", "rave", "body-con"],
        "fullBody": True
    },
    "performance bodysuit": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.AVANT_GARDE],
        "colors": METALLICS + NEONS + JEWEL_TONES + ["dance", "costume", "stretchy"],
        "fullBody": True
    },
    "wrestling singlet bodysuit": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST],
        "colors": BLACKS + BLUES + REDS + ["athletic", "form-fitting", "sporty"],
        "fullBody": True
    },
    "leotard jumpsuit": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.CLUB_PARTY],
        "colors": BLACKS + JEWEL_TONES + METALLICS + ["stretchy", "form-fitting"],
        "fullBody": True
    },
    "sheer mesh bodysuit dress": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + METALLICS + ["sheer", "mesh overlay", "see-through"],
        "fullBody": True
    },
    
    # Wedding and formal
    "wedding dress": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "colors": WHITES + ["ivory", "pearl", "satin", "lace", "tulle", "classic"],
        "fullBody": True
    },
    "bridal sari": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "colors": REDS + JEWEL_TONES + METALLICS + ["traditional", "ornate", "cultural"],
        "fullBody": True
    },
    "bridesmaid dress": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "colors": PASTELS + JEWEL_TONES + ["coordinated", "elegant", "formal"],
        "fullBody": True
    },
    "pageant dress": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": JEWEL_TONES + METALLICS + PASTELS + ["sequined", "glamorous", "stage"],
        "fullBody": True
    },
    "cocktail romper suit": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + JEWEL_TONES + METALLICS + ["sophisticated", "modern"],
        "fullBody": True
    },
    
    # Uniforms and costumes
    "cheerleader uniform": {
        "types": [OutfitType.ATHLEISURE, OutfitType.RETRO, OutfitType.KAWAII],
        "colors": NEONS + PASTELS + PATTERNS + ["sporty", "school colors", "pleated"],
        "fullBody": True
    },
    "school uniform dress": {
        "types": [OutfitType.PREPPY, OutfitType.KAWAII, OutfitType.MINIMALIST],
        "colors": BLUES + GRAYS + BLACKS + ["sailor", "seifuku", "academic"],
        "fullBody": True
    },
    "nurse uniform dress": {
        "types": [OutfitType.MINIMALIST, OutfitType.RETRO],
        "colors": WHITES + PASTELS + ["medical", "professional", "classic"],
        "fullBody": True
    },
    "maid outfit": {
        "types": [OutfitType.KAWAII, OutfitType.GOTHIC, OutfitType.RETRO],
        "colors": BLACKS + WHITES + ["frilly", "cosplay", "French maid"],
        "fullBody": True
    },
    "nun's habit": {
        "types": [OutfitType.GOTHIC, OutfitType.MINIMALIST],
        "colors": BLACKS + WHITES + GRAYS + ["religious", "modest", "traditional"],
        "fullBody": True
    },
    
    # Cultural and traditional
    "kimono": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "colors": JEWEL_TONES + PATTERNS + ["silk", "traditional", "ornate", "Japanese"],
        "fullBody": True
    },
    "yukata": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ETHEREAL, OutfitType.FESTIVAL],
        "colors": PASTELS + PATTERNS + ["cotton", "summer", "casual kimono"],
        "fullBody": True
    },
    "hanbok": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": PASTELS + JEWEL_TONES + PATTERNS + ["Korean", "traditional", "elegant"],
        "fullBody": True
    },
    "sari": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": JEWEL_TONES + METALLICS + PATTERNS + ["draped", "silk", "ornate"],
        "fullBody": True
    },
    "dirndl": {
        "types": [OutfitType.COTTAGECORE, OutfitType.RETRO, OutfitType.FESTIVAL],
        "colors": PASTELS + PATTERNS + EARTH_TONES + ["German", "folk", "traditional"],
        "fullBody": True
    },
    "lederhosen set": {
        "types": [OutfitType.COTTAGECORE, OutfitType.RETRO],
        "colors": BROWNS + EARTH_TONES + ["leather", "bib", "German", "traditional"],
        "fullBody": True
    },
    "flamenco dress": {
        "types": [OutfitType.ROMANTIC, OutfitType.FESTIVAL, OutfitType.EVENING_FORMAL],
        "colors": REDS + BLACKS + JEWEL_TONES + ["ruffled", "Spanish", "passionate"],
        "fullBody": True
    },
    "tango dress": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + JEWEL_TONES + ["fitted", "dramatic", "dance"],
        "fullBody": True
    },
    
    # Performance and dance
    "ballet tutu outfit": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.KAWAII],
        "colors": PASTELS + WHITES + ["tulle", "classical", "graceful"],
        "fullBody": True
    },
    "dance leotard with skirt": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.ETHEREAL],
        "colors": BLACKS + PASTELS + JEWEL_TONES + ["stretchy", "performance", "graceful"],
        "fullBody": True
    },
    "figure skating dress": {
        "types": [OutfitType.ATHLEISURE, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "colors": JEWEL_TONES + PASTELS + METALLICS + ["sequined", "ice", "performance"],
        "fullBody": True
    },
    
    # Themed and costume
    "circus ringmaster outfit": {
        "types": [OutfitType.RETRO, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "colors": REDS + BLACKS + METALLICS + ["theatrical", "bold", "dramatic"],
        "fullBody": True
    },
    "clown costume": {
        "types": [OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.AVANT_GARDE],
        "colors": NEONS + PATTERNS + ["polka dots", "colorful", "whimsical"],
        "fullBody": True
    },
    "superhero bodysuit": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY, OutfitType.FESTIVAL],
        "colors": NEONS + JEWEL_TONES + METALLICS + ["spandex", "heroic", "bold"],
        "fullBody": True
    },
    "fantasy mage robe": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.FESTIVAL],
        "colors": PURPLES + BLACKS + JEWEL_TONES + ["mystical", "flowing", "ornate"],
        "fullBody": True
    },
    "priestess gown": {
        "types": [OutfitType.ETHEREAL, OutfitType.GOTHIC, OutfitType.ROMANTIC],
        "colors": WHITES + JEWEL_TONES + METALLICS + ["ceremonial", "flowing", "divine"],
        "fullBody": True
    },
    "sci-fi space suit": {
        "types": [OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "colors": METALLICS + WHITES + BLACKS + ["futuristic", "technical", "sleek"],
        "fullBody": True
    },
    "armor-inspired outfit": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "colors": METALLICS + BLACKS + GRAYS + ["armored", "protective", "warrior"],
        "fullBody": True
    },
    "animal onesie": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "colors": PASTELS + PATTERNS + ["kigurumi", "cute", "cozy", "character"],
        "fullBody": True
    },
    
    # Coats and robes as dresses
    "trench coat dress": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + BLACKS + GRAYS + ["belted", "classic", "tailored"],
        "fullBody": True
    },
    "long duster coat outfit": {
        "types": [OutfitType.COWBOY, OutfitType.GOTHIC, OutfitType.STEAMPUNK],
        "colors": BROWNS + BLACKS + EARTH_TONES + ["flowing", "dramatic", "western"],
        "fullBody": True
    },
    "cape dress": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.AVANT_GARDE],
        "colors": BLACKS + JEWEL_TONES + ["dramatic", "flowing", "cape-like"],
        "fullBody": True
    },
    "cloak dress": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.FANTASY],
        "colors": BLACKS + PURPLES + JEWEL_TONES + ["hooded", "mysterious", "layered"],
        "fullBody": True
    },
    "poncho dress": {
        "types": [OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC],
        "colors": EARTH_TONES + PATTERNS + ["draped", "flowing", "southwestern"],
        "fullBody": True
    },
    "kaftan": {
        "types": [OutfitType.BOHEMIAN, OutfitType.BEACH_WEAR, OutfitType.ETHEREAL],
        "colors": JEWEL_TONES + PATTERNS + EARTH_TONES + ["flowing", "full-length", "ornate"],
        "fullBody": True
    },
    "kimono robe dress": {
        "types": [OutfitType.ETHEREAL, OutfitType.MINIMALIST, OutfitType.ROMANTIC],
        "colors": PASTELS + JEWEL_TONES + PATTERNS + ["silk", "flowing", "elegant"],
        "fullBody": True
    },
    "abaya": {
        "types": [OutfitType.MINIMALIST, OutfitType.ETHEREAL],
        "colors": BLACKS + GRAYS + JEWEL_TONES + ["modest", "flowing", "cultural"],
        "fullBody": True
    },
    "djellaba": {
        "types": [OutfitType.ETHEREAL, OutfitType.MINIMALIST],
        "colors": WHITES + EARTH_TONES + JEWEL_TONES + ["hooded", "flowing", "traditional"],
        "fullBody": True
    },
    "monk's robe": {
        "types": [OutfitType.MINIMALIST, OutfitType.GOTHIC, OutfitType.ETHEREAL],
        "colors": BROWNS + GRAYS + BLACKS + ["simple", "hooded", "monastic"],
        "fullBody": True
    },
    "wizard robe": {
        "types": [OutfitType.GOTHIC, OutfitType.ETHEREAL, OutfitType.FESTIVAL],
        "colors": PURPLES + BLACKS + JEWEL_TONES + ["mystical", "flowing", "ornate"],
        "fullBody": True
    },
    
    # Avant-garde and experimental
    "cage dress": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY],
        "colors": BLACKS + METALLICS + ["strappy", "geometric", "architectural"],
        "fullBody": True
    },
    "hoop skirt gown": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.RETRO],
        "colors": PASTELS + JEWEL_TONES + ["crinoline", "voluminous", "historical"],
        "fullBody": True
    },
    "bustle gown": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.STEAMPUNK, OutfitType.ROMANTIC],
        "colors": JEWEL_TONES + EARTH_TONES + ["Victorian", "structured", "dramatic"],
        "fullBody": True
    },
    "petticoat statement look": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.ROMANTIC, OutfitType.RETRO],
        "colors": WHITES + PASTELS + ["voluminous", "undergarment", "statement"],
        "fullBody": True
    },
    "transparent PVC dress": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY],
        "colors": ["clear", "transparent"] + NEONS + ["futuristic", "plastic"],
        "fullBody": True
    },
    "inflatable dress": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.FESTIVAL, OutfitType.CYBERPUNK],
        "colors": NEONS + METALLICS + ["inflatable", "sculptural", "experimental"],
        "fullBody": True
    },
    "LED-embedded dress": {
        "types": [OutfitType.CYBERPUNK, OutfitType.FESTIVAL, OutfitType.AVANT_GARDE],
        "colors": NEONS + BLACKS + ["light-up", "electronic", "futuristic"],
        "fullBody": True
    },
    "chainmail dress": {
        "types": [OutfitType.GOTHIC, OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE],
        "colors": METALLICS + BLACKS + ["metal", "armor", "textured"],
        "fullBody": True
    },
    "feather gown": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE, OutfitType.ETHEREAL],
        "colors": WHITES + BLACKS + JEWEL_TONES + ["feathered", "textured", "luxurious"],
        "fullBody": True
    },
    "latex gown": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK],
        "colors": BLACKS + REDS + METALLICS + ["latex", "shiny", "fitted"],
        "fullBody": True
    },
    "sculptural origami dress": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.EVENING_FORMAL],
        "colors": WHITES + BLACKS + GRAYS + ["geometric", "folded", "architectural"],
        "fullBody": True
    },
    "exaggerated shoulder dress": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.RETRO, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + JEWEL_TONES + ["dramatic", "1980s", "structured"],
        "fullBody": True
    },
    "quilted full-body outfit": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.MINIMALIST, OutfitType.COTTAGECORE],
        "colors": EARTH_TONES + PASTELS + ["quilted", "textured", "padded"],
        "fullBody": True
    },
    "deconstructed patchwork gown": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.GRUNGE, OutfitType.PUNK],
        "colors": BLACKS + GRAYS + EARTH_TONES + ["patchwork", "deconstructed", "artistic"],
        "fullBody": True
    },
    "harness bodysuit look": {
        "types": [OutfitType.CYBERPUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + METALLICS + ["strappy", "edgy", "bondage-inspired"],
        "fullBody": True
    },
    "wrapped fabric body look": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.ETHEREAL, OutfitType.MINIMALIST],
        "colors": WHITES + GRAYS + EARTH_TONES + ["draped", "experimental", "couture"],
        "fullBody": True
    }
}
