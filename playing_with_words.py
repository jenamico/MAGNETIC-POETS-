from sys import argv

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

def print_sorted_wordcount(word_counts):
    for key, value in sorted(word_counts.iteritems()):
        print "%s %r" % (key, value)


def main():

    print_sorted_wordcount(alphabetize(wordcount(clean_up(string_splitter(text)))))

main()

