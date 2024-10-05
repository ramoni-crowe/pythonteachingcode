input_test = input("What are the names of people met in the last 24 hours?")
print("John has met in the last 24 hours =", 'John'.lower() in input_test.lower())

print("Ramoni has met in the last 24 hours =", 'Raamoni'.lower() in input_test.lower())

name_test = input("What name do you want to be tested?: ")
print(name_test.capitalize(),"has met in the last 24 hours =", name_test.lower() in input_test.lower())
name_test2 = input("What name do you want to be tested?: ")
print(name_test2.capitalize(),"has met in the last 24 hours =", name_test2.lower() in input_test.lower())
