from random import sample


word_counts = {4: ['again', 'an', 'are', 'father', 'from', 'his', 'kind', 'leaves', 'look', 'or', 'so', 'special', 'when', 'year'], 5: ['be', 'by', 'down', 'give', 'her', 'know', 'me', 'their', 'them', 'with', 'woman'],
6: ['all', 'but', 'watch'], 7: ['as', 'here', 'its'], 8: ['love', 'they', 'where'], 9: ['not'], 10: ['on'], 11: ['this', 'will'], 12: ['at', 'that'], 13: ['out'], 14: ['like']}


signature_list = []
connecting_list = []

# For iterating over just the keys
# for key in word_counts:
#     if key < 10:
#         signature_list.extend(word_counts[key])
#     else:
#         connecting_list.extend(word_counts[key])

# If you want to iterate over key, value, use .items()
for key, value in word_counts.items():
    print key
    if key < 10:
        signature_list.extend(value)
    else:
        connecting_list.extend(value)

# print "Signature list:", signature_list
# print "Connecting list:", connecting_list

random_signature_list = []
random_connecting_list = []

random_signature_list = sample(signature_list, 5)
random_connecting_list = sample(connecting_list, 5)

print "random_signature_list:", signature_list
print "random_connecting_list:", random_connecting_list



# random.sample([1, 2, 3, 4, 5],  3)  # Choose 3 elements
# [4, 1, 5]

# there is also random.sample() in python. For example : random.sample(some_list, 5) will return list of 5 elements where every element is randomly chosen from some_list.






