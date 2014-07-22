prepare_tests:
	mkdir -p tests/bib
	mkdir -p tests/bib/records
	mkdir -p tests/bib/files
	mkdir -p tests/tmp
	cp tests/REF/records/* tests/bib/records/
	cp tests/REF/files/* tests/tmp

coverage: prepare_tests run_tests.py
	coverage run --source=tammy run_tests.py
	coverage report -m

