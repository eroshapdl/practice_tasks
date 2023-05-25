from collections import defaultdict

def count_characters(text):
    char_count = defaultdict(int)
    for char in text:
        char_count[char] += 1
    return char_count

def find_character_indices(text):
    char_indices = defaultdict(list) 
    for i, char in enumerate(text):
        char_indices[char].append(i)
    return char_indices

