.. _userintro:

Introduction
============

What is tammy?
--------------

``tammy`` is a python (2.7) module that allows managing your bibliography
in a simple way. I was looking for a reference manager that

#. Integrates with web tools
#. Would not sell itself to Elsevier
#. Can be used programmatically
#. Works well with unicode
#. Is not based on a database
#. Integrates in my ``pandoc``-based workflow

Why ``yaml``?
-------------

A few months ago I almost lost all of my bibliography (3500+ entries)
because of a loosy export from one manager to an other when it comes to
unicode characters. The issue with ``bibtex`` (or others) files is that a
mistake in a single entry *will* break your whole database. And there is no
way to validate a ``bibtex`` file. And to make things even worse, not all
managers parse the same file in the same way.

Introducing ``yaml``: a human-readable way of storing structured
information. ``yaml`` is translatable from ``json`` in a very efficient
way, and ``citeproc-json`` is a *really good* way to store information
about references.

``tammy`` stores *your whole* list of references in separate ``yaml`` files,
and do its own cuisine internally to decide how to talk with ``json``-speaking
functions and services.
