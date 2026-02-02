import json
import random

# Deciding the start words length
persenteces = {
    "8": 0.05,
    "7": 0.35,
    "6": 0.60
}
def choose_by_probability() -> str:
    return random.choices(
        population=list(persenteces.keys()),
        weights=list(persenteces.values()),
        k=1
    )[0]


# Load the words with tagged with their lenght
def load_words_by_lenght():
    with open('database/lenght.json') as f:
        words_dict = json.load(f)
        f.close()
    return words_dict
load_words_by_lenght = load_words_by_lenght()

def load_all_words():
    with open('database/all_words.json') as f:
        words_list = json.load(f)
        f.close()
    return words_list
# load_all_words = load_all_words()

# Sorted words list
def load_all_sorted_words():
    with open('database/sorted_words.json') as f:
        sorted_words = json.load(f)
        f.close()
    return sorted_words
load_all_sorted_words = load_all_sorted_words()

# Finding the start word
def find_parent():
    words_by_lenght = load_words_by_lenght
    start_word_lenght_list = words_by_lenght[choose_by_probability()]
    start_word = random.choice(start_word_lenght_list)
    return start_word

# Finding other words using starting word's letters
def find_childs(main_word):
    words = []
    main_letters = list(main_word)

    # Checking all words which shorter than parent
    for word in load_all_sorted_words:
        if len(word) <= len(main_word):

            # Trying to match all word's letters with parent word
            word_letters = list(word)
            # Copying the list bc. few lines later we have to remove checked letters from the main word's latter list
            # So we can keep avoid to check multiple letters
            copy_main_letters = main_letters.copy()
            counter = 0

            for word_latter in word_letters:
                if word_latter in main_letters:
                    try:
                        # There might be more than one letter so we are removing the letter which we already checked
                        copy_main_letters.remove(word_latter)
                        counter += 1
                    except ValueError:
                        pass
            if counter == len(word_letters):
                    words.append(word),

    return words, main_letters










