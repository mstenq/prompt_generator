import random
from .enums import LocationType
from .scenes import SCENES

class SceneGenerator:    
    def generate_scene(self, outfit_type_enum, location_filter=None):
        """Generate a scene description compatible with the given outfit type and location"""
        # Filter scenes that match the selected outfit type and location
        compatible_scenes = []
        
        # Convert location string to LocationType enum if specified
        location_enum = None
        if location_filter and location_filter != "anything":
            for loc_type in LocationType:
                if loc_type.value == location_filter:
                    location_enum = loc_type
                    break
        
        # First pass: try to find scenes that match both outfit type and location
        for scene_name, data in SCENES.items():
            # Check if scene matches outfit type
            if outfit_type_enum in data["types"]:
                # If location filter is specified, also check location compatibility
                if location_enum is None:
                    compatible_scenes.append(scene_name)
                else:
                    # Check if scene's location matches the filter
                    if location_enum in data["location"]:
                        compatible_scenes.append(scene_name)
        
        # If no matches found and location is specified (indoor/outdoor), prioritize location over outfit type
        if not compatible_scenes and location_enum is not None:
            # Second pass: find all scenes that match the location, ignoring outfit type
            for scene_name, data in SCENES.items():
                if location_enum in data["location"]:
                    compatible_scenes.append(scene_name)
        
        # Final fallback to all scenes if still no matches found (shouldn't happen with proper data)
        if not compatible_scenes:
            compatible_scenes = list(SCENES.keys())
        
        # Select a random compatible scene
        selected_scene = random.choice(compatible_scenes)
        return selected_scene