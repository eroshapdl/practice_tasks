def search_sentences(sentences, search):
    global has_searched
    if not has_searched:
        results = []
        for sentence in sentences:
            if search in sentence:
                results.append(sentence)
                break
        has_searched = True
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
has_searched = False  
results = search_sentences(sentences, search)

print(search)
for sentence in results:
    print(sentence)
