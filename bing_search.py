import requests

def bing_search(query):
        url = 'https://api.cognitive.microsoft.com/bing/v7.0/news'
            # query string parameters
        payload = {'q': query}
                    # custom headers
        headers = {'Ocp-Apim-Subscription-Key': '24eb8d76e5714f6da0236db40aeb6fc6'}
                            # make GET request
        r = requests.get(url, params=payload, headers=headers)
                                    # get JSON response
        #print(r.json())
        return r.json()

j = bing_search('gun control')
print(j['value']['clusteredArticles'])
#print(j.get('webPages', {}).get('value', {}))
