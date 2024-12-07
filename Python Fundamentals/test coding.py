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
    
    '''
    test = input("Welcom, Ramoni. Enter a 1 sentence quote, non-alpha separate words: ")
letter_test = " "
a_test = " "
for ltr in test:
    if ltr.startswith("a"):
        a_test += ltr[:0]
    else:
        break
        #letter_test(ltr)
        
print(a_test)
    #if ltr.lower().startswith("a"):
        
        #letter_test += ltr[:0]
        a_test = ltr[:0]
        letter_test = a_test
        break
        a_test = test.append(ltr)
        letter_test += a_test
        #strlength = test.replace(" "," ")
        #letter_test = test[len(test)-strlength]        letter_test = test[0:len(test)-strlength]
        #a_test = ltr
        #letter_test = a_test[:0]
        #letter_test += ltr.replace(" ", " ")
        #print(letter_test)
        #ltr += ltr.replace(" ", " ")
        #ltr += ltr.remove("0:")

        elif ltr.lower() == "e":
        letter_test += "?"
    elif ltr.lower() == "t":
        letter_test += "?"
    else:
        letter_test += ltr
        
new_string = ""
for char in letter_test:
    if char == " ":
        new_string += " \n"
    else:
        new_string += char
        
print(new_string)
    new_name = " "
for ltr in first_name:
    if ltr.lower() == "a":
        new_name += "?"
    elif ltr.lower() == "e":
        new_name += "?"
    elif ltr.lower() == "t":
        new_name += "?"
    else:
        new_name += ltr'''
    