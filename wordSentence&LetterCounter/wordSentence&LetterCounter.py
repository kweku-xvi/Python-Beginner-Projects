passage = ""

def letter_counter():
    letterCount = 0
    letter = input("Enter the letter you want to count it's number of appearances: ").lower()

    for i in range(len(passage)):
        if passage[i] == letter:
            letterCount += 1
    print(f"Your letter appeared {letterCount} times in the sentence.")


def word_counter():
    wordCount = 0
    word = input("Enter the word you want to count it's number of occurence: ").lower()

    splittheInput = passage.split()
    for i in splittheInput:
        if i == word:
            wordCount += 1
    print(f"Your word appeared {wordCount} times in the sentence")


def sentence_counter():
    sentenceCount = 0
    sentence = input("Enter the sentence you want to count it's number of occurence: ").lower()
    
    theInputSplit = passage.split(".")
    for i in theInputSplit:
        if i == sentence:
            sentenceCount += 1
    print(f"Your sentences appeared {sentenceCount} times in the passage.")


while True:
    print("""
    Welcome to the letter, word & sentence counter!
    L - for letter
    W - for word
    S - for sentence 
    E - to exit
    """)

    objectToCount = input("Input choice: ").upper()


    if objectToCount == 'L':
        passage = input("Enter your sentence: ").lower()
        letter_counter()
    elif objectToCount == 'W':
        passage = input("Enter your sentence: ").lower()
        word_counter()
    elif objectToCount == 'S':
        passage = input("Enter your passage: ").lower()
        sentence_counter()
    elif objectToCount == 'E':
        print("Thanks for using my word, sentence & letter counter!")
        exit()
    else:
        print("Invalid input entered try again!")