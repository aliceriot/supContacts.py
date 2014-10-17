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










