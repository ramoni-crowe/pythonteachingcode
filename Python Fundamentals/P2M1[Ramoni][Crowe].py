def extract_words_after_g():
    box = input("Enter a 1 sentence quote non-alpha seperate words: ")
    word = ""
    
    for char in box:
        if char.isalpha():
            word += char
        else:
            if word and word[0].lower() >= 'h':  
                print(word)
            word = ""
            
    if word and word[0].lower() >= 'h':  
        print(word)


extract_words_after_g()