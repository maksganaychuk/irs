import json  
  
def search(index, query):
    if query in index:
        return index[query]
    return []

def append_entry_key(dict, keyword, document):
    if keyword not in dict:
        dict[keyword] = [document]
    elif keyword in dict:
        if document not in dict[keyword]:
            dict[keyword].append(document)
      
def append_entry(dict, keys, document):
    for key in keys:
        append_entry_key(dict, key, document)

def print_dictionary(dict):
    print(json.dumps(dict, sort_keys = False, indent = 2))