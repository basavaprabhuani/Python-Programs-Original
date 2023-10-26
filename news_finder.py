import requests
from bs4 import BeautifulSoup
import time
from colorama import Fore, Back, Style

def fun_facts():
    print("\n\n")
    limit = 2
    API_KEY = "bLJUYzFeXqbz1DiWYpEA4Q==rVAtLgDj6dvp8NNt"
    facts_url = f"https://api.api-ninjas.com/v1/facts?limit={limit}"
    result = requests.get(facts_url, headers={"X-Api-Key": API_KEY})
    result_content = result.json()
    print(Fore.CYAN + "Today's fun facts:")
    if result.status_code == 200:
        for fact in result_content:
            print(Style.RESET_ALL + f"{fact['fact']}")
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n\n")
    
def news():
    url_name = "https://www.ndtv.com/latest"
    page = requests.get(url=url_name)
    soup = BeautifulSoup(page.content, features="html.parser")  # Specify the parser and use page.content
    headings = soup.find_all(class_="newsHdng")
    content = soup.find_all(class_="newsCont")
    print(Fore.CYAN + "Today's New")
    for heading, one_content in zip(headings, content):
        print(Style.RESET_ALL + heading.get_text())
        print(one_content.get_text())
        print("---------------------------")

def words():
    words_url = "https://www.dictionary.com/e/word-of-the-day/"
    word_page = requests.get(url=words_url)
    soup = BeautifulSoup(word_page.content, features="html.parser")
    word_heading = soup.find(class_="otd-item-headword__word")
    word_pos = soup.find(class_="italic")
    definition_divs = soup.find_all("div", class_="otd-item-headword__pos-blocks") 

    print(Fore.CYAN + "Word of the Day:")
    print(Fore.LIGHTMAGENTA_EX + word_heading.get_text() if word_heading else "No word heading found.")
    print(Style.RESET_ALL + f"Part Of Speech: {word_pos.get_text() if word_pos else 'No part of speech found.'}")
    
    for definition_div in definition_divs:
        word_definitions = definition_div.find_all("p")
        for definition in word_definitions:
            print(Fore.BLUE + definition.text.strip())

    print("\n\n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n\n\n\n")
    time.sleep(600)

fun_facts()
news()
words()
