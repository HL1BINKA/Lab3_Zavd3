rechennya=str(input("Введіть речення: "))
words=rechennya.split(" ")
for word in words:
    if word.count('е')==3:
        print(word)