import requests
from bs4 import BeautifulSoup
import random

def get_hashtags(topic, num=20):
    url = f'http://best-hashtags.com/hashtag/{topic}/'
    html = requests.get(url=url).text
    soup = BeautifulSoup(html, 'html.parser')

    ptags = [soup.find(f'p{i}').text.split(' ') for i in range(1,4)]
    hashtags = []
    for ptag_list in ptags:
        hashtags += ptag_list
    
    hashtags = [hashtag for hashtag in hashtags if hashtag]
    
    return [random.choice(hashtags) for i in range(min(num,len(hashtags)))]


print(get_hashtags('landscapephotography', 20))