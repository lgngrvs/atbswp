def functionName(argument): 
    internalCode = 'This new function will return'
    resultOfCode = ' whatever the return says it shoud.'
    return internalCode + resultOfCode

print(functionName('hello'))
# None is the only value of the NoneType data type.
# it's like null or undefined
#it's what things return if no return is specified
'''
def exampleCode():
    return None
'''
# print() has return None at the end
# it also has keyword arguments `end` and `sep`
# so if you print("hi",end='') and then print("world")
# you'll get hiworld because print automatically adds a
# newline character. 
# print("thing1", "thing2", "thing3", sep=".")
# gives > thing1.thing2.thing3
# keyword args can be passed to custom functions as
# well but wait for chapter 4 & 5
