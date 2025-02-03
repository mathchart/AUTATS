#github

import nltk as nl
import matplotlib.pyplot as plt
fname = 'texts/LordoftheFlies.txt'
f = open(fname, 'r')
wordfile = f.read()
words = nl.word_tokenize(wordfile)
wordsNL = nl.Text(words)
#[w for w in wordsNL if w.isalpha()]
#fd = nl.FreqDist(wordsNL)
# fd.plot(50,cumulative=False)
# plt.show()
onlySen = nl.sent_tokenize(wordfile)
total_words = 0
for i in range(len(onlySen)):
    #print(i, ': ', onlySen[i],'Length in letters: ',len(onlySen[i])) 
    wds = onlySen[i].split()
    #print(wds)
    #print('Sentence length: ', len(wds))
    total_words += len(wds)
avg_words_sentence = total_words / len(onlySen)
print('Total words: ',total_words)
print('# of sentences', len(onlySen) )
print('Avg. words per sentence', avg_words_sentence)