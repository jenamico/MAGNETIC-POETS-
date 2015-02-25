from sys import argv
from random import sample

script, filename = argv

f = open(filename)
text = f.read()

def string_splitter(text):
    word_list =  text.split()
    return word_list

def clean_up(word_list):
    clean_words = []
    for item in word_list:
        lowercase = item.lower()
        clean_words.append(lowercase.strip('!.?_()*[]#,:;-\\/\'\"'))

    return clean_words

def wordcount(clean_words):
    occurrence_dict = {}
    for item in clean_words:
        if item in occurrence_dict:
            occurrence_dict[item] += 1
        else:
            occurrence_dict.setdefault(item)
            occurrence_dict[item] = 1
    return occurrence_dict

def alphabetize(occurrence_dict):
    word_counts = {}
    for word, num_times in occurrence_dict.iteritems():
        if not word_counts.has_key(num_times):
            word_counts[num_times] = [word]
        else:
            word_counts[num_times].append(word)

    for number, word in word_counts.items():
        word_counts[number] = sorted(word_counts[number])

    return word_counts



def make_two_lists(word_counts):
    signature_list = []
    connecting_list = []

    for key, value in word_counts.items():
        if key < 10:
            # signature_list.extend(value)
            for i in range(len(word_counts[key])):
                for j in range(key):
                    signature_list.append(word_counts[key][i])
        else:
            # connecting_list.extend(value)
            for i in range(len(word_counts[key])):
                for j in range(key):
                    connecting_list.append(word_counts[key][i])


    print "I am the signature list", signature_list
    print "I am the connecting list", connecting_list

    return signature_list, connecting_list


def random_lists(signature_list, connecting_list):
    random_signature_list = []
    random_connecting_list = []


    random_signature_list = sample(signature_list, 100)
    random_connecting_list = sample(connecting_list, 25)

    print random_signature_list
    print random_connecting_list


    return random_signature_list, random_connecting_list


def main():

    split_string = string_splitter(text)
    clean_words = clean_up(split_string)
    counted_words = wordcount(clean_words)
    alpha_words = alphabetize(counted_words)
    list1, list2 = make_two_lists(alpha_words)
    random_sig_list, random_connect_list = random_lists(list1, list2)


     # (make_two_lists(alphabetize(wordcount(clean_up(string_splitter(text))))))

main()