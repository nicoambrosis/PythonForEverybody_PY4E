###############################################################################
#######################  Dictionaries ##########################################
###############################################################################
#Este programa fue pensado para buscar una determinada palabra dentro de un archivo de texto
print('\n################### DICTONARIES ##############################')
print('\n')

file_01=input('Enter file name:')
if len(file_01)<1: file_01='words.txt'

file=open(file_01)

counts={}
for text in file:
    text=text.rstrip()
    #print(text)
    words=text.split()
    #print(words)
    for word in words:
        counts[word]=counts.get(word,0)+1
print('\n################################################################')
print('This program has been developed to search a word in a text file...')
print('################################################################')
word=input('Which word are you looking for?')
if word in counts.keys():
    print("Your word is in the file :)!!!")

else:
    print('Sorry :( your word is not in the file')
