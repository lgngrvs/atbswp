def collatz(number):
    try: 
        number = int(number)
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                print(number)
            elif number % 2 == 1: 
                number = 3 * number + 1
                print(number)
                # Return will exit the funciton!
    except ValueError: 
        collatz(input("That's not a number this recognizes. Try again: "))

collatz(input("Enter a number: "))