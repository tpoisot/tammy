.. _firststep:

First steps
===========

This page will show you the very first steps of installing and configuring ``tammy`` to your liking.

Installing ``tammy``
--------------------

Configuration file
------------------

At the moment, there is only one configuration option. The configuration
file must be stored at ``$HOME/.tammy.yaml``. The ``bib_dir`` variable will
give the root of your library. By default, this is ``$HOME/.bib``. You can
change it with ::

   bib_dir = $HOME/.references

When ``tammy`` will read the content of your library, it will go look for
configuration options here.

Creating a first library
------------------------

Whether or not you already have records on the disk, creating a bibliography is as simple as

::

   >>> import tammy
   >>> my_lib = tammy.new()

Note that the term *creating* is misleading: your library won't be re-created
every time; the ``python`` objects that allow you to interact with it,
on the other hand, will be.
