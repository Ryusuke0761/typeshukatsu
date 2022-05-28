for num in range(1, 101):
    string = ''

    if num % 15 == 0:
        string = "FizzBuzz"
    elif num % 5 == 0:
        string = "Buzz"
    elif num % 3 == 0:
        string = "Fizz"
    else:
        string = num
    print(string)
