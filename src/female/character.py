NATIONALITY = [
    # Europe
    "Swedish", "Norwegian", "Finnish", "Danish", "Icelandic",
    "Irish", "Scottish", "English", "Welsh",
    "French", "Italian", "Spanish", "Portuguese",
    "German", "Austrian", "Swiss",
    "Polish", "Czech", "Slovak", "Hungarian",
    "Greek", "Turkish", "Dutch", "Belgian",
    "Ukrainian", "Russian", "Romanian", "Bulgarian",
    "Serbian", "Croatian", "Bosnian", "Slovenian",
    "Latvian", "Lithuanian", "Estonian",

    # Asia
    "Chinese", "Japanese", "Korean",
    "Thai", "Vietnamese", "Filipino", "Indonesian",
    "Indian", "Pakistani", "Bangladeshi", "Nepali",
    "Sri Lankan", "Mongolian",

    # Americas
    "American", "Canadian", "Mexican", "Brazilian", "Argentinian",
    "Chilean", "Colombian", "Cuban", "Puerto Rican", "Dominican",

    # Africa
    "Nigerian", "Ethiopian", "Egyptian", "South African", "Moroccan",
    "Kenyan", "Ghanaian",

    # Pacific
    "Australian", "New Zealander", "Samoan", "Tongan", "Fijian"
]

BODY_TYPE = [
    "slim", "fit", "athletic", "curvy", "toned", "hourglass", "petite", "plus size", "voluptuous", "lithe", "muscular", "lean"
]

BREAST_SIZES = [
    "small breasts", "medium breasts", "large breasts", "very large breasts",
    "perky breasts", "round breasts", "teardrop-shaped breasts", "wide-set breasts",
    "close-set breasts", "natural breasts", "augmented breasts"
]

# Hair styles with weights (style, weight) - higher weight = more common
# Long/medium common styles have higher weights, very styled/unique styles have lower weights
HAIR_STYLES = [
    # Long hair (most common for women)
    ("long straight hair", 10),
    ("long wavy hair", 10),
    ("long curly hair", 8),
    ("long coily hair", 5),
    ("extra-long silky hair", 4),
    ("long layered hair", 9),
    ("long hair with bangs", 8),
    ("long beach waves", 9),
    ("long tousled hair", 7),
    ("long sleek ponytail", 7),

    # Medium hair (very common)
    ("shoulder-length straight hair", 10),
    ("shoulder-length wavy hair", 10),
    ("medium curly hair", 7),
    ("medium layered cut", 8),
    ("medium bob with bangs", 7),
    ("messy medium waves", 8),
    ("shoulder-length blowout", 6),
    ("textured lob", 7),

    # Short hair (less common)
    ("short bob cut", 5),
    ("angled bob", 5),
    ("pixie cut", 3),
    ("shaggy bob", 4),
    ("boyish short cut", 2),
    ("short curls", 4),
    ("short spiky hair", 2),
    ("sleek short cut", 3),

    # Updos (moderately common)
    ("high ponytail", 8),
    ("low ponytail", 8),
    ("side ponytail", 5),
    ("messy bun", 9),
    ("tight ballerina bun", 5),
    ("elegant chignon", 4),
    ("half-up bun", 7),
    ("space buns", 3),
    ("French twist", 3),
    ("sleek updo", 4),

    # Braids & twists (moderately common to rare)
    ("classic braid", 6),
    ("fishtail braid", 5),
    ("Dutch braid", 4),
    ("French braid", 5),
    ("side braid", 6),
    ("crown braid", 3),
    ("double braids", 4),
    ("box braids", 3),
    ("micro braids", 2),
    ("twist braids", 3),
    ("braided ponytail", 5),

    # Styled looks (rare/special occasion)
    ("retro 60s beehive", 1),
    ("70s feathered hair", 2),
    ("80s crimped hair", 1),
    ("Hollywood glam waves", 3),
    ("red carpet updo", 2),
    ("rocker shag cut", 2),
    ("layered wolf cut", 3),
    ("mullet-inspired cut", 1),

    # Playful/casual (common)
    ("messy bedhead hair", 6),
    ("windswept hair", 5),
    ("wet-look hair", 3),
    ("half-up half-down style", 8),
    ("pigtails", 3),
    ("low pigtails", 3),
    ("side-swept waves", 7),
    ("hair with curtain bangs", 6),

    # Unique (rare)
    ("undercut with long top", 2),
    ("asymmetrical bob", 3),
    ("curly afro", 2),
    ("tight coils", 2),
    ("dreadlocks", 1),
    ("loose dreadlocks", 2),
    ("cornrows", 2),
    ("halo braid", 3),
    ("voluminous curls", 5)
]

# Hair colors with weights (color, weight) - common colors have higher weights
HAIR_COLORS = [
    ("blonde", 8),
    ("platinum blonde", 4),
    ("dirty blonde", 7),
    ("light brown", 9),
    ("chestnut brown", 8),
    ("dark brown", 10),
    ("jet black", 9),
    ("auburn", 5),
    ("fiery red", 3),
    ("strawberry blonde", 4),
    ("silver", 2),
    ("blue highlights", 1),
    ("pink highlights", 1),
    ("ombre", 3),
    ("balayage", 4)
]

# Eye colors with weights (color, weight) - common colors have higher weights
EYE_COLORS = [
    ("blue", 10),
    ("ice blue", 4),
    ("green", 8),
    ("emerald", 5),
    ("brown", 10),
    ("dark brown", 10),
    ("hazel", 7),
    ("amber", 1),
    ("gray", 5)
]

SKIN_TONES = [
    "fair skin", "light skin", "medium skin", "olive skin", "sun-kissed tan",
    "golden tan", "bronze skin", "deep brown skin"
]

FACIAL_FEATURES = [
    # Eyes & brows
    "long curled eyelashes", "thick eyelashes", "delicate lower lashes",
    "arched eyebrows", "soft rounded eyebrows", "perfectly shaped brows",
    "shimmer around eyes",

    # Cheeks & jaw
    "high cheekbones", "sculpted cheeks", "subtle rounded cheeks",
    "slender jawline", "delicate chin",

    # Distinctive feminine touches
    "dimples", "freckles across nose", "beauty mark above lip",
    "tiny beauty spot on cheek", "glowing complexion",

    # Jewelry/piercings (subtle feminine)
    "pierced ears", "small nose stud", "dainty earrings",
    "tiny diamond stud", "thin gold hoop earrings",
]

LIP_SHAPES = [
    "full lips", "plump lips", "heart-shaped lips", "wide lips",
    "bow-shaped lips", "subtle pout"
]

EYE_SHAPES = [
    "almond-shaped eyes", "round eyes", "cat-like eyes",
    "upturned eyes", "downturned eyes", "monolid eyes"
]

NOSE_SHAPES = [
    "button nose", "aquiline nose", "straight nose", "upturned nose",
    "slender nose"
]

MAKEUP_STYLES = [
    "natural makeup",
    "no makeup look",
    "soft glam",
    "dewy makeup",
    "matte makeup",

    # Eyes
    "smokey eye makeup",
    "soft brown smokey eye",
    "neutral eyeshadow tones",
    "cat-eye eyeliner",
    "winged eyeliner",
    "subtle eyeliner",
    "rosy eyeshadow",
    "gold shimmer eyeshadow",
    "soft pastel eyeshadow",

    # Lips
    "bold red lipstick",
    "soft pink lipstick",
    "nude lipstick",
    "glossy lips",
    "matte lipstick finish",
    "peachy lip tint",
    "berry-toned lipstick",

    # Overall look
    "romantic soft makeup",
    "fresh everyday look",
    "bronzed summer look",
    "classic Hollywood glam",
    "evening makeup",
    "subtle contour and highlight",
    "rosy blush focus",
    "glowy highlight look"
]

AGE_GROUPS = [
    "early 20s", "mid 20s", "late 20s",
    "early 30s", "mid 30s", "early 40s", "mid 40s"
]

PERSONALITY_VIBES = [
    "elegant", "playful", "mysterious", "confident", "shy but charming",
    "seductive", "sweet", "bold", "artsy", "classy"
]

FACIAL_EXPRESSIONS = [
    "smiling warmly",
    "smirking playfully",
    "soft gentle smile",
    "wide bright smile",
    "seductive smirk",
    "mischievous grin",
    "subtle closed-mouth smile",
    "pouting lips",
    "biting her lip",
    "resting serious face",
    "thoughtful expression",
    "confident smile",
    "shy smile",
    "cheerful grin",
    "flirty glance with a smirk",
    "dreamy expression",
    "intense stare",
    "playful wink",
    "relaxed and calm expression",
    "mysterious half-smile"
]