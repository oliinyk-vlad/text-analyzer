from collections import Counter
from app.models import Text, Word

import re


def analyzer(text: Text):
    words = [word for word in re.findall(r'\w+', text.content.casefold())]
    for word, count in Counter(words).most_common():
        Word.objects.create(text=text, content=word, count=count)
