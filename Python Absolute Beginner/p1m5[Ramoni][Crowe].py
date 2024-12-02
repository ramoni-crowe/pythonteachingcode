def adding_report(report = print("Which report would you like to show? (A or T): ")):
    num_string = "" 
    total = 0
    report = input()
    if report.lower() == "a":
        print("Input an integer to add to the total or \"Q\" to quit: ")

        while True:
            numb = input()
            print("Enter an integer or \"Q\": ",numb)
            if numb.isalpha():
                print("This is not an invalid number") 
            num_string = num_string + str(numb) + "\n"    
            if numb == "q":
                print("Quit")
                break
            
            if numb.isdigit():
                total += int(numb) 
        
        print("Items\n",num_string)  
        print("Total\n",total,"\nCalculated by: Ramoni Crowe") 
         
      
    elif report.lower() == "t":
        print("Input an integer to add to the total or \"Q\" to quit: ")
        while True:
            numb = input()
            print("Enter an integer or \"Q\": ",numb)
            if numb == "q":
                break
            if numb.isdigit():
                total += int(numb) 
        print("Total\n",total,"\nCalculated by: Ramoni Crowe")    
            
              
        
        
adding_report(" ")