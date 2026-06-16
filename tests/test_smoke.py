"""Smoke tests for scene data integrity and basic generation."""

import re

import pytest

from src.enums import LocationType, OutfitType
from src.PromptGenerator import PromptGenerator
from src.SceneGenerator import SceneGenerator
from src.scenes import SCENES

PLACEHOLDER_PATTERN = re.compile(r"<<[^>]+>>")


@pytest.fixture
def seeded_prompt_generator():
    generator = PromptGenerator()
    return generator


def test_scenes_import_and_nonempty():
    assert len(SCENES) > 0


def test_scenes_have_valid_outfit_and_location_types():
    invalid_outfit_refs: list[str] = []
    invalid_location_refs: list[str] = []
    valid_outfit_types = set(OutfitType)
    valid_location_types = set(LocationType)

    for scene_name, data in SCENES.items():
        for outfit_type in data.get("types", []):
            if outfit_type not in valid_outfit_types:
                invalid_outfit_refs.append(f"{scene_name!r}: {outfit_type!r}")

        for location_type in data.get("location", []):
            if location_type not in valid_location_types:
                invalid_location_refs.append(f"{scene_name!r}: {location_type!r}")

    assert not invalid_outfit_refs, "Invalid OutfitType references:\n" + "\n".join(invalid_outfit_refs[:20])
    assert not invalid_location_refs, "Invalid LocationType references:\n" + "\n".join(invalid_location_refs[:20])


@pytest.mark.parametrize(
    "location_filter",
    [
        "anything",
        "indoors",
        "outdoors",
        "beach",
        "living room",
    ],
)
def test_scene_generator_returns_known_scene(location_filter):
    scene = SceneGenerator.generate_scene(location_filter)
    assert scene in SCENES


def test_scene_generator_outfit_types_for_scene():
    scene = SceneGenerator.generate_scene("anything")
    outfit_types = SceneGenerator.get_outfit_types_for_scene(scene)
    assert outfit_types
    assert all(outfit_type in OutfitType for outfit_type in outfit_types)


def test_prompt_generator_substitutes_scene(seeded_prompt_generator):
    result = seeded_prompt_generator.generate_prompt(
        prompt="A photo in <<scene>>",
        outfit_type="casual chic",
        location="indoors",
        ratio="1:1 square",
        megapixels=1.0,
        seed=42,
    )

    prompt = result["result"][0]
    assert prompt
    assert "<<scene>>" not in prompt
    assert not PLACEHOLDER_PATTERN.search(prompt)


def test_prompt_generator_simple_full_prompt(seeded_prompt_generator):
    result = seeded_prompt_generator.generate_prompt(
        prompt="<<woman>> wearing <<femaleOutfit>> in <<scene>>",
        outfit_type="casual chic",
        location="outdoors",
        ratio="2:3 portrait",
        megapixels=1.0,
        seed=123,
    )

    prompt, width, height = result["result"]
    assert prompt
    assert width > 0
    assert height > 0
    assert not PLACEHOLDER_PATTERN.search(prompt)
