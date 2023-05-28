from collections import defaultdict

def create_inverted_index(sentences):
    inverted_index = defaultdict(list)
    for doc_id, sentence in enumerate(sentences):
        for field, value in sentence.items():
            if isinstance(value, str):  
                words = str(value).split()
                for word in words:
                    inverted_index[word].append(sentence)
    return inverted_index

def search_sentences(inverted_index, search_term):
    if search_term in inverted_index:
        results = inverted_index[search_term]
    else:
        results = []
    return results

sentences = [
    {"id": 1, "name": "erosha", "address": "kathmandu", "company": "abcd"},
    {"id": 2, "name": "ram", "address": "lalitpur", "position": "efgh"},
    {"id": 3, "name": "sita", "address": "chitwan", "position": "ijkl"},
    {"id": 4, "name": "hari", "address": "bhaktapur", "position": "mnop"},

]

inverted_index = create_inverted_index(sentences)

def perform_search(search_term):
    results = search_sentences(inverted_index, search_term)
    print("search term:", search_term)
    if len(results) > 0:
        for sentence in results:
            print(sentence)
    else:
        print("no word found.")

search_terms = ["erosha", "mnop", "chitwan"]
for term in search_terms:
    perform_search(term)
