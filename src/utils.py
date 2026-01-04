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
