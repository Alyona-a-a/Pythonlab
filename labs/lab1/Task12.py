stroka = input("Введите текст: ").lower()
stroka = stroka.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace("-", " ").replace(";", " ").replace('"', " ").replace(':', " ")
words = stroka.split() 
print("Слова по отдельности",words)
count = 0
for word in words:
    count += 1
print("Количество слов:",count)
print("Частота слов:")
for word in words:
    count_word = words.count(word)
    print(word, ":", count_word)

max_count = 0
most_common = ""
for word in words:
    if words.count(word) > max_count:
        max_count = words.count(word)
        most_common = word
print("Самое частое:", most_common)

shortest = words[0]
longest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
    if len(word) > len(longest):
        longest = word
print("Самое короткое:", shortest)
print("Самое длинное:", longest)

new_words = []
for word in words:
    if len(word) >= 3:
        new_words.append(word)
print("Слова от 3 букв:", new_words)