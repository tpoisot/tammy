.. _firststep:

First steps
===========

This page will show you the very first steps of installing and configuring
``tammy`` to your liking.

Installing ``tammy``
--------------------

.. TODO

Configuration file
------------------

There are three possible locations for the configuration file. First, wherever
you feel like, as the ``library`` class accepts a ``cfile`` argument with a
path. Second, in the directory in which you are currently working. Finally,
in your ``$HOME``. Note that in the last two situations (I expect that the
later is the standard), the file *must* be called ``.tammy.yaml``.

At the moment, the only configurable option is the ``bib_dir`` variable, which
will give the root of your library. By default, this is ``$HOME/.bib``. You
can change it with ::

   bib_dir = $HOME/.references

When ``tammy`` will read the content of your library, it will go look for
references here. Over time, I will add options for the default citation key
format (currently ``AutYr``), and things related to the maybe-coming-soon
``ncurses`` interface.

The bib folder
--------------

For the moment, ``tammy`` will *assume* that the ``bib_dir`` folder has two
sub-folders, called ``records`` and ``files``. There is *currently* no check
for the presence of these sub-folders, so crashes are to be expected if this
is not the case. Is that poor design? For sure. Will it change? Hopefully. Is
it hard to do? Not even, no. That's just how I roll.

Creating a first library
------------------------

Whether or not you already have records on the disk, creating a bibliography
is as simple as::

   >>> import tammy
   >>> my_lib = tammy.library()

Note that the term *creating* is misleading: your library won't be re-created
every time, because it doesn't *exist* outside of your session. Rather, the
``python`` objects that allow you to interact with it will be created. Loading
a lot of records *can* take some time, but it's a one-time thing. Future
operations are really fast.
