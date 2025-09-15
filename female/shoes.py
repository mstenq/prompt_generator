"""
Clothing data definitions for the ComfyUI Outfit Generator.
This file contains clothing items tagged with their compatible outfit types and color palettes.
"""

from ..outfit_types import OutfitType
from ..colors import *

# Shoes with their compatible outfit types and color palettes
FEMALE_SHOES = {
    "heels": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.PIN_UP],
        "colors": BLACKS + REDS + METALLICS + ["patent leather", "stiletto", "platform"]
    },
    "combat boots": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY, OutfitType.GOTHIC],
        "colors": BLACKS + BROWNS + ["leather", "steel toe", "lace-up"]
    },
    "sneakers": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "colors": WHITES + BLACKS + NEONS + ["high-top", "chunky", "minimalist"]
    },
    "sandals": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.FESTIVAL],
        "colors": BROWNS + METALLICS + ["strappy", "gladiator", "platform"]
    },
    "boots": {
        "types": [OutfitType.COWBOY, OutfitType.STEAMPUNK, OutfitType.COTTAGECORE, OutfitType.GOTHIC],
        "colors": BROWNS + BLACKS + ["leather", "pointed toe", "ankle", "knee-high"]
    },
    "loafers": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + BLACKS + ["penny loafers", "tasseled"]
    },
    "mary janes": {
        "types": [OutfitType.LOLITA, OutfitType.KAWAII, OutfitType.COTTAGECORE, OutfitType.PIN_UP],
        "colors": BLACKS + REDS + PASTELS + ["patent leather", "T-bar"]
    },
    "platform shoes": {
        "types": [OutfitType.PUNK, OutfitType.CLUB_PARTY, OutfitType.GOTHIC, OutfitType.LOLITA],
        "colors": BLACKS + METALLICS + NEONS + ["chunky", "extreme height"]
    },
    "flip-flops": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + WHITES + NEONS + ["rubber", "embellished"]
    },
    "oxford shoes": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "colors": BLACKS + BROWNS + ["leather", "lace-up", "wingtip"]
    },
    "ballet flats": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.KAWAII],
        "colors": BLACKS + PASTELS + METALLICS + ["pointed toe", "bow detail"]
    },
    "cowboy boots": {
        "types": [OutfitType.COWBOY, OutfitType.FESTIVAL, OutfitType.ROCKABILLY],
        "colors": BROWNS + BLACKS + ["tooled leather", "pointed toe", "stacked heel"]
    },
    
    # Heel variations
    "stiletto pumps": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.BUSINESS_WEAR, OutfitType.PIN_UP],
        "colors": BLACKS + REDS + METALLICS + ["patent leather", "stiletto", "ultra-high"]
    },
    "classic pumps": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + BROWNS + GRAYS + ["mid-heel", "leather", "suede"]
    },
    "block heels": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": BLACKS + BROWNS + METALLICS + ["chunky", "stable", "square heel"]
    },
    "kitten heels": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "colors": BLACKS + PASTELS + METALLICS + ["low heel", "delicate", "pointed toe"]
    },
    "slingback heels": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + BROWNS + METALLICS + ["ankle strap", "open back"]
    },
    "peep-toe heels": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.PIN_UP],
        "colors": BLACKS + REDS + METALLICS + ["open toe", "revealing"]
    },
    "pointed-toe heels": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + METALLICS + ["sharp toe", "sleek"]
    },
    "round-toe heels": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "colors": BLACKS + BROWNS + PASTELS + ["comfortable", "classic"]
    },
    "mary jane heels": {
        "types": [OutfitType.LOLITA, OutfitType.KAWAII, OutfitType.PIN_UP, OutfitType.ROMANTIC],
        "colors": BLACKS + REDS + PASTELS + ["T-strap", "vintage", "sweet"]
    },
    "d'orsay pumps": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "colors": BLACKS + METALLICS + JEWEL_TONES + ["cut-out sides", "elegant"]
    },
    "platform heels": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "colors": BLACKS + METALLICS + NEONS + ["extreme height", "chunky"]
    },
    "wedge heels": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR],
        "colors": BROWNS + EARTH_TONES + ["cork", "rope", "woven"]
    },
    "espadrille wedges": {
        "types": [OutfitType.BOHEMIAN, OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": BROWNS + EARTH_TONES + ["jute", "canvas", "rope sole"]
    },
    "cork wedges": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "colors": BROWNS + EARTH_TONES + ["natural cork", "eco-friendly"]
    },
    "cone heels": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "colors": BLACKS + METALLICS + ["geometric", "architectural"]
    },
    "sculptural heels": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + METALLICS + SPECIAL + ["artistic", "geometric", "unusual shapes"]
    },
    "clear lucite heels": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL],
        "colors": ["clear", "transparent", "see-through", "acrylic"]
    },
    "mule heels": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + METALLICS + ["backless", "slip-on"]
    },
    "ankle-strap heels": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.PIN_UP],
        "colors": BLACKS + REDS + METALLICS + ["ankle wrap", "strappy"]
    },
    "strappy stilettos": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.GOTHIC],
        "colors": BLACKS + REDS + METALLICS + ["multiple straps", "bondage-inspired"]
    },
    "gladiator heels": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.AVANT_GARDE],
        "colors": BROWNS + METALLICS + ["lace-up", "warrior-inspired"]
    },
    "caged heels": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "colors": BLACKS + METALLICS + ["geometric straps", "architectural"]
    },
    "lace-up heels": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.AVANT_GARDE],
        "colors": BLACKS + REDS + ["corset-inspired", "bondage"]
    },
    "satin evening heels": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "colors": JEWEL_TONES + PASTELS + METALLICS + ["luxurious", "formal"]
    },
    "velvet pumps": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.GOTHIC],
        "colors": JEWEL_TONES + BLACKS + PURPLES + ["plush", "luxurious"]
    },
    "sequin heels": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL],
        "colors": METALLICS + SPECIAL + ["sparkly", "glamorous"]
    },
    "metallic heels": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "colors": METALLICS + SPECIAL + ["shimmery", "futuristic"]
    },
    "feather-trimmed heels": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": BLACKS + WHITES + PASTELS + ["feathered", "dramatic"]
    },
    
    # Boot variations
    "ankle boots": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.GRUNGE, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + BROWNS + ["leather", "suede", "versatile"]
    },
    "chelsea boots": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + ["elastic sides", "slip-on", "sleek"]
    },
    "military boots": {
        "types": [OutfitType.MILITARY, OutfitType.GRUNGE, OutfitType.PUNK],
        "colors": BLACKS + BROWNS + GREENS + ["tactical", "heavy duty"]
    },
    "tactical boots": {
        "types": [OutfitType.MILITARY, OutfitType.CYBERPUNK],
        "colors": BLACKS + GREENS + ["reinforced", "utility"]
    },
    "hiking boots": {
        "types": [OutfitType.ATHLEISURE, OutfitType.COTTAGECORE],
        "colors": BROWNS + GREENS + EARTH_TONES + ["outdoor", "rugged"]
    },
    "lace-up heeled boots": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.ROMANTIC],
        "colors": BLACKS + BROWNS + ["corset-style", "vintage"]
    },
    "platform ankle boots": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + METALLICS + ["chunky", "extreme height"]
    },
    "chunky heeled boots": {
        "types": [OutfitType.GRUNGE, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": BLACKS + BROWNS + ["thick heel", "90s inspired"]
    },
    "square-toe boots": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.AVANT_GARDE],
        "colors": BLACKS + BROWNS + GRAYS + ["geometric", "modern"]
    },
    "sock boots": {
        "types": [OutfitType.STREETWEAR, OutfitType.MINIMALIST, OutfitType.AVANT_GARDE],
        "colors": BLACKS + GRAYS + ["stretchy", "form-fitting"]
    },
    "mid-calf boots": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.COWBOY],
        "colors": BROWNS + BLACKS + ["mid-height", "versatile"]
    },
    "slouchy boots": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.GRUNGE],
        "colors": BROWNS + GRAYS + ["relaxed fit", "soft leather"]
    },
    "embroidered cowboy boots": {
        "types": [OutfitType.COWBOY, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "colors": BROWNS + BLACKS + ["decorative", "western"]
    },
    "fringe cowboy boots": {
        "types": [OutfitType.COWBOY, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "colors": BROWNS + EARTH_TONES + ["tasseled", "western"]
    },
    "riding boots": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "colors": BLACKS + BROWNS + ["equestrian", "tall", "leather"]
    },
    "knee-high boots flat": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + ["tall", "flat sole"]
    },
    "knee-high boots heeled": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + BROWNS + ["tall", "heeled"]
    },
    "over-the-knee boots": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.GOTHIC],
        "colors": BLACKS + BROWNS + ["thigh-high", "dramatic"]
    },
    "thigh-high boots flat": {
        "types": [OutfitType.STREETWEAR, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "colors": BLACKS + GRAYS + ["ultra-tall", "flat sole"]
    },
    "thigh-high stiletto boots": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.GOTHIC],
        "colors": BLACKS + REDS + ["ultra-tall", "stiletto heel"]
    },
    "latex thigh-high boots": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": BLACKS + REDS + ["latex material", "fetish"]
    },
    "vinyl thigh-high boots": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.CLUB_PARTY],
        "colors": BLACKS + METALLICS + ["vinyl material", "shiny"]
    },
    "lace-up thigh-highs": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + ["corset-style", "bondage-inspired"]
    },
    "peep-toe boots": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "colors": BLACKS + METALLICS + ["open toe", "unique"]
    },
    "cut-out boots": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.GOTHIC],
        "colors": BLACKS + METALLICS + ["decorative holes", "edgy"]
    },
    "harness boots": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.GRUNGE],
        "colors": BLACKS + BROWNS + ["buckled", "utilitarian"]
    },
    "biker boots": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.ROCKABILLY],
        "colors": BLACKS + BROWNS + ["buckled", "rugged"]
    },
    "punk studded boots": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.GRUNGE],
        "colors": BLACKS + METALLICS + ["studded", "rebellious"]
    },
    "goth platform boots": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.CLUB_PARTY],
        "colors": BLACKS + METALLICS + ["extreme platform", "demonia-style"]
    },
    "victorian lace-up boots": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.ROMANTIC],
        "colors": BLACKS + BROWNS + ["vintage", "historical"]
    },
    "steampunk leather boots": {
        "types": [OutfitType.STEAMPUNK, OutfitType.GOTHIC, OutfitType.AVANT_GARDE],
        "colors": BROWNS + BLACKS + METALLICS + ["buckled", "industrial"]
    },
    "corset-laced boots": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.ROMANTIC],
        "colors": BLACKS + REDS + BROWNS + ["corset-style", "dramatic"]
    },
    "furry winter boots": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "colors": BROWNS + WHITES + GRAYS + ["fur-lined", "cozy"]
    },
    "shearling boots": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.BOHEMIAN],
        "colors": BROWNS + WHITES + ["wool-lined", "warm"]
    },
    "ugg-style boots": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "colors": BROWNS + GRAYS + ["sheepskin", "casual"]
    },
    "snow boots": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + BROWNS + GRAYS + ["waterproof", "insulated"]
    },
    "rubber rain boots": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "colors": BLACKS + GREENS + NEONS + ["waterproof", "wellington"]
    },
    
    # Flat shoe variations
    "pointed-toe flats": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + GRAYS + METALLICS + ["sleek", "professional"]
    },
    "mary jane flats": {
        "types": [OutfitType.KAWAII, OutfitType.LOLITA, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "colors": BLACKS + PASTELS + REDS + ["T-strap", "sweet"]
    },
    "t-strap flats": {
        "types": [OutfitType.PREPPY, OutfitType.ROMANTIC, OutfitType.PIN_UP],
        "colors": BLACKS + BROWNS + PASTELS + ["vintage", "classic"]
    },
    "d'orsay flats": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + GRAYS + METALLICS + ["cut-out sides", "elegant"]
    },
    "loafers classic": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + BLACKS + ["leather", "classic"]
    },
    "penny loafers": {
        "types": [OutfitType.PREPPY, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + BLACKS + ["traditional", "penny keeper"]
    },
    "platform loafers": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": BLACKS + BROWNS + ["chunky sole", "elevated"]
    },
    "moccasins": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE],
        "colors": BROWNS + EARTH_TONES + ["soft leather", "comfortable"]
    },
    "boat shoes": {
        "types": [OutfitType.PREPPY, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + WHITES + BLUES + ["nautical", "deck shoes"]
    },
    "espadrille flats": {
        "types": [OutfitType.BOHEMIAN, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + EARTH_TONES + ["rope sole", "canvas"]
    },
    "smoking slippers": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "colors": BLACKS + JEWEL_TONES + METALLICS + ["embroidered", "luxurious"]
    },
    "oxfords flat": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + ["lace-up", "masculine"]
    },
    "brogues": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "colors": BROWNS + BLACKS + ["perforated", "wingtip"]
    },
    "creepers": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.ROCKABILLY],
        "colors": BLACKS + METALLICS + ["thick sole", "platform"]
    },
    "monk strap shoes": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "colors": BROWNS + BLACKS + ["buckled", "formal"]
    },
    "derby shoes": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "colors": BROWNS + BLACKS + ["open lacing", "casual formal"]
    },
    "two-tone spectator shoes": {
        "types": [OutfitType.RETRO, OutfitType.PIN_UP, OutfitType.PREPPY],
        "colors": BLACKS + WHITES + BROWNS + ["contrasting colors", "vintage"]
    },
    
    # Sneaker variations
    "classic low-top sneakers": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "colors": WHITES + BLACKS + NEONS + ["canvas", "converse-style"]
    },
    "high-top sneakers": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": WHITES + BLACKS + REDS + ["ankle-high", "basketball-style"]
    },
    "platform sneakers": {
        "types": [OutfitType.STREETWEAR, OutfitType.CLUB_PARTY, OutfitType.KAWAII],
        "colors": WHITES + BLACKS + PASTELS + ["chunky sole", "elevated"]
    },
    "slip-on sneakers": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "colors": WHITES + BLACKS + PATTERNS + ["no laces", "easy-on"]
    },
    "chunky dad sneakers": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "colors": WHITES + GRAYS + NEONS + ["bulky", "retro"]
    },
    "running shoes": {
        "types": [OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "colors": WHITES + BLACKS + NEONS + ["athletic", "performance"]
    },
    "cross-training sneakers": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "colors": WHITES + BLACKS + GRAYS + ["versatile", "gym"]
    },
    "skate shoes": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.PUNK],
        "colors": BLACKS + WHITES + GRAYS + ["durable", "flat sole"]
    },
    "basketball sneakers": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "colors": WHITES + BLACKS + REDS + ["high-top", "athletic"]
    },
    "tennis sneakers": {
        "types": [OutfitType.ATHLEISURE, OutfitType.PREPPY],
        "colors": WHITES + BLUES + ["court shoes", "classic"]
    },
    "retro 80s sneakers": {
        "types": [OutfitType.RETRO, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "colors": NEONS + WHITES + METALLICS + ["vintage", "colorful"]
    },
    "90s platform sneakers": {
        "types": [OutfitType.RETRO, OutfitType.STREETWEAR, OutfitType.CLUB_PARTY],
        "colors": WHITES + BLACKS + METALLICS + ["buffalo-style", "chunky"]
    },
    "sock sneakers": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + WHITES + ["stretchy", "form-fitting"]
    },
    "techwear sneakers": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.AVANT_GARDE],
        "colors": BLACKS + GRAYS + METALLICS + ["futuristic", "technical"]
    },
    "cyberpunk led sneakers": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": BLACKS + NEONS + SPECIAL + ["LED lights", "futuristic"]
    },
    "holographic sneakers": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.KAWAII, OutfitType.AVANT_GARDE],
        "colors": SPECIAL + METALLICS + ["iridescent", "rainbow"]
    },
    "custom painted sneakers": {
        "types": [OutfitType.STREETWEAR, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "colors": NEONS + SPECIAL + PATTERNS + ["artistic", "unique"]
    },
    
    # Sandal and slide variations
    "slides sporty": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + WHITES + NEONS + ["slip-on", "athletic"]
    },
    "leather slides": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + BROWNS + ["luxury", "sophisticated"]
    },
    "pool slides": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": WHITES + NEONS + ["waterproof", "poolside"]
    },
    "strappy flat sandals": {
        "types": [OutfitType.BOHEMIAN, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + METALLICS + ["multiple straps", "decorative"]
    },
    "gladiator sandals flat": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.ETHEREAL],
        "colors": BROWNS + METALLICS + ["lace-up", "warrior-inspired"]
    },
    "gladiator sandals knee-high": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.AVANT_GARDE],
        "colors": BROWNS + BLACKS + METALLICS + ["tall lacing", "dramatic"]
    },
    "platform sandals": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.RETRO, OutfitType.BEACH_WEAR],
        "colors": WHITES + METALLICS + NEONS + ["elevated", "chunky"]
    },
    "wedge sandals": {
        "types": [OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR],
        "colors": BROWNS + EARTH_TONES + ["cork", "rope", "woven"]
    },
    "espadrille sandals": {
        "types": [OutfitType.BOHEMIAN, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + EARTH_TONES + ["rope sole", "canvas"]
    },
    "slingback sandals": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.BEACH_WEAR],
        "colors": BLACKS + BROWNS + METALLICS + ["heel strap", "secure"]
    },
    "toe-ring sandals": {
        "types": [OutfitType.BOHEMIAN, OutfitType.BEACH_WEAR, OutfitType.ETHEREAL],
        "colors": METALLICS + BROWNS + ["minimalist", "delicate"]
    },
    "fisherman sandals": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.BEACH_WEAR],
        "colors": BROWNS + WHITES + ["woven", "closed-toe"]
    },
    "t-strap sandals": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.ROMANTIC],
        "colors": BLACKS + BROWNS + METALLICS + ["classic", "secure"]
    },
    "caged sandals": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "colors": BLACKS + METALLICS + ["geometric straps", "architectural"]
    },
    "lace-up sandals": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.ROMANTIC],
        "colors": BROWNS + BLACKS + ["wrap-around", "tie-up"]
    },
    "rope sandals": {
        "types": [OutfitType.BOHEMIAN, OutfitType.BEACH_WEAR, OutfitType.ETHEREAL],
        "colors": BROWNS + EARTH_TONES + ["natural fiber", "woven"]
    },
    "beaded boho sandals": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.ETHEREAL],
        "colors": BROWNS + EARTH_TONES + JEWEL_TONES + ["beaded", "decorative"]
    },
    "festival fringe sandals": {
        "types": [OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "colors": BROWNS + EARTH_TONES + ["tasseled", "movement"]
    },
    "metallic sandals": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL, OutfitType.BEACH_WEAR],
        "colors": METALLICS + SPECIAL + ["shimmery", "glamorous"]
    },
    "crystal-embellished sandals": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.ROMANTIC],
        "colors": METALLICS + JEWEL_TONES + ["bejeweled", "luxury"]
    },
    "jelly sandals": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.KAWAII, OutfitType.RETRO],
        "colors": NEONS + PASTELS + ["plastic", "translucent"]
    },
    "transparent pvc sandals": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.BEACH_WEAR],
        "colors": ["clear", "transparent", "see-through"]
    },
    
    # Special and alternative footwear
    "clogs wooden": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + EARTH_TONES + ["wooden sole", "traditional"]
    },
    "platform clogs": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "colors": BROWNS + BLACKS + ["elevated", "chunky"]
    },
    "crocs casual": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": NEONS + PASTELS + WHITES + ["comfort", "ventilated"]
    },
    "fashion crocs": {
        "types": [OutfitType.STREETWEAR, OutfitType.KAWAII, OutfitType.FESTIVAL],
        "colors": NEONS + PASTELS + METALLICS + ["platform", "embellished"]
    },
    "mule flats": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + BROWNS + GRAYS + ["backless", "slip-on"]
    },
    "mule platforms": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.STREETWEAR, OutfitType.RETRO],
        "colors": BLACKS + METALLICS + NEONS + ["backless", "elevated"]
    },
    "japanese geta": {
        "types": [OutfitType.KAWAII, OutfitType.ETHEREAL, OutfitType.AVANT_GARDE],
        "colors": BROWNS + BLACKS + ["wooden", "traditional", "elevated"]
    },
    "zori sandals": {
        "types": [OutfitType.KAWAII, OutfitType.ETHEREAL, OutfitType.MINIMALIST],
        "colors": BLACKS + WHITES + BROWNS + ["flat", "traditional"]
    },
    "okobo shoes": {
        "types": [OutfitType.KAWAII, OutfitType.LOLITA, OutfitType.AVANT_GARDE],
        "colors": BLACKS + REDS + WHITES + ["platform", "traditional"]
    },
    "babouche slippers": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.CASUAL_CHIC],
        "colors": JEWEL_TONES + METALLICS + EARTH_TONES + ["moroccan", "pointed"]
    },
    "khussa flats": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.FESTIVAL],
        "colors": JEWEL_TONES + METALLICS + ["embroidered", "indian"]
    },
    "ballet pointe shoes": {
        "types": [OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.MINIMALIST],
        "colors": PINKS + WHITES + ["satin", "ribbons", "dance"]
    },
    "jazz shoes": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + ["leather", "dance", "flexible"]
    },
    "tap shoes": {
        "types": [OutfitType.RETRO, OutfitType.PREPPY, OutfitType.ROMANTIC],
        "colors": BLACKS + BROWNS + ["metal taps", "dance"]
    },
    "character shoes": {
        "types": [OutfitType.RETRO, OutfitType.ROMANTIC, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + BROWNS + ["theatre", "mid-heel"]
    },
    "roller skates": {
        "types": [OutfitType.RETRO, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "colors": WHITES + NEONS + PASTELS + ["wheeled", "vintage"]
    },
    "ice skates": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC],
        "colors": WHITES + BLACKS + ["bladed", "athletic"]
    },
    "goth coffin platforms": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.AVANT_GARDE],
        "colors": BLACKS + METALLICS + ["coffin-shaped", "extreme"]
    },
    "fetish ballet boots": {
        "types": [OutfitType.GOTHIC, OutfitType.AVANT_GARDE, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + ["extreme point", "fetish"]
    },
    "fetish extreme platforms": {
        "types": [OutfitType.GOTHIC, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": BLACKS + REDS + METALLICS + ["extreme height", "fetish"]
    },
    "armored avant-garde shoes": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK, OutfitType.STEAMPUNK],
        "colors": METALLICS + BLACKS + ["metallic", "sculptural"]
    },
    "inflatable concept shoes": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK],
        "colors": SPECIAL + NEONS + ["inflatable", "conceptual"]
    },
    "3d-printed sculptural shoes": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK, OutfitType.MINIMALIST],
        "colors": WHITES + BLACKS + SPECIAL + ["3D-printed", "geometric"]
    }
}
