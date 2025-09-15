from .OutfitGenerator import NODE_CLASS_MAPPINGS as OUTFIT_NODE_CLASS_MAPPINGS
import os

custom_node_dir = os.path.dirname(os.path.realpath(__file__))

# Combine node class mappings
NODE_CLASS_MAPPINGS = {**OUTFIT_NODE_CLASS_MAPPINGS}

__all__ = ['NODE_CLASS_MAPPINGS']
