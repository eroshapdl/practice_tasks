from main.count import count_characters

def count_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def test_count_characters():

    assert count_characters("a") == {"a": 1}

    assert count_characters("helloooo") == {"h": 1, "e": 1, "l": 2, "o": 1}
