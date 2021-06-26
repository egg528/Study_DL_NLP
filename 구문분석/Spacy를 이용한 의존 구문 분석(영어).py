import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp('The fat cat sat on the mat')
for token in doc:
    print(token.text, token.dep_, token.head.text)

displacy.render(doc, style='dep', jupyter=True)
