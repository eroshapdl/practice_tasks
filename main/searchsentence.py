def search_sentences(sentences, search):
    results = []
    found = False

    for sentence in sentences:
        if search in sentence:
            results.append(sentence)
            found = True
            break  

    if found:
        return results
    else:
        return []

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




