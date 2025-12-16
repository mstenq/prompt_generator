
import random
from .colors import BLACKS, WHITES, GRAYS, BLUES, REDS, PINKS, GREENS, BROWNS, PURPLES, YELLOWS, ORANGES, NEONS, METALLICS, PASTELS, EARTH_TONES, JEWEL_TONES, PATTERNS, PRINTS, SPECIAL, TEXTURES

class ColorGenerator:

    @staticmethod
    def generate_random_color():
        return random.choice(BLACKS + WHITES + GRAYS + BLUES + REDS + PINKS + GREENS + BROWNS + PURPLES + YELLOWS + ORANGES + NEONS + METALLICS + PASTELS + EARTH_TONES + JEWEL_TONES)
    
    @staticmethod
    def generate_color(color_categories=None):
        """
        Generate a random color from the specified category/categories.
        
        Args:
            color_categories: String or list of strings representing color categories.
                            If None, returns a random color from all categories.
                            If a single string, returns a color from that category.
                            If a list, returns a color from the combined categories.
        
        Returns:
            A random color string from the specified categories.
        """
        # Color category mapping
        color_map = {
            "blacks": BLACKS,
            "whites": WHITES,
            "grays": GRAYS,
            "blues": BLUES,
            "reds": REDS,
            "pinks": PINKS,
            "greens": GREENS,
            "browns": BROWNS,
            "purples": PURPLES,
            "yellows": YELLOWS,
            "oranges": ORANGES,
            "neons": NEONS,
            "metallics": METALLICS,
            "pastels": PASTELS,
            "earth_tones": EARTH_TONES,
            "jewel_tones": JEWEL_TONES
        }
        
        # If no categories specified, use all colors
        if color_categories is None:
            return ColorGenerator.generate_random_color()
        
        # If single string category, convert to list
        if isinstance(color_categories, str):
            color_categories = [color_categories]
        
        # Combine all requested color categories
        combined_colors = []
        for category in color_categories:
            category = category.strip().lower()  # Normalize category name
            if category in color_map:
                combined_colors.extend(color_map[category])
        
        # If no valid categories found, fallback to random color
        if not combined_colors:
            return ColorGenerator.generate_random_color()
        
        return random.choice(combined_colors)

    @staticmethod
    def generate_pattern():
        return random.choice(PATTERNS)

    @staticmethod
    def generate_print():
        return random.choice(PRINTS)

    @staticmethod
    def generate_special():
        return random.choice(SPECIAL)

    @staticmethod
    def generate_texture():
        return random.choice(TEXTURES)
