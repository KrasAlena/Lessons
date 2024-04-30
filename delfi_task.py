import sparknlp

from bs4 import BeautifulSoup
import requests
import random
from pyspark.ml import Pipeline
from sparknlp.annotator import DocumentAssembler, SentenceDetectorDLModel, Tokenizer, LemmatizerModel
from pyspark.sql import SparkSession


sparknlp.start()
# Создаем сессию Spark
spark = SparkSession.builder \
    .appName("News Scraping and Lemmatization") \
    .config("spark.jars.packages", "com.johnsnowlabs.nlp:spark-nlp_2.12:3.1.2") \
    .getOrCreate()

# Создаем пайплайн для обработки текста
document = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentence = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

lemma = LemmatizerModel.pretrained("lemma_alksnis", "lt") \
    .setInputCols(["token"]) \
    .setOutputCol("lemma")

pipeline = Pipeline(stages=[document, sentence, tokenizer, lemma])

# Скрапим новости
source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
news = soup.find_all('h5', class_='C-headline-title')

# Список плохих слов
bad_words = ['COVID', 'mirtis', 'tragedija', 'katastrofa', 'krizė', 'infliacija', 'karas', 'kraujas']

# Обработка новостей
for new in news:
    title = new.find('a').text
    print(title)

    # Создаем DataFrame с текстом новости
    data = spark.createDataFrame([[title]]).toDF("text")

    # Запускаем пайплайн на данных
    result = pipeline.fit(data).transform(data)

    # Получаем результаты лемматизации
    lemmatized_title = result.select("lemma.result").collect()[0][0]

    # Проверяем, содержатся ли плохие слова в лемматизированном заголовке
    for word in bad_words:
        if word in lemmatized_title:
            print(f"This title contains bad word: {title}")
            break  # Если найдено плохое слово, прекратить проверку для этого заголовка