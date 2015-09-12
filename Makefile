python3 = python3
pip3 = $(python3) -m pip
req = requirements.txt

dependencies:
	$(pip3) install -r $(req)

prepare_tests:
	mkdir -p tests/bib
	mkdir -p tests/bib/records
	mkdir -p tests/bib/files
	mkdir -p tests/tmp
	cp tests/REF/records/* tests/bib/records/
	cp tests/REF/files/* tests/tmp

test: prepare_tests run_tests.py
	coverage run --source=tammy run_tests.py
	coverage report -m
	make clean

clean:
	rm -r tests/tmp
	rm -r tests/bib

install:
	$(python3) setup.py install
