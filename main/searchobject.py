from collections import defaultdict

def create_inverted_index(sentences):
    inverted_index = defaultdict(list)
    for doc_id, sentence in enumerate(sentences):
        for field, value in sentence.items():
            if isinstance(value, str):
                words = str(value).split()
                for word in words:
                    inverted_index[word].append((sentence, field))
    return inverted_index

def search_sentences(inverted_index, search_term, field=None):
    results = []
    for sentence, sentence_field in inverted_index[search_term]:
        if field is None or field == sentence_field:
            results.append(sentence.get(sentence_field))
    return results

sentences = [
    {"id": 1, "name": "erosha", "address": "kathmandu", "company": "abcd"},
    {"id": 2, "name": "ram", "address": "lalitpur", "position": "efgh"},
    {"id": 3, "name": "sita", "address": "chitwan", "position": "ijkl"},
    {"id": 4, "name": "hari", "address": "bhaktapur", "position": "mnop"},
]

inverted_index = create_inverted_index(sentences)

def perform_search(search_term):
    field = input("enter the field to retrieve data from: ")
    field_values = []
    for sentence in sentences:
        if field in sentence:
            field_values.append(sentence[field])
    print("field:", field)
    if len(field_values) > 0:
        for value in field_values:
            print(value)
    else:
        print("no data found for the field.")

search_terms = []
perform_search(search_terms)
