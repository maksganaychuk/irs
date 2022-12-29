import sys
import os
import format
import inverted_index

folder_name = False

path = ''
query = ''

file_names = []
query_res = []

index = {}
title = {}

search_mode = False

if len(sys.argv) > 1 and sys.argv[1]:
    folder_name = sys.argv[1]
if len(sys.argv) > 2 and sys.argv[2]:
    if sys.argv[2] == "-s":
        search_mode = True

if folder_name:
    path = "./" + folder_name

    for file in os.listdir(path):
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"

            file_names.append(file_path)
    format.create_index(file_names, index, title)

if search_mode:
    query = input("Query: ")
    if query != "\n":
        query_res = inverted_index.search(index, query)
        if len(query_res) > 0:
            for doc in query_res:
                print(f'Found {title[doc]} in file {doc}')
        else:
            print("Failed to find anything")