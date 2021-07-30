## Lists
- contains values in a sequence w/ order
- list value means the whole list, not a think inside of it (e.g. [thing, thing2, thing3])
- inside the list there are *items*
- comma-delimited
- [] is empty like ''
- len(list) gives you number of items in list

### Get values
list[3] gets the 4th element in the list (it goes 0, 1, 2, 3)

3 is the index in this case
indexError: when you try to get an index that doesn't exist (e.g. list[99999] when there are only 3 things in the list)
indexes must be `int` and not `float` data type

if list contains other lists: 
list = \[\['hi'], \['hello', 'welcome']]
you could get 'hello' with `list[1][0]` (second list's first element, but it starts from 0)

### negative indexes
[-1] goes down from the last element (no -0)

### Slices
take certain values out of a list to get a new list
```PY
list = ['hi', 'hello', 'welcome', 'goodbye']
```
`list[1:3]` gives everything but goodbye
`list[1:-2]` gives hello and welcome

### Leaving out an int

list[3:] goes from element 4 to the end of the list
list [:3] goes from the beginning of the list to 4th element

### Change values
`list[1] = 'hi'` replaces list element in 2nd index w/ 'hi' 

### Combine a list
[1, 2, 3] + ['a', 'b', 'c'] = [1, 2, 3, 'a', 'b', 'c']

[6, 7, 8] * 3 = [6, 7, 8, 6, 7, 8, 6, 7, 8]

### remove an item
del list[x] will remove the item and shift everything over
> \>\>\> spam = ['cat', 'bat', 'rat', 'elephant']
> \>\>\>del spam[2]
> \>\>\> spam
> ['cat', 'bat', 'elephant']

you can also use `del` to just delete a variable; it will cease to exist as though it was never declared in the first place. 

### range()
range(x) = [0, 1, 2, ... x-1]
Then the for loop just loops through it!


### sort()
sort will sort numbers going up and str types in alphabetical order
--> it's ASCIIbetical not Alphabetical; A-Z then a-z
e.g. 
`["hello", "aloha", "Hi"]`
will become 
`["Hi", "aloha", "hello"]`

if you want regular alphabetical order use `sort(key=str.lower)` (treats the items like they're lowercase but doesn't make them lowercase)


it operates directly on the list 
> so use `spam.sort()` to get your list not `spam = spam.sort()`
You can't sort lists with numbers and strings. you'll get a TypeError


## Indentation

Indentation tells python what block the code is in, unless it's enclosed in [], {}, or ().
You can also \ the newline character, e.g.

```PY
 print(5 + \
5)```