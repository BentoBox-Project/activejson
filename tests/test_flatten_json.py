import pytest

from activejson import flatten_json


@pytest.fixture
def pets():
    return {
        "cat": {"grass": "feline", "mud": "you never know", "horse": "my joke"},
        "dolphin": [
            {"tiger": [{"bird": "blue jay"}, {"fish": "dolphin"}]},
            {"cat2": "feline"},
            {"dog2": "canine"},
        ],
        "dog": "canine",
    }


@pytest.fixture
def pets_result():
    return {
        "cat_grass": "feline",
        "cat_horse": "my joke",
        "cat_mud": "you never know",
        "dog": "canine",
        "dolphin_0_tiger_0_bird": "blue jay",
        "dolphin_0_tiger_1_fish": "dolphin",
        "dolphin_1_cat2": "feline",
        "dolphin_2_dog2": "canine",
    }


def test_flatten_json(pets, pets_result):
    assert pets_result == flatten_json(pets)
