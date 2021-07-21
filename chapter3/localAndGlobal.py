# global [var] to modify a global var

greeting = 'hi'

def changeGreeting(): 
    global greeting
    print("old greeting: " + greeting)
    greeting = 'new greeting: hello'

changeGreeting()
print(greeting)