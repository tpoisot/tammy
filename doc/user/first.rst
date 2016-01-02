.. _firststep:

First steps
===========

This page will show you the very first steps of installing and configuring
``tammy`` to your liking.

Installing ``tammy``
--------------------

``sudo make install`` - it uses ``python3``

There will be a version on ``pip``. Sometimes.

Configuration file
------------------

There are three possible locations for the configuration file. First, wherever
you feel like, as the ``library`` class accepts a ``cfile`` argument with a
path. Second, in the directory in which you are currently working. Finally,
in your ``$HOME``. Note that in the last two situations (I expect that the
later is the standard), the file *must* be called ``.tammy.yaml``.

At the moment, the only configurable options are the ``bib_dir`` and
``export_dir`` variables, which will give respectively the the roots of your
library, and where to export lists of references. By default, your library
lives in ``$HOME/.bib``. You can change it with ::

   bib_dir: $HOME/.references

Also by default, the ``export_dir`` is ``$HOME/.pandoc``, so  that the files
generated can be used directly from ``pandoc``.

When ``tammy`` will read the content of your library, it will go look for
references here. You can also specify the key format. For example, mine is ::

   bib_dir: ~/.pandoc
   export_dir: ~/.pandoc
   key:
      - "author"
      - "_"
      - "tl

Everything ``tammy``-related lives in ``~/.pandoc``, and my citation keys are
``authorname_ftl`` (first three letters).

The bib folder
--------------

For the moment, ``tammy`` will *assume* that the ``bib_dir`` folder has two
sub-folders, called ``records`` and ``files``. There is *currently* no check
for the presence of these sub-folders, so crashes are to be expected if this
is not the case. Is that poor design? For sure. Will it change? Hopefully. Is
it hard to do? Not even, no. That's just how I roll. If you think about
complaining it better be in the form of a pull request.

Creating a first library
------------------------

Whether or not you already have records on the disk, creating a bibliography
is as simple as ::

   >>> import tammy
   >>> my_lib = tammy.library()

Note that the term *creating* is misleading: your library won't be re-created
every time, because it doesn't *exist* outside of your session. Rather, the
``python`` objects that allow you to interact with it will be created. Loading
a lot of records *can* take some time, but it's a one-time thing. Future
operations are really fast.

That being said, ``tammy`` uses ``pickle`` to make sure that after the second
loading, things *are* fast. When the library is first created, a ``pickle``
file is stored. If *nothing* in the ``bib_dir`` is newer (according to the
timestamps) than the pickle file, the library will be reloaded from here. In
short: if you go and mess around manually, the library will be reloaded
from scratch. If not, it will be loaded from the pickle and you won't even
notice it.

A short note about design
=========================

.. TODO

library / record objects
