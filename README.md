#Sup Addressbook

Getting the sup addressbook to work correctly is a pain in the ass.

So, I wrote a python script which takes the output of
    
    google contacts list --fields=name,email > sup_contacts

And properly formats it, so that you can just call

    supContacts.py sup_contacts

and it will save a file `contacts.txt` which you can copy to your
sup directory.

Happy supping!
