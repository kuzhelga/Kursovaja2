import pytest

from utils import get_data, get_filtered_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


