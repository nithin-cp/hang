import random

def get_wordlist():
    f=open("/usr/share/dict/words")
    clean_words = []
    for i in f:
        i = i.strip()
        if i.isalpha() and len(i)>5:
            clean_words.append(i.lower())
    return clean_words

def select_word(word_list):
    return random.sample(wordlist,1)[0]

def play_hangman(a):
            for letters in a:
            if letters in gue:
                print letters
            else:
                print"*"
        if gue not in a:
            print" wrong guess"


wordlist = get_wordlist()
secret = select_word(wordlist)
play_hangman('cheese')

