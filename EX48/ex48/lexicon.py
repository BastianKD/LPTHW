# lexicon.py is a lexicon to enable the program to recognize certain words.


lexicon = {
    'north': 'direction',
    'east': 'direction',
    'west': 'direction',
    'south': 'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'bear': 'noun',
    'princess': 'noun',
    '1234': 'number',
    '3': 'number',
    '91234': 'number',
    'ASDFADFASDF': 'error',
    'IAS': 'error'
    }


def scan(sentence):
    words = sentence.split()
    result = []

    for word in words:
        pair = (lexicon[word], word)
        result.append(pair)

    return result



direction_words = ['north','south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['run', 'go', 'stop', 'kill', 'shoot', 'eat']
stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
numbers = [0,9]
