test: ve/bin/python
	./ve/bin/flake8 expvar --max-complexity=7
	./ve/bin/python runtests.py

ve/bin/python: setup.py
	rm -rf ve
	virtualenv ve
	./ve/bin/pip install .
	./ve/bin/pip install flake8

clean:
	rm -rf ve
	find . -name '*.pyc' -exec rm {} \;
