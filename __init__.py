from .src.PromptGenerator import NODE_CLASS_MAPPINGS as OUTFIT_NODE_CLASS_MAPPINGS

# Combine node class mappings
NODE_CLASS_MAPPINGS = {**OUTFIT_NODE_CLASS_MAPPINGS}

__all__ = ['NODE_CLASS_MAPPINGS']
