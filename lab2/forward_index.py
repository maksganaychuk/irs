import json

def search(index, query):
    pages = []
    for key in index.keys():
        if query in index[key]:
            pages.append(key)
    return pages

def append_entry(dict, doc, keys):
    if doc not in dict:
        dict[doc] = keys
    elif doc in dict:
        dict[doc] += keys

        dict[doc] = list(set(dict[doc]))
  
def print_dictionary(dict):
    print(json.dumps(dict, sort_keys=False, indent=2))