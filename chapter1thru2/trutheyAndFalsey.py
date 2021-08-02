# "There are some values in other data types that 
# conditions will consider equivalent to True and False. 
# When used in conditions, 0, 0.0, and '' 
# (the empty string) are considered False, 
# while all other values are considered True."

name = ''
while not name: # while name str (which would normally be false because it is empty) is empty (this makes it true)
    print('Enter your name:')
    name = input() # set name
print('How many guests will you have?')
numOfGuests = int(input()) #intify the amount
if numOfGuests: # if you are going to have ANY guests (0 (the int) is falsey)
    print('Be sure to have enough room for all your guests.')
print('Done')