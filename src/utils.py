from typing import Optional

from .enums import OutfitType


def filter_items(
    items_dict: dict,
    outfit_type_enum: OutfitType,
    search_query: str = "",
    *,
    exclude_keys: Optional[set[str]] = None,
) -> list[str]:
    """Filter clothing dict keys by outfit type and optional search query.

    Search fallback chain:
    1. outfit type + search
    2. all items + search (relax outfit type)
    3. outfit type only (ignore search)
    """
    all_keys = list(items_dict.keys())
    if exclude_keys:
        all_keys = [name for name in all_keys if name not in exclude_keys]

    def by_outfit_type(keys: list[str]) -> list[str]:
        return [
            name for name in keys
            if outfit_type_enum in items_dict[name]["types"]
        ]

    def by_search(keys: list[str], query: str) -> list[str]:
        q = query.strip().lower()
        if not q:
            return keys
        return [name for name in keys if q in name.lower()]

    type_filtered = by_outfit_type(all_keys)
    if not type_filtered:
        type_filtered = all_keys

    if not search_query or not search_query.strip():
        return type_filtered

    searched = by_search(type_filtered, search_query)
    if searched:
        return searched

    all_searched = by_search(all_keys, search_query)
    if all_searched:
        return all_searched

    return type_filtered


def clean_generated_text(text: str) -> str:
    """
    Clean up generated text by removing extra commas, whitespace, and formatting issues.
    
    Args:
        text: Raw generated text that may contain formatting issues
        
    Returns:
        Cleaned text with proper formatting
        
    Example:
        >>> clean_generated_text("cream ballet tutu outfit,  , wine red mary jane flats, ")
        "cream ballet tutu outfit, wine red mary jane flats"
    """
    # Split by comma to process each part
    parts = text.split(',')
    
    # Strip whitespace from each part and filter out empty strings
    cleaned_parts = [part.strip() for part in parts if part.strip()]
    
    # Rejoin with proper comma spacing
    cleaned_text = ', '.join(cleaned_parts)
    
    return cleaned_text
