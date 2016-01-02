.. _userintro:

Introduction
============

Why tammy?
----------

``tammy`` is a python 3 module that allows managing your bibliography in
a simple way. I was dissatisfied by all the tools I used, so I decided to
build my own. I was looking for a reference manager that...

Can be used programmatically
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Being able to manage my references in a programmatic way is important to me,
because it means that I can automate a lot of things. Importing, exporting,
etc etc. And because ``tammy`` is essentially an API to manage bibliographic
records, along with a few helper functions, automation is easy.

Works well with unicode
~~~~~~~~~~~~~~~~~~~~~~~

Us Europeans tend to have accents in our names. ``BibTeX`` is bad at that,
and unicode conversion is in my experience the first source of screw-ups
when opening a ``bib`` file in different programs. I wanted something that
would play nicely with unicode.

Is not based on a database
~~~~~~~~~~~~~~~~~~~~~~~~~~

There were two things I absolutely wanted to avoid: relying on a database,
and relying on a single, massive file. I wanted something light, that I can
easily manipulate using ``grep`` and other nice things if I feel like it. And
because there is no reason that a single corrupted record should render your
whole database useless, I decided to assign each record to its own file,
and build export functions instead.

Integrates in my ``pandoc``-based workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I use ``pandoc`` and ``markdown`` to write papers. ``pandoc`` can read
bibliography files in citeproc-JSON, so using ``bibtex`` as a storage format
makes very little sense (see also: unicodes, and the fact that it's not the
1980s anymore).

Can do web search
~~~~~~~~~~~~~~~~~

Getting the informations on a paper with just a ``DOI``, ``PMID``, ``ArXiV``
identifier, etc, is useful, so I am building a set of functions to do
that. Also, if journals expose their papers in citeproc-JSON (as *PeerJ*
does), it's easy to write a function for integration.

ICanHazPDF, YouCanHazPDF, EVERYONECanHazPDF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tammy`` has *literaly* a ``ICanHazPDF`` module. It looks at the DOI
(currently, other means to do lookup coming soon), and then will use a lot
of requests, regex, and web parsing to get you the PDF if you have access.

With all these informations in hand, if you think ``tammy`` is right for you,
read on!
