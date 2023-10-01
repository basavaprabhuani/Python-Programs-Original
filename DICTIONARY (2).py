import requests
import pandas as pd
from openpyxl.workbook import Workbook

merriam_key = "423ff893-bf47-4f30-823b-1258591f6c96"
words = []
phonetics = []
partofspeeches = []
defenitions = []
synonyms = []
antonyms = []
examples = []

def check():
    word_ask = input("Enter the word to be checked: ")
    if word_ask == "stop":
        panda_data = {
            "Word": words,
            "Part Of Speech": partofspeeches,
            "Defenition": defenitions,
            "Synonyms": synonyms,
            "Antonyms": antonyms,
            "Example Sentence": examples,
            
        }

        real_data = pd.DataFrame(panda_data)
        file_path = "C:/Users/Basavaprabhu Ani/Desktop"
        name = input("What do you want to name the file? ")
        real_data.to_excel(f"{file_path}/{name}.xlsx", sheet_name=name, engine="openpyxl")
    else:
        endpoint = f"https://www.dictionaryapi.com/api/v3/references/ithesaurus/json/{word_ask}?key=423ff893-bf47-4f30-823b-1258591f6c96"

        data = requests.get(endpoint).json()
        global word_ddisplay
        global word_part
        global word_defenition
        global word_synonym_1
        global word_antonym
        global example_sentence

        try:
            word_ddisplay = data[0]["meta"]["id"]
        
        except:
            word_ddisplay = data[0][0][0]["id"]
        word_part = data[0]["fl"]
        try:
            word_defenition = data[0]["def"][0]["sseq"][1][0][1]["dt"][0][1]
        except:
            word_defenition = data[0]["def"][0]["sseq"][0][0][1]["dt"][0][1]
        
        try:
            example_sentence = data[0]["def"][0]["sseq"][1][0][1]["dt"][1][1][0]["t"]
            
        except:
            example_sentence = "No Example Sentence Found"
        
        try:
            word_synonym_1 = data[0]["meta"]["syns"][1][0]["t"]
        except:
            word_synonym_1 = "No Synonym Found"

        try:
            word_antonym = data[0]["meta"]["ants"][0][0]
        except:
            word_antonym = "No antonym Found"

        examples.append(example_sentence)
        words.append(word_ddisplay)
        partofspeeches.append(word_part)
        defenitions.append(word_defenition)
        synonyms.append(word_synonym_1)
        antonyms.append(word_antonym)
        check()

check()
