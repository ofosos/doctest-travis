.. doctest-travis documentation master file, created by
   sphinx-quickstart on Sun Jan  6 13:25:30 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to doctest-travis's documentation!
==========================================


.. testsetup:: *

   from doctest_travis import *


doctest_travis
--------------

.. automodule:: doctest_travis
   :members:


.. autofunction:: doctest_travis.stupid_sum

.. doctest::

	>>> stupid_sum(2, 3)
	6

.. autofunction:: doctest_travis.stupid_mul

.. doctest::

	>>> stupid_mul(4,4)
	32
