import random
from .enums import LOCATION_TYPE_NAMES, LocationType
from .scenes import SCENES

class SceneGenerator:  
    def __init__(self):
     pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "location": (LOCATION_TYPE_NAMES, {}),
            },
            "optional": {
                "seed": ("INT", {"default": -1, "min": -1, "max": 2147483647}),
            },
        }

    RETURN_TYPES = ("PROMPT_VAR",)
    RETURN_NAMES = ("scene",)

    FUNCTION = "generate_scene_node"

    CATEGORY = "prompt_generator"
    OUTPUT_NODE = True  
    
    def generate_scene_node(self, location, seed=-1):
        """Node function to generate scene with optional seed for randomness"""
        if seed != -1:
            random.seed(seed)
            

        scene_description = self.generate_scene(location)
        return {
            "ui": {"text": (scene_description,)},
            "result": (scene_description,)
        }
    
    @staticmethod
    def generate_scene(location_filter=None):
        """Generate a scene description based on location filter (outfit type filtering removed)"""
        # Filter scenes that match the location filter only
        compatible_scenes = []
        
        # Convert location string to LocationType enum if specified
        location_enum = None
        if location_filter and location_filter != "anything":
            for loc_type in LocationType:
                if loc_type.value == location_filter:
                    location_enum = loc_type
                    break
        
        # Filter scenes based on location only (no outfit type filtering)
        for scene_name, data in SCENES.items():
            # If location filter is specified, check location compatibility
            if location_enum is None:
                # No location filter, all scenes are compatible
                compatible_scenes.append(scene_name)
            else:
                # Check if scene's location matches the filter
                if location_enum in data["location"]:
                    compatible_scenes.append(scene_name)
        
        # Final fallback to all scenes if no matches found (shouldn't happen with proper data)
        if not compatible_scenes:
            compatible_scenes = list(SCENES.keys())
        
        # Select a random compatible scene
        selected_scene = random.choice(compatible_scenes)
        return selected_scene
    
    @staticmethod
    def get_outfit_types_for_scene(scene_name):
        """Get the list of compatible outfit types for a given scene"""
        if scene_name in SCENES:
            return SCENES[scene_name].get("types", [])
        return []