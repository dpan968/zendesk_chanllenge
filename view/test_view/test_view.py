import pytest
from view import menu_enum


def test_menu():
    assert menu_enum.TYPE_SEARCH_VALUE == 'Enter search value (type \'missing\' for items that do not have this field)\n'
