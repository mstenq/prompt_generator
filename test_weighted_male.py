#!/usr/bin/env python3
"""Test script to verify weighted character generation for both male and female"""

import sys
sys.path.insert(0, '/home/masonsten/comfy/ComfyUI/custom_nodes/outfit_generator/src')

from CharacterGenerator import CharacterGenerator

# Generate 15 male characters
print("=" * 80)
print("MALE CHARACTERS - Testing weighted hair style/color generation")
print("=" * 80)

for i in range(15):
    character = CharacterGenerator.generate_simple_character(sex="male")
    print(f"{i+1}. {character}")

print("\n" + "=" * 80)
print("FEMALE CHARACTERS - Testing weighted hair style/color generation")
print("=" * 80)

# Generate 15 female characters
for i in range(15):
    character = CharacterGenerator.generate_simple_character(sex="female")
    print(f"{i+1}. {character}")

print("\n" + "=" * 80)
print("\nExpected Results:")
print("MALE: More short hair (buzz cut, crew cut, fade) than long/unusual styles")
print("FEMALE: More long/medium hair than short/extreme styles")
print("BOTH: Common colors (dark brown, black, light brown) > rare colors (red, highlights)")
print("=" * 80)
