prepare_tests:
	mkdir -p tests/bib
	mkdir -p tests/bib/records
	mkdir -p tests/bib/files
	cp mkdir tests/REF/records/* tests/bib/records/
	cp mkdir tests/REF/files/* tests/bib/files/
	
clean:
	rm tests/bib/records/*
	rm default.yaml
	rm tests/bib/default.{json,yaml}
	#rm tests/bib/files/*

test: run_tests.py
	python run_tests.py

coverage: run_tests.py
	coverage run --source=tammy run_tests.py
	coverage report -m

