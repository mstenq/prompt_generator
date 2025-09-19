"""
Clothing data definitions for the ComfyUI Outfit Generator.
This file contains clothing items tagged with their compatible outfit types and color palettes.
"""

from ..enums import OutfitType
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
    "halter neck top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + JEWEL_TONES + ["halter neck", "tie neck", "elegant"]
    },
    "high-neck bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["high neckline", "modest coverage", "athletic"]
    },
    "bandeau bikini top": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["strapless", "bandeau"]
    },
    "bandeau top (strapless)": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + JEWEL_TONES + ["strapless", "bandeau", "minimal"]
    },
    "bandeau with tie front": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["tie detail", "bandeau", "adjustable"]
    },
    "bandeau with shoulder straps": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["detachable straps", "bandeau", "supportive"]
    },
    "bralette bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.LINGERIE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["bralette", "comfortable", "wireless"]
    },
    "underwire bikini top": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + JEWEL_TONES + ["underwire", "supportive", "structured"]
    },
    "push-up bikini top": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["push-up", "enhancing", "padded"]
    },
    "balconette bikini top": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + JEWEL_TONES + ["balconette", "half-cup", "vintage-inspired"]
    },
    "plunge bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["deep V", "plunging neckline", "dramatic"]
    },
    "one-shoulder bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + JEWEL_TONES + ["asymmetrical", "one-shoulder", "modern"]
    },
    "asymmetrical strap bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.AVANT_GARDE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["asymmetrical straps", "unique design", "architectural"]
    },
    "off-the-shoulder bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + PATTERNS + NEONS + ["off-shoulder", "romantic", "feminine"]
    },
    "strappy cage bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + NEONS + PATTERNS + ["cage design", "strappy", "edgy"]
    },
    "multi-strap crisscross bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["crisscross straps", "athletic", "trendy"]
    },
    "wrap-around bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + EARTH_TONES + ["wrap style", "adjustable", "bohemian"]
    },
    "tie-front bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["tie front", "cute", "adjustable"]
    },
    "knot-front bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["knot detail", "front tie", "feminine"]
    },
    "zip-front bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + METALLICS + ["zip closure", "sporty", "modern"]
    },
    "cut-out bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["cut-out details", "revealing", "sexy"]
    },
    "sporty racerback bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + BLUES + GRAYS + ["racerback", "athletic", "sporty"]
    },
    "athletic crop bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + GRAYS + ["crop top", "athletic", "performance"]
    },
    "tankini top (short tank style)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["modest coverage", "tank style", "comfortable"]
    },
    "longline bikini top (extra torso coverage)": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["longline", "extra coverage", "modest"]
    },
    "crop top bikini": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["crop style", "trendy", "casual"]
    },
    "mesh panel bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + NEONS + ["mesh inserts", "athletic", "modern"]
    },
    "sheer overlay bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + BLACKS + ["sheer fabric", "romantic", "layered"]
    },
    "ruffle bikini top (frilly trim)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + PATTERNS + PINKS + ["ruffles", "feminine", "playful"]
    },
    "fringe bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + EARTH_TONES + ["fringe detail", "bohemian", "movement"]
    },
    "peplum bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.RETRO],
        "colors": BLACKS + WHITES + PASTELS + PATTERNS + JEWEL_TONES + ["peplum hem", "vintage", "flattering"]
    },
    "embellished/sequin bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY, OutfitType.FESTIVAL],
        "colors": METALLICS + JEWEL_TONES + BLACKS + WHITES + ["sequins", "beading", "glamorous"]
    },
    "metallic bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY, OutfitType.FESTIVAL],
        "colors": METALLICS + ["gold", "silver", "bronze", "copper", "shimmery", "metallic finish"]
    },
    "crochet bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.FESTIVAL],
        "colors": WHITES + EARTH_TONES + PASTELS + NEONS + ["handmade", "crochet", "bohemian", "textured"]
    },
    "macramé bikini top": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.FESTIVAL],
        "colors": WHITES + EARTH_TONES + BROWNS + ["macramé", "rope design", "bohemian", "artisanal"]
    },
    "classic one-piece swimsuit (scoop neck, full coverage)": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["classic", "scoop neck", "full coverage"],
        "fullBody": True
    },
    "tank suit swimsuit (sporty, thicker straps)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + BLUES + GRAYS + ["sporty", "thick straps", "athletic"],
        "fullBody": True
    },
    "high-neck one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["high neckline", "modest", "athletic"],
        "fullBody": True
    },
    "square-neck swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.RETRO],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["square neckline", "vintage", "structured"],
        "fullBody": True
    },
    "halter one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + JEWEL_TONES + ["halter neck", "supportive", "elegant"],
        "fullBody": True
    },
    "strapless bandeau one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["strapless", "bandeau", "minimal tan lines"],
        "fullBody": True
    },
    "strapless bandeau with detachable straps swimsuit": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["convertible", "detachable straps", "versatile"],
        "fullBody": True
    },
    "plunge neckline one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["deep V", "plunging", "dramatic"],
        "fullBody": True
    },
    "V-neck one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + JEWEL_TONES + ["V-neckline", "flattering", "classic"],
        "fullBody": True
    },
    "U-back one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["U-back", "sporty", "back detail"],
        "fullBody": True
    },
    "high-cut leg one-piece swimsuit (80s inspired)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.RETRO],
        "colors": NEONS + BLACKS + WHITES + PATTERNS + ["high-cut", "80s", "retro", "bold"],
        "fullBody": True
    },
    "high-waist vintage-style one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.RETRO],
        "colors": BLACKS + WHITES + PASTELS + PATTERNS + JEWEL_TONES + ["high-waisted", "vintage", "pin-up", "retro"],
        "fullBody": True
    },
    "one-shoulder one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + JEWEL_TONES + ["asymmetrical", "one-shoulder", "modern"],
        "fullBody": True
    },
    "asymmetrical cut one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.AVANT_GARDE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["asymmetrical", "unique cut", "architectural"],
        "fullBody": True
    },
    "cut-out one-piece swimsuit (side cutouts)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["side cutouts", "revealing", "sexy"],
        "fullBody": True
    },
    "monokini (deep side cutouts)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + NEONS + PATTERNS + ["deep cutouts", "monokini", "dramatic", "bold"],
        "fullBody": True
    },
    "wrap-front swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + EARTH_TONES + ["wrap front", "adjustable", "flattering"],
        "fullBody": True
    },
    "knot-front one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["knot detail", "front tie", "cute"],
        "fullBody": True
    },
    "tie-front one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["tie front", "adjustable", "bohemian"],
        "fullBody": True
    },
    "belted swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.RETRO],
        "colors": BLACKS + WHITES + PASTELS + PATTERNS + JEWEL_TONES + ["belted", "defined waist", "vintage"],
        "fullBody": True
    },
    "ring-detail one-piece swimsuit (metal hoops on sides/center)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + NEONS + METALLICS + ["metal rings", "hardware", "edgy"],
        "fullBody": True
    },
    "lace-up front one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["lace-up", "adjustable", "sexy"],
        "fullBody": True
    },
    "lace-up sides one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["side lacing", "adjustable", "strappy"],
        "fullBody": True
    },
    "zip-front one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + METALLICS + ["zip closure", "sporty", "modern"],
        "fullBody": True
    },
    "longline torso swimsuit (extra coverage)": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["longline", "extra coverage", "modest"],
        "fullBody": True
    },
    "backless one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["open back", "backless", "dramatic"],
        "fullBody": True
    },
    "open-back with cross straps swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["cross straps", "open back", "athletic"],
        "fullBody": True
    },
    "sheer panel swimsuit (mesh details)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + NEONS + ["mesh panels", "sheer inserts", "modern"],
        "fullBody": True
    },
    "embellished swimsuit (sequins, beads)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY, OutfitType.FESTIVAL],
        "colors": METALLICS + JEWEL_TONES + BLACKS + WHITES + ["sequins", "beading", "glamorous"],
        "fullBody": True
    },
    "metallic swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY, OutfitType.FESTIVAL],
        "colors": METALLICS + ["gold", "silver", "bronze", "copper", "shimmery", "metallic finish"],
        "fullBody": True
    },
    "holographic swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY, OutfitType.FESTIVAL],
        "colors": ["holographic", "iridescent", "rainbow", "prismatic", "futuristic"],
        "fullBody": True
    },
    "patterned/crochet overlay one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.FESTIVAL],
        "colors": WHITES + EARTH_TONES + PASTELS + PATTERNS + ["crochet overlay", "textured", "bohemian"],
        "fullBody": True
    },
    "racerback one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + BLUES + GRAYS + ["racerback", "athletic", "sporty"],
        "fullBody": True
    },
    "high-neck racerback swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + GRAYS + ["high neck", "racerback", "performance", "modest"],
        "fullBody": True
    },
    "competition swimsuit (streamlined, full coverage)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + BLUES + GRAYS + ["competition", "streamlined", "performance"],
        "fullBody": True
    },
    "surfsuit (long-sleeve, zip-up)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + BLUES + ["long sleeve", "zip-up", "UV protection", "surfing"],
        "fullBody": True
    },
    "short-sleeve surf swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + BLUES + ["short sleeve", "surf style", "UV protection"],
        "fullBody": True
    },
    "swim bodysuit (athletic stretch, high coverage)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + GRAYS + ["athletic", "stretch", "high coverage", "performance"],
        "fullBody": True
    },
    "ruffle trim one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + PATTERNS + PINKS + ["ruffle trim", "feminine", "playful"],
        "fullBody": True
    },
    "fringe one-piece swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + NEONS + EARTH_TONES + ["fringe detail", "bohemian", "movement"],
        "fullBody": True
    },
    "peplum swimsuit": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.RETRO],
        "colors": BLACKS + WHITES + PASTELS + PATTERNS + JEWEL_TONES + ["peplum hem", "vintage", "flattering"],
        "fullBody": True
    },
    "skirted one-piece swimsuit (swimdress)": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + PASTELS + PATTERNS + JEWEL_TONES + ["skirted", "modest", "swimdress"],
        "fullBody": True
    },
    "swim romper swimsuit (shorts + top one-piece)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["romper style", "shorts", "playful"],
        "fullBody": True
    },
    "swim unitard swimsuit (shorts style)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + GRAYS + ["unitard", "shorts style", "athletic", "coverage"],
        "fullBody": True
    },
    "swim leggings bodysuit swimsuit(full coverage)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + GRAYS + ["leggings", "full coverage", "modest", "athletic"],
        "fullBody": True
    },
    "convertible swimsuit (removable straps or wrap ties)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["convertible", "removable straps", "versatile"],
        "fullBody": True
    },
    "sheer maxi overlay one-piece swimsuit (lingerie-inspired)": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC, OutfitType.LINGERIE],
        "colors": WHITES + PASTELS + BLACKS + ["sheer overlay", "maxi length", "lingerie-inspired", "romantic"],
        "fullBody": True
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
    },
    
    # Lingerie and Intimate Wear
    "classic underwire bra": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC],
        "colors": WHITES + BLACKS + PASTELS + PINKS + ["lace", "satin", "cotton"]
    },
    "push-up bra": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.CLUB_PARTY],
        "colors": WHITES + BLACKS + PINKS + REDS + ["lace", "satin", "padded"]
    },
    "balconette bra": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.PIN_UP],
        "colors": WHITES + BLACKS + PINKS + REDS + ["lace", "satin", "half-cup"]
    },
    "plunge bra": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.CLUB_PARTY],
        "colors": WHITES + BLACKS + PINKS + JEWEL_TONES + ["deep V", "lace", "satin"]
    },
    "T-shirt seamless bra": {
        "types": [OutfitType.LINGERIE, OutfitType.CASUAL_CHIC],
        "colors": WHITES + BLACKS + PASTELS + ["seamless", "smooth", "cotton blend"]
    },
    "half-cup bra": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.PIN_UP],
        "colors": WHITES + BLACKS + PINKS + REDS + ["demi-cup", "lace", "satin"]
    },
    "full-cup bra": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC],
        "colors": WHITES + BLACKS + PASTELS + BROWNS + ["full coverage", "cotton", "lace"]
    },
    "longline bra": {
        "types": [OutfitType.LINGERIE, OutfitType.VINTAGE, OutfitType.PIN_UP],
        "colors": WHITES + BLACKS + REDS + JEWEL_TONES + ["vintage style", "boned", "satin"]
    },
    "strapless bra": {
        "types": [OutfitType.LINGERIE, OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY],
        "colors": WHITES + BLACKS + PASTELS + ["strapless", "adhesive", "silicone"]
    },
    "convertible multi-way bra": {
        "types": [OutfitType.LINGERIE, OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY],
        "colors": WHITES + BLACKS + PASTELS + ["convertible straps", "versatile", "seamless"]
    },
    "adhesive sticky cup bra": {
        "types": [OutfitType.LINGERIE, OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY],
        "colors": WHITES + BLACKS + PASTELS + ["adhesive", "backless", "silicone"]
    },
    "lace bralette": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.BOHEMIAN],
        "colors": WHITES + BLACKS + PASTELS + PINKS + ["delicate lace", "wireless", "soft"]
    },
    "satin bralette": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "colors": WHITES + BLACKS + PASTELS + JEWEL_TONES + ["silk", "satin", "smooth"]
    },
    "sheer mesh bralette": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": BLACKS + WHITES + JEWEL_TONES + ["sheer", "mesh", "see-through"]
    },
    "racerback bralette": {
        "types": [OutfitType.LINGERIE, OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "colors": WHITES + BLACKS + PASTELS + GRAYS + ["sporty", "racerback", "cotton"]
    },
    "triangle bralette": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "colors": WHITES + BLACKS + PASTELS + PINKS + ["minimal", "wireless", "soft"]
    },
    "cage strappy bra": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + JEWEL_TONES + ["strappy", "harness", "elastic bands"]
    },
    "harness bondage-inspired bra": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + METALLICS + ["leather", "straps", "hardware"]
    },
    "open-cup bra": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC],
        "colors": BLACKS + REDS + JEWEL_TONES + ["open design", "lace", "satin"]
    },
    "peekaboo cutout bra": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.ROMANTIC],
        "colors": BLACKS + REDS + PINKS + ["cutout details", "playful", "lace"]
    },
    "quarter-cup bra": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.PIN_UP],
        "colors": BLACKS + REDS + PINKS + JEWEL_TONES + ["minimal coverage", "lace", "satin"]
    },
    "shelf bra": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.PIN_UP],
        "colors": BLACKS + REDS + WHITES + ["supportive", "underwire", "lace"]
    },
    "lace-up boned corset top": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.VINTAGE, OutfitType.STEAMPUNK],
        "colors": BLACKS + REDS + JEWEL_TONES + BROWNS + ["boned", "lace-up", "structured"]
    },
    "bustier top": {
        "types": [OutfitType.LINGERIE, OutfitType.EVENING_FORMAL, OutfitType.VINTAGE],
        "colors": BLACKS + REDS + JEWEL_TONES + METALLICS + ["strapless", "boned", "satin"]
    },
    "underbust corset": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.STEAMPUNK],
        "colors": BLACKS + BROWNS + REDS + JEWEL_TONES + ["underbust", "boned", "lace-up"]
    },
    "overbust corset": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.VINTAGE, OutfitType.STEAMPUNK],
        "colors": BLACKS + REDS + JEWEL_TONES + BROWNS + ["full bust", "boned", "structured"]
    },
    "bandeau lingerie top": {
        "types": [OutfitType.LINGERIE, OutfitType.BEACH_WEAR, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + PINKS + JEWEL_TONES + ["strapless", "bandeau", "lace"]
    },
    "sheer flowy baby doll top": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + PASTELS + PINKS + ["sheer", "flowing", "delicate"]
    },
    "silk satin camisole": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "colors": WHITES + BLACKS + PASTELS + JEWEL_TONES + ["silk", "satin", "luxury"]
    },
    "lace trim camisole": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + PASTELS + PINKS + ["lace details", "delicate", "feminine"]
    },
    "chemise slip top": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["slip style", "satin", "flowing"]
    },
    "halter lingerie top": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.ROMANTIC],
        "colors": BLACKS + REDS + JEWEL_TONES + ["halter neck", "tied", "revealing"]
    },
    "halter teddy top": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + PINKS + JEWEL_TONES + ["one-piece style", "halter", "lace"]
    },
    "mesh crop lingerie top": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": BLACKS + WHITES + NEONS + ["mesh", "cropped", "sheer"]
    },
    "see-through lace blouse": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + BLACKS + PASTELS + ["transparent", "delicate lace", "feminine"]
    },
    "bra with choker strap": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + METALLICS + ["choker detail", "strappy", "hardware"]
    },
    "bra with garter harness straps": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + JEWEL_TONES + ["garter straps", "harness", "elastic"]
    },
    "pasties with chain harness": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": BLACKS + METALLICS + JEWEL_TONES + ["chain details", "minimal", "hardware"]
    },
    "open-front lingerie robe top": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["open front", "flowing", "sheer"]
    },
    "sheer mesh lace bolero shrug": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + BLACKS + PASTELS + ["sheer", "delicate", "cropped jacket"]
    },
    
    # Full Body Lingerie
    "bodysuit": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.ROMANTIC],
        "colors": WHITES + BLACKS + PASTELS + JEWEL_TONES + ["lace", "mesh", "satin", "silk", "cutout details"],
        "fullBody": True
    },
    "teddy": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.CLUB_PARTY],
        "colors": WHITES + BLACKS + PINKS + REDS + JEWEL_TONES + ["classic lace", "satin", "silk", "mesh sheer", "halter style", "plunge neckline", "strappy", "cage", "open-crotch", "backless"],
        "fullBody": True
    },
    "corset bodysuit": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.VINTAGE],
        "colors": BLACKS + REDS + JEWEL_TONES + BROWNS + ["boned", "lace-up", "structured"],
        "fullBody": True
    },
    "bustier bodysuit": {
        "types": [OutfitType.LINGERIE, OutfitType.EVENING_FORMAL, OutfitType.VINTAGE],
        "colors": BLACKS + REDS + JEWEL_TONES + METALLICS + ["strapless", "boned", "structured"],
        "fullBody": True
    },
    "longline corset dress": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.VINTAGE, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + REDS + JEWEL_TONES + BROWNS + ["floor-length", "boned", "lace-up"],
        "fullBody": True
    },
    "chemise slip dress": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + PASTELS + PINKS + JEWEL_TONES + ["short slip", "lace trim", "delicate"],
        "fullBody": True
    },
    "baby doll dress": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + PASTELS + PINKS + ["sheer", "flowy skirt", "empire waist"],
        "fullBody": True
    },
    "negligee dress": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["luxury slip", "sheer", "satin", "flowing"],
        "fullBody": True
    },
    "nightgown": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["floor-length", "flowing", "satin", "silk"],
        "fullBody": True
    },
    "lingerie robe dress": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["sheer", "lace", "satin wrap", "belted"],
        "fullBody": True
    },
    "kimono lingerie robe": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + PASTELS + JEWEL_TONES + REDS + ["silk", "satin", "embroidered", "wide sleeves"],
        "fullBody": True
    },
    "sheer caftan lingerie wrap": {
        "types": [OutfitType.LINGERIE, OutfitType.ETHEREAL, OutfitType.BEACH_WEAR],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["flowing", "sheer", "oversized"],
        "fullBody": True
    },
    "see-through maxi slip dress": {
        "types": [OutfitType.LINGERIE, OutfitType.ETHEREAL, OutfitType.CLUB_PARTY],
        "colors": WHITES + BLACKS + JEWEL_TONES + ["transparent", "floor-length", "bias cut"],
        "fullBody": True
    },
    "lace peignoir set": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + PASTELS + PINKS + ["robe and gown", "matching set", "delicate lace"],
        "fullBody": True
    },
    "harness bodysuit": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + METALLICS + ["leather", "straps", "hardware", "buckles"],
        "fullBody": True
    },
    "cage teddy": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + JEWEL_TONES + ["strappy", "geometric", "elastic bands"],
        "fullBody": True
    },
    "strappy lingerie catsuit": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + METALLICS + ["full coverage", "strappy details", "form-fitting"],
        "fullBody": True
    },
    "sheer bodysuit with garter harness": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + JEWEL_TONES + ["sheer", "garter straps", "harness"],
        "fullBody": True
    },
    "lingerie unitard": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": BLACKS + WHITES + JEWEL_TONES + ["lace", "mesh", "long sleeves"],
        "fullBody": True
    },
    "cutout bodysuit with garters": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + JEWEL_TONES + ["strategic cutouts", "attached garters", "strappy"],
        "fullBody": True
    },
    "strappy open bodysuit": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + METALLICS + ["open design", "strappy", "minimal coverage"],
        "fullBody": True
    },
    "bodystocking": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.GOTHIC],
        "colors": BLACKS + WHITES + JEWEL_TONES + ["full fishnet", "lace pattern", "opaque mesh combo", "crotchless", "halter style", "garter cutouts", "attached gloves"],
        "fullBody": True
    },
    "sheer catsuit bodystocking": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": BLACKS + WHITES + NEONS + ["full body", "sheer", "form-fitting"],
        "fullBody": True
    },
    "strappy bondage bodystocking": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + METALLICS + ["bondage style", "strappy", "hardware"],
        "fullBody": True
    },
    "satin slip dress": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.MINIMALIST],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["bias cut", "satin", "lingerie version"],
        "fullBody": True
    },
    "silk gown with thigh slit": {
        "types": [OutfitType.LINGERIE, OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "colors": WHITES + JEWEL_TONES + METALLICS + ["silk", "high slit", "floor-length"],
        "fullBody": True
    },
    "embroidered mesh dress": {
        "types": [OutfitType.LINGERIE, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["embroidered", "mesh", "delicate"],
        "fullBody": True
    },
    "sequin lingerie gown": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + JEWEL_TONES + METALLICS + ["sequined", "glamorous", "sparkling"],
        "fullBody": True
    },
    "sheer rhinestone mesh dress": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + WHITES + METALLICS + ["rhinestones", "sheer mesh", "sparkling"],
        "fullBody": True
    },
    "pearl-embellished teddy": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["pearl details", "luxury", "embellished"],
        "fullBody": True
    },
    "feather-trimmed robe dress": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["feather trim", "flowing", "luxury"],
        "fullBody": True
    },
    "velvet lingerie slip": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": JEWEL_TONES + REDS + BLACKS + ["velvet", "luxury", "rich texture"],
        "fullBody": True
    },
    "lingerie playsuit romper": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.ROMANTIC],
        "colors": WHITES + BLACKS + PINKS + JEWEL_TONES + ["short", "strappy", "playful"],
        "fullBody": True
    },
    "mini dress teddy hybrid": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.ROMANTIC],
        "colors": BLACKS + REDS + JEWEL_TONES + ["mini length", "dress style", "form-fitting"],
        "fullBody": True
    },
    "schoolgirl lingerie dress": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.KAWAII],
        "colors": WHITES + BLACKS + BLUES + ["plaid skirt", "attached top", "costume style"],
        "fullBody": True
    },
    "maid lingerie outfit": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.KAWAII],
        "colors": WHITES + BLACKS + ["apron-style", "teddy", "costume", "frilly"],
        "fullBody": True
    },
    "nurse lingerie costume": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.KAWAII],
        "colors": WHITES + REDS + ["nurse costume", "bodysuit", "medical theme"],
        "fullBody": True
    },
    "bunny teddy costume": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.KAWAII],
        "colors": WHITES + BLACKS + PINKS + ["corset", "tail accessory", "ears", "bunny theme"],
        "fullBody": True
    },
    "cat lingerie set": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.KAWAII],
        "colors": BLACKS + WHITES + JEWEL_TONES + ["bodysuit", "tail accessory", "ears", "cat theme"],
        "fullBody": True
    },
    "sheer superhero teddy": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.FANTASY],
        "colors": REDS + BLUES + METALLICS + ["superhero inspired", "sheer", "cape details"],
        "fullBody": True
    },
    "latex catsuit": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + METALLICS + ["latex", "full coverage", "shiny", "form-fitting"],
        "fullBody": True
    },
    "triangle top with string tie sides bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["triangle bikini", "string ties", "minimal coverage"],
        "fullBody": True
    },
    "bandeau top with high-cut cheeky bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["bandeau", "high-cut", "cheeky", "strapless"],
        "fullBody": True
    },
    "halter top with classic bikini brief bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["halter", "classic", "bikini brief"],
        "fullBody": True
    },
    "underwire balconette top with low-rise hipster bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["underwire", "balconette", "low-rise", "hipster"],
        "fullBody": True
    },
    "one-shoulder top with minimal Brazilian bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["one-shoulder", "asymmetrical", "Brazilian", "minimal"],
        "fullBody": True
    },
    "sporty crop top with boyshort bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["sporty", "crop top", "boyshort", "athletic"],
        "fullBody": True
    },
    "tie-front knot top with ruched side-tie bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["tie-front", "knot detail", "ruched", "side-tie"],
        "fullBody": True
    },
    "push-up padded top with skimpy thong bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["push-up", "padded", "skimpy", "thong"],
        "fullBody": True
    },
    "mesh overlay bralette top with strappy cut-out bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["mesh overlay", "bralette", "strappy", "cut-out"],
        "fullBody": True
    },
    "ruffled bandeau top with high-waist retro bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.RETRO],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["ruffled", "bandeau", "high-waist", "retro"],
        "fullBody": True
    },
    "triangle crochet top with tie-side crochet bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN],
        "colors": WHITES + PASTELS + EARTH_TONES + ["crochet", "triangle", "tie-side", "handmade"],
        "fullBody": True
    },
    "chain strap triangle top with chain-link thong bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + METALLICS + NEONS + ["chain strap", "triangle", "chain-link", "metallic"],
        "fullBody": True
    },
    "cut-out halter top with cut-out Brazilian bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["cut-out", "halter", "Brazilian", "revealing"],
        "fullBody": True
    },
    "asymmetrical strap top with ruched micro bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["asymmetrical", "strap detail", "ruched", "micro"],
        "fullBody": True
    },
    "front zipper sporty top with cheeky surf short bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["front zipper", "sporty", "cheeky", "surf shorts"],
        "fullBody": True
    },
    "lace bralette bikini top with lace-trimmed hipster bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + PINKS + TEXTURES + ["lace", "bralette", "lace-trimmed", "hipster"],
        "fullBody": True
    },
    "triangle microkini top with ultra-minimal string bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["triangle", "microkini", "ultra-minimal", "string"],
        "fullBody": True
    },
    "strapless bandeau with O-ring detail bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + METALLICS + ["strapless", "bandeau", "O-ring", "hardware detail"],
        "fullBody": True
    },
    "crisscross wrap top with wrap-around strap thong bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["crisscross", "wrap", "wrap-around strap", "thong"],
        "fullBody": True
    },
    "padded balconette bikini top with adjustable scrunch bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["padded", "balconette", "adjustable", "scrunch"],
        "fullBody": True
    },
    "macramé bikini top with fringe-trimmed bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN],
        "colors": WHITES + PASTELS + EARTH_TONES + ["macramé", "fringe-trimmed", "handcrafted", "boho"],
        "fullBody": True
    },
    "metallic chainmail-style triangle top with chain-link G-string bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": METALLICS + BLACKS + WHITES + ["metallic", "chainmail", "triangle", "chain-link", "G-string"],
        "fullBody": True
    },
    "sport racerback bikini top with seamless V-cut bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["sport", "racerback", "seamless", "V-cut"],
        "fullBody": True
    },
    "off-the-shoulder ruffle sleeve top with high-leg cheeky bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + PINKS + PATTERNS + ["off-the-shoulder", "ruffle sleeve", "high-leg", "cheeky"],
        "fullBody": True
    },
    "triangle leather-look top with strappy bondage-style bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.GOTHIC],
        "colors": BLACKS + REDS + METALLICS + TEXTURES + ["leather-look", "triangle", "strappy", "bondage-style"],
        "fullBody": True
    },
    "sheer mesh triangle top with layered string bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + ["sheer mesh", "triangle", "layered", "string"],
        "fullBody": True
    },
    "zip-front bustier bikini top with high-waist shaping bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.RETRO],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["zip-front", "bustier", "high-waist", "shaping"],
        "fullBody": True
    },
    "deep plunge halter top with adjustable slider thong bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["deep plunge", "halter", "adjustable slider", "thong"],
        "fullBody": True
    },
    "knitted crochet halter top with tassel-trimmed bikini bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN],
        "colors": WHITES + PASTELS + EARTH_TONES + ["knitted crochet", "halter", "tassel-trimmed", "handmade"],
        "fullBody": True
    },
    "scallop-edge bralette top with scallop-edge hipster bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + PINKS + PATTERNS + ["scallop-edge", "bralette", "hipster", "detailed trim"],
        "fullBody": True
    },
    "triangle top with dangling chain charms and tie-side bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + METALLICS + NEONS + ["triangle", "dangling chain", "charms", "tie-side"],
        "fullBody": True
    },
    "strapless twist bandeau with Brazilian cut ruched bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["strapless", "twist bandeau", "Brazilian cut", "ruched"],
        "fullBody": True
    },
    "high-neck halter top with mesh-insert bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["high-neck", "halter", "mesh-insert", "sporty"],
        "fullBody": True
    },
    "minimal coverage microkini triangle top with micro thong bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["minimal coverage", "microkini", "triangle", "micro thong"],
        "fullBody": True
    },
    "ring-detail triangle top with triple-strap ring bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + METALLICS + NEONS + ["ring-detail", "triangle", "triple-strap", "hardware"],
        "fullBody": True
    },
    "peekaboo cutout bandeau top with cutout strappy bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["peekaboo", "cutout", "bandeau", "strappy"],
        "fullBody": True
    },
    "adjustable drawstring bralette top with scrunch butt bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["adjustable", "drawstring", "bralette", "scrunch butt"],
        "fullBody": True
    },
    "bustier corset-style bikini top with lace-up thong bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.GOTHIC],
        "colors": BLACKS + REDS + METALLICS + TEXTURES + ["bustier", "corset-style", "lace-up", "thong"],
        "fullBody": True
    },
    "triangle velvet-look top with seamless thong bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": JEWEL_TONES + BLACKS + TEXTURES + ["triangle", "velvet-look", "seamless", "thong"],
        "fullBody": True
    },
    "keyhole halter bikini top with keyhole V-front bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["keyhole", "halter", "V-front", "cutout details"],
        "fullBody": True
    },
    "bralette bikini top with double-string tie-side bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["bralette", "double-string", "tie-side", "minimal"],
        "fullBody": True
    },
    "high-neck sports mesh bikini top with V-cut thong bottom": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["high-neck", "sports mesh", "V-cut", "thong"],
        "fullBody": True
    },
    "caged strap bralette top with caged strappy thong bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["caged strap", "bralette", "strappy", "thong"],
        "fullBody": True
    },
    "plunge balconette bikini top with high-rise cheeky thong bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["plunge", "balconette", "high-rise", "cheeky thong"],
        "fullBody": True
    },
    "adjustable slider micro triangle top with tie-front thong bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["adjustable slider", "micro triangle", "tie-front", "thong"],
        "fullBody": True
    },
    "cropped tankini-style bikini top with low-rise hipster bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["cropped tankini", "bikini top", "low-rise", "hipster"],
        "fullBody": True
    },
    "wrap-around halter bikini top with wrap strap thong bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["wrap-around", "halter", "wrap strap", "thong"],
        "fullBody": True
    },
    "padded push-up bandeau with seamless cheeky bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + NEONS + PASTELS + PATTERNS + ["padded", "push-up", "bandeau", "seamless cheeky"],
        "fullBody": True
    },
    "triangle bikini top with gold hardware accents and hipster bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + METALLICS + PASTELS + ["triangle", "gold hardware", "accents", "hipster"],
        "fullBody": True
    },
    "halter bikini top with detachable chains and cheeky cut bottom": {
        "types": [OutfitType.BEACH_WEAR],
        "colors": BLACKS + WHITES + METALLICS + NEONS + ["halter", "detachable chains", "cheeky cut", "hardware"],
        "fullBody": True
    }
}
