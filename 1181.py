N = int(input())
words_list = []

for _ in range(N):
    word = str(input())
    word_len = len(word)
    words_list.append((word, word_len))

words_list = list(set(words_list))
words_list.sort(key = lambda word : (word[1], word[0]))

for w in words_list:
    print(w[0])