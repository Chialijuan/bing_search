from py_ms_cognitive import PyMsCognitiveNewsSearch
"""
Go to site-packages/py_ms_cognitive/py_ms_cognitive_search/py_ms_cognitive_web_search.py file
Replace SEARCH_WEB_BASE = https://api.cognitive.microsoft.com/bing/v5.0/search with
SEARCH_WEB_BASE = 'https://api.cognitive.microsoft.com/bing/v7.0/search'
"""
API_KEY = '24eb8d76e5714f6da0236db40aeb6fc6'

search_term = 'gun control'
search_service = PyMsCognitiveNewsSearch(API_KEY, search_term)

result = search_service.search(limit=2, format='json')
# Variables avaliable: ['category', 'url', 'date_published', 'name', 'image_url', 'json', 'description']
print(result[0].json)
print(result[0].category)
