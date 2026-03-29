# ============================================================
# 📌 WORD2VEC 
# ============================================================

"""
Word2Vec is one of the most important techniques in NLP
for converting words into meaningful numerical vectors.

This file covers:
- What are Word Embeddings
- CBOW (Continuous Bag of Words)
- Skip-Gram Model
- Training Word2Vec
- Practical Example (Game of Thrones dataset)
"""


# ============================================================
# 🧠 WHAT ARE WORD EMBEDDINGS?
# ============================================================

"""
Word Embeddings are numerical representations of words
in the form of dense vectors.

Key Idea:
Words with similar meanings are placed close to each other
in vector space.

Example:
king ≈ queen
tea ≈ coffee

Simple definition:
Convert words into vectors while preserving meaning.
"""


# ============================================================
# 🔄 TYPES OF TEXT REPRESENTATION
# ============================================================

"""
1. Frequency-Based Methods:
   - Bag of Words (BoW)
   - TF-IDF
   - GloVe

2. Prediction-Based Methods:
   - Word2Vec (uses neural networks)
"""


# ============================================================
# 📌 WHAT IS WORD2VEC?
# ============================================================

"""
Word2Vec is a neural network-based technique used to learn
word embeddings from text.

It converts each word into a dense vector (list of numbers)
based on its context.
"""


# ============================================================
# ❓ WHY WORD2VEC?
# ============================================================

"""
Problems with traditional methods (BoW, TF-IDF):
- Sparse vectors (mostly zeros)
- No semantic meaning
- High dimensionality

Word2Vec advantages:
- Captures semantic meaning
- Low-dimensional vectors → faster computation
- Dense vectors → no sparsity
"""


# ============================================================
# ⚖️ DIFFERENCE FROM OTHER TECHNIQUES
# ============================================================

"""
Word2Vec vs Traditional Methods:

1. Captures semantic meaning ✔
2. Low dimensional vectors ✔
3. Dense vectors (non-zero values) ✔
"""


# ============================================================
# 🛠 HOW TO USE WORD2VEC?
# ============================================================

"""
Two approaches:

1. Pretrained Models:
   - Example: Google News Word2Vec
   - Already trained on large corpus

2. Self-Trained Models:
   - Train on your own dataset
   - Useful for domain-specific tasks
"""


# ============================================================
# 💡 INTUITION
# ============================================================

"""
Word2Vec learns meaning from context.

Example:
"I drink tea"
"I drink coffee"

→ "tea" and "coffee" will have similar vectors

Reason:
They appear in similar contexts.
"""


# ============================================================
# 🔹 TYPES OF WORD2VEC
# ============================================================

"""
1. CBOW (Continuous Bag of Words)
2. Skip-Gram
"""


# ============================================================
# 🔸 CBOW (CONTINUOUS BAG OF WORDS)
# ============================================================

"""
CBOW predicts the target word using surrounding words.

Example:
"I ___ tea" → predict "drink"

Input  → Context words
Output → Target word

Characteristics:
- Faster training
- Works well with small datasets
- Less effective for rare words
"""


# ============================================================
# 🔸 SKIP-GRAM MODEL
# ============================================================

"""
Skip-Gram does the opposite of CBOW.

It predicts surrounding words using the target word.

Example:
Input  → "drink"
Output → ["I", "tea"]

Characteristics:
- Slower than CBOW
- Works well with large datasets
- Better for rare words
"""


# ============================================================
# 🔁 CBOW vs SKIP-GRAM
# ============================================================

"""
CBOW:
- Fast
- Best for small datasets

Skip-Gram:
- Slow
- Best for large datasets
- Better for rare words
"""


# ============================================================
# ⚙️ FACTORS TO IMPROVE WORD2VEC
# ============================================================

"""
To improve model quality:

1. Increase training data
2. Increase vector dimensions (e.g., 100 → 300)
3. Increase window size (context size)
4. Increase epochs (training iterations)
"""


# ============================================================
# ⚡ ADVANCED CONCEPTS
# ============================================================

"""
- Negative Sampling → speeds up training
- Hierarchical Softmax → efficient training
- FastText → handles unseen words
- BERT/GPT → contextual embeddings (modern NLP)
"""


# ============================================================
# 🧪 TRAINING WORD2VEC (GENSIM)
# ============================================================

"""
We use Gensim library to train Word2Vec.
"""

from gensim.models import Word2Vec

# Sample dataset (tokenized sentences)
sentences = [
    ["winter", "is", "coming"],
    ["arya", "is", "strong"],
    ["jon", "snow", "is", "king"]
]

# Train Word2Vec model
model = Word2Vec(
    sentences,
    vector_size=100,   # size of word vectors
    window=5,          # context window size
    min_count=1,       # ignore words with freq < 1
    workers=4          # number of CPU cores
)

# Get vector of a word
vector = model.wv["arya"]

# Find similar words
similar_words = model.wv.most_similar("arya")

print("Vector of 'arya':", vector)
print("Similar words to 'arya':", similar_words)


# ============================================================
# 🧩 PRACTICAL EXAMPLE: GAME OF THRONES DATASET
# ============================================================

"""
Dataset:
https://www.kaggle.com/khulasasndh/game-of-thrones-books

Goal:
Train Word2Vec on GOT dataset and learn relationships between characters.
"""


# Example workflow:

"""
1. Load dataset
2. Clean text
3. Tokenize sentences
4. Train Word2Vec
5. Analyze word similarity
"""


# Expected results:

"""
- "jon" → close to "snow"
- "arya" → close to "stark"
- "king" → close to "queen"

This shows semantic understanding.
"""


# ============================================================
# 🧠 FINAL SUMMARY
# ============================================================

"""
- Word2Vec converts words into meaningful dense vectors
- Learns from context using neural networks
- Two models: CBOW and Skip-Gram
- Widely used in NLP tasks
- Foundation for modern embeddings like BERT and GPT
"""
