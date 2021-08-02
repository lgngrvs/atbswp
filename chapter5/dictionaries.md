```py
dictionaryName = {"key": "value"}
dictionaryName["key"]
# value
```
Dictionaries are not ordered, so you can use integer values for keys but can't find values via index e.g. `dictionaryName[0]` will not return `value`
order thus does not matter when comparing two lists; as long as the key-value pairs are the same, you're good

## ok, from now on I am going to skip stuff that I don't need to write down. Exhaustive notes don't matter when stackOverflow and my Brain are enough -- and programming is not like writing papers. 

check if a value exists in a dictionary: `if <key> in <dictionary>:`

get list of keys/values/both wih keys() values() and items()
iterate over both with `for k, v, in <dictionary>`

get(value for 'key', fallback value to use if nothing gotten)
setdefault(key to set, value to set unless key already exists) so that you don't get `KeyError`s

```py
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)
# p 110
```
## pretty printing
import pprint
- pprint (prints, even with nested dictionaries or lists)
- pformat (gives as a string)
print dictionary values with newlines for each set

```py
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests, item):
    numBrought = 0
u     for k, v in guests.items():
v         numBrought = numBrought + v.get(item, 0)
    return numBrought
print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies'))
```
^^ a nice example of getting stuff out of nested dictionaries (118)