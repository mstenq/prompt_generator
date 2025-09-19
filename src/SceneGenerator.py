import random
from .enums import LocationType
from .scenes import SCENES

class SceneGenerator:    
    
    @staticmethod
    def generate_scene(outfit_type_enum, location_filter=None):
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