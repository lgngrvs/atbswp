import sys

print("welcome to exit practice. You can practice exiting.")
while True: 
    print ("type exit and hit enter to exit")
    userInput = str(input())
    if userInput == "exit" or userInput == "Exit":
        sys.exit()
        #ends the program entirely, like break but for the whole file
    else:
        print("why did you type " + userInput)
