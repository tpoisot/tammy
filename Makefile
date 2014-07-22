test_folders:
	mkdir -p tests/bib
	mkdir -p tests/bib/records
	mkdir -p tests/bib/files
	
clean:
	rm tests/bib/records/*
	rm default.yaml
	rm tests/bib/default.{json,yaml}
	#rm tests/bib/files/*

test: run_tests.py
	python run_tests.py

