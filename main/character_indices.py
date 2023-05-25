def find_character_indices(text):
    char_indices = {}
    for i, char in enumerate(text):
        if char in char_indices:
            char_indices[char].append(i)
        else:
            char_indices[char] = [i]
    return char_indices



input_text = input("Enter some text: ")
char_indices = find_character_indices(input_text)


print("Character indices:")
for char, indices in char_indices.items():
    print(f"{char}: {indices}")
