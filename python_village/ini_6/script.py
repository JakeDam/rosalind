string = "'
word_dict = {}

words = string.split(' ')

for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

for word, count in word_dict.items():
    print(word + ' '+ str(count))
