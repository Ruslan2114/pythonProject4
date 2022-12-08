import json
from classes.question import Question
from random import shuffle
import requests
# questions = requests.get('https://jsonkeeper.com/b/32WA')
questions = json.load(open('questions.json', encoding='utf-8'))
questions = [Question(i['q'], i['d'], i['a']) for i in questions]
shuffle(questions)