import json
import urllib.parse
import urllib.request

def read_webhose_key():
    webhose_api_key=None
    try:
        with open('search.key','r') as f:
            webhose_api_key=f.readline().strip()
    except:
        raise IOError('search.key file not found')
    return webhose_api_key

def run_query(search_items,size=10):
    webhose_api_key=read_webhose_key()
    if not webhose_api_key:
        raise KeyError('Webhose key not found')
    search_url='http://webhose.io/search?token={0}&format=json&q={1}&sort=relevancy&size={2}'.format(
        webhose_api_key,search_items,size)
    print(search_url)
    results=[]
    try:
        response=urllib.request.urlopen(search_url).read().decode('utf-8')
        json_response=json.loads(response)
        for post in json_response['posts']:
            results.append({'title':post['title'],
                            'link':post['url'],
                            'summary':post['text'][:200]})
    except:
        print('Error when querying the Webhose API')
    return results


