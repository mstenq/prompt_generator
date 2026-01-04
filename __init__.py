from .src.main import NODE_CLASS_MAPPINGS as OUTFIT_NODE_CLASS_MAPPINGS

# Combine node class mappings
NODE_CLASS_MAPPINGS = {**OUTFIT_NODE_CLASS_MAPPINGS}

# Register js directory for JavaScript extensions
WEB_DIRECTORY = "./js"

__all__ = ['NODE_CLASS_MAPPINGS', 'WEB_DIRECTORY']
