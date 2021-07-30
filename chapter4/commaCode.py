# Write a function that takes a list value as an 
# argument and returns 
# a string with all the items separated by a 
# comma and a space, with and 
# inserted before the last item. 

def commaAdder(listValue):
    mainStr = ''
    listIndex = 0 
    for entry in listValue:
        if listIndex == len(listValue) - 1:
            mainStr += str(entry) + ' '
        elif listIndex == len(listValue) - 2: 
            mainStr += str(entry) + ', and '
        elif listIndex != len(listValue) - 2:
            mainStr += str(entry) + ', '
        listIndex = listIndex + 1
    return mainStr

greetings = ["Hello", "aloha", "hi"]
print(commaAdder(greetings))