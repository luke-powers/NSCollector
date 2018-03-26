NS Collector
==============

Script for gathering data out of NS.

How it works
============


Encountered census issues
-------------------------

When issues are encountered, for a given issue:
  #. lookup the id
  #. see what the Previously Encountered Changes (PEC) are per option
  #. if any of the options have a PEC > 3 (the heighest take weight)
  #. select the option with the highest weight
  #. store list of changes to the PEC


Issue prioritization
--------------------

Each attribute is given a weight 0 being disregareded 3 being highest
want weight, -3 being highest avoid weight.

Previously Encountered Changes
------------------------------

Previously Encountered Changes (PEC) change based on the current
values of various options. A high value attribute might not change
even if the PEC indicates that a particular issue should increase the
attribute. Thus ranges or rates of change need to be stored for each
attribute.


Install
=======

With python2.7 and pip > 9.0 ::

  sudo -H pip install ~/path/to/NSCollector

Run
===

See: ::

  ns-collector -h

Remove
======

sudo -H pip uninstall nscollector


Notes:

Typical test run ::

  sudo pip uninstall --yes nscollector; sudo pip install ~/NSCollector/; ns-collector -h
