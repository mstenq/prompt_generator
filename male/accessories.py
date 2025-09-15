"""
Clothing data definitions for the ComfyUI Outfit Generator.
This file contains clothing items tagged with their compatible outfit types and color palettes.
"""

from ..outfit_types import OutfitType
from ..colors import *

# Accessories with their compatible outfit types and color palettes
MALE_ACCESSORIES = {
    # Belts
    "belt": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.COWBOY, OutfitType.PUNK],
        "colors": BLACKS + BROWNS + ["leather", "studded", "chain", "buckle"]
    },
    "leather belt": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + ["genuine leather", "dress belt", "classic buckle"]
    },
    "dress belt": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.PREPPY],
        "colors": BLACKS + BROWNS + ["polished leather", "formal", "silver buckle", "gold buckle"]
    },
    "casual belt": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR],
        "colors": BROWNS + BLACKS + ["everyday wear", "versatile", "simple buckle"]
    },
    "western belt": {
        "types": [OutfitType.COWBOY, OutfitType.ROCKABILLY],
        "colors": BROWNS + BLACKS + ["tooled leather", "large buckle", "ornate", "rodeo style"]
    },
    "studded belt": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.ROCKABILLY],
        "colors": BLACKS + ["metal studs", "spikes", "edgy", "alternative"]
    },
    "chain belt": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "colors": METALLICS + BLACKS + ["metal chain", "industrial", "wallet chain"]
    },
    "canvas belt": {
        "types": [OutfitType.MILITARY, OutfitType.CASUAL_CHIC, OutfitType.NORMCORE],
        "colors": GREENS + BROWNS + BLACKS + ["fabric", "military style", "web belt"]
    },
    "rope belt": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + WHITES + ["nautical", "braided", "casual"]
    },
    "suspenders": {
        "types": [OutfitType.RETRO, OutfitType.PREPPY, OutfitType.STEAMPUNK],
        "colors": BLACKS + BROWNS + BLUES + ["vintage", "braces", "adjustable"]
    },
    
    # Watches
    "dress watch": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + METALLICS + ["leather strap", "gold", "silver", "classic"]
    },
    "sports watch": {
        "types": [OutfitType.ATHLEISURE, OutfitType.CASUAL_CHIC, OutfitType.MILITARY],
        "colors": BLACKS + BLUES + GRAYS + ["digital", "waterproof", "rubber strap"]
    },
    "smartwatch": {
        "types": [OutfitType.ATHLEISURE, OutfitType.MINIMALIST, OutfitType.CYBERPUNK],
        "colors": BLACKS + WHITES + GRAYS + ["tech", "fitness tracker", "modern"]
    },
    "vintage watch": {
        "types": [OutfitType.RETRO, OutfitType.PREPPY, OutfitType.STEAMPUNK],
        "colors": METALLICS + BROWNS + ["antique", "mechanical", "classic design"]
    },
    "diving watch": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR, OutfitType.MILITARY],
        "colors": BLACKS + BLUES + METALLICS + ["waterproof", "rotating bezel", "professional"]
    },
    "chronograph": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE],
        "colors": METALLICS + BLACKS + ["stopwatch", "racing style", "multiple dials"]
    },
    "pilot watch": {
        "types": [OutfitType.MILITARY, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": BLACKS + METALLICS + ["aviation", "large face", "leather strap"]
    },
    "tactical watch": {
        "types": [OutfitType.MILITARY, OutfitType.ATHLEISURE, OutfitType.CYBERPUNK],
        "colors": BLACKS + GREENS + GRAYS + ["survival features", "durable", "military grade"]
    },
    
    # Hats
    "baseball cap": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "colors": BLACKS + BLUES + REDS + WHITES + ["adjustable", "team logo", "flat brim", "curved brim"]
    },
    "beanie": {
        "types": [OutfitType.STREETWEAR, OutfitType.GRUNGE, OutfitType.NORMCORE, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + GRAYS + BLUES + ["wool", "knit", "slouchy", "cuffed"]
    },
    "fedora": {
        "types": [OutfitType.RETRO, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + GRAYS + ["felt", "classic", "brimmed", "vintage"]
    },
    "snapback": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": BLACKS + BLUES + REDS + WHITES + ["flat brim", "adjustable", "urban"]
    },
    "bucket hat": {
        "types": [OutfitType.STREETWEAR, OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + WHITES + BLUES + ["cotton", "reversible", "casual"]
    },
    "trucker hat": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.NORMCORE, OutfitType.COWBOY],
        "colors": BLUES + REDS + BLACKS + ["mesh back", "foam front", "adjustable"]
    },
    "panama hat": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": WHITES + BROWNS + ["straw", "woven", "summer", "brimmed"]
    },
    "beret": {
        "types": [OutfitType.BOHEMIAN, OutfitType.RETRO, OutfitType.AVANT_GARDE],
        "colors": BLACKS + BLUES + REDS + ["wool", "French style", "artistic"]
    },
    "newsboy cap": {
        "types": [OutfitType.RETRO, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "colors": GRAYS + BROWNS + BLUES + ["wool", "vintage", "cabbie hat"]
    },
    "cowboy hat": {
        "types": [OutfitType.COWBOY, OutfitType.ROCKABILLY],
        "colors": BROWNS + BLACKS + ["felt", "wide brim", "western", "rodeo"]
    },
    "top hat": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.STEAMPUNK, OutfitType.GOTHIC],
        "colors": BLACKS + ["silk", "formal", "Victorian", "classic"]
    },
    "bowler hat": {
        "types": [OutfitType.RETRO, OutfitType.STEAMPUNK, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + BROWNS + ["felt", "derby hat", "vintage", "formal"]
    },
    "flat cap": {
        "types": [OutfitType.RETRO, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "colors": GRAYS + BROWNS + BLUES + ["wool", "tweed", "Irish cap", "driver cap"]
    },
    "military cap": {
        "types": [OutfitType.MILITARY, OutfitType.PUNK, OutfitType.STREETWEAR],
        "colors": GREENS + BLACKS + ["service cap", "peaked cap", "uniform"]
    },
    "visor": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR, OutfitType.PREPPY],
        "colors": WHITES + BLUES + BLACKS + ["sun visor", "golf", "tennis"]
    },
    
    # Glasses
    "sunglasses": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + ["UV protection", "polarized", "classic", "trendy"]
    },
    "aviator sunglasses": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.MILITARY],
        "colors": METALLICS + ["pilot style", "classic", "gold frame", "silver frame"]
    },
    "wayfarer sunglasses": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.STREETWEAR],
        "colors": BLACKS + BROWNS + ["classic shape", "vintage", "iconic"]
    },
    "round sunglasses": {
        "types": [OutfitType.BOHEMIAN, OutfitType.RETRO, OutfitType.AVANT_GARDE],
        "colors": BLACKS + METALLICS + ["circular", "vintage", "John Lennon style"]
    },
    "sport sunglasses": {
        "types": [OutfitType.ATHLEISURE, OutfitType.BEACH_WEAR],
        "colors": BLACKS + BLUES + NEONS + ["wraparound", "athletic", "performance"]
    },
    "prescription glasses": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.PREPPY],
        "colors": BLACKS + BROWNS + METALLICS + ["reading glasses", "clear lens", "professional"]
    },
    "reading glasses": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + BROWNS + METALLICS + ["magnification", "professional", "classic"]
    },
    "blue light glasses": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CYBERPUNK],
        "colors": BLACKS + BROWNS + ["computer glasses", "screen protection", "modern"]
    },
    "safety glasses": {
        "types": [OutfitType.MILITARY, OutfitType.NORMCORE, OutfitType.CYBERPUNK],
        "colors": BLACKS + ["protective", "industrial", "work safety"]
    },
    "monocle": {
        "types": [OutfitType.STEAMPUNK, OutfitType.RETRO, OutfitType.EVENING_FORMAL],
        "colors": METALLICS + ["single lens", "vintage", "Victorian", "gentleman"]
    },
    
    # Additional Accessories
    "pocket watch": {
        "types": [OutfitType.STEAMPUNK, OutfitType.RETRO, OutfitType.EVENING_FORMAL],
        "colors": METALLICS + ["chain", "vintage", "mechanical", "antique"]
    },
    "bow tie": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.PREPPY, OutfitType.RETRO],
        "colors": BLACKS + WHITES + REDS + BLUES + ["silk", "formal", "adjustable", "self-tie"]
    },
    "necktie": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.PREPPY],
        "colors": BLUES + REDS + GRAYS + ["silk", "striped", "solid", "patterned"]
    },
    "ascot": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.RETRO, OutfitType.PREPPY],
        "colors": BLUES + GRAYS + ["silk", "formal", "Victorian", "cravat"]
    },
    "cufflinks": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.PREPPY],
        "colors": METALLICS + ["gold", "silver", "formal", "dress shirt"]
    },
    "tie clip": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.PREPPY],
        "colors": METALLICS + ["gold", "silver", "tie bar", "formal accessory"]
    },
    "pocket square": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.PREPPY],
        "colors": WHITES + BLUES + REDS + ["silk", "cotton", "formal", "suit accessory"]
    },
    "scarf": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.BOHEMIAN, OutfitType.PREPPY],
        "colors": GRAYS + BLUES + BROWNS + ["wool", "cashmere", "winter", "neck scarf"]
    },
    "bandana": {
        "types": [OutfitType.STREETWEAR, OutfitType.COWBOY, OutfitType.PUNK, OutfitType.GRUNGE],
        "colors": REDS + BLUES + BLACKS + ["cotton", "paisley", "head wrap", "neck wear"]
    }
}

