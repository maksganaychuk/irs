import os

def format():
    keys = {}

    newWords = {}

    with open('keys.txt', 'r') as KeywordsFile:
        keys = KeywordsFile.read().lower().split()
        
    cwd = os.getcwd()

    os.chdir(cwd + '/mock')

    fileList = os.listdir(os.getcwd())

    fileList.sort()
    for file in fileList:
        with open(file, 'r') as f:
            words = f.read().lower().split()
            newWords[f.name] = []
            for word in words:
                if word[-1] in [',', '!', '?', '.']:
                    word = word[:-1]
                if word in keys and word not in newWords[f.name]:
                    newWords[f.name] += [word]
    os.chdir(cwd)
    return newWords, cwd

def write(words, cwd):
    os.chdir(cwd)

    with open('forward_index.txt', 'w') as indexFile:
        for file, files in words.items():
            indexFile.write(file[:file.find(".txt")] + " ")
            for word in files:
                indexFile.write(word + " ")
            indexFile.write('\n')

write(*format())