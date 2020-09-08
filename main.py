import nltk
from bs4 import BeautifulSoup
import requests


def get_wikipedia_raw(search_query: str) -> str:
    response = requests.get(
        'https://en.wikipedia.org/w/api.php',
        params={
            'action': 'parse',
            'format': 'json',
            'page': search_query
        }
    ).json()

    raw = response["parse"]["text"]["*"]
    soup = BeautifulSoup(raw, 'html.parser').get_text()
    return soup


tokens = nltk.word_tokenize(get_wikipedia_raw("Barack Obama"))
text = nltk.Text(tokens)
words = [w.lower() for w in text]

word_frequency_map = dict()
for word in words:
    if word not in word_frequency_map:
        word_frequency_map[word] = 1
    else:
        word_frequency_map[word] += 1
print(word_frequency_map)
