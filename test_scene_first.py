#!/usr/bin/env python3
"""
Test script to verify scene-first outfit generation logic.
Tests that when outfit_type is "random" and location is set (e.g., "office"),
the generator will first select an appropriate scene, then choose an outfit type
that fits that scene (e.g., BUSINESS_WEAR for office locations).
"""

import sys
import random
from src.PromptGenerator import PromptGenerator
from src.enums import LocationType

def test_scene_first_generation():
    """Test that office location generates business-appropriate outfits"""
    generator = PromptGenerator()
    
    print("Testing scene-first generation with office location...")
    print("=" * 70)
    
    # Test multiple times to see the variety
    for i in range(5):
        print(f"\nTest {i+1}:")
        
        # Set seed for reproducibility of this test
        seed = random.randint(1, 1000000)
        
        # Generate with office location and random outfit type
        result = generator.generate_prompt(
            prompt="A photo of <<woman>> wearing <<femaleOutfit>> in <<scene>>",
            outfit_type="random",
            location="office",  # This should trigger scene-first logic
            ratio="1:1 square",
            megapixels=1.0,
            seed=seed,
            force_barefoot=False
        )
        
        final_prompt, width, height = result
        print(f"Seed: {seed}")
        print(f"Generated prompt: {final_prompt}")
        print(f"Dimensions: {width}x{height}")
    
    print("\n" + "=" * 70)
    print("Testing with 'anything' location (no scene-first logic)...")
    print("=" * 70)
    
    # Test with "anything" location - should NOT trigger scene-first logic
    for i in range(3):
        print(f"\nTest {i+1}:")
        
        seed = random.randint(1, 1000000)
        
        result = generator.generate_prompt(
            prompt="A photo of <<woman>> wearing <<femaleOutfit>> in <<scene>>",
            outfit_type="random",
            location="anything",  # This should NOT trigger scene-first logic
            ratio="1:1 square",
            megapixels=1.0,
            seed=seed,
            force_barefoot=False
        )
        
        final_prompt, width, height = result
        print(f"Seed: {seed}")
        print(f"Generated prompt: {final_prompt}")
    
    print("\n" + "=" * 70)
    print("Testing with specific outfit type (no scene-first logic)...")
    print("=" * 70)
    
    # Test with specific outfit type - should NOT trigger scene-first logic
    for i in range(3):
        print(f"\nTest {i+1}:")
        
        seed = random.randint(1, 1000000)
        
        result = generator.generate_prompt(
            prompt="A photo of <<woman>> wearing <<femaleOutfit>> in <<scene>>",
            outfit_type="casual chic",  # Specific type, not random
            location="office",
            ratio="1:1 square",
            megapixels=1.0,
            seed=seed,
            force_barefoot=False
        )
        
        final_prompt, width, height = result
        print(f"Seed: {seed}")
        print(f"Generated prompt: {final_prompt}")

if __name__ == "__main__":
    test_scene_first_generation()
