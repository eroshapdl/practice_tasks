def search_sentences(sentences, search):
    results = []
    for sentence in sentences:
        if search in sentence:
            results.append(sentence)
    return results

sentences = [
    "iam eru",
    "eru paudel",
    "hellooooooooooo",
    "sup eru",
    "ttyl ok bye",
    "aajha jado cha",
]

search = "eru"
results = search_sentences(sentences, search)

print(search)
for sentence in results:
    print(sentence)