word_to_count = {}
text = input("pls enter the text:")
words = text.split()
for word in words:
    f = word_to_count.get(word, 0)
    word_to_count[word] = f + 1
words = list(word_to_count.keys())
for word in words:
    print("{} : {}".format(word, word_to_count[word]))