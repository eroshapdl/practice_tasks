from collections import defaultdict

def create_inverted_index(sentences):
    inverted_index = defaultdict(list)
    for doc_id, sentence in enumerate(sentences):
        for field, value in sentence.items():
            words = str(value).split()
            for word in words:
                inverted_index[word].append(doc_id)
    return inverted_index

def search_sentences(inverted_index, search_term, sentences):
    results = []
    for doc_id, sentence in enumerate(sentences):
        for value in sentence.values():
            if search_term in str(value):
                results.append(sentence)
                break
    return results

sentences = [
    {"id": 1, "text": "iam erosha paudel"},
    {"id": 2, "text": "hello how are you?"},
    {"id": 3, "text": "my name is erosha"},
    {"id": 4, "text": "aajha jado cha"},
    {"id": 5, "text": "kathmandu is jado"},
]

inverted_index = create_inverted_index(sentences)

def search(search_term):
    results = search_sentences(inverted_index, search_term, sentences)
    return results

search("erosha")
search("jado")
search("kathmandu")
