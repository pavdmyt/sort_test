Sorting algorithms performance test
===================================

For each sorting algorithm the measurement suite is running seven times
keeping only the best time (this reduces measurement distortions due to
other processes running on the system). Measurement suite consists of 100
algorithm launches.

Methodology of testing is borrowed from *Raymond Hettinger's* response_
at stackoverflow_.

Results below represent times best measurement suite took, in seconds.

Example and results
-------------------

::

	$ python sortalgs_timeit.py
	bubble_sort
	14.6841878891

	insertion_sort
	10.7499198914

	selection_sort
	5.76975679398

	merge_sort
	0.808687925339

	quick_sort
	0.533707141876

	heap_sort
	0.386697053909

	radix_sort
	0.253129005432


.. _response: http://stackoverflow.com/questions/8220801/how-to-use-timeit-module/8220943#8220943
.. _stackoverflow: http://stackoverflow.com/