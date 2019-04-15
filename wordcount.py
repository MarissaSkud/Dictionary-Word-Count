def count_words(filepath):
    text = open(filepath)

    word_count = {}

    for line in text:
        line = line.rstrip()
        words = line.split(" ")

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
    for key, value in word_count.items():
        print(f"{key} {value}")

count_words("test.txt")
