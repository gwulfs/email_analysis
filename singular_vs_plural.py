import json
from functions import get_bin_month, extract_words
from nltk.stem import WordNetLemmatizer
from email_reply_parser import EmailReplyParser
import pdb

wnl = WordNetLemmatizer()


def test_plural():
    def isplural(word):
        lemma = wnl.lemmatize(word, 'n')
        plural = True if word is not lemma else False
        return plural, lemma

    nounls = ['geese', 'mice', 'bars', 'foos', 'foo',
              'families', 'family', 'dog', 'dogs', 'strygwyr', 'werkzeugserg']

    for nn in nounls:
        isp, lemma = isplural(nn)
        print nn, lemma, isp


def is_plural(word):
    lemma = wnl.lemmatize(word, 'n')
    plural = True if word is not lemma else False
    pdb.set_trace()
    return plural


#from pattern.en import pluralize
#def is_plural2(word):
#    return True if pluralize(word) == word else False


def singular_plural_month(messages):
    data = {}
    for m in messages:
        if m['body'] and m['body'].get('content'):
            month = get_bin_month(m['date'])
            if not data.get(month):
                data[month] = {'singular': 0, 'plural': 0}

            for word in extract_words(EmailReplyParser.parse_reply(m['body']['content'])):
                if is_plural(word):
                    data[month]['plural'] += 1
                else:
                    data[month]['singular'] += 1
    return data


def singular_plural_words(messages):
    windowsize = 10000
    wordNum = 0
    data_id = 0
    data = {data_id: {'plural': 0, 'singular': 0}}
    for m in messages:
        if m.get('body') and m['body'].get('content'):
            if wordNum > windowsize:
                wordNum = 0
                data_id += windowsize
                data[data_id] = {'plural': 0, 'singular': 0}

            words = extract_words(EmailReplyParser.parse_reply(m['body']['content']))
            for word in words:
                if is_plural(word):
                    data[data_id]['plural'] += 1
                else:
                    data[data_id]['singular'] += 1
            wordNum += len(words)
    return data

f = open('email.json', 'r')
rawemails = json.load(f)
f.close()
data_months = singular_plural_month(rawemails)
data_words = singular_plural_words(rawemails)
# print data
with open('analyze_10k.json', 'wb') as f:
    f.write(json.dumps(data_months))
