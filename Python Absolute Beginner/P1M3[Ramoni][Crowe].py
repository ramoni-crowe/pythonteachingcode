
print("Please give a number: ")
num_one = int(input())
print("Please give another number: ")
num_two = int(input())

if num_one == 0:
    print("Don't divide by zero!")
elif num_two == 0:
    print("Don't divide by zero!")
elif num_one > num_two:
    sum = num_one / num_two
    print(int(sum))
elif num_two > num_one:
    sum = num_two / num_one
    print(int(sum))
else:
    print("Something went wrong!")