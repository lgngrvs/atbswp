list variables are *references* to the actual list... so if you set a list to another list they will both end up referencing the same list
> >>> spam = [0, 1, 2, 3, 4, 5]
> v >>> cheese = spam
> w >>> cheese[1] = 'Hello!'
> >>> spam
> [0, 'Hello!', 2, 3, 4, 5]
> >>> cheese
> [0, 'Hello!', 2, 3, 4, 5]
from the book

basically lists have id numbers that python uses to reference them so you'll have

spam = (reference for id 'x')

reference for id 'x': [0, 1, 2, 3, 4, 5]

cheese = (reference for id 'x')

and then when you operate on spam or cheese the changes are forwarded to the list

*i hate the variable names he uses :P*

and global/local variable stuff doesn't apply in the same way either. 
```Py

greetings = ["hi", "aloha"]

def addHelloToTheOriginalList(parameter1)
    parameter1.append("Hello")

addHelloToTheOriginalList(greetings)
```
now `greetings` will return `["hi", "aloha", "Hello"]` even though the modification happened in a function