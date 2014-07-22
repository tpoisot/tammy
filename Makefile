test: tests/*.py
	chmod +x tests/*py
	mkdir -p tests/bib
	mkdir -p tests/bib/records
	mkdir -p tests/bib/files
	# tests go here
	./tests/services.py
	./tests/keygen.py
	./tests/write.py
	# cleanup
	rm tests/bib/records/*
#	rm tests/bib/files/*

