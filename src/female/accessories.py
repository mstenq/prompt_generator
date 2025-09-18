"""
Clothing data definitions for the ComfyUI Outfit Generator.
This file contains clothing items tagged with their compatible outfit types and color palettes.
"""

from ..enums import OutfitType
from ..colors import *

# Accessories with their compatible outfit types and color palettes
FEMALE_ACCESSORIES = {
    "belt": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.COWBOY, OutfitType.PUNK],
        "colors": BLACKS + BROWNS + ["leather", "studded", "chain", "buckle"]
    },
    "tie": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL, OutfitType.PREPPY],
        "colors": BLUES + REDS + ["striped", "polka dots", "silk"]
    },
    "scarf": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "colors": PASTELS + JEWEL_TONES + PATTERNS + ["silk", "flowing"]
    },
    "choker": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + ["velvet", "leather", "spiked", "chain"]
    },
    "pearl necklace": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.EVENING_FORMAL, OutfitType.COTTAGECORE],
        "colors": WHITES + ["classic", "vintage", "layered"]
    },
    "flower crown": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "colors": PASTELS + ["dried flowers", "fresh flowers", "braided"]
    },
    "snapback": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "colors": BLACKS + NEONS + ["logo", "flat brim"]
    },
    "cowboy hat": {
        "types": [OutfitType.COWBOY, OutfitType.FESTIVAL],
        "colors": BROWNS + BLACKS + ["leather", "felt", "straw"]
    },
    "beanie": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": BLACKS + GRAYS + NEONS + ["knitted", "slouchy"]
    },
    "sunglasses": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["aviator", "cat-eye", "oversized"]
    },
    "crossbody bag": {
        "types": [OutfitType.STREETWEAR, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "colors": BLACKS + BROWNS + NEONS + ["leather", "canvas"]
    },
    "clutch": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + METALLICS + JEWEL_TONES + ["sequined", "beaded"]
    },
    "dog tags": {
        "types": [OutfitType.MILITARY, OutfitType.PUNK, OutfitType.GRUNGE],
        "colors": METALLICS + ["chain", "stamped"]
    },
    "hair bow": {
        "types": [OutfitType.LOLITA, OutfitType.KAWAII, OutfitType.PIN_UP],
        "colors": PASTELS + REDS + ["oversized", "polka dots", "satin"]
    },
    "goggles": {
        "types": [OutfitType.STEAMPUNK, OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE],
        "colors": METALLICS + BROWNS + ["brass", "leather straps"]
    },

    # --- Necklaces & Chains ---
    "pendant necklace": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.PREPPY],
        "colors": METALLICS + JEWEL_TONES + ["delicate", "minimal", "statement"]
    },
    "choker necklace": {
        "types": [OutfitType.GRUNGE, OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + METALLICS + ["velvet", "leather", "metal", "chain"]
    },
    "collar necklace": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.AVANT_GARDE, OutfitType.ROMANTIC],
        "colors": METALLICS + JEWEL_TONES + WHITES + ["structured", "bold"]
    },
    "bib necklace": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "colors": JEWEL_TONES + METALLICS + ["statement", "embellished"]
    },
    "beaded necklace": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.COTTAGECORE, OutfitType.KAWAII, OutfitType.BEACH_WEAR],
        "colors": PASTELS + EARTH_TONES + JEWEL_TONES + ["handmade", "layered", "natural"]
    },
    "pearl strand necklace": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.EVENING_FORMAL, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "colors": WHITES + ["classic", "layered", "luminous"]
    },
    "multi-layered necklace": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.STREETWEAR, OutfitType.ROMANTIC],
        "colors": METALLICS + PASTELS + ["layered", "delicate", "stacked"]
    },
    "lariat necklace": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.ROMANTIC],
        "colors": METALLICS + JEWEL_TONES + ["draped", "minimal", "elegant"]
    },
    "medallion necklace": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.STREETWEAR, OutfitType.PUNK],
        "colors": METALLICS + EARTH_TONES + ["engraved", "vintage"]
    },
    "chain necklace": {
        "types": [OutfitType.STREETWEAR, OutfitType.PUNK, OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY, OutfitType.BUSINESS_WEAR],
        "colors": METALLICS + BLACKS + ["chunky", "fine", "layered"]
    },
    "oversized statement necklace": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.FESTIVAL],
        "colors": METALLICS + JEWEL_TONES + NEONS + ["oversized", "sculptural"]
    },
    "crystal pendant": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.COTTAGECORE, OutfitType.FESTIVAL],
        "colors": JEWEL_TONES + PASTELS + ["raw crystal", "polished", "glowing"]
    },
    "lock necklace": {
        "types": [OutfitType.PUNK, OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.STREETWEAR, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["padlock", "chain", "industrial"]
    },
    "spike choker": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["spiked", "leather", "aggressive"]
    },
    "body chain": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.ETHEREAL, OutfitType.CLUB_PARTY, OutfitType.BOHEMIAN],
        "colors": METALLICS + ["delicate", "layered", "draped"]
    },
    "anklet chain": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.ETHEREAL],
        "colors": METALLICS + PASTELS + ["delicate", "charms"]
    },
    "toe ring": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.BOHEMIAN, OutfitType.FESTIVAL],
        "colors": METALLICS + ["delicate", "engraved"]
    },

    # --- Rings ---
    "signet ring": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.RETRO, OutfitType.MINIMALIST],
        "colors": METALLICS + ["engraved", "initial", "bold"]
    },
    "cocktail ring": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.ROMANTIC],
        "colors": JEWEL_TONES + METALLICS + ["gemstone", "oversized", "sparkling"]
    },
    "stacking rings": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.MINIMALIST, OutfitType.BOHEMIAN],
        "colors": METALLICS + PASTELS + ["delicate", "mixed", "layered"]
    },
    "mood ring": {
        "types": [OutfitType.RETRO, OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.STREETWEAR],
        "colors": JEWEL_TONES + NEONS + ["color-changing"]
    },
    "claddagh ring": {
        "types": [OutfitType.ROMANTIC, OutfitType.RETRO, OutfitType.COTTAGECORE, OutfitType.PREPPY],
        "colors": METALLICS + WHITES + ["traditional", "symbolic"]
    },
    "engagement-style ring": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.BUSINESS_WEAR],
        "colors": METALLICS + WHITES + ["solitaire", "halo", "sparkling"]
    },
    "gemstone ring": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.BOHEMIAN, OutfitType.AVANT_GARDE],
        "colors": JEWEL_TONES + METALLICS + ["faceted", "ornate"]
    },
    "pearl ring": {
        "types": [OutfitType.ROMANTIC, OutfitType.PREPPY, OutfitType.EVENING_FORMAL, OutfitType.COTTAGECORE],
        "colors": WHITES + METALLICS + ["delicate"]
    },

    # --- Bracelets & Arm Adornments ---
    "bracelet (bangle)": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.BOHEMIAN],
        "colors": METALLICS + ["stacked", "minimal"]
    },
    "bracelet (cuff)": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.PUNK, OutfitType.BUSINESS_WEAR, OutfitType.STEAMPUNK],
        "colors": METALLICS + BLACKS + ["bold", "engraved"]
    },
    "tennis bracelet": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.ROMANTIC, OutfitType.PREPPY],
        "colors": WHITES + METALLICS + ["sparkling", "diamond"]
    },
    "beaded bracelet": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.COTTAGECORE, OutfitType.KAWAII],
        "colors": PASTELS + EARTH_TONES + JEWEL_TONES + ["handmade", "stacked"]
    },
    "leather wrap bracelet": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.STEAMPUNK],
        "colors": BROWNS + BLACKS + ["wrap", "braided", "studded"]
    },
    "charm bracelet": {
        "types": [OutfitType.PREPPY, OutfitType.KAWAII, OutfitType.ROMANTIC, OutfitType.FESTIVAL],
        "colors": METALLICS + PASTELS + ["personalized", "dangling"]
    },
    "chain-link bracelet": {
        "types": [OutfitType.STREETWEAR, OutfitType.PUNK, OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY],
        "colors": METALLICS + BLACKS + ["chunky", "industrial"]
    },
    "spiked bracelet": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.CLUB_PARTY],
        "colors": BLACKS + METALLICS + ["leather", "aggressive"]
    },
    "studded cuff": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.GRUNGE],
        "colors": BLACKS + METALLICS + ["leather", "wide"]
    },
    "wristband (fabric/festival)": {
        "types": [OutfitType.FESTIVAL, OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.KAWAII],
        "colors": NEONS + PASTELS + ["printed", "woven"]
    },
    "arm cuff": {
        "types": [OutfitType.FESTIVAL, OutfitType.ETHEREAL, OutfitType.BOHEMIAN, OutfitType.AVANT_GARDE],
        "colors": METALLICS + ["engraved", "spiral"]
    },
    "slave bracelet": {
        "types": [OutfitType.ETHEREAL, OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.ROMANTIC],
        "colors": METALLICS + ["chain", "delicate"]
    },

    # --- Earrings ---
    "earrings (studs)": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.ROMANTIC, OutfitType.PREPPY, OutfitType.EVENING_FORMAL],
        "colors": METALLICS + WHITES + JEWEL_TONES + ["tiny", "sparkling"]
    },
    "earrings (hoops, small)": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "colors": METALLICS + ["classic", "thin"]
    },
    "earrings (hoops, oversized)": {
        "types": [OutfitType.STREETWEAR, OutfitType.CLUB_PARTY, OutfitType.PUNK, OutfitType.FESTIVAL],
        "colors": METALLICS + NEONS + ["bold", "chunky"]
    },
    "drop earrings": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.BUSINESS_WEAR, OutfitType.COTTAGECORE],
        "colors": JEWEL_TONES + METALLICS + WHITES + ["dangling", "delicate"]
    },
    "chandelier earrings": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE, OutfitType.CLUB_PARTY, OutfitType.ROMANTIC],
        "colors": JEWEL_TONES + METALLICS + WHITES + ["ornate", "sparkling"]
    },
    "ear climbers": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "colors": METALLICS + JEWEL_TONES + ["curved", "delicate"]
    },
    "ear cuffs": {
        "types": [OutfitType.PUNK, OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE, OutfitType.STREETWEAR],
        "colors": METALLICS + BLACKS + ["stacked", "industrial"]
    },
    "industrial earrings": {
        "types": [OutfitType.PUNK, OutfitType.CYBERPUNK, OutfitType.GOTHIC, OutfitType.GRUNGE],
        "colors": METALLICS + BLACKS + ["barbell", "pierced"]
    },
    "spike earrings": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY],
        "colors": METALLICS + BLACKS + ["spiked", "sharp"]
    },
    "feather earrings": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.ETHEREAL, OutfitType.COTTAGECORE],
        "colors": PASTELS + EARTH_TONES + ["natural", "dyed"]
    },
    "beaded dangly earrings": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.KAWAII, OutfitType.COTTAGECORE],
        "colors": PASTELS + JEWEL_TONES + ["handmade", "layered"]
    },

    # --- Hats & Headwear ---
    "baseball cap": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.NORMCORE, OutfitType.FESTIVAL],
        "colors": BLACKS + NEONS + PATTERNS + ["logo", "classic"]
    },
    "snapback cap": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.NORMCORE],
        "colors": BLACKS + NEONS + ["flat brim", "logo"]
    },
    "trucker hat": {
        "types": [OutfitType.STREETWEAR, OutfitType.FESTIVAL, OutfitType.NORMCORE, OutfitType.RETRO],
        "colors": BLACKS + NEONS + PATTERNS + ["mesh", "logo"]
    },
    "bucket hat": {
        "types": [OutfitType.STREETWEAR, OutfitType.FESTIVAL, OutfitType.KAWAII, OutfitType.BEACH_WEAR],
        "colors": NEONS + PASTELS + PATTERNS + ["reversible", "embroidered"]
    },
    "fisherman's cap": {
        "types": [OutfitType.RETRO, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "colors": BROWNS + BLACKS + BLUES + ["canvas", "utility"]
    },
    "beanie (classic knit)": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": BLACKS + GRAYS + ["ribbed", "classic"]
    },
    "oversized slouch beanie": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + NEONS + GRAYS + ["slouchy", "oversized"]
    },
    "pom-pom beanie": {
        "types": [OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.STREETWEAR, OutfitType.COTTAGECORE],
        "colors": PASTELS + NEONS + ["fluffy", "playful"]
    },
    "beret (classic wool)": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.RETRO],
        "colors": REDS + BLACKS + WHITES + ["wool", "classic"]
    },
    "leather beret": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.STREETWEAR, OutfitType.PUNK, OutfitType.GOTHIC],
        "colors": BLACKS + METALLICS + ["leather", "sleek"]
    },
    "military beret": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.PUNK],
        "colors": BLACKS + BROWNS + GREENS + ["insignia", "structured"]
    },
    "newsboy cap": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.COTTAGECORE],
        "colors": BROWNS + GRAYS + BLUES + ["tweed", "vintage"]
    },
    "flat cap": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR, OutfitType.COTTAGECORE],
        "colors": GRAYS + BROWNS + BLUES + ["wool", "tweed"]
    },
    "fedora": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL],
        "colors": BROWNS + BLACKS + GRAYS + ["felt", "wide brim"]
    },
    "trilby": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.BUSINESS_WEAR],
        "colors": BROWNS + BLACKS + ["narrow brim", "felt"]
    },
    "bowler hat": {
        "types": [OutfitType.RETRO, OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + GRAYS + ["felt", "classic"]
    },
    "top hat": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE],
        "colors": BLACKS + METALLICS + ["tall", "silk"]
    },
    "mini top hat": {
        "types": [OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "colors": BLACKS + METALLICS + ["decorated", "brass"]
    },
    "straw sun hat": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.COTTAGECORE, OutfitType.FESTIVAL],
        "colors": WHITES + BROWNS + YELLOWS + ["woven", "brimmed"]
    },
    "wide-brim floppy hat": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.FESTIVAL, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + BROWNS + ["flowing", "floppy"]
    },
    "cloche hat": {
        "types": [OutfitType.RETRO, OutfitType.ROMANTIC, OutfitType.COTTAGECORE],
        "colors": PASTELS + WHITES + BROWNS + ["felt", "vintage"]
    },
    "fascinator": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE, OutfitType.GOTHIC, OutfitType.FESTIVAL],
        "colors": BLACKS + JEWEL_TONES + METALLICS + ["feathered", "netted"]
    },
    "veiled hat": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + WHITES + ["veil", "mysterious"]
    },
    "sailor cap": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.FESTIVAL, OutfitType.RETRO],
        "colors": WHITES + BLUES + BLACKS + ["embroidered", "naval"]
    },
    "military peaked cap": {
        "types": [OutfitType.MILITARY, OutfitType.PUNK, OutfitType.CYBERPUNK, OutfitType.STREETWEAR],
        "colors": BLACKS + GREENS + METALLICS + ["structured", "insignia"]
    },
    "aviator cap": {
        "types": [OutfitType.STEAMPUNK, OutfitType.RETRO, OutfitType.MILITARY, OutfitType.FESTIVAL],
        "colors": BROWNS + BLACKS + ["leather", "lined"]
    },
    "ushanka": {
        "types": [OutfitType.RETRO, OutfitType.FESTIVAL, OutfitType.STREETWEAR],
        "colors": BROWNS + BLACKS + GRAYS + ["fur", "warm"]
    },
    "turban wrap": {
        "types": [OutfitType.ETHEREAL, OutfitType.FESTIVAL, OutfitType.ROMANTIC, OutfitType.AVANT_GARDE],
        "colors": JEWEL_TONES + PASTELS + WHITES + ["wrapped", "draped"]
    },
    "headscarf": {
        "types": [OutfitType.COTTAGECORE, OutfitType.ROMANTIC, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "colors": PASTELS + PATTERNS + ["silk", "tied"]
    },
    "hijab (styled as accessory)": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR],
        "colors": PASTELS + JEWEL_TONES + WHITES + ["styled", "flowing"]
    },
    "floral crown": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.COTTAGECORE, OutfitType.ETHEREAL],
        "colors": PASTELS + ["dried flowers", "fresh flowers", "braided"]
    },
    "tiara": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.ETHEREAL, OutfitType.KAWAII],
        "colors": METALLICS + WHITES + JEWEL_TONES + ["sparkling", "delicate"]
    },
    "crystal crown": {
        "types": [OutfitType.ETHEREAL, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL, OutfitType.GOTHIC],
        "colors": JEWEL_TONES + METALLICS + WHITES + ["glowing", "spiked"]
    },
    "horned headpiece": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.STEAMPUNK],
        "colors": BLACKS + EARTH_TONES + METALLICS + ["horned", "mythic"]
    },
    "bunny ears headband": {
        "types": [OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.LOLITA, OutfitType.CLUB_PARTY],
        "colors": PASTELS + WHITES + NEONS + ["plush", "playful"]
    },
    "cat ears headband": {
        "types": [OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.LOLITA, OutfitType.CLUB_PARTY],
        "colors": BLACKS + PASTELS + ["plush", "sparkly"]
    },
    "kawaii oversized bow headband": {
        "types": [OutfitType.KAWAII, OutfitType.LOLITA, OutfitType.FESTIVAL],
        "colors": PASTELS + REDS + ["oversized", "bow"]
    },
    "gothic lace veil": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.ETHEREAL],
        "colors": BLACKS + ["lace", "sheer"]
    },
    "witch hat": {
        "types": [OutfitType.GOTHIC, OutfitType.FESTIVAL, OutfitType.STEAMPUNK, OutfitType.AVANT_GARDE],
        "colors": BLACKS + PURPLES + ["pointed", "felt"]
    },
    "helmet": {
        "types": [OutfitType.STEAMPUNK, OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.AVANT_GARDE],
        "colors": METALLICS + BLACKS + ["visor", "padded", "decorated"]
    },

    # --- Eyewear ---
    "classic sunglasses": {
        "types": [OutfitType.BEACH_WEAR, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY, OutfitType.STREETWEAR],
        "colors": BLACKS + METALLICS + ["aviator", "wayfarer", "cat-eye"]
    },
    "round sunglasses": {
        "types": [OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.RETRO, OutfitType.STREETWEAR],
        "colors": METALLICS + BLACKS + PASTELS + ["round", "vintage"]
    },
    "oversized sunglasses": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.CLUB_PARTY, OutfitType.KAWAII],
        "colors": BLACKS + WHITES + PASTELS + ["oversized", "shield"]
    },
    "sport sunglasses": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + NEONS + ["wraparound", "performance"]
    },
    "mirrored sunglasses": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.CLUB_PARTY, OutfitType.ATHLEISURE],
        "colors": METALLICS + NEONS + ["mirrored", "reflective"]
    },
    "gradient lens sunglasses": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BEACH_WEAR, OutfitType.FESTIVAL],
        "colors": PASTELS + BLACKS + ["gradient", "tinted"]
    },
    "heart-shaped sunglasses": {
        "types": [OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.LOLITA, OutfitType.BEACH_WEAR],
        "colors": PASTELS + NEONS + REDS + ["heart", "playful"]
    },
    "star-shaped sunglasses": {
        "types": [OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.CLUB_PARTY],
        "colors": NEONS + PASTELS + ["star", "playful"]
    },
    "colored lens fashion glasses": {
        "types": [OutfitType.FESTIVAL, OutfitType.STREETWEAR, OutfitType.KAWAII, OutfitType.CYBERPUNK],
        "colors": NEONS + PASTELS + ["tinted", "transparent"]
    },
    "cyberpunk LED visor glasses": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "colors": NEONS + METALLICS + ["LED", "visor", "glowing"]
    },
    "futuristic shield sunglasses": {
        "types": [OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE, OutfitType.CLUB_PARTY, OutfitType.STREETWEAR],
        "colors": METALLICS + NEONS + BLACKS + ["shield", "wraparound"]
    },
    "steampunk goggles": {
        "types": [OutfitType.STEAMPUNK, OutfitType.AVANT_GARDE, OutfitType.GOTHIC, OutfitType.FESTIVAL],
        "colors": METALLICS + BROWNS + ["brass", "leather", "gears"]
    },
    "aviator goggles": {
        "types": [OutfitType.STEAMPUNK, OutfitType.MILITARY, OutfitType.FESTIVAL, OutfitType.RETRO],
        "colors": METALLICS + BROWNS + ["leather", "strap"]
    },
    "snow goggles": {
        "types": [OutfitType.ATHLEISURE, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "colors": NEONS + BLACKS + WHITES + ["protective", "wraparound"]
    },
    "reading glasses": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.RETRO],
        "colors": BLACKS + BROWNS + METALLICS + ["thin", "classic"]
    },
    "cat-eye eyeglasses": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.RETRO, OutfitType.KAWAII, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + PASTELS + REDS + ["cat-eye", "vintage"]
    },
    "oversized square glasses": {
        "types": [OutfitType.STREETWEAR, OutfitType.AVANT_GARDE, OutfitType.KAWAII, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + NEONS + ["oversized", "square"]
    },
    "half-rim glasses": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.RETRO],
        "colors": METALLICS + BLACKS + ["half-rim", "lightweight"]
    },
    "rimless glasses": {
        "types": [OutfitType.MINIMALIST, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "colors": METALLICS + ["rimless", "lightweight"]
    },
    "anime-style oversized round glasses": {
        "types": [OutfitType.KAWAII, OutfitType.LOLITA, OutfitType.FESTIVAL, OutfitType.STREETWEAR],
        "colors": PASTELS + BLACKS + ["oversized", "round"]
    },

    # --- Bags & Packs ---
    "shoulder bag": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.BUSINESS_WEAR, OutfitType.FESTIVAL],
        "colors": BLACKS + BROWNS + PASTELS + ["leather", "structured"]
    },
    "tote bag": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.BEACH_WEAR, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + WHITES + BROWNS + ["canvas", "oversized"]
    },
    "messenger bag": {
        "types": [OutfitType.STREETWEAR, OutfitType.BUSINESS_WEAR, OutfitType.MILITARY, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + BLACKS + GREENS + ["canvas", "leather"]
    },
    "satchel bag": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.PREPPY, OutfitType.COTTAGECORE],
        "colors": BROWNS + BLACKS + ["structured", "leather"]
    },
    "saddle bag": {
        "types": [OutfitType.COWBOY, OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.COTTAGECORE],
        "colors": BROWNS + EARTH_TONES + ["leather", "curved"]
    },
    "doctor's bag": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.RETRO, OutfitType.CASUAL_CHIC],
        "colors": BROWNS + BLACKS + ["vintage", "structured"]
    },
    "bowling bag": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "colors": BLACKS + WHITES + REDS + ["rounded", "vintage"]
    },
    "frame box bag": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.AVANT_GARDE],
        "colors": METALLICS + BLACKS + JEWEL_TONES + ["structured", "boxy"]
    },
    "hobo bag": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.BOHEMIAN, OutfitType.STREETWEAR],
        "colors": EARTH_TONES + BROWNS + ["slouchy", "soft"]
    },
    "bucket bag": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "colors": BROWNS + BLACKS + PASTELS + ["drawstring", "leather"]
    },
    "drawstring pouch": {
        "types": [OutfitType.FESTIVAL, OutfitType.EVENING_FORMAL, OutfitType.BOHEMIAN, OutfitType.KAWAII],
        "colors": PASTELS + JEWEL_TONES + METALLICS + ["drawstring", "soft"]
    },
    "backpack (classic)": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.FESTIVAL, OutfitType.NORMCORE],
        "colors": BLACKS + NEONS + BROWNS + ["canvas", "nylon"]
    },
    "mini backpack": {
        "types": [OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.STREETWEAR, OutfitType.LOLITA],
        "colors": PASTELS + NEONS + BLACKS + ["mini", "cute"]
    },
    "fanny pack / belt bag": {
        "types": [OutfitType.STREETWEAR, OutfitType.FESTIVAL, OutfitType.ATHLEISURE, OutfitType.CYBERPUNK],
        "colors": NEONS + BLACKS + METALLICS + ["zip", "utility"]
    },
    "sling bag": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.FESTIVAL],
        "colors": BLACKS + NEONS + ["crossbody", "compact"]
    },
    "camera bag": {
        "types": [OutfitType.STREETWEAR, OutfitType.FESTIVAL, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + BROWNS + ["padded", "leather"]
    },
    "laptop bag": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.STREETWEAR, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + BROWNS + ["padded", "sleek"]
    },
    "briefcase bag": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.PREPPY, OutfitType.MINIMALIST],
        "colors": BLACKS + BROWNS + ["structured", "leather"]
    },
    "clutch bag": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.BUSINESS_WEAR],
        "colors": BLACKS + METALLICS + JEWEL_TONES + ["sequined", "beaded"]
    },
    "envelope clutch": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + METALLICS + WHITES + ["envelope", "sleek"]
    },
    "minaudiere clutch": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": METALLICS + JEWEL_TONES + ["embellished", "beaded"]
    },
    "wristlet clutch": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CASUAL_CHIC, OutfitType.CLUB_PARTY],
        "colors": METALLICS + BLACKS + PASTELS + ["wristlet"]
    },
    "evening purse": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.CLUB_PARTY],
        "colors": JEWEL_TONES + METALLICS + WHITES + ["beaded", "satin"]
    },
    "beaded pouch bag": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.KAWAII, OutfitType.COTTAGECORE],
        "colors": PASTELS + JEWEL_TONES + ["beaded", "handmade"]
    },
    "sequin party bag": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.EVENING_FORMAL],
        "colors": METALLICS + NEONS + ["sequin", "sparkling"]
    },
    "metallic purse": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.CLUB_PARTY, OutfitType.CASUAL_CHIC],
        "colors": METALLICS + BLACKS + ["shiny", "reflective"]
    },
    "faux-fur purse": {
        "types": [OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.GOTHIC, OutfitType.STREETWEAR],
        "colors": PASTELS + BLACKS + WHITES + ["faux fur", "plush"]
    },
    "transparent PVC purse": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.FESTIVAL, OutfitType.CYBERPUNK, OutfitType.STREETWEAR],
        "colors": NEONS + METALLICS + ["transparent", "PVC"]
    },
    "jelly purse": {
        "types": [OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.BEACH_WEAR],
        "colors": NEONS + PASTELS + ["translucent", "jelly"]
    },
    "chainmail purse": {
        "types": [OutfitType.STEAMPUNK, OutfitType.GOTHIC, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "colors": METALLICS + BLACKS + ["chainmail", "linked"]
    },
    "spiked punk bag": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.GRUNGE, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["spiked", "studded"]
    },
    "coffin-shaped goth bag": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.FESTIVAL, OutfitType.AVANT_GARDE],
        "colors": BLACKS + METALLICS + ["coffin", "chain"]
    },
    "heart-shaped kawaii bag": {
        "types": [OutfitType.KAWAII, OutfitType.LOLITA, OutfitType.FESTIVAL, OutfitType.ROMANTIC],
        "colors": PASTELS + REDS + ["heart", "cute"]
    },
    "bunny-shaped plush bag": {
        "types": [OutfitType.KAWAII, OutfitType.LOLITA, OutfitType.FESTIVAL],
        "colors": PASTELS + WHITES + ["plush", "bunny"]
    },
    "lolita lace purse": {
        "types": [OutfitType.LOLITA, OutfitType.KAWAII, OutfitType.ROMANTIC],
        "colors": PASTELS + WHITES + ["lace", "bows"]
    },
    "festival fringe crossbody": {
        "types": [OutfitType.FESTIVAL, OutfitType.BOHEMIAN, OutfitType.COWBOY],
        "colors": EARTH_TONES + BROWNS + NEONS + ["fringe", "movement"]
    },
    "military utility pouch": {
        "types": [OutfitType.MILITARY, OutfitType.STREETWEAR, OutfitType.FESTIVAL],
        "colors": GREENS + BROWNS + BLACKS + ["utility", "straps"]
    },
    "ammo belt bag": {
        "types": [OutfitType.MILITARY, OutfitType.PUNK, OutfitType.FESTIVAL, OutfitType.STEAMPUNK],
        "colors": GREENS + BROWNS + BLACKS + ["ammo", "utility"]
    },
    "holster-style crossbody": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.STEAMPUNK, OutfitType.PUNK],
        "colors": BLACKS + METALLICS + ["holster", "strapped"]
    },

    # --- Belt Variants & Harnesses ---
    "classic leather belt": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.COWBOY],
        "colors": BROWNS + BLACKS + ["leather", "classic"]
    },
    "skinny belt": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST],
        "colors": BROWNS + BLACKS + METALLICS + ["skinny", "sleek"]
    },
    "wide waist belt": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.BUSINESS_WEAR, OutfitType.STEAMPUNK, OutfitType.GOTHIC],
        "colors": BLACKS + BROWNS + METALLICS + ["wide", "cinched"]
    },
    "corset belt": {
        "types": [OutfitType.STEAMPUNK, OutfitType.GOTHIC, OutfitType.AVANT_GARDE, OutfitType.PUNK],
        "colors": BLACKS + BROWNS + ["lace-up", "cincher"]
    },
    "obi belt": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.FESTIVAL],
        "colors": PASTELS + JEWEL_TONES + EARTH_TONES + ["wrap", "sash"]
    },
    "sash belt": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": PASTELS + WHITES + ["sash", "bow"]
    },
    "braided belt": {
        "types": [OutfitType.COTTAGECORE, OutfitType.BOHEMIAN, OutfitType.CASUAL_CHIC, OutfitType.COWBOY],
        "colors": EARTH_TONES + BROWNS + ["braided", "woven"]
    },
    "chain belt": {
        "types": [OutfitType.CLUB_PARTY, OutfitType.PUNK, OutfitType.CYBERPUNK, OutfitType.FESTIVAL],
        "colors": METALLICS + BLACKS + ["chain", "dangling"]
    },
    "studded belt": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.GRUNGE],
        "colors": BLACKS + METALLICS + ["studded"]
    },
    "spike belt": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["spiked"]
    },
    "grommet belt": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CYBERPUNK, OutfitType.GRUNGE],
        "colors": BLACKS + METALLICS + ["grommet", "holes"]
    },
    "western-style belt": {
        "types": [OutfitType.COWBOY, OutfitType.FESTIVAL, OutfitType.BOHEMIAN],
        "colors": BROWNS + EARTH_TONES + ["tooled", "buckle"]
    },
    "double-buckle belt": {
        "types": [OutfitType.FESTIVAL, OutfitType.PUNK, OutfitType.STREETWEAR],
        "colors": BLACKS + METALLICS + ["double buckle", "statement"]
    },
    "harness belt": {
        "types": [OutfitType.PUNK, OutfitType.STEAMPUNK, OutfitType.CYBERPUNK, OutfitType.AVANT_GARDE],
        "colors": BLACKS + METALLICS + ["harness", "strapped"]
    },
    "utility belt": {
        "types": [OutfitType.MILITARY, OutfitType.FESTIVAL, OutfitType.STEAMPUNK, OutfitType.PUNK],
        "colors": GREENS + BROWNS + BLACKS + ["utility", "pouches"]
    },
    "fanny pack belt": {
        "types": [OutfitType.FESTIVAL, OutfitType.STREETWEAR, OutfitType.ATHLEISURE],
        "colors": NEONS + BLACKS + ["zip", "utility"]
    },
    "body harness straps": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CYBERPUNK, OutfitType.PUNK, OutfitType.CLUB_PARTY],
        "colors": BLACKS + METALLICS + ["harness", "straps"]
    },

    # --- Gloves & Handwear ---
    "knit gloves": {
        "types": [OutfitType.COTTAGECORE, OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": BROWNS + GRAYS + WHITES + ["knit", "wool"]
    },
    "leather gloves": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.GOTHIC, OutfitType.STEAMPUNK, OutfitType.CASUAL_CHIC],
        "colors": BLACKS + BROWNS + ["leather", "sleek"]
    },
    "driving gloves": {
        "types": [OutfitType.STEAMPUNK, OutfitType.PUNK, OutfitType.STREETWEAR, OutfitType.RETRO],
        "colors": BROWNS + BLACKS + ["fingerless", "vented"]
    },
    "fingerless knit gloves": {
        "types": [OutfitType.GRUNGE, OutfitType.STREETWEAR, OutfitType.PUNK],
        "colors": BLACKS + GRAYS + ["fingerless", "knit"]
    },
    "opera-length satin gloves": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.GOTHIC],
        "colors": WHITES + BLACKS + JEWEL_TONES + ["opera", "satin"]
    },
    "elbow-length gloves": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.GOTHIC, OutfitType.ROMANTIC],
        "colors": BLACKS + WHITES + JEWEL_TONES + ["velvet", "lace", "elbow-length"]
    },
    "sheer mesh gloves": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.CLUB_PARTY, OutfitType.GOTHIC, OutfitType.ROMANTIC],
        "colors": BLACKS + WHITES + PASTELS + ["sheer", "mesh"]
    },
    "fishnet gloves": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CLUB_PARTY, OutfitType.CYBERPUNK],
        "colors": BLACKS + NEONS + ["fishnet"]
    },
    "spiked punk gloves": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["spiked", "studded"]
    },
    "arm warmers": {
        "types": [OutfitType.GRUNGE, OutfitType.GOTHIC, OutfitType.STREETWEAR, OutfitType.KAWAII],
        "colors": BLACKS + PASTELS + ["knit", "cozy"]
    },
    "gauntlet gloves": {
        "types": [OutfitType.STEAMPUNK, OutfitType.AVANT_GARDE, OutfitType.GOTHIC, OutfitType.PUNK],
        "colors": METALLICS + BLACKS + BROWNS + ["gauntlet", "armor"]
    },
    "lace bridal gloves": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.COTTAGECORE],
        "colors": WHITES + PASTELS + ["lace", "bridal"]
    },
    "winter mittens": {
        "types": [OutfitType.COTTAGECORE, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": PASTELS + BROWNS + WHITES + ["knit", "warm"]
    },
    "fur-trimmed gloves": {
        "types": [OutfitType.GOTHIC, OutfitType.EVENING_FORMAL, OutfitType.COTTAGECORE],
        "colors": BLACKS + WHITES + BROWNS + ["fur-trimmed"]
    },
    "tech touchscreen gloves": {
        "types": [OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.MINIMALIST],
        "colors": BLACKS + GRAYS + ["tech", "touchscreen"]
    },

    # --- Scarves, Shawls & Wraps ---
    "silk scarf": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": PASTELS + JEWEL_TONES + ["silk", "printed"]
    },
    "chiffon scarf": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "colors": PASTELS + WHITES + ["sheer", "lightweight"]
    },
    "square neckerchief": {
        "types": [OutfitType.RETRO, OutfitType.CASUAL_CHIC, OutfitType.PREPPY],
        "colors": REDS + PASTELS + PATTERNS + ["square", "tied"]
    },
    "bandana": {
        "types": [OutfitType.FESTIVAL, OutfitType.COWBOY, OutfitType.STREETWEAR, OutfitType.PUNK],
        "colors": REDS + BLACKS + PATTERNS + ["bandana", "paisley"]
    },
    "infinity scarf": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE, OutfitType.NORMCORE],
        "colors": PASTELS + BROWNS + WHITES + ["infinity", "loop"]
    },
    "knit scarf": {
        "types": [OutfitType.COTTAGECORE, OutfitType.STREETWEAR, OutfitType.NORMCORE],
        "colors": BROWNS + GRAYS + WHITES + ["knit", "chunky"]
    },
    "oversized blanket scarf": {
        "types": [OutfitType.STREETWEAR, OutfitType.COTTAGECORE, OutfitType.FESTIVAL],
        "colors": EARTH_TONES + PASTELS + ["oversized", "blanket"]
    },
    "plaid scarf": {
        "types": [OutfitType.COTTAGECORE, OutfitType.STREETWEAR, OutfitType.PREPPY],
        "colors": PATTERNS + EARTH_TONES + ["plaid", "tartan"]
    },
    "fringe shawl": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.ETHEREAL],
        "colors": EARTH_TONES + PASTELS + ["fringe", "shawl"]
    },
    "lace shawl": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.COTTAGECORE],
        "colors": WHITES + PASTELS + ["lace", "delicate"]
    },
    "feather stole": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.AVANT_GARDE, OutfitType.ETHEREAL],
        "colors": WHITES + BLACKS + PASTELS + ["feather", "luxury"]
    },
    "faux fur stole": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.GOTHIC, OutfitType.ROMANTIC],
        "colors": BLACKS + WHITES + BROWNS + ["faux fur", "plush"]
    },
    "sheer organza wrap": {
        "types": [OutfitType.ETHEREAL, OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + ["sheer", "organza"]
    },
    "pashmina scarf": {
        "types": [OutfitType.BUSINESS_WEAR, OutfitType.CASUAL_CHIC, OutfitType.COTTAGECORE],
        "colors": EARTH_TONES + PASTELS + ["pashmina", "soft"]
    },
    "hijab wrap": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.BUSINESS_WEAR, OutfitType.MINIMALIST],
        "colors": PASTELS + JEWEL_TONES + WHITES + ["wrap", "styled"]
    },
    "capelet wrap": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.ETHEREAL],
        "colors": WHITES + BLACKS + JEWEL_TONES + ["capelet", "structured"]
    },
    "poncho-style wrap": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.COTTAGECORE],
        "colors": EARTH_TONES + PATTERNS + ["poncho", "woven"]
    },

    # --- Hair Accessories ---
    "hair bow (large)": {
        "types": [OutfitType.LOLITA, OutfitType.KAWAII, OutfitType.PIN_UP],
        "colors": PASTELS + REDS + ["large", "satin", "polka dots"]
    },
    "hair bow (small)": {
        "types": [OutfitType.LOLITA, OutfitType.KAWAII, OutfitType.PIN_UP],
        "colors": PASTELS + REDS + ["small", "satin", "polka dots"]
    },
    "barrette (plain)": {
        "types": [OutfitType.MINIMALIST, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "colors": METALLICS + WHITES + ["plain", "sleek"]
    },
    "bejeweled barrette": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC, OutfitType.KAWAII],
        "colors": METALLICS + JEWEL_TONES + ["bejeweled", "sparkling"]
    },
    "hair comb (decorative)": {
        "types": [OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL, OutfitType.COTTAGECORE],
        "colors": METALLICS + WHITES + ["decorative", "pearls"]
    },
    "crystal hairpins": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "colors": WHITES + JEWEL_TONES + ["crystal", "sparkling"]
    },
    "pearl hairpins": {
        "types": [OutfitType.ROMANTIC, OutfitType.PREPPY, OutfitType.EVENING_FORMAL],
        "colors": WHITES + ["pearl", "delicate"]
    },
    "scrunchie": {
        "types": [OutfitType.KAWAII, OutfitType.STREETWEAR, OutfitType.FESTIVAL, OutfitType.LOLITA],
        "colors": PASTELS + NEONS + ["fabric", "soft"]
    },
    "silk scrunchie": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.ROMANTIC],
        "colors": PASTELS + WHITES + ["silk", "smooth"]
    },
    "ribbon tie": {
        "types": [OutfitType.ROMANTIC, OutfitType.LOLITA, OutfitType.COTTAGECORE],
        "colors": PASTELS + WHITES + REDS + ["ribbon", "bow"]
    },
    "headband (plain)": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.ATHLEISURE, OutfitType.KAWAII],
        "colors": PASTELS + BLACKS + ["plain", "stretch"]
    },
    "headband (padded statement)": {
        "types": [OutfitType.KAWAII, OutfitType.CASUAL_CHIC, OutfitType.EVENING_FORMAL],
        "colors": PASTELS + JEWEL_TONES + ["padded", "statement"]
    },
    "beaded headband": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.KAWAII],
        "colors": JEWEL_TONES + WHITES + ["beaded", "delicate"]
    },
    "flower headband": {
        "types": [OutfitType.BOHEMIAN, OutfitType.FESTIVAL, OutfitType.COTTAGECORE],
        "colors": PASTELS + JEWEL_TONES + ["floral", "wreath"]
    },
    "tiara-style headband": {
        "types": [OutfitType.ROMANTIC, OutfitType.KAWAII, OutfitType.EVENING_FORMAL],
        "colors": METALLICS + WHITES + ["tiara", "sparkling"]
    },
    "lace headpiece": {
        "types": [OutfitType.GOTHIC, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "colors": BLACKS + WHITES + ["lace", "veil"]
    },
    "feathered fascinator": {
        "types": [OutfitType.AVANT_GARDE, OutfitType.EVENING_FORMAL, OutfitType.FESTIVAL],
        "colors": JEWEL_TONES + BLACKS + ["feathered", "decorated"]
    },
    "hair stick": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "colors": EARTH_TONES + METALLICS + ["hair stick", "carved"]
    },
    "decorative chopsticks": {
        "types": [OutfitType.BOHEMIAN, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "colors": EARTH_TONES + METALLICS + ["chopsticks", "decorative"]
    },
    "hair claw clip": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.MINIMALIST, OutfitType.KAWAII],
        "colors": PASTELS + BLACKS + ["claw", "acrylic"]
    },
    "glitter hair clip": {
        "types": [OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.LOLITA],
        "colors": NEONS + PASTELS + ["glitter", "sparkling"]
    },
    "kawaii animal-ear clips": {
        "types": [OutfitType.KAWAII, OutfitType.LOLITA, OutfitType.FESTIVAL],
        "colors": PASTELS + NEONS + ["ears", "cute"]
    },
    "gothic bat-wing hair clip": {
        "types": [OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.FESTIVAL],
        "colors": BLACKS + METALLICS + ["bat-wing", "dark"]
    },
    "steampunk gear hair accessory": {
        "types": [OutfitType.STEAMPUNK, OutfitType.AVANT_GARDE, OutfitType.GOTHIC],
        "colors": METALLICS + BROWNS + ["gears", "brass"]
    },

    # --- Other Unique Accessories ---
    "parasol": {
        "types": [OutfitType.LOLITA, OutfitType.GOTHIC, OutfitType.COTTAGECORE, OutfitType.ROMANTIC],
        "colors": WHITES + BLACKS + PASTELS + ["lace", "parasol"]
    },
    "folding hand fan": {
        "types": [OutfitType.LOLITA, OutfitType.FESTIVAL, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": PASTELS + JEWEL_TONES + ["fan", "folding"]
    },
    "mask (masquerade)": {
        "types": [OutfitType.EVENING_FORMAL, OutfitType.GOTHIC, OutfitType.AVANT_GARDE, OutfitType.CLUB_PARTY],
        "colors": BLACKS + METALLICS + JEWEL_TONES + ["masquerade", "lace"]
    },
    "gas mask": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STEAMPUNK, OutfitType.PUNK, OutfitType.AVANT_GARDE],
        "colors": BLACKS + METALLICS + ["gas mask", "industrial"]
    },
    "LED face visor": {
        "types": [OutfitType.CYBERPUNK, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "colors": NEONS + METALLICS + ["LED", "visor"]
    },
    "spiked collar harness": {
        "types": [OutfitType.PUNK, OutfitType.GOTHIC, OutfitType.CYBERPUNK],
        "colors": BLACKS + METALLICS + ["spiked", "collar", "harness"]
    },
    "shoulder armor accessory": {
        "types": [OutfitType.STEAMPUNK, OutfitType.AVANT_GARDE, OutfitType.GOTHIC, OutfitType.PUNK],
        "colors": METALLICS + BLACKS + ["armor", "shoulder"]
    },
    "chainmail shawl": {
        "types": [OutfitType.STEAMPUNK, OutfitType.GOTHIC, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL],
        "colors": METALLICS + BLACKS + ["chainmail", "draped"]
    },
    "feather wings": {
        "types": [OutfitType.ETHEREAL, OutfitType.FESTIVAL, OutfitType.AVANT_GARDE, OutfitType.ROMANTIC],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["feather", "wings"]
    },
    "demon horns": {
        "types": [OutfitType.GOTHIC, OutfitType.AVANT_GARDE, OutfitType.FESTIVAL, OutfitType.PUNK],
        "colors": BLACKS + REDS + METALLICS + ["horns", "demonic"]
    },
    "halo headpiece": {
        "types": [OutfitType.ETHEREAL, OutfitType.ROMANTIC, OutfitType.AVANT_GARDE],
        "colors": WHITES + METALLICS + ["halo", "glowing"]
    },
    "body jewelry": {
        "types": [OutfitType.ETHEREAL, OutfitType.FESTIVAL, OutfitType.CLUB_PARTY, OutfitType.BOHEMIAN],
        "colors": METALLICS + ["body chain", "harness"]
    },
    "keychains / purse charms": {
        "types": [OutfitType.KAWAII, OutfitType.FESTIVAL, OutfitType.STREETWEAR],
        "colors": NEONS + PASTELS + ["charm", "dangling"]
    },
    "techwear straps and clips": {
        "types": [OutfitType.CYBERPUNK, OutfitType.STREETWEAR, OutfitType.ATHLEISURE, OutfitType.PUNK],
        "colors": BLACKS + METALLICS + ["techwear", "utility", "clips"]
    },
    
    # Lingerie Accessories - Garter Belts & Hosiery Support
    "garter belt": {
        "types": [OutfitType.LINGERIE, OutfitType.VINTAGE, OutfitType.ROMANTIC],
        "colors": WHITES + BLACKS + REDS + JEWEL_TONES + ["classic", "vintage style", "suspenders"]
    },
    "suspender belt": {
        "types": [OutfitType.LINGERIE, OutfitType.VINTAGE, OutfitType.PIN_UP],
        "colors": WHITES + BLACKS + REDS + BROWNS + ["classic style", "adjustable", "metal clips"]
    },
    "strappy harness garter belt": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + METALLICS + ["harness style", "strappy", "hardware"]
    },
    "corset-style garter belt": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.VINTAGE],
        "colors": BLACKS + REDS + JEWEL_TONES + ["boned", "lace-up", "structured"]
    },
    
    # Stockings & Hosiery
    "classic sheer stockings": {
        "types": [OutfitType.LINGERIE, OutfitType.BUSINESS_WEAR, OutfitType.EVENING_FORMAL],
        "colors": WHITES + BLACKS + ["sheer", "nude", "classic"]
    },
    "fishnet stockings": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.PUNK, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + REDS + ["fishnet", "patterned", "textured"]
    },
    "lace-top stockings": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + BLACKS + PASTELS + ["lace trim", "delicate", "feminine"]
    },
    "back-seam stockings": {
        "types": [OutfitType.LINGERIE, OutfitType.VINTAGE, OutfitType.PIN_UP],
        "colors": WHITES + BLACKS + ["vintage style", "seamed", "retro"]
    },
    "thigh-high opaque stockings": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + JEWEL_TONES + ["opaque", "thigh-high", "stay-up"]
    },
    "over-the-knee lingerie socks": {
        "types": [OutfitType.LINGERIE, OutfitType.KAWAII, OutfitType.CLUB_PARTY],
        "colors": WHITES + BLACKS + PASTELS + PINKS + ["over-knee", "soft", "cute"]
    },
    "stay-up silicone grip stockings": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.CLUB_PARTY],
        "colors": WHITES + BLACKS + PASTELS + ["stay-up", "silicone band", "no garters"]
    },
    "lace anklets": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + BLACKS + PASTELS + ["delicate lace", "ankle socks", "feminine"]
    },
    "sheer footless stockings": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + BLACKS + PASTELS + ["footless", "sheer", "leg warmers"]
    },
    
    # Gloves & Arm Accessories
    "short lace gloves": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + BLACKS + PASTELS + ["delicate lace", "wrist length", "feminine"]
    },
    "elbow-length lace gloves": {
        "types": [OutfitType.LINGERIE, OutfitType.EVENING_FORMAL, OutfitType.VINTAGE],
        "colors": WHITES + BLACKS + PASTELS + ["long gloves", "elegant", "formal"]
    },
    "sheer mesh gloves": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.AVANT_GARDE],
        "colors": WHITES + BLACKS + JEWEL_TONES + ["sheer", "mesh", "see-through"]
    },
    "opera length satin gloves": {
        "types": [OutfitType.LINGERIE, OutfitType.EVENING_FORMAL, OutfitType.VINTAGE],
        "colors": WHITES + BLACKS + JEWEL_TONES + ["satin", "opera length", "luxury"]
    },
    "fishnet gloves": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.PUNK],
        "colors": BLACKS + WHITES + REDS + ["fishnet", "textured", "edgy"]
    },
    "fingerless lace gloves": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.ROMANTIC],
        "colors": WHITES + BLACKS + PASTELS + ["fingerless", "lace", "vintage"]
    },
    "latex fetish gloves": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + METALLICS + ["latex", "vinyl", "fetish", "shiny"]
    },
    "feather-trim gloves": {
        "types": [OutfitType.LINGERIE, OutfitType.VINTAGE, OutfitType.ROMANTIC],
        "colors": WHITES + BLACKS + PASTELS + ["feather trim", "luxury", "glamorous"]
    },
    "sheer detachable sleeves": {
        "types": [OutfitType.LINGERIE, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "colors": WHITES + BLACKS + PASTELS + ["detachable", "sheer", "flowing"]
    },
    
    # Body Accessories & Harnesses
    "waist cincher belt": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.VINTAGE],
        "colors": BLACKS + REDS + BROWNS + ["cinching", "corset style", "structured"]
    },
    "corset belt": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.VINTAGE],
        "colors": BLACKS + REDS + JEWEL_TONES + ["boned", "lace-up", "waist defining"]
    },
    "underbust harness": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + METALLICS + ["underbust", "strappy", "hardware"]
    },
    "leather chest harness": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + BROWNS + REDS + ["leather", "chest piece", "buckles"]
    },
    "body chains": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.ETHEREAL],
        "colors": METALLICS + JEWEL_TONES + ["gold", "silver", "draped chains"]
    },
    "belly chain": {
        "types": [OutfitType.LINGERIE, OutfitType.BEACH_WEAR, OutfitType.ETHEREAL],
        "colors": METALLICS + JEWEL_TONES + ["waist chain", "delicate", "body jewelry"]
    },
    "pearl body harness": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + PASTELS + ["pearl strands", "luxury", "elegant"]
    },
    "rhinestone harness": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL],
        "colors": WHITES + METALLICS + JEWEL_TONES + ["rhinestones", "sparkling", "glamorous"]
    },
    "strappy elastic harness": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + REDS + JEWEL_TONES + ["elastic bands", "strappy", "adjustable"]
    },
    
    # Neck & Head Accessories
    "lace choker": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.GOTHIC],
        "colors": WHITES + BLACKS + PASTELS + ["delicate lace", "feminine", "vintage"]
    },
    "satin ribbon choker": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.KAWAII],
        "colors": WHITES + PASTELS + PINKS + JEWEL_TONES + ["satin ribbon", "bow", "soft"]
    },
    "pearl jewel choker": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["pearls", "jeweled", "elegant"]
    },
    "leather fetish collar": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + BROWNS + REDS + ["leather", "fetish style", "buckles"]
    },
    "chain choker with pendant": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + METALLICS + JEWEL_TONES + ["chain", "pendant", "hardware"]
    },
    "harness choker with rings": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + METALLICS + REDS + ["harness style", "O-rings", "hardware"]
    },
    "lace masquerade eye mask": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.EVENING_FORMAL],
        "colors": WHITES + BLACKS + JEWEL_TONES + ["lace", "masquerade", "mysterious"]
    },
    "satin blindfold": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC],
        "colors": WHITES + BLACKS + REDS + JEWEL_TONES + ["satin", "soft", "sensual"]
    },
    "lingerie bunny ears headband": {
        "types": [OutfitType.LINGERIE, OutfitType.KAWAII, OutfitType.CLUB_PARTY],
        "colors": WHITES + BLACKS + PINKS + ["bunny ears", "cute", "costume"]
    },
    "cat ears headband": {
        "types": [OutfitType.LINGERIE, OutfitType.KAWAII, OutfitType.CLUB_PARTY],
        "colors": BLACKS + WHITES + JEWEL_TONES + ["cat ears", "cute", "costume"]
    },
    "feathered headpiece": {
        "types": [OutfitType.LINGERIE, OutfitType.VINTAGE, OutfitType.EVENING_FORMAL],
        "colors": WHITES + BLACKS + JEWEL_TONES + ["feathers", "vintage", "glamorous"]
    },
    "lace tiara crown": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + PASTELS + METALLICS + ["lace", "tiara", "princess"]
    },
    
    # Foot & Ankle Accessories
    "lace anklets hosiery": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + BLACKS + PASTELS + ["delicate lace", "ankle socks", "feminine"]
    },
    "decorative shoe clips": {
        "types": [OutfitType.LINGERIE, OutfitType.VINTAGE, OutfitType.EVENING_FORMAL],
        "colors": WHITES + METALLICS + JEWEL_TONES + ["bows", "pearls", "feathers", "clips"]
    },
    "ankle strap heels": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL],
        "colors": WHITES + BLACKS + REDS + METALLICS + ["ankle straps", "heels", "sexy"]
    },
    
    # Wraps & Cover-ups
    "silk lingerie robe": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["silk", "short", "sheer", "trimmed"]
    },
    "feather boa": {
        "types": [OutfitType.LINGERIE, OutfitType.VINTAGE, OutfitType.CLUB_PARTY],
        "colors": WHITES + BLACKS + JEWEL_TONES + ["feathers", "glamorous", "vintage"]
    },
    "satin sash": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["satin", "tied", "bow"]
    },
    "lace mesh lingerie capelet": {
        "types": [OutfitType.LINGERIE, OutfitType.ETHEREAL, OutfitType.ROMANTIC],
        "colors": WHITES + BLACKS + PASTELS + ["lace", "mesh", "cape", "delicate"]
    },
    
    # Wrist & Arm Restraints
    "decorative lace cuffs": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + BLACKS + PASTELS + ["lace", "decorative", "feminine"]
    },
    "satin decorative cuffs": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.CLUB_PARTY],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["satin", "soft", "luxury"]
    },
    "leather decorative cuffs": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + BROWNS + REDS + ["leather", "buckles", "edgy"]
    },
    "silk ribbon wrist ties": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["silk ties", "ribbons", "soft"]
    },
    
    # Leg Accessories
    "lace leg garters": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + BLACKS + PASTELS + ["lace", "thigh garter", "delicate"]
    },
    "satin leg garters": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + PASTELS + JEWEL_TONES + ["satin", "smooth", "elegant"]
    },
    "jeweled leg garters": {
        "types": [OutfitType.LINGERIE, OutfitType.EVENING_FORMAL, OutfitType.ROMANTIC],
        "colors": WHITES + METALLICS + JEWEL_TONES + ["jeweled", "sparkling", "luxury"]
    },
    "bridal garter": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + PASTELS + ["classic white", "bow", "bridal", "tradition"]
    },
    "sheer tutu mini skirt overlay": {
        "types": [OutfitType.LINGERIE, OutfitType.ETHEREAL, OutfitType.KAWAII],
        "colors": WHITES + PASTELS + PINKS + ["sheer", "tutu", "overlay", "playful"]
    },
    
    # Intimate Accessories
    "sequin pasties": {
        "types": [OutfitType.LINGERIE, OutfitType.CLUB_PARTY, OutfitType.EVENING_FORMAL],
        "colors": METALLICS + JEWEL_TONES + NEONS + ["sequins", "sparkling", "minimal"]
    },
    "lace pasties": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.ETHEREAL],
        "colors": WHITES + BLACKS + PASTELS + ["delicate lace", "feminine", "soft"]
    },
    "pearl pasties": {
        "types": [OutfitType.LINGERIE, OutfitType.ROMANTIC, OutfitType.VINTAGE],
        "colors": WHITES + PASTELS + ["pearls", "luxury", "elegant"]
    },
    "feather pasties": {
        "types": [OutfitType.LINGERIE, OutfitType.VINTAGE, OutfitType.CLUB_PARTY],
        "colors": WHITES + BLACKS + JEWEL_TONES + ["feathers", "glamorous", "burlesque"]
    },
    "chain nipple covers": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + METALLICS + JEWEL_TONES + ["chains", "hardware", "edgy"]
    },
    
    # Costume Accessories
    "decorative whip": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + BROWNS + REDS + ["decorative", "costume", "roleplay"]
    },
    "riding crop accessory": {
        "types": [OutfitType.LINGERIE, OutfitType.GOTHIC, OutfitType.CLUB_PARTY],
        "colors": BLACKS + BROWNS + ["riding crop", "costume", "prop"]
    }
}

