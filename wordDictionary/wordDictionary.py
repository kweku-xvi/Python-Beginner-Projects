def main():
    word_dictionary = {
        'hi': 'a way of greeting',
        'eye': 'an organ for seeing',
        'earth': 'a planet in space'
    }

    
    while True:
        word = input('Enter a word: ').lower()
        if word == "":
            break
        if word in word_dictionary:
            print(word)
            print(word, ":", word_dictionary[word])


main()