# -*- coding: utf-8 -*-

"""
For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin

>>> Benjamin Franklin's birthday is 01/17/1706.
"""
import json
from collections import Counter

months_dict = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
    }

birthdays = {
	"Albert Einstein": "03/14/1879",
	"Ada Byron Lovelace": "12/10/1815",
	"Benjamin Franklin": "01/17/1706"
}


months = []
bdays = []


with open('bday.json', 'w') as f:
    json.dump(birthdays, f)

with open('bday.json', 'r') as f:
    bday_dict = json.load(f)

print('Welcome to the birthday dictionary. We know the birthdays of: ')

while True:
    with open('bday.json', 'r') as f:
        bday_dict = json.load(f)

    for i in bday_dict:
        print(i)
    
    cmd = raw_input('1) Enter a scientist\'s name, 2) \'add\' to add a scientist or type 3) \'exit\' to quit: ')
    if cmd == 'exit':       
        break
    elif cmd == 'add':
        name_to_add = raw_input('Enter a scientist\'s name to add to the list: ')
        birthday_to_add = raw_input('Enter a birthday to correspond to the scientist: ')
        birthdays.update({name_to_add : birthday_to_add})
        with open('bday.json', 'w') as f:
            json.dump(birthdays, f)
    else:
        print('%s\'s birthday is %s' % (cmd, bday_dict[cmd]))



for i in bday_dict:
    bdays.append(str(bday_dict[i]))

for i in bdays:
    months.append(months_dict[i[0:2]])

m = Counter(months)

mon = dict(m)

print(mon)






"""
print('Welcome to the birthday dictionary. We know the birthdays of: ')
for i in birthdays.keys():
    print(i)

name = raw_input('Who\'s birthday do you want to look up?')
print('%s\'s birthday is %s' % (name, birthdays[name]))
"""
