Sorting algorithms performance test
===================================

Methodology of testing is borrowed from Raymond Hettinger's response_
at stackoverflow_.

Example and results
-------------------

::

	$ python sortalgs_timeit.py
	bubble_sort
	1.54256296158

	insertion_sort
	1.11028289795

	selection_sort
	0.62717294693

	merge_sort
	0.0857241153717

	quick_sort
	0.0562069416046


.. _response: http://stackoverflow.com/questions/8220801/how-to-use-timeit-module/8220943#8220943
.. _stackoverflow: http://stackoverflow.com/