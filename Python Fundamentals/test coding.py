def words_after_g(quote = "enter a 1 sentence quote, non-alpha separate words: "):
    start = 0
    #space_index = quote.find(" ")
    filtered_quote = " "
    print("What is your quote: ")
    quote = input()
    while start < len(quote):
        space = quote.find('', start)
        if space == -1:
            space = len(quote)
            
        word = quote[start:space]
        
        if word[0].lower() in "abcdefg" == False:
            filtered_quote += word + " " 
            
        start = space + 1 
    print(filtered_quote.strip())