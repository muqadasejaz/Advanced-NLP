# ============================================================
# 📌 PART OF SPEECH (POS) TAGGING
# ============================================================

"""
POS Tagging (Part-of-Speech Tagging) is a fundamental NLP task
where each word in a sentence is assigned its grammatical label.

Example:
Sentence: "She runs fast"

She   → Pronoun
runs  → Verb
fast  → Adverb
"""


# ============================================================
# 📌 WHERE IS POS TAGGING USED?
# ============================================================

"""
POS tagging is used in:

1. Information Retrieval Systems (Search Engines)
2. NLP Pipelines (as a preprocessing step)
3. Chatbots
4. Text Analysis Systems
5. Machine Translation
"""


# ============================================================
# 📌 WHAT IS POS TAGGING?
# ============================================================

"""
Simple Definition:

POS Tagging is the process of assigning each word in a sentence
its correct part of speech.

Example:
"I love NLP"

I     → Pronoun
love  → Verb
NLP   → Noun
"""


# ============================================================
# 📌 APPLICATIONS OF POS TAGGING
# ============================================================

"""
- Named Entity Recognition (NER)
- Question Answering Systems
- Word Sense Disambiguation
- Chatbots
- Grammar Checking
"""


# ============================================================
# 📌 TYPES OF POS TAGGING
# ============================================================

"""
1. Coarse-Grained POS Tagging:
   - General categories
   Example: Noun, Verb, Adjective

2. Fine-Grained POS Tagging:
   - Detailed tags
   Example:
   NNP → Proper Noun
   VBD → Past tense verb
"""


# ============================================================
# 📌 SEQUENCE MODELING IN POS TAGGING
# ============================================================

"""
POS tagging is a sequence modeling problem.

Why?
Because the tag of a word depends on:
- The word itself
- The previous words (context)

Example:
"can" → noun or verb depending on context

So we model sequences instead of independent words.
"""


# ============================================================
# 📌 HIDDEN MARKOV MODEL (HMM)
# ============================================================

"""
HMM is a probabilistic model used for sequence modeling.

In POS tagging:

- Hidden states → POS tags
- Observations → Words

Goal:
Find the most probable sequence of POS tags
for a given sentence.
"""


# ============================================================
# 📌 HOW HMM WORKS?
# ============================================================

"""
Steps:

1. Tag training dataset with POS labels

2. Calculate Emission Probability:
   P(word | tag)
   → Probability of word given a tag

3. Calculate Transition Probability:
   P(tag_t | tag_t-1)
   → Probability of current tag given previous tag

4. Add START and END states

5. Build HMM model
"""


# ============================================================
# 📌 PROBLEM: EXPONENTIAL COMPLEXITY
# ============================================================

"""
Problem:

For a sentence of length n with k tags:
Total combinations = k^n

Example:
5 words, 10 tags → 10^5 = 100,000 combinations

Very slow and inefficient.
"""


# ============================================================
# 📌 SOLUTION: VITERBI ALGORITHM
# ============================================================

"""
Viterbi Algorithm is a dynamic programming algorithm
used to find the most probable sequence of tags efficiently.

Key Idea:
Instead of checking all paths,
store only the best path at each step.
"""


# ============================================================
# 📌 VITERBI ALGORITHM (INTUITION)
# ============================================================

"""
Sentence: "Time flies fast"

Possible tags:
Time  → Noun / Verb
flies → Noun / Verb
fast  → Adjective / Adverb

Goal:
Find best tag sequence.
"""


# Step-by-step process:

"""
Step 1:
Initialize probabilities using START state

Step 2:
For each word:
- Compute:
  previous_score × transition_prob × emission_prob

Step 3:
Store best score and path (dynamic programming)

Step 4:
Backtrack to get final sequence
"""


# Example (simplified probabilities):

"""
Emission:
P(Time | Noun) = 0.6
P(Time | Verb) = 0.4

Transition:
P(Noun → Verb) = 0.5
P(Verb → Adverb) = 0.6
"""

# Final Output:
"""
Time  → Noun
flies → Verb
fast  → Adverb
"""


# ============================================================
# 📌 WHY VITERBI IS IMPORTANT?
# ============================================================

"""
- Reduces complexity from exponential → polynomial
- Efficient for sequence prediction
- Used in:
  - POS Tagging
  - Speech Recognition
  - DNA sequence analysis
"""


# ============================================================
# 📌 PRACTICAL IMPLEMENTATION (NLTK)
# ============================================================

"""
Basic POS tagging using NLTK
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

sentence = "She enjoys reading books"

words = word_tokenize(sentence)
tags = pos_tag(words)

print(tags)


# ============================================================
# 📌 ADVANCED APPROACHES
# ============================================================

"""
Modern POS tagging methods:

1. Conditional Random Fields (CRF)
   - Better than HMM (no independence assumption)

2. BiLSTM (Bidirectional LSTM)
   - Uses past and future context

3. Transformers (BERT, RoBERTa)
   - Contextual embeddings
   - State-of-the-art performance
"""


# ============================================================
# 📌 MORE ADVANCED CONCEPTS
# ============================================================

"""
1. Contextual POS Tagging:
   - Same word → different tags depending on context

2. Transfer Learning:
   - Fine-tune pretrained models like BERT

3. Subword Tokenization:
   - Handles unknown words

4. Multilingual POS Tagging:
   - Works across multiple languages

5. Domain Adaptation:
   - Adapt POS models to specific domains (medical, legal)

6. Error Analysis:
   - Analyze confusion between tags

7. Real-Time POS Tagging:
   - Optimized for fast inference in production systems
"""


# ============================================================
# 📌 FINAL SUMMARY
# ============================================================

"""
- POS tagging assigns grammatical labels to words
- It is a sequence modeling problem
- HMM is a classical probabilistic method
- Viterbi algorithm solves efficiency issue
- Modern NLP uses deep learning (BiLSTM, Transformers)
"""
