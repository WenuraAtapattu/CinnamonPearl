import string

# Common stop words to ignore
stop_words = ["the", "and", "of", "in", "a", "to"]

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def analyze_text(text):
    word_freq = {}
    
    # Tokenize the input text into words
    words = text.lower().split()
    
    for word in words:
        word = remove_punctuation(word)
        if word not in stop_words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    
    least_freq_words = sorted(word_freq.items(), key=lambda x: x[1])[:5]
    
    return least_freq_words

# Prompt user to input a paragraph of text
paragraph = input("Enter a paragraph of text: ")

least_freq_words = analyze_text(paragraph)

print("Top 5 least frequently used words and their counts:")
for i, (word, count) in enumerate(least_freq_words, 1):
    print(f"{i}. {word}: {count} time" if count == 1 else f"{i}. {word}: {count} times")