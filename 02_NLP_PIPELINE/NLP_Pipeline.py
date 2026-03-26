# ============================================================
# 1. WHAT IS AN NLP PIPELINE?
# ============================================================

"""
An NLP pipeline is a sequence of steps used to build,
train, evaluate, and deploy a Natural Language Processing system.

It transforms raw text into meaningful insights or predictions.

Typical pipeline stages:

1. Data Acquisition
2. Text Preparation
3. Feature Engineering
4. Modeling
5. Evaluation
6. Deployment
7. Monitoring & Continuous Improvement
"""


# ============================================================
# 2. DATA ACQUISITION
# ============================================================

"""
In real-world projects, data availability usually falls into three cases:

1. Data is already available
2. Data is available externally
3. Data is not available
"""


# ------------------------------------------------------------
# Case 1: Data is Available
# ------------------------------------------------------------

"""
Data sources:
- CSV / Excel files
- Databases (SQL / NoSQL)
- Internal company storage

Best practices:
- Use SQL queries for efficient extraction
- Validate data quality (missing values, duplicates)
- Perform exploratory data analysis (EDA)

If data is small:
→ Use data augmentation techniques
"""


# ----------------------
# Data Augmentation
# ----------------------

"""
Techniques:
- Synonym replacement
- Back translation (e.g., English → French → English)
- Random insertion/deletion
- Noise injection
- Paraphrasing

Advanced:
- Contextual augmentation using transformers

Tools:
- nlpaug
- TextAttack
- HuggingFace datasets
"""


# ------------------------------------------------------------
# Case 2: Data is Available Elsewhere
# ------------------------------------------------------------

"""
Sources:

1. Public Datasets:
   - Kaggle
   - HuggingFace Datasets
   - UCI Repository

2. Web Scraping:
   - BeautifulSoup
   - Scrapy

3. APIs:
   - REST APIs
   - RapidAPI

4. Multi-format Data:
   - PDF → pdfplumber, PyPDF2
   - Images → OCR (Tesseract)
   - Audio → Speech-to-text (Whisper)

Advanced:
- Use data pipelines (Airflow, Prefect) for automation
"""


# ------------------------------------------------------------
# Case 3: Data is Not Available
# ------------------------------------------------------------

"""
Solutions:
- Create surveys or feedback forms
- Collect user-generated data
- Use crowdsourcing platforms
- Generate synthetic data (carefully)

Advanced:
- Use LLMs to generate synthetic datasets
- Active learning for efficient labeling
"""


# ============================================================
# 3. TEXT PREPARATION
# ============================================================

"""
Text preparation converts raw text into a clean format.

Stages:
1. Basic Cleaning
2. Basic Preprocessing
3. Advanced Preprocessing
"""


# ------------------------------------------------------------
# 3.1 Basic Cleaning
# ------------------------------------------------------------

"""
Tasks:
- Remove HTML tags
- Remove URLs
- Remove emojis (or convert to meaning)
- Unicode normalization
- Spelling correction
"""

import re

def remove_html(text):
    return re.sub(r'<.*?>', '', text)


# ------------------------------------------------------------
# 3.2 Basic Preprocessing
# ------------------------------------------------------------

"""
Includes:
- Lowercasing
- Tokenization (word/sentence)
- Stopword removal (optional)
- Stemming / Lemmatization
- Removing digits
- Language detection
"""

from nltk.tokenize import word_tokenize

def tokenize_text(text):
    return word_tokenize(text)


from nltk.corpus import stopwords

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [w for w in tokens if w.lower() not in stop_words]


# ------------------------------------------------------------
# 3.3 Advanced Preprocessing
# ------------------------------------------------------------

"""
Advanced steps:
- Handling negation (e.g., "not good")
- Handling slang and chat words
- Named Entity normalization
- Coreference resolution
- Text normalization for multilingual data

Advanced tools:
- spaCy
- HuggingFace tokenizers
"""


# ============================================================
# 4. FEATURE ENGINEERING (TEXT REPRESENTATION)
# ============================================================

"""
Convert text into numerical form.

Traditional methods:
- Bag of Words (BoW)
- TF-IDF
- N-grams

Dense representations:
- Word2Vec
- GloVe
- FastText

Modern:
- Contextual embeddings (BERT, RoBERTa)
"""

from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf_vectorize(corpus):
    vectorizer = TfidfVectorizer()
    return vectorizer.fit_transform(corpus)


# ============================================================
# 5. MODELING
# ============================================================

"""
Model selection depends on:
- Data size
- Task (classification, generation, etc.)
- Available compute
"""


# ------------------------------------------------------------
# Traditional ML Models
# ------------------------------------------------------------

"""
Best for small datasets:
- Logistic Regression
- Naive Bayes
- SVM
- Random Forest
"""


# ------------------------------------------------------------
# Deep Learning Models
# ------------------------------------------------------------

"""
Best for large datasets:
- RNN, LSTM, GRU
- CNN for text
- Transformers (BERT, GPT)
"""


# ------------------------------------------------------------
# Modern Approach (Pretrained Models)
# ------------------------------------------------------------

"""
Use pretrained models and fine-tune:

Advantages:
- Requires less data
- High accuracy

Examples:
- BERT for classification
- GPT for generation
"""


# ============================================================
# 6. EVALUATION
# ============================================================

"""
Evaluation measures model performance.
"""


# ------------------------------------------------------------
# Intrinsic Evaluation
# ------------------------------------------------------------

"""
Metrics:
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Perplexity (language models)
"""


# ------------------------------------------------------------
# Extrinsic Evaluation
# ------------------------------------------------------------

"""
Business-level evaluation:
- Does it improve user experience?
- Does it solve the real problem?
"""


# ============================================================
# 7. DEPLOYMENT
# ============================================================

"""
Deploy the model so users can interact with it.

Methods:
- REST API (Flask / FastAPI)
- Web apps (Streamlit)
- Cloud deployment (AWS, GCP, Azure)
"""


# ------------------------------------------------------------
# Production Considerations
# ------------------------------------------------------------

"""
- Latency (response time)
- Scalability
- Security
- Logging
"""


# ============================================================
# 8. MONITORING & CONTINUOUS LEARNING
# ============================================================

"""
After deployment, continuously monitor the system.
"""


# ------------------------------------------------------------
# Monitoring
# ------------------------------------------------------------

"""
Track:
- Model drift (model performance drops)
- Data drift (input distribution changes)
- Latency and errors
"""


# ------------------------------------------------------------
# Updating
# ------------------------------------------------------------

"""
- Retrain model periodically
- Fine-tune with new data
- Use feedback loops

Advanced:
- MLOps pipelines
- CI/CD for ML
- A/B testing
"""


# ============================================================
# 9. MODERN NLP PIPELINE (LLM-BASED)
# ============================================================

"""
Modern pipelines often include:

- Pretrained LLM (GPT, BERT)
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- Vector Databases (FAISS, Pinecone)

Pipeline:
User Query → Retriever → Context → LLM → Response
"""
