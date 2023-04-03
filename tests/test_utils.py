import pytest

from utils import get_data, get_filtered_data, get_data_with_from


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 6


def test_get_data_with_from(test_data):
   assert len(get_data_with_from(test_data)) == 5


