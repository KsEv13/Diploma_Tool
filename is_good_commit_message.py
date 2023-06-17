from nltk.stem import PorterStemmer
import re

def is_good_commit_message(commit_message):

    good_commit_bag_of_words = [
        'fix', 'optimize', 'add', 'test',
        'clean', 'update', 'refactor', 'implement'
        ]
    
    ps = PorterStemmer()
    stemmed_words = set(ps.stem(word) for word in good_commit_bag_of_words)
    
    # Tokenize the commit message into individual words
    words = re.findall(r'\w+', commit_message.lower())
    
    # Check if any stemmed word is present in the commit message
    for word in words:
        if ps.stem(word) in stemmed_words:
            return True
    
    return False