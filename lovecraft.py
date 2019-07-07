import nltk
import numpy as np
import pickle


"""
Lovecraft text generation
"""


def text(start_word="Cthulhu", size=10):
    lovecraft_bigram_cfd = read_cfd()
    random_words = generate_model_from_word(lovecraft_bigram_cfd, start_word, num=size)
    return format_random_text(random_words)


# Get the type of words of each word
def format_random_text(generated_words):
    return ' '.join(generated_words)
    
    #generated_tagged_words = nltk.tag.pos_tag(generated_words)
    #word_type = dict(generated_tagged_words)

    # Add a "." before each capital letter that is not a proper name or "I"
    #text = ""
    #for i in range(0, len(list(generated_words))):
    #    if i >= len(list(generated_words)) - 1:
    #        text += " "+generated_words[i]+"."
    #    else:
    #        text += " "+generated_words[i] + ("." if generated_words[i+1][0].isupper() and word_type.get(generated_words[i+1]) not in ("NNP", "POS") and generated_words[i+1] != "I" else "")

    #return text.strip()


def generate_model_from_word(cfdist, word, num=15):
    words = []
    for i in range(num):
        words.append(word)
        word_fd = cfdist[word]
        word = get_random_word_from_fd(word_fd)
    return words


def generate_model(cfdist, fd, num=15):
    words = []
    word = get_random_word_from_fd(fd)
        
    for i in range(num):
        words.append(word)
        word_fd = cfdist[word]
        word = get_random_word_from_fd(word_fd)
    return words


def get_random_word_from_fd(fd):
    # Construct probabilities for each word that belongs to the frequency distribution
    word_prob_pairs = [(word_i,word_i_freq/fd.N()) for word_i,word_i_freq in fd.items()]
    words = [word_prob_pair[0] for word_prob_pair in word_prob_pairs]
    probabilities = [word_prob_pair[1] for word_prob_pair in word_prob_pairs]

    # Select a random chose according to the probabilities of each word
    random_word_chose = np.random.multinomial(1, probabilities)
    random_word_index = list(random_word_chose).index(1)
    return words[random_word_index]


def read_cfd():
    # Read conditional frequency distribution from pickle
    lovecraft_bigram_cfd_file = open('lovecraft_bigram_cfd.pkl', 'rb')
    lovecraft_bigram_cfd = pickle.load(lovecraft_bigram_cfd_file)
    lovecraft_bigram_cfd_file.close()
    return lovecraft_bigram_cfd

