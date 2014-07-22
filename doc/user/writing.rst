.. _writinglib:

Writing the library to disk
===========================

One important thing to keep in mind is that, unless explicitely asked,
``tammy`` will *not* write the contents of the records to the disk. Actually,
``tammy`` will never manipulate the library as a whole, only apply actions
to the different records.

There are two ways to write *something* to disk.

Exporting the library
---------------------

The ``library`` class has an ``export`` method, that allows you to export
either the entire content of the library, or only some keys, to the disk.::
   
   my_lib.export()

Without any arguments, this will write a ``default.json`` file to the
path specificied in the ``export_dir`` configuration option. Available
options are ``keys`` (a list of keys to export), ``path`` (where the
exported file will be), and ``output``. Output can be one of the values in
``tammy.IO.serializers``, and defaults to ``citeproc-json``.

Despite its simplicity, this function is all you need to export a file with
your references. If you want all citations published in ``Nature`` in a
``citeproc-yaml`` file in your ``~/Dropbox`` folder, then this is::

   keys = [k for k, v in my_lib.records.items() if 'container-title' in v.content and v['container-title'].lower() == 'nature']
   my_lib.export(keys=keys, path="~/Dropbox", output="citeproc-yaml")

As long as you have some familiarity with the citeproc format, selecting
the keys you want is relatively easy.
