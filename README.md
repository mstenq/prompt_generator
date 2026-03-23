# ComfyUI Outfit Generator

A ComfyUI custom node that generates randomized, detailed prompt descriptions for people, outfits, poses, scenes, and locations. Perfect for creating varied AI-generated character images with consistent prompt structures.

## Overview

ComfyUI Outfit Generator provides a powerful template-based prompt generation system that can create comprehensive character descriptions including:

-   **Character Attributes**: Nationality, body type, hair style/color, eye color/shape, skin tone, facial features, age, personality vibes, expressions
-   **Outfits**: 30+ outfit style types (casual, formal, gothic, cyberpunk, beach wear, lingerie, etc.) with gender-specific clothing options
-   **Poses**: Sitting, standing, walking, running, jumping, dancing, leaning, crouching, kneeling, lying, and more
-   **Scenes/Locations**: Context-aware scene generation (bedroom, beach, city, office, mall, etc.)
-   **Colors**: Randomized color selection with category filters
-   **Image Dimensions**: Automatic width/height calculation based on aspect ratio and megapixels

## Features

-   Template-based prompt system with placeholder tags
-   Gender-specific character and outfit generation (male/female)
-   30+ outfit style types with location-aware scene matching
-   Weighted randomization for realistic attribute distributions
-   Scene-first or outfit-first generation logic
-   Automatic image dimension calculation
-   Optional seed control for reproducible results
-   Force barefoot option for specific styles

## Installation

This node is **not available via ComfyUI Manager** and must be installed manually.

### Manual Installation

1. Navigate to your ComfyUI custom nodes directory:

    ```bash
    cd ComfyUI/custom_nodes/
    ```

2. Clone this repository:

    ```bash
    git clone https://github.com/mstenq/prompt_generator.git
    ```

3. Restart ComfyUI

No additional dependencies are required - the module uses only Python standard library.

## Usage

### Basic Setup

1. In ComfyUI, add the **Prompt Generator** node (found under the `prompt_generator` category)
2. The node has the following inputs:

    - **prompt**: Template string with placeholder tags (default: `"A photo of <<woman>> wearing <<femaleOutfit>> in <<scene>>"`)
    - **outfit_type**: Select from 30+ styles or "random"
    - **location**: Filter scenes by location type or "anything"
    - **ratio**: Image aspect ratio (1:1, 2:3, 3:4, 4:7, 3:2, 4:3, 7:4)
    - **megapixels**: Image resolution (0.1 to 10.0 MP)
    - **seed** (optional): Random seed (-1 for random)
    - **force_barefoot** (optional): Override footwear generation
    - **var_1** to **var_6** (optional): `PROMPT_VAR` inputs for reusable prompt fragments from other generator nodes

3. The node outputs:
    - **prompt**: Generated text prompt string
    - **width**: Calculated image width
    - **height**: Calculated image height

### Template Tags

Use these placeholder tags in your prompt template. Each tag is replaced with randomly generated content:

#### Character Tags

-   `<<female>>` or `<<woman>>` - Full female character description
-   `<<male>>` or `<<man>>` - Full male character description
-   `<<simpleFemale>>` or `<<simpleWoman>>` - Simplified female description
-   `<<simpleMale>>` or `<<simpleMan>>` - Simplified male description

#### Outfit Tags

-   `<<femaleOutfit>>` - Female outfit matching selected style
-   `<<maleOutfit>>` - Male outfit matching selected style
-   `<<femaleTop>>` - Female top matching selected style
-   `<<maleTop>>` - Male top matching selected style
-   `<<femaleBottom>>` - Female bottom matching selected style
-   `<<maleBottom>>` - Male bottom matching selected style
-   `<<femaleShoe>>` - Female footwear matching selected style
-   `<<maleShoe>>` - Male footwear matching selected style

#### Variable Tags

-   `<<var1>>` or `<<var_1>>` - Inject value from the `var_1` input
-   `<<var2>>` or `<<var_2>>` - Inject value from the `var_2` input
-   `<<var3>>` or `<<var_3>>` - Inject value from the `var_3` input
-   `<<var4>>` or `<<var_4>>` - Inject value from the `var_4` input
-   `<<var5>>` or `<<var_5>>` - Inject value from the `var_5` input
-   `<<var6>>` or `<<var_6>>` - Inject value from the `var_6` input

#### Pose Tags

-   `<<anyPose>>` - Random pose from all categories
-   `<<sitting>>` or `<<sittingOnGround>>` - Sitting on ground poses
-   `<<sittingOnA>>` - Sitting on furniture poses
-   `<<standing>>` - Standing poses
-   `<<walking>>` - Walking poses
-   `<<running>>` - Running poses
-   `<<jumping>>` - Jumping poses
-   `<<dancing>>` - Dancing poses
-   `<<posing>>` - Model/photo poses
-   `<<leaning>>` - Leaning poses
-   `<<crouching>>` - Crouching poses
-   `<<kneeling>>` - Kneeling poses
-   `<<onAllFours>>` - On all fours poses
-   `<<lying>>` or `<<laying>>` - Lying down poses

#### Scene/Location Tags

-   `<<scene>>` or `<<location>>` - Scene description matching outfit and location filter

#### Color Tags

-   `<<color>>` - Random color from all categories
-   `<<color:warm>>` - Random warm color
-   `<<color:cool>>` - Random cool color
-   `<<color:neutral>>` - Random neutral color
-   `<<color:earth>>` - Random earth tone
-   `<<color:jewel>>` - Random jewel tone
-   `<<color:pastel>>` - Random pastel color
-   `<<color:neon>>` - Random neon color
-   `<<color:metallic>>` - Random metallic color
-   Mix categories: `<<color:warm,pastel>>` - Random color from both categories

### Examples

#### Example 1: Basic Portrait

```
Template: "A photo of <<woman>> wearing <<femaleOutfit>>"
Outfit Type: "casual chic"
Location: "anything"

Output: "A photo of Brazilian woman, athletic, with long wavy black hair, amber eyes, almond-shaped eyes, olive skin tone, high cheekbones, full lips, small nose, subtle makeup, mid-20s, confident vibe, smiling expression wearing white blouse, blue jeans, black sneakers, silver necklace"
```

#### Example 2: Scene-Specific

```
Template: "<<man>> <<standing>> in <<scene>>, professional photography"
Outfit Type: "business wear"
Location: "office"

Output: "Japanese man, slim build, short straight brown hair, brown eyes, monolid eyes, fair skin tone, clean-shaven, thin lips, straight nose, no makeup, early 30s, professional vibe, serious expression standing confidently in modern corporate office with glass walls, professional photography"
```

#### Example 3: Complex Multi-Character

```
Template: "<<woman>> wearing <<femaleOutfit>> and <<man>> wearing <<maleOutfit>> <<dancing>> together in <<scene>>"
Outfit Type: "evening/formal wear"
Location: "indoors"

Output: "French woman, hourglass figure, shoulder-length curly blonde hair, blue eyes, wide eyes, porcelain skin tone, defined cheekbones, full lips, button nose, elegant makeup, late 20s, elegant vibe, smiling expression wearing red evening gown, black high heels, diamond earrings and Italian man, athletic build, short wavy dark brown hair, green eyes, hooded eyes, olive skin tone, strong jawline, medium lips, roman nose, no makeup, early 30s, confident vibe, neutral expression wearing black tuxedo, black dress shoes, silver watch dancing closely together in elegant ballroom with crystal chandeliers"
```

#### Example 4: Creative Fashion

```
Template: "Fashion photograph of <<woman>> in <<femaleOutfit>>, <<posing>>, <<scene>>, dramatic lighting, high fashion"
Outfit Type: "avant-garde"
Location: "city"

Output: "Fashion photograph of Korean woman, petite, long straight platinum blonde hair, hazel eyes, almond-shaped eyes, fair skin tone, sharp cheekbones, thin lips, small nose, artistic makeup, mid-20s, mysterious vibe, intense expression in geometric structured black leather ensemble with asymmetric cuts, platform boots, architectural headpiece, posing with hand on hip in urban alleyway with graffiti walls, dramatic lighting, high fashion"
```

#### Example 5: Beach Scene

```
Template: "<<simpleWoman>> wearing <<femaleOutfit>> <<lying>> on <<scene>>, sunset lighting"
Outfit Type: "beach wear"
Location: "beach"
Force Barefoot: True

Output: "Athletic blonde woman with blue eyes lying on her back on sandy beach with palm trees, barefoot with toenails painted with coral, wearing turquoise bikini, white sun hat, sunset lighting"
```

#### Example 6: Reusing Generator Outputs

```
Template: "Studio photo of <<var1>> wearing <<var2>>, <<standing>>, seamless backdrop"
var_1: output from Simple Female Generator
var_2: output from Outfit Generator
Outfit Type: "random"
Location: "anything"

Output: "Studio photo of petite brunette woman with green eyes wearing beige cardigan, pleated skirt, brown ankle boots, standing with one hand on hip, seamless backdrop"
```

### Outfit Style Types

Available outfit types (select from dropdown):

-   random, anime, athleisure, avant-garde, beach wear, bohemian, business wear, casual chic, club/party wear, cottagecore, cowboy, cyberpunk, ethereal, evening/formal wear, fantasy, festival wear, gothic, grunge, kawaii, lingerie, lolita, military, minimalist, normcore, pin-up, preppy, punk, retro, rockabilly, romantic, steampunk, streetwear, vintage

### Location Types

Available location filters (select from dropdown):

-   anything, bathroom, beach, bedroom, city, indoors, kitchen, living room, mall, office, outdoors, store

### Tips

1. **Scene-First Logic**: When using `outfit_type: "random"` with a specific location, the generator picks a scene first, then selects a compatible outfit type.
2. **Multiple Tags**: Use the same tag multiple times to generate different variations, such as two different characters in one prompt.
3. **Seed Control**: Set a specific seed value for reproducible prompts and prompt variations.
4. **Image Dimensions**: The node automatically calculates dimensions from aspect ratio and megapixels. Connect `width` and `height` to your Empty Latent Image node.
5. **Composable Fragments**: Use `<<femaleTop>>`, `<<maleBottom>>`, or shoe tags when you want to build outfits manually instead of inserting a complete outfit.
6. **Generator Chaining**: Connect outputs from `Female Generator`, `Male Generator`, `Outfit Generator`, `Top Generator`, `Bottoms Generator`, `Shoe Generator`, or `Scene Generator` into `var_1` through `var_6`, then reference them with `<<var1>>` through `<<var6>>`.
7. **Color Consistency**: Use color category filters for cohesive palettes.

## Technical Details

-   **Language**: Python (no external dependencies)
-   **Node Type**: Custom ComfyUI node with string and integer outputs
-   **Category**: prompt_generator
-   **Randomization**: Uses Python's `random` module with optional seed control
-   **Dimensions**: Calculated to nearest multiple of 8 (standard for AI image generation)

## Development

The project structure:

-   `src/PromptGenerator.py` - Main node class and template substitution logic
-   `src/CharacterGenerator.py` - Character attribute generation
-   `src/OutfitGenerator.py` - Outfit generation with gender/style matching
-   `src/SceneGenerator.py` - Scene/location generation
-   `src/PoseGenerator.py` - Pose description generation
-   `src/ColorGenerator.py` - Color generation with category filters
-   `src/ShoeGenerator.py` - Footwear generation with optional barefoot handling
-   `src/enums.py` - Outfit and location type definitions
-   `src/male/` - Male-specific attributes and clothing
-   `src/female/` - Female-specific attributes and clothing

## Contributing

Contributions welcome! Feel free to:

-   Add new outfit styles or clothing items
-   Expand character attributes
-   Add more pose variations
-   Improve scene descriptions
-   Report bugs or suggest features

## License

[GNU General Public License v3](LICENSE)
