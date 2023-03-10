# -*- coding: utf-8 -*-
"""KH1_NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15ZotNU2dSrV14VSlc2iY6MtYUGSrDfA1

**Natural Language Processing**
 * NLP is an interdesciplinary subfield of linguistics, compute science , and artificial intelligence concerned with the interactions between computers and human language, or how to program computers to process and analyze large amount of human language data.

**Libraries for NLP**
 * NLTK - Natural language tool kit
 * Textblob

**Tokenization**
 * Word Tokenization
 * Sent Tokenization
 * Blankline Tokenization
"""

!pip install nltk

import nltk

nltk.download('punkt')

"""* Word Tokenization"""

AI = "Hello Mr. John, how are you doing today? The weather is great, and Python is awesome Programming Language. The sky is blue. You shouldn't eat sugar. "

from nltk.tokenize import word_tokenize
AI_token = word_tokenize(AI)
print(AI_token)

"""* Sentence Tokenization"""

from nltk.tokenize import sent_tokenize
AI_token_sent = sent_tokenize(AI)
print(AI_token_sent)

"""* Blankline Tokenization"""

from nltk.tokenize import blankline_tokenize
AI_token_blank = blankline_tokenize(AI)
print(AI_token_blank)

"""* Frequency Distribution"""

from nltk.probability import FreqDist
fdist = FreqDist()

for word in AI_token:
  fdist[word.lower()] += 1

fdist

fdist.keys()

len(fdist)

fdist_top_10 = fdist.most_common(10)
fdist_top_10

"""**Three Types of token**
 * Biagram :- token of two consecutive written words
 * Trigram :- token of three consecutive written words
 * Ngram :- token of n-number of consecutive written words
"""

string = 'The most beautiful things in the world cannot be seen or even touched, they must be felt with the heart'
quotes_token = nltk.word_tokenize(string)
print(quotes_token)

quotes_bigrams = list(nltk.bigrams(quotes_token))
quotes_bigrams

quotes_trigrams = list(nltk.trigrams(quotes_token))
quotes_trigrams

quotes_ngrams = list(nltk.ngrams(quotes_token , 5))
quotes_ngrams

"""**Steeming :- Changes to the token**
  * Normalize a word to its base form or root form
  * Affection, Affects, Affections, Affected, Affecting => Affect
  * stemming algorithm works by cutting ends or beginning of the words taking into account most common word.
"""

from nltk.stem import PorterStemmer
pst = PorterStemmer()
pst.stem('having')

#word_to_stem = ['give' , 'giving' , 'given' , 'gave']
#word_to_stem = ['argue', ' argued' , 'argues' , 'arguing']
word_to_stem = ['eating' , 'eats' , 'eat' , 'ate' , 'eaten']

for word in word_to_stem:
  print(word , '-' , pst.stem(word))

from nltk.stem import LancasterStemmer
lst = LancasterStemmer()

for word in word_to_stem:
  print(word , '-' , lst.stem(word))

"""* Lancaster Stemmer is more aggresive then Porter Stemmmer
* Snowball Stemmer is a update in porter stemmer with multi language supports
"""

from nltk.stem import SnowballStemmer
sbst = SnowballStemmer('english')

for word in word_to_stem:
  print(word , '-' , sbst.stem(word))

"""**Lemmatization:- In case when stemming don't results correctly for example fish, fishes, fisherman. I uses morphological analysis of words which may turn it into fish using stemming**"""

word_to_stem = ['study' , 'studies' , 'studying']

pst = PorterStemmer()
lst = LancasterStemmer()
sbst = SnowballStemmer('english')

for word in word_to_stem:
  print(word , '-' , sbst.stem(word))

"""**What does lemmatization do?**
 * Group together different infected forms of word, called lemma.
 * Somehow similar to stemming, as it maps several word into common root.
 * Output of lemmatization is a proper word
 * For example, a lemmatizer can map gone, going and went into go.
"""

nltk.download('wordnet')

nltk.download('omw-1.4')

from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
word_len = WordNetLemmatizer()
word_len.lemmatize('corpora')

word_to_lem = ['study' , 'studies' , 'studying']

for word in word_to_lem:
  print(word , '-' , word_len.lemmatize(word))

"""**Stop words**
 * Several word in english such as I,at,or,begin,got,know,various etc. which areusefull in making sentences but these are not that useful in NLP.
 * So these are called stopwords.
"""

nltk.download('stopwords')

from nltk.corpus import stopwords
print(stopwords.words('english'))

print(len(stopwords.words('english')))

"""**Punctuations**"""

import re
punctuations = re.compile(r'[-.?!,:;()\'|0-9]')

post_punctuations = []
for word in AI_token:
  word = punctuations.sub('_',word)
  post_punctuations.append(word)

print(post_punctuations)

"""**Parts of Speech (POS Tags)**
  * Generally speaking gramatical types of words like noun, verb, adverb, adjectives etc.
  * A word can have more then one part of speech based upon context it is used
  * Ex. "Google Someyhing on internet" , Here google is used as a verb although it is a noun.
  * these are some sort of ambiquities or difficulties which makes things complicated.
  *****
  POS Tags are used to describe whether a word is a noun, an adjective , a proper noun , singular, plural , verb , adverb, symbol etc.
"""

nltk.download('averaged_perceptron_tagger')

"""**Abbreviation 	Meaning**
* **CC** 	coordinating conjunction
* **CD** 	cardinal digit
* **DT** 	determiner
* **EX** 	existential there
* **FW** 	foreign word
* **IN** 	preposition/subordinating conjunction
* **JJ** 	This NLTK POS Tag is an adjective (large)
* **JJR** 	adjective, comparative (larger)
* **JJS** 	adjective, superlative (largest)
* **LS** 	list market
* **MD** 	modal (could, will)
* **NN** 	noun, singular (cat, tree)
* **NNS** 	noun plural (desks)
* **NNP** 	proper noun, singular (sarah)
* **NNPS** 	proper noun, plural (indians or americans)
* **PDT** 	predeterminer (all, both, half)
* **POS** 	possessive ending (parent\ ???s)
* **PRP** 	personal pronoun (hers, herself, him, himself)
* **PRP$** 	possessive pronoun (her, his, mine, my, our )
* **RB** 	adverb (occasionally, swiftly)
* **RBR** 	adverb, comparative (greater)
* **RBS** 	adverb, superlative (biggest)
* **RP** 	particle (about)
* **TO** 	infinite marker (to)
* **UH** 	interjection (goodbye)
* **VB** 	verb (ask)
* **VBG** 	verb gerund (judging)
* **VBD** 	verb past tense (pleaded)
* **VBN** 	verb past participle (reunified)
* **VBP** 	verb, present tense not 3rd person singular(wrap)
* **VBZ** 	verb, present tense with 3rd person singular (bases)
* **WDT** 	wh-determiner (that, what)
* **WP** 	wh- pronoun (who)
* **WRB** 	wh- adverb (how)
"""

sent = 'Joy is a natural when it comes to a singing.'

s_token = word_tokenize(sent)
print(s_token)

for token in s_token:
  print(nltk.pos_tag([token]))

for token in AI_token:
  print(nltk.pos_tag([token]))

"""**Named Entity Recognition**
* Naming such as - 
  * Movie
  * monetary value
  * organization
  * location
  * Quantities
  * person from a text

"""

NE_sent = "Google's CEO Sundar Pichai introduced the new pixel at Minnesota Roi Centre Event"
NE_token = word_tokenize(NE_sent)
NE_tags = nltk.pos_tag(NE_token)
NE_tags

nltk.download('maxent_ne_chunker')

nltk.download('words')

from nltk import ne_chunk
NE_NER = ne_chunk(NE_tags)
print(NE_NER)

"""**NER Entities List**
* Facility
* Location
* Organization
* Person
* GEO-Socio-Political Group
* GEO-Political Entity

**Syntax**
* Linguistics syntax is a set of rules, principal, and process that govern the structure of a sentence in a given language
* The term syntax is also used to refer the study of such pricipal and processess

* **Syntax Tree** is a tree representation of syntatic structure of sentences or strings.
"""

!pip install svgling

new = "the big cat ate the little mouse who was after fresh cheese"

new_token = nltk.pos_tag(word_tokenize(new))
print(new_token)

grammer_np = r"AA: {<DT><JJ><NN>}"
grammer_np = r"AA: {<JJ><NN>}"
grammer_np = r"AA: {<.*><JJ><NN>}"

grammer_np = r"""
AA: {<DT><JJ>+}
{<NN><VBD>+}
"""

chunk_parser = nltk.RegexpParser(grammer_np)
chunk_result = chunk_parser.parse(new_token)
chunk_result

"""**TextBlob**"""

from textblob import TextBlob

sent = "John used to be very happy if no one ask him to work."

TextBlob(sent).words

TextBlob(sent).tags

TextBlob(sent).sentiment.polarity

sent = "John is very sad and upset today"
TextBlob(sent).sentiment.polarity

sent = "John is feeling nice today"
TextBlob(sent).sentiment.polarity

sent = "John is travelling today"
TextBlob(sent).sentiment.polarity

