def create_inverted_index(sentences):
    inverted_index = {}
    for doc_id, sentence in enumerate(sentences):
        words = sentence.split()
        for word in words:
            if word not in inverted_index:
                inverted_index[word] = []
            inverted_index[word].append(doc_id)
    return inverted_index

def search_sentences(inverted_index, search_term, sentences):
    if search_term in inverted_index:
        results = [sentences[doc_id] for doc_id in inverted_index[search_term]]
    else:
        results = []
    return results

sentences = [
    "iam eru",
    "eru paudel",
    "hello",
    "sup eru",
    "ttyl ok bye",
    "aajha jado cha",
]

inverted_index = create_inverted_index(sentences)

def perform_search(search_term):
    results = search_sentences(inverted_index, search_term, sentences)
    print("search term:", search_term)
    if len(results) > 0:
        for sentence in results:
            print(sentence)
    else:
        print("no word found.")
        
search_terms = ["eru", "hello", "sup"]
for term in search_terms:
    perform_search(term)
