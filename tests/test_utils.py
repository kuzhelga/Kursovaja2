import pytest

from utils import get_data, get_filtered_data, get_five_last_values, get_formated_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 6


def test_get_five_last_values(test_data):
    assert len(get_five_last_values(test_data)) == 5


def test_get_formated_data(test_data):
    assert type(get_formated_data(test_data)) == list
