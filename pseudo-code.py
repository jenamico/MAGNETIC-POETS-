from sys import argv
from random import sample

script, filename = argv


############# open the file and read it in it's entirety ##################
def open_read_file(filename):
    f = open(filename)
    text = f.read()
    return text

##### split the text on each blank space and turn that into a list ########

def string_splitter(text):
    word_list =  text.split()
    return word_list

############# take each word on the list and turn into lowercase  #########
############# strip of some punctuation ###################################
############# then add to a list called clean_words  ######################

def clean_up(word_list):
    clean_words = []
    for item in word_list:
        lowercase = item.lower()
        clean_words.append(lowercase.strip('!.?_()*[]#,:;-\\/\'\"'))

    return clean_words

############ take those clean words and create an occurrence dictionary ###
############ if the word IS NOT already in it, add it  ####################
############ if the word IS in it, increase the count by 1 ################

def wordcount(clean_words):
    occurrence_dict = {}
    for item in clean_words:
        if item in occurrence_dict:
            occurrence_dict[item] += 1
        else:
            occurrence_dict.setdefault(item)
            occurrence_dict[item] = 1

    return occurrence_dict

########### count each occurence of the word and order them by keyword #####
########### keyword = number of times each word occurs #####################
########### then sort the key values alphabetically ########################

def alphabetize(occurrence_dict):
    word_counts = {}
    for word, num_times in occurrence_dict.items():
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
           signature_list.extend(value)
        else:
            connecting_list.extend(value)

    return signature_list
    return connecting_list

# For iterating over just the keys
# for key in word_counts:
#     if key < 10:
#         signature_list.extend(word_counts[key])
#     else:
#         connecting_list.extend(word_counts[key])

# If you want to iterate over key, value, use .items()

# for key, value in word_counts.items():
#     print key
#     if key < 10:
#         signature_list.extend(value)
#     else:
#         connecting_list.extend(value)

# print "Signature list:", signature_list
# print "Connecting list:", connecting_list
def make_random_lists(signature_list, connecting_list):
    random_signature_list = []
    random_connecting_list = []

    random_signature_list = sample(signature_list, 75)
    random_connecting_list = sample(connecting_list, 25)

    return random_signature_list
    return random_connecting_list

print "random_signature_list:", random_signature_list
print "random_connecting_list:", random_connecting_list




# def print_signature_words(signature_words):
#     print signature_list
#     print connecting_list



# def print_sorted_wordcount(word_counts):
#     for key, value in sorted(word_counts.items()):
#         print "%s %r" % (key, value)

########### this is the main loop which repeatedly executes ###############
########### the primary task of the program, in this case   ###############
########### taking text, splitting it, cleaning it up  ####################
########### counting each occurence of words and alphabitizing them #######

# def main():


#     # print_sorted_wordcount(alphabetize(wordcount(clean_up(string_splitter(text)))))


if __name__ == "__main__":
    main()