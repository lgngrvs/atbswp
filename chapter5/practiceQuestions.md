1. What does the code for an empty dictionary look like?
{}
2. What does a dictionary value with a key 'foo' and a value 42 look like?

{'foo': 42}

3. What is the main difference between a dictionary and a list?
dictionaries have keys rather than indices

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
KeyError

5. If a dictionary is stored in `spam`, what is the difference between the 
expressions 'cat' in `spam` and 'cat' in spam.keys()?
the same thing? 

6. If a dictionary is stored in spam, what is the difference between the 
expressions 'cat' in spam and 'cat' in spam.values()?
'cat' in spam checks for the existence of a key, cat in spam.values checks if there is a value


7. What is a shortcut for the following code?
if 'color' not in spam:
    spam['color'] = 'black'

spam.setdefault('color', black)

8. What module and function can be used to “pretty print” dictionary 
values?
import pprint
pprint.pprint()