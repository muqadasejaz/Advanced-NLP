# ============================================================
# Text Representation (Feature Extraction)
# ============================================================


## 1. What is Feature Extraction from Text?

Feature extraction from text is the process of converting textual data into numerical form (vectors) so that machine learning models can understand it.

It is also called:
- Feature Representation  
- Text Vectorization  

---

## 2. Why Do We Need It?

Machine learning models cannot understand raw text. They only work with numbers.

A simple rule:

> **Garbage in = Garbage out**  
> Poor input features → Poor model performance  

So, good feature extraction is critical for building accurate models.

---

## 3. Why is it Difficult?

Feature extraction from text is more difficult compared to images or structured data because:

- Text is unstructured  
- Words can have multiple meanings (ambiguity)  
- Context matters a lot  
- Same meaning can be expressed in different ways  
- Language is highly flexible and complex  

---

## 4. What is the Core Idea?

The main goal is:

> When we convert text into numbers, those numbers should represent the **meaning (semantics)** of the text.

---

## 5. Techniques for Text Representation

### 🔹 Traditional Methods
- One-Hot Encoding  
- Bag of Words (BoW)  
- N-Grams  
- TF-IDF  
- Custom Features  

### 🔹 Deep Learning Methods
- Word Embeddings (Word2Vec, GloVe, FastText)  

---

## 📖 Common Terms

- **Corpus (C)** → Collection of all documents  
- **Vocabulary (V)** → Unique words in the corpus  
- **Document (D)** → A single text/sample  
- **Word (W)** → Individual token in a document  

---

## 🔹 1. One-Hot Encoding

Each word is converted into a vector of size equal to the vocabulary.

### Example:
If vocabulary = `["I", "love", "NLP"]`

"I" → [1, 0, 0]
"love" → [0, 1, 0]
"NLP" → [0, 0, 1]


###  Advantages
- Simple and easy to understand  
- Easy to implement  

###  Disadvantages
- Sparsity (most values are 0)  
- High dimensionality  
- Out-of-Vocabulary (OOV) problem  
- No semantic meaning  

---

## 🔹 2. Bag of Words (BoW)

Counts how many times each word appears in a document.

### Ignores:
- Word order  
- Context  

### Example:
Sentence 1: *"This movie is good"*  
Sentence 2: *"This movie is bad"*  

Both look similar due to similar word frequency.

###  Advantages
- Simple and intuitive  
- Works well for text classification  
- No fixed input size issue  

###  Disadvantages
- Sparsity  
- OOV problem  
- No context understanding  

---

## 🔹 3. N-Grams

N-Grams consider combinations of words.

- Unigram → single word  
- Bigram → two words  
- Trigram → three words  

### Example:
"This movie is good" →  
Bigrams: `["this movie", "movie is", "is good"]`

###  Advantages
- Captures some context  
- Helps differentiate similar sentences  

###  Disadvantages
- High dimensionality  
- Slower computation  
- OOV problem  

---

## 🔹 4. TF-IDF (Term Frequency – Inverse Document Frequency)

TF-IDF assigns importance (weight) to each word.

###  Formula

**TF (Term Frequency):**

TF(t, d) = (Number of times term t appears in document d)
/ (Total number of terms in document d)


**IDF (Inverse Document Frequency):**

IDF(t) = log (Total number of documents / Number of documents containing term t)


###  Final Value:

TF-IDF = TF × IDF



### 🔍 Key Idea
- Common words → low importance  
- Rare words → high importance  

###   Advantages
- Better than BoW  
- Useful in search engines  

###  Disadvantages
- Sparse representation  
- High dimensionality  
- OOV problem  
- Limited semantic understanding  

---

## 🔹 5. Custom Features

Manually created features based on problem.

### Examples:
- Number of positive words  
- Number of negative words  
- Sentence length  
- Number of exclamation marks  

###  Advantages
- Task-specific improvements  
- Can boost performance  

###  Disadvantages
- Requires domain knowledge  
- Time-consuming  

---

## 🔹 6. Deep Learning Approaches (Word Embeddings)

Embeddings capture meaning instead of just counts.

Words with similar meanings have similar vectors.

### Examples:
- Word2Vec  
- GloVe  
- FastText  

###  Advantages
- Capture semantic meaning  
- Dense representation  
- Better performance  

###  Disadvantages
- Requires more data  
- Computationally expensive  
- Harder to interpret  

---

##  Final Summary

| Method      | Captures Meaning | Handles Context | Sparse |
|------------|-----------------|----------------|--------|
| One-Hot    |   No           |   No          |  Yes |
| BoW        |   Limited      |   No          |  Yes |
| N-Grams    |   Partial      |   Partial     |  Yes |
| TF-IDF     |   Better       |   No          |  Yes |
| Embeddings |   Yes          |   Yes         |  No  |
