from nltk.corpus import wordnet

#finding synonyms and antonymns

synonyms = []
antonyms = []

for syn in wordnet.synsets("hate"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

