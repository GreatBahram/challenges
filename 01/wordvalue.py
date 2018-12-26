from data import DICTIONARY, LETTER_SCORES

def load_words(filename=DICTIONARY):
    """Load dictionary into a list and return list"""
    words = []
    with open(filename, mode='rt') as dictionary_file:
        words = [word.strip() for word in dictionary_file]
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for char in word:
        score += LETTER_SCORES.get(char.upper(), 0)
    return score

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        words = load_words()
    words_score = {calc_word_value(word): word for word in words}
    return words_score[max(words_score)]

if __name__ == "__main__":
    max_word_value()
