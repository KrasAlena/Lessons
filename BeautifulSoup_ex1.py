'''
Write a program to read delfi headers, check if they contain a colon.
The part before the colon would be put in one list, the part after the colon in another.
Shuffle the second list (google). Then print the first parts from the first list,
connect to them the second parts from the second list. We should get similar options:

Weather: 26 thousand euros will have to be paid for 9 slags
On Tuesday evening, the residents of Kaunas were frightened by the thermal power plant:
will there be a baby boom?
Create a list of bad words to filter out posts about COVID, deaths, etc. Filter out early,
before the headlines break.
'''
from bs4 import BeautifulSoup
import requests
import random
import nltk
from nltk.stem import SnowballStemmer

nltk.download('punkt')


stemmer = SnowballStemmer('english')

source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
news = soup.find_all('h5', class_ = 'C-headline-title')

bad_words = ['COVID', 'mirtis', 'tragedija', 'katastrofa', 'krizė', 'infliacija', 'karas', 'kraujas']

stemmed_bad_words = [stemmer.stem(word) for word in bad_words]

first_parts = []
second_parts = []

for new in news:
    title = new.find('a').text

    tokens = nltk.word_tokenize(title)
    stemmed_titles = [stemmer.stem(word) for word in tokens]

    # if any(word in title for word in bad_words):
    if any(word in stemmed_titles for word in stemmed_bad_words):
        print(f'This title contains bad word: {title}')

    else:

        parts = title.split(':')

        if len(parts) > 1:
            first_parts.append(parts[0].strip())
            second_parts.append(parts[1].strip())

random.shuffle(first_parts)
random.shuffle(second_parts)

new_titles = [f'{first}: {second}' for first, second in zip(first_parts, second_parts)]

for title in new_titles:
    print(title)

