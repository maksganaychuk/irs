import string
import inverted_index

def read(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def modify_document(text):
    words = text.split()

    array = []

    modified = ''

    for term in words:
        modified = term.strip(string.punctuation)
        
        modified = modified.lower()
        if len(modified) > 0:
            array.append(modified)
    return array

def get_text_title(text):
    return text.partition('\n')[0]

def create_index(file_names, index, title):
    for file in file_names:
        text = read(file) 

        title[file] = get_text_title(text)

        terms = modify_document(text)

        inverted_index.append_entry(index, terms, file)

def print_index(index):
    inverted_index.print_dictionary(index)