tammy
=====

`tammy` is an (in progress) set of commands to manage bibliographic references
from the command line. It's written in `python` 3, and uses `yaml` files in
the citeproc format to store the references. It has neat features such as
integration with the CrossRef API.

[![Build Status](https://travis-ci.org/tpoisot/tammy.svg?branch=master)](https://travis-ci.org/tpoisot/tammy)
[![Coverage Status](https://coveralls.io/repos/tpoisot/tammy/badge.png)](https://coveralls.io/r/tpoisot/tammy)

[READ THE DOC](http://tammy.readthedocs.org/en/latest/index.html#)

`tammy` has been designed to meet *my* needs: a minimalistic references
manager, command-line based, scriptable, with a hard-to-corrupt database,
that will play nicely with `pandoc`, and that is **not** based on `bibtex`.

Storing the database as `yaml` files mean that

1. I don't have to deal with running a database locally
2. I can still use `grep` and other things to retrieve information
3. A screw-up in one file won't corrupt my whole DB
4. I can easily edit things manually

Yes, the name comes from [Parks & Rec][pr]. That show is awesome.

[pr]: http://www.imdb.com/title/tt1266020/
