# ============================================================
# TEXT PREPROCESSING IN NLP
# ============================================================

"""
Text preprocessing is the process of cleaning and transforming
raw text into a format that can be understood by machine learning
or deep learning models.

Raw text is noisy and unstructured. It may contain:
- HTML tags
- URLs
- Emojis
- Slang words
- Punctuation
- Stopwords

Goal:
Make text clean, consistent, and meaningful for modeling.
"""


# ============================================================
# TYPES OF TEXT PREPROCESSING
# ============================================================

"""
1. Basic Text Preprocessing
2. Advanced Text Preprocessing
"""


# ============================================================
# 1. BASIC TEXT PREPROCESSING
# ============================================================

"""
Basic preprocessing includes simple and commonly used steps.
"""


# ------------------------------------------------------------
# 1.1 LOWERCASING
# ------------------------------------------------------------

"""
Convert all text to lowercase.

Why?
- "Hello" and "hello" should be treated the same
- Reduces vocabulary size
"""

text = "Hello World"
text = text.lower()


# ------------------------------------------------------------
# 1.2 REMOVING HTML TAGS
# ------------------------------------------------------------

"""
HTML tags do not add value to text analysis.
"""

import re

def remove_html(text):
    return re.sub(r'<.*?>', '', text)


# ------------------------------------------------------------
# 1.3 REMOVING URLs
# ------------------------------------------------------------

"""
URLs usually do not contribute to meaning.
"""

def remove_urls(text):
    return re.sub(r'http\S+|www\S+', '', text)


# ------------------------------------------------------------
# 1.4 REMOVING PUNCTUATION
# ------------------------------------------------------------

"""
Two cases:

Case 1:
Punctuation treated as separate tokens:
['hello', '!', 'world', '.']
→ increases document length (noise)

Case 2:
Punctuation attached to words:
['hello!', 'world.']
→ model treats them as different words

Solution:
Remove punctuation to standardize text
"""

import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))


# ------------------------------------------------------------
# 1.5 TOKENIZATION
# ------------------------------------------------------------

"""
Tokenization = splitting text into smaller units

Types:
- Word Tokenization
- Sentence Tokenization
- Paragraph Tokenization
"""

from nltk.tokenize import word_tokenize, sent_tokenize

text = "NLP is amazing. It is very powerful."

words = word_tokenize(text)
sentences = sent_tokenize(text)


# ----------------------
# Challenges in Tokenization
# ----------------------

"""
- Prefixes (unhappy)
- Suffixes (running)
- Infixes (don't → do + not)
- Exceptions (U.S.A, numbers, abbreviations)
"""


# ----------------------
# Tokenization Methods
# ----------------------

"""
1. Split Function:
   text.split()
   ❌ Problem: cannot handle punctuation, contractions

2. Regular Expressions:
   Flexible but complex

3. NLTK:
   Easy and widely used
   ❌ Problem: not always perfect

4. spaCy:
   More accurate and faster
   Used in production systems
"""


# ------------------------------------------------------------
# 1.6 STOPWORDS REMOVAL
# ------------------------------------------------------------

"""
Stopwords are common words:
- is, the, and, am

They usually do not carry important meaning.
"""

from nltk.corpus import stopwords

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]


# ------------------------------------------------------------
# 1.7 STEMMING
# ------------------------------------------------------------

"""
Stemming reduces words to root form.

Example:
running → run

Properties:
- Fast
- Used in Information Retrieval systems
- May produce incorrect words
"""

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stemmer.stem("running")


# ------------------------------------------------------------
# 1.8 LEMMATIZATION
# ------------------------------------------------------------

"""
Lemmatization converts words to their base (dictionary) form.

Example:
better → good
running → run

Properties:
- More accurate
- Slower than stemming
"""

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("running", pos='v')


# ------------------------------------------------------------
# 1.9 HANDLING EMOJIS
# ------------------------------------------------------------

"""
Two approaches:

1. Remove emojis
2. Convert to meaning (recommended for sentiment analysis)

Example:
😊 → happy
😢 → sad
"""

def remove_emojis(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)


# ------------------------------------------------------------
# 1.10 HANDLING CHAT WORDS (SLANG)
# ------------------------------------------------------------

"""
Convert informal words into proper form.

Examples:
lol → laughing out loud
asap → as soon as possible
fr → for real
"""

chat_words = {
    "lol": "laughing out loud",
    "asap": "as soon as possible",
    "fr": "for real"
}


# ============================================================
# 2. ADVANCED TEXT PREPROCESSING
# ============================================================

"""
Advanced preprocessing is used in real-world systems.
"""


# ------------------------------------------------------------
# 2.1 SPELLING CORRECTION
# ------------------------------------------------------------

"""
Correct misspelled words.

Tools:
- TextBlob
- autocorrect

Example:
recieve → receive
"""


# ------------------------------------------------------------
# 2.2 HANDLING NEGATION
# ------------------------------------------------------------

"""
Negation changes meaning.

Example:
"not good" → negative

Technique:
Combine words:
not good → not_good
"""


# ------------------------------------------------------------
# 2.3 NAMED ENTITY HANDLING
# ------------------------------------------------------------

"""
Recognize entities like:
- Person
- Location
- Organization

Example:
"Elon Musk" → PERSON
"""


# ------------------------------------------------------------
# 2.4 TEXT NORMALIZATION
# ------------------------------------------------------------

"""
Standardize text:
- Expand contractions (don't → do not)
- Normalize repeated characters (soooo → so)
"""


# ------------------------------------------------------------
# 2.5 LANGUAGE DETECTION
# ------------------------------------------------------------

"""
Detect language before processing.

Useful for multilingual datasets.
"""


# ------------------------------------------------------------
# 2.6 ADVANCED TOKENIZATION (TRANSFORMERS)
# ------------------------------------------------------------

"""
Modern NLP uses subword tokenization:

- WordPiece (BERT)
- Byte Pair Encoding (BPE)
- SentencePiece

Advantages:
- Handles unknown words
- Reduces vocabulary size
"""


# ============================================================
# IMPORTANT NOTES
# ============================================================

"""
1. Not all steps are required for every problem

2. For Machine Learning:
   → More preprocessing is needed

3. For Deep Learning:
   → Less preprocessing (models learn features automatically)

4. For Transformers:
   → Minimal preprocessing required

5. Always experiment to find best combination
"""


# ============================================================
# FINAL PIPELINE
# ============================================================

"""
Typical preprocessing flow:

Lowercase
→ Remove noise (HTML, URLs, punctuation)
→ Tokenization
→ Stopword removal
→ Stemming/Lemmatization
→ Feature extraction
"""
