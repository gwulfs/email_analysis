import json
from functions import get_bin_month, extract_words
from email_reply_parser import EmailReplyParser
import nltk
import pdb

stemmer = nltk.stem.snowball.EnglishStemmer()

files = ['Positive.txt', 'fillersyouth.txt', 'negative.txt',
 'a.txt', 'headProblems.txt', 'negativemarkers.txt',
 'an.txt', 'headProblemsExtended.txt', 'the.txt',
 'discrepancy.txt', 'hearLoud.txt', 'think.txt',
 'exclusives.txt', 'hearSoft.txt', 'fillers.txt',
 'hearSpeak.txt']

def inside(word):
    stemmed = stemmer.stem(word)
    increment = True if stemmed in stemmed_list else False
    return increment

def counts_month(messages):
    data = {}
    for m in messages:
        if m['body'] and m['body'].get('content'):
            month = get_bin_month(m['date'])
            if not data.get(month):
                data[month] = {'+': 0, '-': 0}

            for word in extract_words(EmailReplyParser.parse_reply(m['body']['content'])):
                if inside(word):
                    data[month]['+'] += 1
                else:
                    data[month]['-'] += 1
    return data

def counts_words(messages):
    windowsize = 10000
    wordNum = 0
    data_id = 0
    data = {data_id: {'+': 0, '-': 0}}
    for m in messages:
        if m.get('body') and m['body'].get('content'):
            if wordNum > windowsize:
                wordNum = 0
                data_id += windowsize
                data[data_id] = {'+': 0, '-': 0}

            words = extract_words(EmailReplyParser.parse_reply(m['body']['content']))
            for word in words:
                if inside(word):
                    data[data_id]['+'] += 1
                else:
                    data[data_id]['-'] += 1
            wordNum += len(words)
    return data

f = open('email.json', 'r')
rawemails = json.load(f)
f.close()

for filename in files:
    f = open('dicts/{}'.format(filename))
    stemmed_list = [stemmer.stem(x.strip('\r\n')) for x in f.readlines()]
    f.close()
    data_months = counts_month(rawemails)
    data_words = counts_words(rawemails)
    wordfile = 'results/{}_10k.json'.format(filename[:-4])
    # monthfile = 'results/{}_month.json'.format(filename[:-4])
    with open(wordfile, 'wb') as f:
        f.write(json.dumps(data_words))
    # with open(monthfile, 'wb') as f:
    #     f.write(json.dumps(data_months))
