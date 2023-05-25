from main.count import count_characters




def test_count_characters():

    assert count_characters("a") == {"a": 1}

    assert count_characters("helloooo") == {"h": 1, "e": 1, "l": 2, "o": 1}
