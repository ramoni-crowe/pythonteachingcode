def str_analysis(test = "Ramoni Crowe, please enter an integer or a word: "): 
    test = input()
    while True: 
        print("Ramoni Crowe, please enter an integer or a word: ")
        test = input()
        if test.isdigit():
            test = int(test)
            if test > 99:
                test = str(test)
                print(test+" is a big number.")
            else:
                test = str(test)
                print(test+" is a small number.")
            break
        elif test.isalpha():
            if test.isalpha():
                print("\""+test+"\", is an all alphabetical letter. ")
                break
        elif test != "":
                print("This is neither an all alphabetical or numerical input. ")
                break
  

str_analysis("")
