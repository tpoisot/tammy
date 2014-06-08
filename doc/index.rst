.. tammy documentation master file, created by
   sphinx-quickstart on Fri Jun  6 23:38:43 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to tammy's documentation!
=================================

``tammy`` is a python module to manage your bibliography in a sane,
minimalistic, scriptable, hacker-ish way.

::

   >>> import tammy
   >>> lib = tammy.library()
   >>> lib.new(tammy.get_ref_from_doi('10.7717/peerj.251'))
   >>> lib.write()


User guide
----------

.. toctree::
   :maxdepth: 1

   user/intro

API guide
---------

.. toctree::
   :maxdepth: 2

   dev/classes

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

