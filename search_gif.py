import requests
import sys
import random
import pyperclip

PUBLIC_KEY = 'dc6zaTOxFJmzC'
URL = 'http://api.giphy.com'
SEARCH_PATH = '/v1/gifs/search'

search_key = ''
for arg in sys.argv[1:]:
    search_key = search_key + ' ' + arg
payload = {'api_key': PUBLIC_KEY, 'q': search_key}
r = requests.get(URL + SEARCH_PATH, params=payload)
data = r.json()['data']
array_size = len(data)
image_position = random.randrange(0, array_size)
image_url = data[image_position]['images']['original']['url']
pyperclip.copy('![]('+image_url+')')
print image_url + '\n'
print 'Image url copied to your clipboard'
