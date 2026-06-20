"""Tests for outfit search filtering."""

from src.enums import OutfitType
from src.utils import filter_items


FIXTURE_ITEMS = {
    "white t-shirt": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "colors": ["white"],
    },
    "black t-shirt": {
        "types": [OutfitType.CASUAL_CHIC],
        "colors": ["black"],
    },
    "evening gown": {
        "types": [OutfitType.EVENING_FORMAL],
        "colors": ["red"],
    },
    "jeans": {
        "types": [OutfitType.CASUAL_CHIC, OutfitType.STREETWEAR],
        "colors": ["blue"],
    },
}


def test_filter_items_no_search_returns_type_matches():
    result = filter_items(FIXTURE_ITEMS, OutfitType.CASUAL_CHIC, "")
    assert set(result) == {"white t-shirt", "black t-shirt", "jeans"}


def test_filter_items_no_search_falls_back_to_all_when_type_empty():
    result = filter_items(FIXTURE_ITEMS, OutfitType.ANIME, "")
    assert set(result) == set(FIXTURE_ITEMS.keys())


def test_filter_items_search_with_type_match():
    result = filter_items(FIXTURE_ITEMS, OutfitType.CASUAL_CHIC, "t-shirt")
    assert set(result) == {"white t-shirt", "black t-shirt"}


def test_filter_items_search_relaxes_type_when_no_type_match():
    result = filter_items(FIXTURE_ITEMS, OutfitType.EVENING_FORMAL, "t-shirt")
    assert set(result) == {"white t-shirt", "black t-shirt"}


def test_filter_items_search_ignores_query_when_no_matches():
    result = filter_items(FIXTURE_ITEMS, OutfitType.CASUAL_CHIC, "nonexistent")
    assert set(result) == {"white t-shirt", "black t-shirt", "jeans"}


def test_filter_items_exclude_keys():
    result = filter_items(
        FIXTURE_ITEMS,
        OutfitType.CASUAL_CHIC,
        "",
        exclude_keys={"jeans"},
    )
    assert set(result) == {"white t-shirt", "black t-shirt"}
