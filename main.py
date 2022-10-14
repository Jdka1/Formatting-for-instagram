from scripts.gethashtags import get_hashtags
from scripts.tojpg import convert_to_jpg


[print('\n') for i in range(10)]


print(get_hashtags('landscapephotography', 10))
convert_to_jpg('testim.png', portrait=False)