from collections import defaultdict

# -----------------------------
# Training Corpus
# -----------------------------
corpus = [
    "I like NLP",
    "I like Python"
]

# -----------------------------
# Build Vocabulary
# -----------------------------
words = []

for sentence in corpus:
    words.extend(sentence.split())

vocabulary = sorted(set(words))
V = len(vocabulary)

# -----------------------------
# Count Unigrams
# -----------------------------
unigram = defaultdict(int)

for word in words:
    unigram[word] += 1

# -----------------------------
# Count Bigrams
# -----------------------------
bigram = defaultdict(int)

for sentence in corpus:
    tokens = sentence.split()

    for i in range(len(tokens) - 1):
        bigram[(tokens[i], tokens[i + 1])] += 1

# -----------------------------
# Display Vocabulary
# -----------------------------
print("Vocabulary:", vocabulary)
print("Vocabulary Size =", V)

# -----------------------------
# Display Unigram Counts
# -----------------------------
print("\nUnigram Counts")
for word, count in unigram.items():
    print(f"{word} : {count}")

# -----------------------------
# Display Bigram Counts
# -----------------------------
print("\nBigram Counts")
for pair, count in bigram.items():
    print(f"{pair} : {count}")

# -----------------------------
# Calculate MLE Probability
# -----------------------------
previous_word = "like"
next_word = "Python"

count_bigram = bigram[(previous_word, next_word)]
count_previous = unigram[previous_word]

mle = count_bigram / count_previous

# -----------------------------
# Calculate Laplace Probability
# -----------------------------
laplace = (count_bigram + 1) / (count_previous + V)

print("\nObserved Bigram: (like, Python)")
print("MLE Probability      =", round(mle, 4))
print("Laplace Probability  =", round(laplace, 4))

# -----------------------------
# Unseen Bigram Example
# -----------------------------
previous_word = "like"
next_word = "AI"

count_bigram = bigram[(previous_word, next_word)]

mle_unseen = 0

laplace_unseen = (count_bigram + 1) / (unigram[previous_word] + V)

print("\nUnseen Bigram: (like, AI)")
print("MLE Probability      =", mle_unseen)
print("Laplace Probability  =", round(laplace_unseen, 4))

# -----------------------------
# Compare Probabilities
# -----------------------------
print("\nComparison")
print("-" * 50)
print("{:<20}{:<15}{:<15}".format("Bigram", "MLE", "Laplace"))
print("-" * 50)

# Observed bigrams
for next_word in ["NLP", "Python"]:
    mle = bigram[("like", next_word)] / unigram["like"]
    laplace = (bigram[("like", next_word)] + 1) / (unigram["like"] + V)
    print("{:<20}{:<15.3f}{:<15.3f}".format(f"like {next_word}", mle, laplace))

# Unseen bigram
laplace = (bigram[("like", "AI")] + 1) / (unigram["like"] + V)
print("{:<20}{:<15.3f}{:<15.3f}".format("like AI", 0.0, laplace))