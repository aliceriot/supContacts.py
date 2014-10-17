#Sup Addressbook

Getting the sup addressbook to work correctly is a pain in the ass.

So, I wrote a python script which takes the output of
    
    google contacts list --fields=name,email > sup_contacts.txt

And properly formats it, so that you can just call

    python supContacts.py sup_contacts

and it will save a file `contacts.txt` which you can copy to your
sup directory.

Note: googlecl is kind of strange, if you are sending the stdout 
to a file (as above) you need to hit enter once more after executing
the command, it is waiting on some input (Please specify title) and
will not start printing contacts until you do so.

Happy supping!
