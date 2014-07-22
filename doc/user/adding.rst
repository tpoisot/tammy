.. _addingref:

Adding references
=================

This page will go over how to add records to your bibliography. Creating
a new record is done through the ``new`` method of the ``library`` class
(it actually creates an object of class ``record``).  Whenever a new object
is created *by the user* (remember that one object is created for each file
in the bibliography folder when starting up), two things happen. First, the
object is checked, and a unique ``id`` (citation key) is generated. Then,
a new file is created to store this reference.

From a DOI
----------

Most *recent* papers have a Digital Object Identifier. It's a Good
Thing. Whenever you have the choice, and unless there is a special function for
the database you are querying, import things from their DOI. This is simple: ::

   >>> my_doi = 'doi.journal/xx.xxx.xxxxx'
   >>> record = tammy.from_crossref_doi(my_doi)
   >>> lib.new(record)

Note that the function is called ``from_crossref_doi``, because at the
moment, the *CrossRef* API is the easiest way to get a ``json`` output from
a DOI. Essentially, these commands will (i) get the record as a ``json``
string (it will be converted in a ``python`` object on the fly), then add
this object to the library.

From PeerJ
----------

From a file
-----------

Nothing prevents you from manually writing a reference (besides mental
sanity and a sense of priorities, that is). Any ``.yaml`` file in the
``$bib_dir/records`` will be read and parsed when the ``library`` is
created. Alternatively, you *can* do: ::

   >>> import json
   >>> with ('my/file/ref.json', 'r') as ref_file:
   ...   record = json.load(ref_file)
   >>> lib.new(record)

This will read a ``json`` file, and create a new record from it.

