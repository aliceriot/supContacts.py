#Sup Addressbook

Getting the sup addressbook to work correctly proved a bit difficult.
I wanted to make my google email contacts available when composing a
mail from sup.

So, I wrote a python script which takes the output of:
    
    google contacts list --fields=name,email > sup_contacts.txt

And properly formats it, so that in sup all addresses and names in
your google contacts will autocomplete when starting a new mail.

Usage is:

    ./getContacts.sh
    python supContacts.py sup_contacts

where, as above, `sup_contacts` is the output of the [googlecl](https://code.google.com/p/googlecl/) contact
utility (`getContacts.sh` runs the necessary command). It will save a file `contacts.txt` which you can copy to your
`.sup` directory.

Note: [googlecl](https://code.google.com/p/googlecl/) is kind of strange, 
if you are sending the stdout 
to a file (as above) you need to hit enter once more after executing
the command, it is waiting on some input (Please specify title) and
will not start printing contacts until you do so.

Happy supping!
