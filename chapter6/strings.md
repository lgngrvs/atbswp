make strings with 
'hello'
'this\'s logan'
'making a \n new line'
or just use double quotes for the backslash e.g.
"this's logan"

\t does a tab btw

## Raw strings
print(r'That\'s mine!')
the backslash still works but it will print as `That\'s mine!`

## multiline strings
'''String

string's string

string''' prints with these newlines (and don't worry about that `'`)

It's common to use these for multiline comments cause they'll just be ignored.

## in
'hello' in 'hello world' # true
'' in 'hello world' # true
case sensitive

## upper lower isupper islower
return the string altered to fit that (e.g. print("string".upper()) will give STRING)
isupper/lower gives whether all characters are upper or lower (if there aren't any letters it's false)

> Here are some common isX 
> string methods:
> •  isalpha() returns True if the string consists only of letters and is not blank.
> •  isalnum() returns True if the string consists only of letters and numbers and is not blank.
> •  isdecimal() returns True if the string consists only of numeric characters and is not blank.
> •  isspace() returns True if the string consists only of spaces, tabs, and newlines and is not blank.
> •  istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

good for data validation

## startswith and endswith
self-explanatory, like == but for the beginning or end


## join() split()
cats a list of strings but the syntax is kinda weird
```py
" ".join(["List", "values", "go", "here"])
```
you call the method on the string you want to use to stick all the strings together

split... is even weirder
```py
stringToSplit.split(thingToRemoveAndSplit)
```
if you pass it with no params it'll split by any whitespace character lol

## justifies

pushes string to the right: string.rjust(amount, character to justify with [default is ' '])
pushes string to the left with string.ljust
string.center, same syntax but it just rjust and ljust on both sides

done at pg. 134 for the day