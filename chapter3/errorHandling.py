# an error right now means that the whole thing will crash
# handle with a try/except statement
'''
def divideBy(number):
    return 50 / number

print(divideBy(3))
print(divideBy(4))
print(divideBy(0))
'''
#gives divisionBy0Error
# instead do 

def divideBy(number):
    try: 
        return 50 / number
        #if you got an error by calling another function here, though, you'd get an error.
    except ZeroDivisionError: 
        print("You can't divide by 0.")

print(divideBy(3))
print(divideBy(4))
print(divideBy(0)) 
print(divideBy(5))