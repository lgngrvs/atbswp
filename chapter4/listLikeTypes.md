# things that are like lists but not

## Strings
strings are lists of characters so you can
string[x] to get the character # x-1 in the string
you can slice them, `for` through them (cool!, see funNameProgram.py)

however, you can't change a character within the string using an index
`name[x] = 'new thing'` while `name` is a string will give a TypeError

so you need to slice the characters around the character to get it to work 
`newName = name[0:x] + "replacement" + name[(x+1):]` should work if x is the character to be replaced

## Tuples
tuples are like lists but they're written with parentheses (`name = (x, y)` rather than `name = [x, y]`)

if you only have one thing in your tuple you need to do `name = ("hello",)`

use a tuple to show that you aren't going to change the thing... like constants but for lists

you can just listify and tuplify by doing `list()` on your tuple and `tuple()` on your list