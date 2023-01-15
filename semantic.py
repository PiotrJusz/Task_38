"""
similarity of cat, monkey and banana
cat     cat     1.0
cat     banana  0.2235882580280304
cat     monkey  0.5929929614067078
banana  cat     0.2235882580280304
banana  banana  1.0
banana  monkey  0.404150128364563
monkey  cat     0.5929929614067078
monkey  banana  0.404150128364563
monkey  monkey  1.0
cat and monkey are more similar than cat and banana or monkey and banana - both of them are animals
monkey and banana are more similar than cat and banana - there is relation beetween monkey and banana set by model
banana and cat is the lowest simirality
my examples:
car car 1.0
car petrol 0.4519859552383423
car wood 0.1641036421060562
petrol car 0.4519859552383423
petrol petrol 1.0
petrol wood 0.18785129487514496
wood car 0.1641036421060562
wood petrol 0.18785129487514496
wood wood 1.0

carrot  carrot  1.0
carrot  rabbit  0.42742154002189636
carrot  wolf    0.18191209435462952
rabbit  carrot  0.42742154002189636
rabbit  rabbit  1.0
rabbit  wolf    0.5857271552085876
wolf    carrot  0.18191209435462952
wolf    rabbit  0.5857271552085876
wolf    wolf    1.0
"""

import spacy

nlp_sm = spacy.load("en_core_web_sm")
nlp_md = spacy.load("en_core_web_md")

words = "cat banana monkey USA"
words_nlp_sm = nlp_sm(words)
print("Tokenisation:")
print([(token,  token.orth) for token in words_nlp_sm])
print("Entity:")
print([(i, i.label_, i.label) for i in words_nlp_sm.ents])

words_nlp_md = nlp_md(words)
for item1 in words_nlp_md:
    for item2 in words_nlp_md:
        if item1 != item2:
            print(item1.text, item2.text, item1.similarity(item2))
        
