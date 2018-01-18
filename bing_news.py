"""
Go to site-packages/py_ms_cognitive/py_ms_cognitive_search/py_ms_cognitive_web_search.py file
Replace SEARCH_WEB_BASE = https://api.cognitive.microsoft.com/bing/v5.0/search with
SEARCH_WEB_BASE = 'https://api.cognitive.microsoft.com/bing/v7.0/search'
"""
import argparse
from py_ms_cognitive import PyMsCognitiveNewsSearch
from newsplease import NewsPlease 
from random import *
import gensim

API_KEY = '24eb8d76e5714f6da0236db40aeb6fc6'

def get_search(search_term,k):
    
    search_service = PyMsCognitiveNewsSearch(API_KEY, search_term)
    result = search_service.search(limit=k, format='json')
    return result
    # Variables avaliable: ['category', 'url', 'date_published', 'name', 'image_url', 'json', 'description']
    #print(result[0].json)

def get_sumtext(result):

    n = randint(1,len(result)-1)
    #n = 5
    try:
        article = NewsPlease.from_url(result[n].url)
        # Assuming that len of news articles are at least 150 words long and not an ad or block
        if len(article.text) <=150:
            print('Article is less than 150 words...')
            get_sumtext(result)    
        else:
            print(n)
            print(article.text)
            print('-------------------')
            sumtext = gensim.summarization.summarizer.summarize(article.text, word_count=20)
            print(sumtext)
            return sumtext

    except Exception as e:
        print(e)
        print("Retriving from another url...")
        get_sumtext(result)

#print("Category:{}".format(result[0].category))
##url = result[0].url
#url = 'http://www.columbiabasinherald.com/local_news/20180117/state_lawmakers_consider_gun_control_bills'
#print("News url:{}".format(url))
#article = NewsPlease.from_url(url)
#print("Title:{}".format(article.title))
#print("Text:{}".format(article.text))

#print(get_text(result))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--search-term', help='Search term')
    parser.add_argument('--topk', help='Top k articles', default=10)

    args = parser.parse_args()
    print(args)

    with open('text.txt', 'w') as f:
        f.write(get_sumtext(get_search(args.search_term, args.topk)))

