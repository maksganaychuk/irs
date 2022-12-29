import os

def format():
    cwd = os.getcwd()

    newWords = {}

    os.chdir(cwd + '/mock')

    fileList = os.listdir(os.getcwd())
    fileList.sort()
    for file in fileList:
        with open(file, 'r') as f:
            words = f.read().lower().split()
            for word in words:
                fileName = f.name
                if word[-1] in [',', '!', '?', '.']:
                    word = word[:-1]
                if word not in newWords.keys():
                    newWords[word] = [fileName]
                else:
                    if file not in newWords[word]:
                        newWords[word] += [fileName]
    os.chdir(cwd)
    return newWords, cwd

def write(words, cwd):
    os.chdir(cwd)
    
    with open('inverted_index.txt', 'w') as indexFile:
        for word, files in words.items():
            indexFile.write(word + " ")
            for file in files:
                indexFile.write(file[:file.find(".txt") + 4] + " ")
            indexFile.write('\n')

write(*format()) 