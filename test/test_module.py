from main.count import count_characters
from main.character_indices import find_character_indices


def test_count_characters():

    assert count_characters("a") == {"a": 1}

    assert count_characters("helloooo") == {"h": 1, "e": 1, "l": 2, "o": 1}


def test_find_character_indices():
    text = "Hello, World!"
    result = find_character_indices(text)
    assert result == {'H': [0], 'e': [1], 'l': [2, 3, 9], 'o': [4, 7], ',': [5], ' ': [6], 'W': [8], 'r': [10], 'd': [11], '!': [12]}

