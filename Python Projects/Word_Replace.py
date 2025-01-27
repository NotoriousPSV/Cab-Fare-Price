#Similar to Madlibs

print("Please choose the word you wish to replace in this sentence: Hi, my name is Philip! Nice to meet you!")

def replace_word():

    str = "Hi, my name is Philip! Nice to meet you!"
    word_to_replace = input("Please enter the word you wish to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()