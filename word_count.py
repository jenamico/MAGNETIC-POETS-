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
        clean_words.append(lowercase.strip('!:.?_()*[]#,:;-\\/\'\"'))

    return clean_words

# def wordcount(clean_words):
#     occurrence_dict = {}
#     for item in clean_words:
#         if item in occurrence_dict:
#             occurrence_dict[item] += 1
#         else:
#             occurrence_dict.setdefault(item)
#             occurrence_dict[item] = 1
#     return occurrence_dict

# def alphabetize(occurrence_dict):
#     word_counts = {}
#     for word, num_times in occurrence_dict.iteritems():
#         if not word_counts.has_key(num_times):
#             word_counts[num_times] = [word]
#         else:
#             word_counts[num_times].append(word)

#     for number, word in word_counts.items():
#         word_counts[number] = sorted(word_counts[number])

#     return word_counts


def main():

    split_string = string_splitter(text)
    cleaned_words = clean_up(split_string)
    # word_counts = wordcount(cleaned_words)
    # alpha_word_counts = alphabetize(word_counts)

    print cleaned_words


     # (make_two_lists(alphabetize(wordcount(clean_up(string_splitter(text))))))

main()