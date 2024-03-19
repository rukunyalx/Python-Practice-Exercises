def count_word_occurrences(text):
    words = text.split()
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

text = "hello world, hello world! This is a hello world example"
print(count_word_occurrences(text))