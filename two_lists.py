from sys import argv

script, filename = argv

### Get the words that appear less than 10 times in the corpus and put them ##
### in a list  - this will be the signature word list. #######################

### Take the words that appear more than 10 times and put them in a another ##
### list - this will be the linking word list. ###############################


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
    signature_list = []
    linking_list = []
    for item in clean_words:

# ### how do I say if the item in clean words appears more than 10 times in the
# ### list add it to the signature list I created above - if it does NOT appear
# ### more than 10 times add it to the linking list.

        if item in clean_words > 10:
            signature_list.append(item)
        else:
            linking_list.append(item)

    return signature_list
    return linking_list

print signature_list
print linking_list



### I found this on the stackoverflow and it looked good ################

# listOfWords = inputString.split() # splits the words up from whitespace
# setOfWords = Set(listOfWords) #  Gives you all the unique words (no duplicates)

# for each word in setOfWords  #Count how many words are in the list
#    print word + " appears: " + listOfWords.Count(word) + "times"