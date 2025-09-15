"""
Clothing data definitions for the ComfyUI Outfit Generator.
This file contains clothing items tagged with their compatible outfit types and color palettes.
"""

from ..outfit_types import OutfitType
from ..colors import *

# Shoes with their compatible outfit types and color palettes
MALE_SHOES = {
    # Formal/Dress Shoes
    "oxford shoes": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.PREPPY],
        "colors": BLACKS + BROWNS + ["leather", "polished", "cap toe", "wingtip"]
    },
    "derby shoes": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "colors": BLACKS + BROWNS + ["leather", "open lacing", "classic"]
    },
    "brogues": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + BLACKS + ["wingtip", "perforated", "leather", "traditional"]
    },
    "dress boots": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + ["leather", "ankle height", "sleek"]
    },
    "patent leather shoes": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": BLACKS + ["shiny", "formal", "tuxedo shoes"]
    },
    "monk strap shoes": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + ["buckle", "leather", "elegant"]
    },
    "loafers": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "colors": BROWNS + BLACKS + ["penny loafers", "tassel", "slip-on", "leather"]
    },
    "boat shoes": {
        "types": [OutfitType.PREPPY, OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + BLUES + ["leather", "deck shoes", "nautical", "moccasin style"]
    },
    "dress slippers": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "colors": BLACKS + ["velvet", "embroidered", "formal", "smoking slippers"]
    },
    
    # Casual Shoes
    "sneakers": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "colors": WHITES + BLACKS + NEONS + ["high-top", "chunky", "minimalist", "canvas"]
    },
    "white sneakers": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "colors": WHITES + ["clean", "minimalist", "court shoes", "leather"]
    },
    "running shoes": {
        "types": [OutfitType.ATHLEISURE],
        "colors": WHITES + BLACKS + BLUES + NEONS + ["athletic", "mesh", "cushioned"]
    },
    "basketball shoes": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR],
        "colors": BLACKS + WHITES + REDS + BLUES + ["high-top", "performance", "retro"]
    },
    "canvas shoes": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "colors": WHITES + BLACKS + BLUES + REDS + ["converse style", "vintage", "low-top"]
    },
    "slip-on sneakers": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.STREETWEAR],
        "colors": WHITES + BLACKS + GRAYS + ["vans style", "checkered", "canvas"]
    },
    "skateboard shoes": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE],
        "colors": BLACKS + WHITES + GRAYS + ["vulcanized", "flat sole", "durable"]
    },
    "retro sneakers": {
        "types": [OutfitType.RETRO, OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC],
        "colors": WHITES + BLUES + REDS + ["vintage", "chunky", "dad shoes"]
    },
    
    # Boots
    "combat boots": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.MILITARY, OutfitType.GOTHIC],
        "colors": BLACKS + BROWNS + ["leather", "steel toe", "lace-up", "tactical"]
    },
    "work boots": {
        "types": [OutfitType.NORMCORE, OutfitType.MILITARY, OutfitType.COWBOY],
        "colors": BROWNS + BLACKS + ["steel toe", "leather", "durable", "construction"]
    },
    "chelsea boots": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.ROCKABILLY],
        "colors": BLACKS + BROWNS + ["elastic sides", "ankle boots", "sleek"]
    },
    "chukka boots": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "colors": BROWNS + BLACKS + ["suede", "leather", "desert boots", "lace-up"]
    },
    "hiking boots": {
        "types": [OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "colors": BROWNS + BLACKS + GREENS + ["waterproof", "rugged", "outdoor"]
    },
    "motorcycle boots": {
        "types": [OutfitType.PUNK, OutfitType.ROCKABILLY, OutfitType.STREETWEAR],
        "colors": BLACKS + BROWNS + ["leather", "buckles", "harness", "engineer boots"]
    },
    "cowboy boots": {
        "types": [OutfitType.COWBOY, OutfitType.ROCKABILLY],
        "colors": BROWNS + BLACKS + ["leather", "pointed toe", "western", "ostrich skin"]
    },
    "rain boots": {
        "types": [OutfitType.NORMCORE, OutfitType.MINIMALIST],
        "colors": BLACKS + BLUES + GREENS + ["rubber", "wellington", "waterproof"]
    },
    "snow boots": {
        "types": [OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "colors": BLACKS + BROWNS + GRAYS + ["insulated", "waterproof", "winter"]
    },
    "steel toe boots": {
        "types": [OutfitType.NORMCORE, OutfitType.MILITARY, OutfitType.PUNK],
        "colors": BLACKS + BROWNS + ["safety", "industrial", "heavy-duty"]
    },
    "platform boots": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + ["thick sole", "height", "alternative"]
    },
    "lace-up boots": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.GOTHIC],
        "colors": BLACKS + BROWNS + ["high lacing", "combat style", "chunky"]
    },
    
    # Athletic/Sports
    "cross trainers": {
        "types": [OutfitType.ATHLEISURE],
        "colors": WHITES + BLACKS + GRAYS + ["versatile", "gym shoes", "athletic"]
    },
    "tennis shoes": {
        "types": [OutfitType.ATHLEISURE, OutfitType.PREPPY],
        "colors": WHITES + ["court shoes", "classic", "leather", "minimalist"]
    },
    "golf shoes": {
        "types": [OutfitType.PREPPY, OutfitType.BUSINESS_WEAR],
        "colors": WHITES + BROWNS + BLACKS + ["spiked", "leather", "waterproof"]
    },
    "soccer cleats": {
        "types": [OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + NEONS + ["studded", "performance", "lightweight"]
    },
    "football cleats": {
        "types": [OutfitType.ATHLEISURE],
        "colors": BLACKS + WHITES + ["high-top", "ankle support", "studded"]
    },
    "wrestling shoes": {
        "types": [OutfitType.ATHLEISURE],
        "colors": BLACKS + REDS + BLUES + ["lightweight", "grip sole", "athletic"]
    },
    
    # Sandals/Summer
    "flip-flops": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.NORMCORE],
        "colors": BLACKS + BROWNS + BLUES + ["rubber", "casual", "summer"]
    },
    "sandals": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "colors": BROWNS + BLACKS + ["leather", "strappy", "open toe"]
    },
    "slides": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR, OutfitType.STREETWEAR],
        "colors": BLACKS + WHITES + ["slip-on", "pool shoes", "athletic"]
    },
    "espadrilles": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "colors": BROWNS + WHITES + BLUES + ["rope sole", "canvas", "summer"]
    },
    "aqua shoes": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + BLUES + ["water shoes", "quick-dry", "rubber sole"]
    },
    
    # Alternative/Subculture
    "doc martens": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.GOTHIC],
        "colors": BLACKS + BROWNS + REDS + ["iconic", "air cushion", "leather"]
    },
    "creepers": {
        "types": [OutfitType.PUNK, OutfitType.ROCKABILLY, OutfitType.GOTHIC],
        "colors": BLACKS + ["thick sole", "suede", "platform", "underground"]
    },
    "pointed toe boots": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.ROCKABILLY],
        "colors": BLACKS + ["sharp toe", "edgy", "leather", "aggressive"]
    },
    "studded shoes": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC],
        "colors": BLACKS + ["metal studs", "spikes", "edgy", "alternative"]
    },
    "bondage boots": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC],
        "colors": BLACKS + ["straps", "buckles", "chains", "fetish style"]
    },
    
    # Specialty/Themed
    "moccasins": {
        "types": [OutfitType.PREPPY, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN],
        "colors": BROWNS + BLACKS + ["soft leather", "traditional", "slip-on"]
    },
    "driving shoes": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "colors": BROWNS + BLACKS + BLUES + ["rubber soles", "leather", "luxury"]
    },
    "boat sneakers": {
        "types": [OutfitType.PREPPY, OutfitType.BEACH_WEAR],
        "colors": WHITES + BLUES + BROWNS + ["hybrid", "nautical", "canvas"]
    },
    "military boots": {
        "types": [OutfitType.MILITARY, OutfitType.PUNK, OutfitType.STREETWEAR],
        "colors": BLACKS + BROWNS + GREENS + ["tactical", "combat ready", "durable"]
    },
    "western boots": {
        "types": [OutfitType.COWBOY, OutfitType.ROCKABILLY],
        "colors": BROWNS + BLACKS + ["pointed toe", "heel", "tooled leather"]
    },
    
    # Tech/Modern
    "tech sneakers": {
        "types": [OutfitType.CYBERPUNK, OutfitType.MINIMALIST, OutfitType.STREETWEAR],
        "colors": BLACKS + WHITES + GRAYS + ["futuristic", "technical fabric", "modern"]
    },
    "smart shoes": {
        "types": [OutfitType.MINIMALIST, OutfitType.CYBERPUNK],
        "colors": BLACKS + GRAYS + ["tech features", "sleek", "modern"]
    },
    "performance boots": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CYBERPUNK],
        "colors": BLACKS + GRAYS + ["technical", "lightweight", "performance"]
    },
    
    # Vintage/Retro
    "saddle shoes": {
        "types": [OutfitType.RETRO, OutfitType.PREPPY, OutfitType.ROCKABILLY],
        "colors": ["black and white", "two-tone", "vintage", "classic"]
    },
    "spectator shoes": {
        "types": [OutfitType.RETRO, OutfitType.PREPPY],
        "colors": ["black and white", "brown and white", "two-tone", "vintage"]
    },
    "wingtip boots": {
        "types": [OutfitType.RETRO, OutfitType.PREPPY, OutfitType.BUSINESS_WEAR],
        "colors": BROWNS + BLACKS + ["perforated", "brogue style", "vintage"]
    },
    "penny loafers": {
        "types": [OutfitType.PREPPY, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + BLACKS + ["classic", "slip-on", "leather", "traditional"]
    },
    
    # Luxury/Designer
    "designer sneakers": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "colors": WHITES + BLACKS + ["luxury", "high-end", "fashion"]
    },
    "luxury loafers": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "colors": BROWNS + BLACKS + ["premium leather", "designer", "elegant"]
    },
    "italian leather shoes": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + BLACKS + ["handcrafted", "luxury", "premium"]
    },
    
    # Comfort/Casual
    "house slippers": {
        "types": [OutfitType.NORMCORE],
        "colors": BROWNS + GRAYS + BLACKS + ["comfortable", "indoor", "fuzzy"]
    },
    "mules": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + WHITES + ["backless", "slip-on", "casual"]
    },
    "slip-on shoes": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + WHITES + ["easy wear", "comfortable", "laceless"]
    }
}
