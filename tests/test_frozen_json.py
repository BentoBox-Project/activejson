import pytest

from activejson import FrozenJSON
from .example_dicts import oscon_feed, dict_with_keyword, nested_dict


@pytest.fixture
def frozen_oscon_feed():
    return FrozenJSON(oscon_feed)


@pytest.fixture
def frozen_dict_with_keywords():
    return FrozenJSON(dict_with_keyword)


@pytest.fixture
def frozen_nested_data():
    return FrozenJSON(nested_dict)


def test_has_keys(frozen_oscon_feed):
    frozen_keys = frozen_oscon_feed.Schedule.keys()
    assert list(frozen_keys) == ['conferences', 'events', 'speakers', 'venues']


def test_keyword_handling(frozen_dict_with_keywords):
    assert frozen_dict_with_keywords.class_ is not None


def test_raises_exception(frozen_oscon_feed):
    with pytest.raises(AttributeError):
        value = frozen_oscon_feed.city


def test_contains_funcionality(frozen_oscon_feed):
    assert 'Schedule' in frozen_oscon_feed


def test_getitem_getattr(frozen_oscon_feed):
    assert frozen_oscon_feed.Schedule.keys() == frozen_oscon_feed['Schedule'].keys()


def test_remove_nested_data(frozen_nested_data):
    frozen_nested_data.get('main_data').pop('simple_key')
    assert 'simple_key' not in frozen_nested_data.get('main_data')
