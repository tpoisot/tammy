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

   - bib_dir = $HOME/.references

When ``tammy`` will read the content of your library, it will go look here.
