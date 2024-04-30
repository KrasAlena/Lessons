import asyncio

from bs4 import BeautifulSoup
import requests
import nltk
from nltk.stem import WordNetLemmatizer
from telegram import Bot
import os
import dotenv

dotenv.load_dotenv()

bot_api_key = os.environ.get('TELEGRAM_BOT_TOKEN')
telegram_chat_id = os.environ.get('TELEGRAM_CHAT_ID')


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


class NewsAnalyzer:
    def __init__(self, url):
        self.url = url
        self.lemmatizer = WordNetLemmatizer()
        self.source = requests.get(url).text
        self.soup = BeautifulSoup(self.source, 'html.parser')
        self.news = self.soup.find_all('h3')
        self.bad_words = ['COVID', 'death', 'murder', 'crisis', 'kill', 'war']
        self.lemmatized_bad_words = [self.lemmatizer.lemmatize(word) for word in self.bad_words]

    def get_news_titles(self):
        titles = [headline.get_text(strip=True) for headline in self.news if headline]
        return titles

    def get_bad_news(self):
        bad_news_count = 0
        titles = self.get_news_titles()
        for title in titles:
            if any(word in title for word in self.bad_words):
                bad_news_count += 1
        return bad_news_count

    def find_news_by_word(self, word):
        matching_news = [headline.get_text(strip=True) for headline in self.news if word.lower() in headline.get_text(strip=True).lower()]
        return matching_news

    def get_link_with_headlines(self):
        links_with_headlines = []
        for link in self.soup.find_all('a'):
            if link.find('h3'):
                href = link.get('href')
                headline = link.find('h3').get_text(strip=True)
                links_with_headlines.append((headline, href))
        return links_with_headlines


class Menu:
    def __init__(self):
        self.news_analyzer = NewsAnalyzer('https://time.com')
        self.telegram_bot_token = bot_api_key

    async def run_async(self):
        while True:
            print('\nMenu:')
            print('1. Print today\'s news headlines')
            print('2. How many bad news are today?')
            print('3. Find specific news')
            print('4. Send news to Telegram')
            print('0. Exit')
            choice = input('Enter your choice: ')
            if choice == '1':
                self.print_news_headlines()
            elif choice == '2':
                self.show_bad_news_count()
            elif choice == '3':
                self.find_news_by_word()
            elif choice == '4':
                await self.send_matching_news_to_telegram()
            elif choice == '0':
                print('Exit...')
                break
            else:
                print('Invalid choice')

    async def send_telegram_message(self, message):
        bot = Bot(token=bot_api_key)
        await bot.send_message(chat_id=telegram_chat_id, text=message)

    async def send_matching_news_to_telegram(self):
        keyword = input('Enter the keyword: ')
        links_with_headlines = self.news_analyzer.get_link_with_headlines()
        if links_with_headlines:
            matching_news = [(headline, self.make_absolute_link(href)) for headline, href in links_with_headlines if keyword.lower() in headline.lower()]
            if matching_news:
                for headline, href in matching_news:
                    message = f'{headline}: {href}'
                    await self.send_telegram_message(message)
                print('Matching news sent to your Telegram')
            else:
                print('No matching newws found')
        else:
            print('No news found')

    def make_absolute_link(self, href):
        if href.startswith('http://') or href.startswith('https://'):
            return href
        else:
            return f'https://time.com{href}'

    def print_news_headlines(self):
        titles = self.news_analyzer.get_news_titles()
        print('\nToday\'s news headlines:')
        for title in titles:
            print(title)

    def show_bad_news_count(self):
        count = self.news_analyzer.get_bad_news()
        print(f'\nNumber of news containing bad words: {count}')

    def find_news_by_word(self):
        word = input('Enter the key word: ')
        matching_news = self.news_analyzer.find_news_by_word(word)
        if matching_news:
            print(f'\nNews containing "{word}":')
            for news in matching_news:
                print(news)
            else:
                print(f'No news find containing word: {word}.')


def main():
    menu = Menu()
    asyncio.run(menu.run_async())

if __name__ == '__main__':
    main()

