from py_ms_cognitive impotr PyMsCognitiveNewsSearch

API_KEY = '24eb8d76e5714f6da0236db40aeb6fc6'

search_term = 'gun control'
search_service = PyMsCognitiveNewsSearch(APT_KEY, search_term)

result = search_service.search(limit=2, format='json')
print('result:{}'.format(result))
