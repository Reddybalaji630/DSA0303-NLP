from collections import defaultdict

# Step 1: Read corpus
corpus = """I love NLP
I love Python
I study NLP
We study Python
You love NLP
I study Python"""

# Step 2: Tokenize text
sentences = corpus.split("\n")
tokens_list = [sentence.split() for sentence in sentences]

# Step 3: Unigram frequency
unigram_freq = defaultdict(int)
for tokens in tokens_list:
    for word in tokens:
        unigram_freq[word] += 1

# Step 4: Bigram frequency
bigram_freq = defaultdict(int)
for tokens in tokens_list:
    for i in range(len(tokens) - 1):
        bigram = (tokens[i], tokens[i+1])
        bigram_freq[bigram] += 1

# Step 5: Unigram probabilities
total_words = sum(unigram_freq.values())
unigram_prob = {}
for word in unigram_freq:
    unigram_prob[word] = unigram_freq[word] / total_words

# Step 6: Bigram probabilities (MLE)
bigram_prob = {}
for (w1, w2) in bigram_freq:
    bigram_prob[(w1, w2)] = bigram_freq[(w1, w2)] / unigram_freq[w1]

# Step 7: Display Results

print("\nUnigram Frequency")
for word, freq in unigram_freq.items():
    print(f"{word} : {freq}")

print("\nBigram Frequency")
for (w1, w2), freq in bigram_freq.items():
    print(f"{w1} {w2} : {freq}")

print("\nBigram Probabilities")
for (w1, w2), prob in bigram_prob.items():
    print(f"P({w2}|{w1}) = {prob:.2f}")

# Step 8: Check Bigram existence
def check_bigram(w1, w2):
    print(f"\nBigram: {w1} {w2}")
    if (w1, w2) in bigram_freq:
        print("Result: Bigram found in corpus.")
        print(f"P({w2}|{w1}) = {bigram_prob[(w1, w2)]:.2f}")
    else:
        print("Result: Bigram not found in corpus.")
        print(f"P({w2}|{w1}) = 0")

# Example check
check_bigram("love", "AI")
