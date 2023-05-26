from collections import defaultdict

def create_inverted_index(sentences, field):
    inverted_index = defaultdict(list)
    for doc_id, sentence in enumerate(sentences):
        words = sentence.get(field, "").split()
        for word in words:
            inverted_index[word].append(doc_id)
    return inverted_index

def search_sentences(inverted_index, search_term, sentences):
    if search_term in inverted_index:
        results = [sentences[doc_id] for doc_id in inverted_index[search_term]]
    else:
        results = []
    return results

sentences = [
    {"id": 1, "text": "iam erosha paudel"},
    {"id": 2, "text": "hello how are you?"},
    {"id": 3, "text": "my name is erosha"},
    {"id": 4, "text": "aajha jado cha"},
    {"id": 5, "text": "kathmandu is jado "},
]

field = "text"

inverted_index = create_inverted_index(sentences, field)

def search(search_term):
    results = search_sentences(inverted_index, search_term, sentences)
    print("search term:", search_term)
    if len(results) > 0:
        for sentence in results:
            print(sentence)
    else:
        print("no results found.")


search("erosha")
search("jado")
search("kathmandu")