#!/usr/bin/python

import sys






handle = sys.argv[1]

with open(handle) as myfile:
    rawContacts = myfile.read().split('\n')



def supFormat(line):
    """
    we call this on one line of the file at a time
    """
    elements = line.split(',')
    name = elements[0]
    email = ''.join([x for x in elements[1].split(' ') if '@' in x])
    return name + ': ' + name + ' ' + '<' + email + '>' + '\n'

    





betterContacts = ""

for i in range(1,len(rawContacts)-1):
    line = rawContacts[i]
    if '@' in line:
        if ';' in line:
            emails = line.split(';')
            weird_ones = emails[1:]
            betterContacts += supFormat(emails[0])
            name = ' '.join([x for x in supFormat(emails[0]).split(' ') if '@' not in x])
            for j in weird_ones:
                email = '<' + ' '.join([x for x in j.split(' ') if '@' in x]) + '>'
                entry = name + ': ' + name + ' ' + email + '\n'
                betterContacts += entry
        else:
            betterContacts += supFormat(line)


with open("contacts.txt",'w') as writefile:
    writefile.write(betterContacts)


# Copyright (C) 2014 Benjamin Pote

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.







