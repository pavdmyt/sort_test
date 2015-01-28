flake:
	flake8 sortalgs.py sortalgs_timeit.py ./tests/tests.py 
	
clean:
	rm -f `find . -type f -name '*.py[co]'`

