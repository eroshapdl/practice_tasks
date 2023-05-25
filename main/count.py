def count_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_text = input("Enter some text: ")
result = count_characters(input_text)
print("Character counts:")
for char, count in result.items():
    print(f"{char}: {count}")