from sys import argv

script, filename = argv

############# open the file and read it in it's entirety ##################

f = open(filename)
text = f.read()

##### split the text on each blank space and turn that into a list ########

word_list =  text.split()

print word_list

print len(word_list)